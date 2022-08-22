import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        # Setting size and Title of the Window
        self.title("NOC")
        self.geometry('450x250')

        # Labels
        self.login = ttk.Label(self, text="Login").place(x=200, y=20)
        self.username = ttk.Label(self,
                                  text="Username").place(x=30,
                                                         y=60)
        self.password = ttk.Label(self,
                                  text="Password").place(x=30,
                                                         y=100)
        self.register = ttk.Label(
            self, text="Not a member?").place(x=30, y=215)

        # Entry
        self.username_input = ttk.Entry(self,
                                        width=30)
        self.username_input.place(x=100, y=60)
        self.password_input = ttk.Entry(self, show="*",
                                        width=30)
        self.password_input.place(x=100, y=100)

        # Buttons
        self.submit = ttk.Button(self,
                                 text="Submit", command=self.on_submit).place(x=240,
                                                                              y=130)

        self.exit = ttk.Button(self,
                               text="Exit", command=self.close).place(x=360, y=210)

        self.register_button = ttk.Button(self,
                                          text="Register", command=self.registration).place(x=130, y=210)

    # Methods

    def registration(self):
        pass

    def on_submit(self):
        print(self.username_input.get())
        print(self.password_input.get())

    def close(self):
        self.destroy()


if __name__ == "__main__":
    root = Application()
    root.mainloop()
