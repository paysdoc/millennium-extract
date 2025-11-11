"""
Port management for parallel review batches.
Tracks which ports are in use and finds available ports.
"""
import json
import socket
from pathlib import Path
from typing import Optional


class PortManager:
    """Manages port allocation for HTTP servers."""

    def __init__(self, state_file: Path = None):
        """Initialize port manager."""
        self.state_file = state_file or Path("sourced_images/review/.ports.json")
        self.min_port = 8000
        self.max_port = 8020

    def _load_state(self) -> dict:
        """Load port state from file."""
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save_state(self, state: dict):
        """Save port state to file."""
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)

    def is_port_available(self, port: int) -> bool:
        """Check if a port is available."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.bind(('localhost', port))
                return True
        except (OSError, socket.error):
            return False

    def find_available_port(self) -> Optional[int]:
        """
        Find the first available port, preferring lower ports.

        Returns:
            Port number, or None if no ports available
        """
        # Load current state
        state = self._load_state()

        # Clean up stale entries (ports that are no longer in use)
        active_ports = {}
        for port_str, info in state.items():
            port = int(port_str)
            if not self.is_port_available(port):
                # Port is still in use
                active_ports[port_str] = info

        # Save cleaned state
        if active_ports != state:
            self._save_state(active_ports)

        # Find first available port
        for port in range(self.min_port, self.max_port + 1):
            if self.is_port_available(port):
                return port

        return None

    def register_port(self, port: int, category: str, batch_info: str, pid: int = None):
        """Register a port as in use."""
        state = self._load_state()
        state[str(port)] = {
            'category': category,
            'batch_info': batch_info,
            'pid': pid
        }
        self._save_state(state)

    def release_port(self, port: int):
        """Release a port."""
        state = self._load_state()
        if str(port) in state:
            del state[str(port)]
            self._save_state(state)

    def get_active_ports(self) -> dict:
        """Get all active ports and their info."""
        state = self._load_state()

        # Verify ports are actually in use
        active = {}
        for port_str, info in state.items():
            port = int(port_str)
            if not self.is_port_available(port):
                active[port_str] = info

        # Update state if needed
        if len(active) != len(state):
            self._save_state(active)

        return active

    def cleanup_all(self):
        """Clean up all port registrations."""
        if self.state_file.exists():
            self.state_file.unlink()
