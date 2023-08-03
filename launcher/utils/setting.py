from collections import UserDict
from json import dump, load

from launcher.utils import *

DEFAULT_SETTING = {"language": "<auto>", "appearence": "light"}


class Setting(UserDict):
    """Game setting.

    It inherits from `collections.UserDict`, so it can be set
    as a dict.

    All changes must be stored via the `save` method.
    """

    def __init__(self):
        self._file = get_settings_path() / "setting.json"
        try:
            self.data = load(open(self._file, "r", encoding="utf-8"))
        except:
            self.data = DEFAULT_SETTING

    def __missing__(self, key):
        return None

    def __repr__(self) -> str:
        return f"Setting({self.data})"

    def save(self):
        """Save setting."""
        dump(
            self.data,
            open(self._file, "w+", encoding="utf-8"),
            ensure_ascii=False,
            indent=4,
        )


__all__ = "DEFAULT_SETTING", "Setting"
