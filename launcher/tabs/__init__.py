from tkinter.ttk import Frame

import launcher


class LauncherTab(Frame):
    def __init__(self, master, launcher: "launcher.Launcher", **kwargs):
        super().__init__(master, **kwargs)
        self.launcher = launcher
        self.tab_name = ""

    def change_language(self):
        """This function is called when the language is changed."""
        pass


__all__ = "LauncherTab"
