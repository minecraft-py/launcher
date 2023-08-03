from locale import getdefaultlocale
from pathlib import Path
from tkinter import *
from tkinter.ttk import Notebook
from typing import List

from launcher.assets import LauncherAssets
from launcher.tabs import LauncherTab
from launcher.tabs.setting import SettingTab
from launcher.utils.setting import Setting


class Launcher:
    def __init__(self, root: Tk):
        self.root = root
        # self.root.resizable(FALSE, FALSE)
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
            self.root.tk.call("set_theme", "dark")

        self.tabs: List[LauncherTab] = []
        self.notebook = Notebook(self.root)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.notebook.grid(row=0, column=0, sticky=(N, E, W, S))

        self.add_tab(SettingTab)

    def add_tab(self, cls: LauncherTab):
        tab = cls(self.root, self)
        tab_name = self.assets.translate(f"tab.{tab.tab_name}.name")
        self.notebook.add(tab, text=tab_name)

    def change_language(self, lang_code: str):
        self.assets.language = lang_code
        self.root.title(self.assets.translate("root.title"))
        for tab in self.tabs.values():
            tab.change_language()


__all__ = "Launcher"
