"""
Cleanup utility for HTTP servers.
Lists and stops HTTP servers started by web_main.py
"""
import sys
import os
import signal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.download_images.port_manager import PortManager


def list_servers():
    """List all active servers."""
    pm = PortManager()
    active = pm.get_active_ports()

    if not active:
        print("No active servers found")
        return

    print("="*80)
    print("Active HTTP Servers")
    print("="*80)
    for port, info in sorted(active.items(), key=lambda x: int(x[0])):
        print(f"\nPort {port}:")
        print(f"  Category: {info.get('category', 'Unknown')}")
        print(f"  Batch: {info.get('batch_info', 'Unknown')}")
        print(f"  PID: {info.get('pid', 'Unknown')}")
        print(f"  URL: http://localhost:{port}/index.html")
    print("="*80)


def stop_server(port: int):
    """Stop a specific server."""
    pm = PortManager()
    active = pm.get_active_ports()

    port_str = str(port)
    if port_str not in active:
        print(f"No server found on port {port}")
        return False

    pid = active[port_str].get('pid')
    if pid:
        try:
            os.kill(pid, signal.SIGTERM)
            print(f"✅ Stopped server on port {port} (PID: {pid})")
            pm.release_port(port)
            return True
        except ProcessLookupError:
            print(f"⚠️  Process {pid} not found (already stopped?)")
            pm.release_port(port)
            return True
        except PermissionError:
            print(f"❌ Permission denied to stop process {pid}")
            return False
    else:
        print(f"⚠️  No PID found for port {port}, releasing port anyway")
        pm.release_port(port)
        return True


def stop_all_servers():
    """Stop all servers."""
    pm = PortManager()
    active = pm.get_active_ports()

    if not active:
        print("No active servers to stop")
        return

    print(f"Stopping {len(active)} server(s)...")
    for port in active.keys():
        stop_server(int(port))

    pm.cleanup_all()
    print("\n✅ All servers stopped")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        # Default: list servers
        list_servers()
        print("\nUsage:")
        print("  List servers:     python -m src.download_images.cleanup_servers")
        print("  Stop specific:    python -m src.download_images.cleanup_servers stop 8000")
        print("  Stop all:         python -m src.download_images.cleanup_servers stop-all")
        return

    command = sys.argv[1].lower()

    if command == "list":
        list_servers()
    elif command == "stop":
        if len(sys.argv) < 3:
            print("Error: Please specify a port number")
            print("Usage: python -m src.download_images.cleanup_servers stop 8000")
            return
        try:
            port = int(sys.argv[2])
            stop_server(port)
        except ValueError:
            print(f"Error: Invalid port number: {sys.argv[2]}")
    elif command == "stop-all":
        stop_all_servers()
    else:
        print(f"Unknown command: {command}")
        print("Valid commands: list, stop, stop-all")


if __name__ == "__main__":
    main()
