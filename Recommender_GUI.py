#RecommenderGUI
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
# import matplotlib.pyplot as plt # type: ignore
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type: ignore
from Recommender import Recommender
from Show import Show
from Media import Media
from Book import Book


class RecommenderGUI:
    def __init__(self):
        self.recommender = Recommender()  # Create an instance of the Recommender class

        # Set up the main window
        self.root = tk.Tk()
        self.root.title("Media Recommender System")
        self.root.geometry("1200x800")  # Set the dimensions of the window

        # Create a notebook widget to manage tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Set up the tabs
        self.setup_movies_tab()
        self.setup_tv_shows_tab()
        self.setup_books_tab()
        self.setup_search_tv_movies_tab()
        self.setup_search_books_tab()
        self.setup_recommendations_tab()
        # self.setup_ratings_tab()
        self.setup_buttons()
        # self.loadShows()
        # self.loadBooks()
        # self.loadAssociations()
        # self.creditInfoBox()

        # Run the tkinter main loop
        self.root.mainloop()

    def setup_movies_tab(self):
        # Create a tab for movies
        movie_tab = ttk.Frame(self.notebook)
        self.notebook.add(movie_tab, text="Movies")

        # Text widget for movie titles and runtimes
        self.movie_text = tk.Text(movie_tab, height=10, width=100, state='disabled')
        self.movie_text.pack(pady=10, padx=10,expand=True, fill='both')

        # Text widget for movie statistics
        self.movie_stats_text = tk.Text(movie_tab, height=10, width=100, state='disabled')
        self.movie_stats_text.pack(pady=10, padx=10,expand=True, fill='both')

        # Populate the text areas if data is available
        if self.recommender.shows:
            self.movie_text.config(state='normal')
            self.movie_text.insert('end', self.recommender.getMovieList())
            self.movie_text.config(state='disabled')

            self.movie_stats_text.config(state='normal')
            self.movie_stats_text.insert('end', str(self.recommender.getMovieStats()))
            self.movie_stats_text.config(state='disabled')
        else:
            self.movie_text.config(state='normal')
            self.movie_text.insert('end', 'No movie data loaded yet.')
            self.movie_text.config(state='disabled')

    def setup_tv_shows_tab(self):
        # Create a tab for TV shows
        tv_tab = ttk.Frame(self.notebook)
        self.notebook.add(tv_tab, text="TV Shows")

        # Text widget for TV show titles and seasons
        self.tv_text = tk.Text(tv_tab, width=100, height=10, state='disabled')
        self.tv_text.pack(pady=10, padx=10, expand=True, fill='both')

        # Text widget for TV show statistics
        self.tv_stats_text = tk.Text(tv_tab, width=100 , height=10, state='disabled')
        self.tv_stats_text.pack(pady=10, padx=10, expand=True, fill='both')

        # Populate the text areas if data is available
        if self.recommender.shows:
            self.tv_text.config(state='normal')
            self.tv_text.insert('end', self.recommender.getTVList())
            self.tv_text.config(state='disabled')

            self.tv_stats_text.config(state='normal')
            self.tv_stats_text.insert('end', str(self.recommender.getTVStats()))
            self.tv_stats_text.config(state='disabled')
        else:
            self.tv_text.config(state='normal')
            self.tv_text.insert('end', 'No TV show data loaded yet.')
            self.tv_text.config(state='disabled')

    def setup_books_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Books")

        self.books_text = scrolledtext.ScrolledText(tab, width=100, height=10, state='disabled')
        self.books_text.pack(pady=10, padx=10, fill='both', expand=True)

        self.books_stats_text = scrolledtext.ScrolledText(tab, width=100, height=10, state='disabled')
        self.books_stats_text.pack(pady=10, padx=10, fill='both', expand=True)

        if self.recommender.books:
            self.books_text.config(state='normal')
            self.books_text.insert('end', self.recommender.getBookList())
            self.books_text.config(state='disabled')

            self.books_stats_text.config(state='normal')
            self.books_stats_text.insert('end', str(self.recommender.getBookStats()))
            self.books_stats_text.config(state='disabled')
        else:
            self.books_text.config(state='normal')
            self.books_text.insert('end', 'No book data loaded yet.')
            self.books_stats_text.insert('end', 'No book statistics available.')

    def setup_search_tv_movies_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Search TV/Movies")

        # Create entry fields and labels
        tk.Label(tab, text="Type:").pack(pady=(10, 0))
        self.type_combobox = ttk.Combobox(tab, values=["Movie", "TV Show"], state="readonly")
        self.type_combobox.pack(fill='x', padx=20)

        tk.Label(tab, text="Title:").pack()
        self.title_entry = ttk.Entry(tab)
        self.title_entry.pack(fill='x', padx=20)

        tk.Label(tab, text="Director:").pack()
        self.director_entry = ttk.Entry(tab)
        self.director_entry.pack(fill='x', padx=20)

        tk.Label(tab, text="Actor:").pack()
        self.actor_entry = ttk.Entry(tab)
        self.actor_entry.pack(fill='x', padx=20)

        tk.Label(tab, text="Genre:").pack()
        self.genre_entry = ttk.Entry(tab)
        self.genre_entry.pack(fill='x', padx=20)

        # Search button
        ttk.Button(tab, text="Search", command=self.search_shows).pack(pady=10)

        # Result area
        self.results_text = scrolledtext.ScrolledText(tab, width=100, height=15, state='disabled')
        self.results_text.pack(pady=10, padx=10, fill='both', expand=True)

    def setup_search_books_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Search Books")

        # Create entry fields and labels
        tk.Label(tab, text="Title:").pack()
        self.book_title_entry = ttk.Entry(tab)
        self.book_title_entry.pack(fill='x', padx=20)

        tk.Label(tab, text="Author:").pack()
        self.author_entry = ttk.Entry(tab)
        self.author_entry.pack(fill='x', padx=20)

        tk.Label(tab, text="Publisher:").pack()
        self.publisher_entry = ttk.Entry(tab)
        self.publisher_entry.pack(fill='x', padx=20)

        # Search button
        ttk.Button(tab, text="Search", command=self.search_books).pack(pady=10)

        # Result area
        self.book_results_text = scrolledtext.ScrolledText(tab, width=100, height=15, state='disabled')
        self.book_results_text.pack(pady=10, padx=10, fill='both', expand=True)

    def setup_recommendations_tab(self):
        tab = ttk.Frame(self.notebook)
        if tab is None:
            tab = 'Movie'
        self.notebook.add(tab, text="Recommendations")

        # Dropdown menu for type selection
        tk.Label(tab, text="Select Type:").pack(padx=10, pady=10)
        self.recommendation_type = ttk.Combobox(tab, values=["Movie", "TV Show", "Book"], state="readonly")
        self.recommendation_type.pack(fill='x', padx=20)

        # Entry widget for title
        tk.Label(tab, text="Title:").pack(padx=10, pady=10)
        self.recommendation_title = ttk.Entry(tab)
        self.recommendation_title.pack(fill='x', padx=20)

        # Button to trigger recommendation search
        ttk.Button(tab, text="Get Recommendations", command=self.get_recommendations).pack(pady=20)

        # Text area for displaying results
        self.recommendation_results = scrolledtext.ScrolledText(tab, width=100, height=25, state='disabled')
        self.recommendation_results.pack(padx=10, pady=10)
        

    # def setup_ratings_tab(self):
    #     # Create a tab for Ratings
    #     ratings_tab = ttk.Frame(self.notebook)
    #     self.notebook.add(ratings_tab, text="Ratings")

    #     # Assuming get_movie_ratings and get_tv_ratings are methods that return dictionaries
    #     # with ratings percentages like {'G': 10.00, 'PG': 15.00, 'R': 25.00}
    #     movie_ratings = self.recommender.get_movie_ratings() if hasattr(self.recommender, 'get_movie_ratings') else {}
    #     tv_ratings = self.recommender.get_tv_ratings() if hasattr(self.recommender, 'get_tv_ratings') else {}

    #     # Create pie charts for movies and TV shows
    #     self.create_pie_chart(ratings_tab, movie_ratings, "Movie Ratings", 0)
    #     self.create_pie_chart(ratings_tab, tv_ratings, "TV Show Ratings", 1)

    # def create_pie_chart(self, tab, data, title, column):
    #     fig, ax = plt.subplots()
    #     labels = list(data.keys())
    #     sizes = list(data.values())
    #     # Create pie chart with labels and display percentages with 2 decimal places
    #     ax.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
    #     ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #     plt.title(title)

    #     # Embedding the plot in the Tkinter widget
    #     canvas = FigureCanvasTkAgg(fig, master=tab)
    #     canvas.draw()
    #     canvas.get_tk_widget().grid(row=0, column=column, sticky='nsew')

    #     # Ensure the column expands to fill available space
    #     tab.grid_columnconfigure(column, weight=1)


    def get_recommendations(self):
        type = self.recommendation_type.get()
        title = self.recommendation_title.get()
        if not title:
            messagebox.showerror("Error", "Please enter a title to receive recommendations.")
            return


        results = self.recommender.getRecommendations(type, title)
        self.recommendation_results.config(state='normal')
        self.recommendation_results.delete(1.0, tk.END)
        self.recommendation_results.insert(tk.END, results)
        self.recommendation_results.config(state='disabled')

    def setup_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(side='bottom', fill='x')

        tk.Button(frame, text="Load Shows", command=self.loadShows).pack(side='left',padx=30,pady=10)
        tk.Button(frame, text="Load Books", command=self.loadBooks).pack(side='left',padx=130,pady=10)
        tk.Button(frame, text="Load Recommendations", command=self.loadAssociations).pack(side='left',padx=130,pady=10)
        tk.Button(frame, text="Information", command=self.creditInfoBox).pack(side='left',padx=130,pady=10)
        tk.Button(frame, text="Quit", command=self.root.quit).pack(side='right',padx=30,pady=10)

    def loadShows(self):
        # Load show data from the Recommender object
        self.recommender.loadShows()  # Assuming this method populates self.recommender.shows

        # Update movies text area
        movies_info = self.recommender.getMovieList()  # Assuming this returns formatted movie list
        movie_stats = self.recommender.getMovieStats()  # Assuming this returns movie statistics

        self.movie_text.config(state='normal')
        self.movie_text.delete(1.0, tk.END)
        self.movie_text.insert(tk.END, movies_info)
        self.movie_text.config(state='disabled')

        #formatted_movie_stats = "\n".join(f"{key}:\n  " + "\n  ".join(f"{k} {v}" for k, v in value.items()) if isinstance(value, dict) else f"{key}: {value}"for key, value in movie_stats.items())
        self.movie_stats_text.config(state='normal')
        self.movie_stats_text.delete(1.0, tk.END)
        formatted_movie_stats = ""
        for key, value in movie_stats.items():
            if key == "Ratings":
                formatted_movie_stats += f"{key}:\n" + "\n".join(f"{k} {v}%" for k, v in value.items()) + "\n"
            else:
                formatted_movie_stats += f"{key}: {value}\n"
        #formatted_movie_stats = "\n".join(f"{key}: {value}" for key, value in movie_stats.items())
        self.movie_stats_text.insert(tk.END, formatted_movie_stats)
        self.movie_stats_text.config(state='disabled')

        # Update TV shows text area
        tv_shows_info = self.recommender.getTVList()  # Assuming this returns formatted TV show list
        tv_stats = self.recommender.getTVStats()  # Assuming this returns TV show statistics
        
        self.tv_text.config(state='normal')
        self.tv_text.delete(1.0, tk.END)
        self.tv_text.insert(tk.END, tv_shows_info)
        self.tv_text.config(state='disabled')

        
        self.tv_stats_text.config(state='normal')
        self.tv_stats_text.delete(1.0, tk.END)
        formatted_tv_stats = "\n".join(f"{key} : {value}" if not isinstance(value, dict) else f"{key}: \n" + "\n".join(f"  {k}  {v} " for k, v in value.items()) for key, value in tv_stats.items())
        self.tv_stats_text.insert(tk.END, formatted_tv_stats)
        self.tv_stats_text.config(state='disabled')
        
    def loadBooks(self):
        # Load book data from the Recommender object
        self.recommender.loadBooks()  # Assuming this method populates self.recommender.books

        # Update books text area
        books_info = self.recommender.getBookList()  # Assuming this returns formatted book list
        book_stats = self.recommender.getBookStats()  # Assuming this returns book statistics

        self.books_text.config(state='normal')
        self.books_text.delete(1.0, tk.END)
        self.books_text.insert(tk.END, books_info)
        self.books_text.config(state='disabled')

        self.books_stats_text.config(state='normal')
        self.books_stats_text.delete(1.0, tk.END)
        formatted_stats = "\n".join(f"{key}:{value}" for key, value in book_stats.items())
        self.books_stats_text.insert(tk.END, formatted_stats)
        self.books_stats_text.config(state='disabled')

    def loadAssociations(self):
        self.recommender.loadAssociations()

    def creditInfoBox(self):
        messagebox.showinfo("Credits", "Developed by: Jaikishan Patel & Hrushikesha Mewada \nCompletion Date: 05-05-2024")

    def search_shows(self):
        type = self.type_combobox.get()
        title = self.title_entry.get() 
        director = self.director_entry.get()
        actor = self.actor_entry.get()
        genre = self.genre_entry.get()

        results = self.recommender.searchTVMovies(type, title, director, actor, genre)
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, results)
        self.results_text.config(state='disabled')

    def search_books(self):
        title = self.book_title_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()

        results = self.recommender.searchBooks(title, author, publisher)
        self.book_results_text.config(state='normal')
        self.book_results_text.delete(1.0, tk.END)
        self.book_results_text.insert(tk.END, results)
        self.book_results_text.config(state='disabled')


if __name__ == '__main__':
    RecommenderGUI()
