from json import dump

from launcher.utils import *
from launcher.utils.setting import DEFAULT_SETTING


def first_run():
    """This function will create some important files and
    directories when they are missing.
    """
    data_path = get_data_path()
    settings_path = get_settings_path()

    if not data_path.exists:
        data_path.mkdir()
    if not settings_path.exists:
        settings_path.mkdir()

    for subpath in ["cache", "versions"]:
        if not (data_path / subpath).exists:
            (data_path / subpath).mkdir()

    if not (f := settings_path / "setting.json").exists:
        dump(DEFAULT_SETTING, open(f, "w+"))


__all__ = "first_run"
