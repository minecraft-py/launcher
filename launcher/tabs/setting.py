from tkinter import *
from tkinter.ttk import *
from launcher.tabs import LauncherTab


class SettingTab(LauncherTab):
    def __init__(self, master, launcher, **kwargs):
        super().__init__(master, launcher, **kwargs)
        self.tab_name = "setting"

        self.setting_area = Frame(self)
        self.choose_language_label = Label(
            self.setting_area,
            text=launcher.assets.translate("tab.setting.choose_language"),
            font="TkTextFont 16",
        )
        self.choose_language_combobox = Combobox(self.setting_area, width=32)
        self.appearence_label = Label(
            self.setting_area,
            text=launcher.assets.translate("tab.setting.appearence"),
            font="TkTextFont 16",
        )
        self.appearence_combobox = Combobox(self.setting_area, width=20)
        self.copyright_label = Label(self, text="Copyright \xa9 2023 minecraftpy team")

        self.setting_area.pack(side=TOP, anchor=NW)
        self.choose_language_label.grid(row=0, column=0, sticky=W, pady=8)
        self.choose_language_combobox.grid(row=0, column=1, sticky=W, pady=8)
        self.appearence_label.grid(row=1, column=0, sticky=W)
        self.appearence_combobox.grid(row=1, column=1, sticky=W)
        self.copyright_label.pack(side=BOTTOM, anchor=SE, padx=3, pady=5)


__all__ = "SettingTab"
