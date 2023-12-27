import tkinter
from utilis import authenticate


def login_page():
    def action():
        window.destroy()
        main_page()

    def counter_action():
        error_label.config(text="Invalid credentials")

    window = tkinter.Tk()
    window.title("Login form")
    window.geometry('640x440')
    window.configure(bg='#333333')

    frame = tkinter.Frame(bg='#333333')

    # Creating widgets
    login_label = tkinter.Label(
        frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
    username_label = tkinter.Label(
        frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    username_entry = tkinter.Entry(frame, font=("Arial", 16))
    password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    password_label = tkinter.Label(
        frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    login_button = tkinter.Button(
        frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
        command=lambda: authenticate(username_entry.get(), password_entry.get(), action, counter_action))
    error_label = tkinter.Label(frame, text="", bg="#333333", fg="red", font=("Arial", 8))

    # Placing the widgets on the screen
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    error_label.grid(row=3)
    login_button.grid(row=4, column=0, columnspan=2, pady=30)

    frame.pack()

    window.mainloop()


def main_page():
    window = tkinter.Tk()
    window.title("Main page")
    window.geometry('640x440')
    window.configure(bg='#333333')
    window.mainloop()
