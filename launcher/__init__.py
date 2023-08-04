from locale import getdefaultlocale
from pathlib import Path
from tkinter import Tk
from tkinter.ttk import Notebook
from typing import Dict, Type
from atexit import register

from launcher.assets import LauncherAssets
from launcher.tabs import LauncherTab
from launcher.tabs.setting import SettingTab
from launcher.utils.setting import Setting


class Launcher:
    def __init__(self, root: Tk):
        self.root = root
        self.tabs: Dict[str, LauncherTab] = {}
        self.root.tk.call("source", Path(__file__).parent / "theme" / "azure.tcl")

        self.assets = LauncherAssets()
        self.setting = Setting()
        if self.setting.get("language", "<auto>") == "<auto>":
            lang_code = getdefaultlocale()[0].lower()
        else:
            lang_code = self.setting.get("language", "en_us").lower()
        self.assets.language = lang_code
        self.root.title(self.assets.translate("root.title"))
        if self.setting.get("appearence", "light") == "dark":
            self.root.tk.call("set_theme", "dark")
        else:
            self.root.tk.call("set_theme", "light")

        self.notebook = Notebook(self.root)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.notebook.grid(row=0, column=0, sticky="news")

        self.add_tab(SettingTab)
        register(self.on_exit)

    def add_tab(self, cls: Type[LauncherTab]):
        tab = cls(self.root, self)
        tab_name = self.assets.translate(f"tab.{tab.tab_name}.name")
        self.tabs.setdefault(tab.tab_name, tab)
        self.notebook.add(tab, text=tab_name, padding=3)

    def change_language(self, lang_code: str):
        self.setting["language"] = lang_code
        self.assets.language = lang_code
        self.root.title(self.assets.translate("root.title"))
        for tab in self.tabs.values():
            tab.change_language()

    def on_exit(self):
        self.setting.save()


__all__ = "Launcher"
