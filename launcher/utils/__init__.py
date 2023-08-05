import os
import sys
from functools import lru_cache
from pathlib import Path

# Like pyglet, the launcher treats *BSD systems as Linux
compat_platform = sys.platform
if "bsd" in compat_platform:
    compat_platform = "linux-compat"


@lru_cache(maxsize=1)
def get_settings_path() -> Path:
    """Get a directory to save user preferences.

    From `pyglet.resource.get_settings_path`.
    """
    name = "minecraftpy-launcher"
    HOME = Path.home()
    if compat_platform in ("cygwin", "win32"):
        if "APPDATA" in os.environ:
            return Path(os.environ["APPDATA"]) / name
        else:
            return HOME / name
    elif compat_platform == "darwin":
        return HOME / "Library" / "Application Support" / name
    elif compat_platform.startswith("linux"):
        if "XDG_CONFIG_HOME" in os.environ:
            return Path(os.environ["XDG_CONFIG_HOME"]) / name
        else:
            return HOME / ".config" / name
    else:
        return HOME / ("." + name)


@lru_cache(maxsize=1)
def get_data_path() -> Path:
    """Get a directory to save user data.

    From `pyglet.resource.get_data_path`.
    """
    name = "minecraftpy-launcher"
    HOME = Path.home()
    if compat_platform in ("cygwin", "win32"):
        if "APPDATA" in os.environ:
            return Path(os.environ["APPDATA"]) / name
        else:
            return HOME / name
    elif compat_platform == "darwin":
        return HOME / "Library" / "Application Support" / name
    elif compat_platform.startswith("linux"):
        if "XDG_DATA_HOME" in os.environ:
            return Path(os.environ["XDG_DATA_HOME"]) / name
        else:
            return HOME / ".local" / "share" / name
    else:
        return HOME / ("." + name)


__all__ = ("compat_platform", "get_settings_path", "get_data_path")
