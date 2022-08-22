import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        # init function for class of tk.Tk
        super().__init__()

        # Setting size and Title of the Window
        self.title("NOC")
        self.geometry('450x250')

        # Adding Exit button at the bottom of window

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        exit = ttk.Button(self,
                          text="Exit", command=self.quit).pack(side="right", padx=10, pady=10)
        # initialising frames

        self.frames = {}

        for f in (LoginPage, RegisterPage, ProcessPage):
            frame = f(container, self)

            self.frames[f] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Labels
        login = ttk.Label(self, text="Login").place(x=200, y=20)

        username = ttk.Label(self,
                             text="Username").place(x=20,
                                                    y=60)
        password = ttk.Label(self,
                             text="Password").place(x=20,
                                                    y=100)
        register = ttk.Label(
            self, text="Not a member?").place(x=300, y=80)

        # Separator
        separator = ttk.Separator(self, orient="vertical")
        separator.place(relheight=0.6, relwidth=0, relx=0.56, rely=0.23)

        # Entry
        self.username_input = ttk.Entry(self,
                                        width=20)
        self.username_input.place(x=90, y=60)
        self.password_input = ttk.Entry(self, show="*",
                                        width=20)
        self.password_input.place(x=90, y=100)

        # Buttons
        login = ttk.Button(self,
                           text="Login", command=self.on_login).place(x=158,
                                                                      y=130)

        register_button = ttk.Button(self,
                                     text="Register",
                                     command=lambda: controller.show_frame(RegisterPage)).place(x=310, y=110)

    # Methods
    def on_login(self):
        print(self.username_input.get())
        print(self.password_input.get())


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        login = ttk.Label(self, text="Registration").place(x=180, y=20)


class ProcessPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        login = ttk.Label(self, text="Process Page").place(x=200, y=20)


if __name__ == "__main__":
    root = Application()
    root.mainloop()
