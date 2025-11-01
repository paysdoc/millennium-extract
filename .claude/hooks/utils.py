"""Utility functions for Claude hooks."""

import subprocess


def make_sound(sound_name):
    """Make a system sound by name (without extension).
    
    Args:
        sound_name: Name of the sound file without extension (e.g., "Hero", "Basso")
    """
    try:
        # Use macOS system sound
        subprocess.run(["afplay", f"/System/Library/Sounds/{sound_name}.aiff"], 
                      capture_output=True, timeout=5)
    except:
        try:
            # Fallback to terminal bell
            print("\a", end="", flush=True)
        except:
            pass