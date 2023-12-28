import tkinter as tk

from utilis import search_movie
from utilis import add_liked_movie
from utilis import logout
from utilis import give_recommendation


def main_page():
    def on_search():
        clear_list()
        movie = search_movie(search_entry.get())
        if not movie.empty:
            list1.insert('end', movie['title'].values[0])
            list1.insert(tk.END, " ")
            list1.insert(tk.END, "Budget: ", (str(movie["budget"].values[0]) + " $"))
            list1.insert(tk.END, " ")
            list1.insert(tk.END, "Genre: ", (movie["genres"].values[0]))
            list1.insert(tk.END, " ")
            list1.insert(tk.END, "production_companies: ", (movie["production_companies"].values[0]))
            list1.insert(tk.END, " ")
            list1.insert(tk.END, "overview: ", (movie["overview"].values[0]))
            list1.insert(tk.END, " ")
            list1.insert(tk.END, "release_date: ", (movie["release_date"].values[0]))
            list1.insert(tk.END, " ")
            list1.insert(tk.END, "revenue: ", (str(movie["revenue"].values[0]) + " $"))
            list1.insert(tk.END, " ")
            list1.insert(tk.END, "director: ", (movie["director"].values[0]))
            list1.insert(tk.END, " ")
            like_button['state'] = 'normal'
        else:
            list1.insert(tk.END, "Sorry, no results!")

    def clear_list():
        list1.delete(0, tk.END)
        like_button['state'] = 'disabled'

    def recommend():
        clear_list()
        list1.insert(tk.END, "Loading...")
        recommendation_set = give_recommendation()
        clear_list()
        if len(recommendation_set) > 0:
            list1.insert(tk.END, "Here is your recommendation:")
            for element in recommendation_set:
                list1.insert(tk.END, element)
        else:
            list1.insert(tk.END, "We don't know much about you. Try trending!")

    window = tk.Tk()
    window.title("Main page")
    window.geometry('650x440')
    window.configure(bg='#333333')

    frame = tk.Frame(bg='#333333')

    welcome_label = tk.Label(frame, text="Welcome to Notflix", font=("Arial", 20), bg='#333333', fg="#FF3399")
    welcome_label.grid(row=0, column=0, padx=(10, 0))

    logout_button = tk.Button(frame, text="Logout", command=lambda: logout(lambda: window.destroy()))
    logout_button.grid(row=0, column=3, padx=(0, 10))

    # Search label, entry, and button
    search_label = tk.Label(frame, text="Search", bg='#333333', fg="#FF3399", width=30)
    search_label.grid(row=1, column=0, pady=30)

    search_entry = tk.Entry(frame, font=("Arial", 16))
    search_entry.grid(row=1, column=1, pady=30, padx=(0, 10))

    search_button = tk.Button(frame, text="Search", command=on_search)
    search_button.grid(row=1, column=2, pady=30)

    list1 = tk.Listbox(frame, height=16, width=95)
    list1.grid(row=20, column=0, rowspan=50, columnspan=60)

    # Attach scrollbar to the list - easily explore the list
    sb1 = tk.Scrollbar(frame)
    sb1.grid(row=20, column=3, rowspan=60, columnspan=60)

    # Configure that scroll bar to our list box
    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    recommend_button = tk.Button(window, text="Recommend", width=20, command=recommend)
    recommend_button.place(x=10, y=400)

    trending_button = tk.Button(window, text="Trending", width=20)
    trending_button.place(x=170, y=400)

    clear_button = tk.Button(window, text="Clear result", command=clear_list, width=20)
    clear_button.place(x=330, y=400)

    like_button = tk.Button(window, text="Like", command=lambda: add_liked_movie(search_entry.get()), width=20)
    like_button.place(x=490, y=400)
    like_button['state'] = 'disabled'

    frame.pack()
    # Run the Tkinter event loop
    window.mainloop()
