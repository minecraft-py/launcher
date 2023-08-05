import sys
from json import load
from threading import Thread
from tkinter import StringVar
from tkinter.ttk import Combobox, Label, LabelFrame, Radiobutton
from typing import Dict

from launcher.assets import ASSETS_HOME
from launcher.tabs import LauncherTab
from launcher.utils import *


class SettingTab(LauncherTab):
    def __init__(self, master, launcher, **kwargs):
        super().__init__(master, launcher, **kwargs)
        self.tab_name = "setting"
        self.lang_cache: Dict[str, str] = {}

        self.basic_settings = LabelFrame(
            self, text=self.launcher.assets.translate("tab.setting.basic_settings")
        )
        self.choose_language_label = Label(
            self.basic_settings,
            text=self.launcher.assets.translate("tab.setting.choose_language"),
        )
        self.language = StringVar()
        self.choose_language_combobox = Combobox(
            self.basic_settings,
            state="disable",
            width=32,
            textvariable=self.language,
        )
        self.choose_language_combobox.bind(
            "<<ComboboxSelected>>", self.on_choose_language_selected
        )
        self.choose_language_combobox.set(
            self.launcher.assets.translate("gui.waiting"),
        )
        self.appearence_label = Label(
            self.basic_settings,
            text=launcher.assets.translate("tab.setting.appearence"),
        )
        self.appearence = StringVar(
            value=self.launcher.setting.get("appearence", "light")
        )
        self.appearence_light_radio = Radiobutton(
            self.basic_settings,
            text=self.launcher.assets.translate("tab.setting.appearence.light"),
            variable=self.appearence,
            value="light",
            command=self.on_appearence_radio_click,
        )
        self.appearence_dark_radio = Radiobutton(
            self.basic_settings,
            text=self.launcher.assets.translate("tab.setting.appearence.dark"),
            variable=self.appearence,
            value="dark",
            command=self.on_appearence_radio_click,
        )
        self.python_settings = LabelFrame(self, text="Python")
        self.version_label = Label(
            self.python_settings,
            text=self.launcher.assets.translate("tab.setting.interpreter_verion"),
        )
        self.version_combobox = Combobox(
            self.python_settings, state="disable", width=32
        )
        self.version_combobox.set(
            self.launcher.assets.translate("gui.waiting"),
        )
        self.interpreter_path = Label(
            self.python_settings, text=sys.executable, wraplength=225
        )
        self.copyright_label = Label(self, text="Copyright \xa9 2023 minecraftpy team")

        self.basic_settings.pack(side="top", anchor="nw", fill="x", padx=3, pady=3)
        self.python_settings.pack(side="top", anchor="nw", fill="x", padx=3, pady=3)
        self.copyright_label.pack(side="bottom", anchor="se")
        self.choose_language_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.choose_language_combobox.grid(
            row=0, column=1, columnspan=2, sticky="w", padx=5, pady=5
        )
        self.appearence_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.appearence_light_radio.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.appearence_dark_radio.grid(row=1, column=2, sticky="w")
        self.version_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.version_combobox.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        self.interpreter_path.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        Thread(target=self.load_languages).start()

    def on_choose_language_selected(self, *event):
        lang = self.language.get()
        lang_code = list(self.lang_cache.keys())
        diaplay_name = list(self.lang_cache.values())
        now_lang = lang_code[diaplay_name.index(lang)]
        self.launcher.change_language(now_lang)

    def on_appearence_radio_click(self, *event):
        self.launcher.setting["appearence"] = self.appearence.get()
        if self.launcher.setting.get("appearence") == "dark":
            self.master.tk.call("set_theme", "dark")
        else:
            self.master.tk.call("set_theme", "light")

    def change_language(self):
        self.basic_settings["text"] = self.launcher.assets.translate(
            "tab.settings.basic_settings"
        )
        self.choose_language_label["text"] = self.launcher.assets.translate(
            "tab.setting.choose_language"
        )
        self.appearence_label["text"] = self.launcher.assets.translate(
            "tab.setting.appearence"
        )
        self.appearence_light_radio["text"] = self.launcher.assets.translate(
            "tab.setting.appearence.light"
        )
        self.appearence_dark_radio["text"] = self.launcher.assets.translate(
            "tab.setting.appearence.dark"
        )
        self.version_label["text"] = self.launcher.assets.translate(
            "tab.setting.interpreter_verion"
        )

    def load_languages(self):
        values = []
        for f in (ASSETS_HOME / "lang").glob("*.json"):
            content = load(f.open("r", encoding="utf-8"))
            display_name = f"{content['language.name']}({content['language.region']})"
            self.lang_cache.setdefault(content["language.code"], display_name)
            values.append(display_name)
        self.choose_language_combobox["values"] = values
        self.choose_language_combobox.set(
            self.lang_cache[self.launcher.assets.language]
        )
        self.choose_language_combobox["state"] = "readonly"


__all__ = "SettingTab"
