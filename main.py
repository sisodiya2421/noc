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
        exit = ttk.Button(self,
                          text="Exit", command=self.quit).place(x=360, y=210)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

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
                             text="Username").place(x=60,
                                                    y=60)
        password = ttk.Label(self,
                             text="Password").place(x=60,
                                                    y=100)
        register = ttk.Label(
            self, text="Not a member?").place(x=30, y=215)

        # Entry
        username_input = ttk.Entry(self,
                                   width=30)
        username_input.place(x=130, y=60)
        password_input = ttk.Entry(self, show="*",
                                   width=30)
        password_input.place(x=130, y=100)

        # Buttons
        submit = ttk.Button(self,
                            text="Submit", command=self.on_submit).place(x=270,
                                                                         y=130)

        register_button = ttk.Button(self,
                                     text="Register", command=lambda: controller.show_frame(RegisterPage)).place(x=130, y=210)

    # Methods
    def on_submit(self):
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
