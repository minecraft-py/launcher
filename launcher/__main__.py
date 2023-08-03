from tkinter import Tk

from launcher import Launcher
from launcher.utils.prepare import first_run

if __name__ == "__main__":
    first_run()
    root = Tk()
    Launcher(root)
    root.mainloop()
