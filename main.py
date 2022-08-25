import logging
from time import sleep
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
import pandas as pd
import subprocess
import os
import platform
from scrape import Scrapper

DB_FILE = 'database.xlsx'
OUTPUT_FILE = 'output.xlsx'
db = pd.read_excel(DB_FILE)


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
                           text="Login", command=lambda: self.on_login(controller)).place(x=158,
                                                                                          y=130)

        register_button = ttk.Button(self,
                                     text="Register",
                                     command=lambda: controller.show_frame(RegisterPage)).place(x=310, y=110)

    # Methods
    def on_login(self, controller):
        data_series = pd.Series(data=[self.username_input.get(), self.password_input.get()],
                                index=['username', 'password'])
        if db['username'].isin([self.username_input.get()]).any().any():
            # check if password is correct
            user_details = db[db['username'].isin([self.username_input.get()])]
            if self.password_input.get() == str(user_details['password'].iloc[0]):
                controller.show_frame(ProcessPage)
            else:
                showerror("error", "incorrect password")
        else:
            # user does not exists
            showerror("error", "username does not exists")


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        registration = ttk.Label(self, text="Registration").place(x=180, y=20)

        # Labels in Registration page
        fullname = ttk.Label(self,
                             text="Full Name").place(x=40,
                                                     y=60)
        username = ttk.Label(self,
                             text="Username").place(x=250,
                                                    y=60)
        password = ttk.Label(self,
                             text="Password").place(x=40,
                                                    y=120)
        confirm_password = ttk.Label(self,
                                     text="Confirm Password").place(x=250,
                                                                    y=120)

        # Entries in Registration page
        self.fullname_input = ttk.Entry(self,
                                        width=20)
        self.fullname_input.place(x=40, y=80)

        self.username_input = ttk.Entry(self,
                                        width=20)
        self.username_input.place(x=250, y=80)

        self.password_input = ttk.Entry(self,
                                        width=20, show="*")
        self.password_input.place(x=40, y=140)

        self.cnfpassword_input = ttk.Entry(self,
                                           width=20, show="*")
        self.cnfpassword_input.place(x=250, y=140)

        # Button
        submit = ttk.Button(self,
                            text="Submit", command=lambda: self.on_submit(controller)).place(x=180,
                                                                                             y=180)

    def on_submit(self, controller):
        global db
        new_data_series = pd.Series(data=[self.username_input.get(),
                                          self.fullname_input.get(), self.password_input.get()],
                                    index=['username', 'fullname', 'password'])
        if self.cnfpassword_input.get() != self.password_input.get():
            showerror("error", "Password Mismatch")
        elif db.empty:
            db = db.append(new_data_series, ignore_index=True)
            db.to_excel(DB_FILE, index=False)
            showinfo('Success', 'Registration Successful. Please login now')
            controller.show_frame(LoginPage)
        else:
            # check if username exists or not
            if db['username'].isin([self.username_input.get()]).any().any():
                # username is already present show an error
                showerror("error", "Username already present")
            else:
                # username is not present, insert into db
                db = db.append(new_data_series, ignore_index=True)
                db.to_excel(DB_FILE, index=False)
                showinfo('Success', 'Registration Successful. Please login now')
                controller.show_frame(LoginPage)


class ProcessPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        process = ttk.Label(self, text="Process").place(x=200, y=20)
        run_button = ttk.Button(self,
                                text="Run",
                                command=self.run, padding=10).place(x=185, y=100)

    def run(self):
        global OUTPUT_FILE
        url = "https://www.myntra.com/men-tshirts?p=1"
        scraper = Scrapper()
        iteration = 3
        scraped_data = None
        for _ in range(0, iteration):
            scrape = scraper.scrape(url)
            scraped_data = scrape['scrapped_data']
            if scrape['next_page'] != None:
                url = scrape['next_page']
        scraper.driver.close()
        scraped_df = pd.DataFrame(scraped_data)
        scraped_df.to_excel(OUTPUT_FILE, index=False)
        answer = askokcancel("Scrapping completed",
                             "Do you want to open the generated file?", icon='info')
        if answer:
            try:
                if platform.system() == 'Darwin':       # macOS
                    subprocess.call(('open', OUTPUT_FILE))
                elif platform.system() == 'Windows':    # Windows
                    os.startfile(OUTPUT_FILE)
                else:                                   # linux variants
                    subprocess.call(("xdg-open", OUTPUT_FILE))
            except Exception as e:
                logging.error(f"some error occured : {e}")


if __name__ == "__main__":
    root = Application()
    root.mainloop()
