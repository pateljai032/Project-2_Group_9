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
    """
        A graphical user interface for the Media Recommender System using Tkinter.

        This class sets up the main window and tabs for the application, allowing the
        user to interact with various functionalities such as viewing media lists,
        searching for specific media, and getting recommendations based on media types.

        Attributes:
            recommender (Recommender): An instance of the Recommender class to manage the
                                       recommendation logic.
        """
    def __init__(self):
        self.recommender = Recommender()  # Create an instance of the Recommender class

        # Set up the main window
        self.root = tk.Tk() #root (tk.Tk): The main window of the application.
        self.root.title("Media Recommender System")
        self.root.geometry("1200x800")  # Set the dimensions of the window

        # Create a notebook widget to manage tabs
        self.notebook = ttk.Notebook(self.root) #notebook (ttk.Notebook): A notebook widget to manage different tabs within the GUI.
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
        """
            Sets up the tab for managing movie displays within the GUI.

            This method creates a dedicated tab for movies in the notebook widget. It includes
            two text widgets, one for displaying movie titles and runtimes, and another for
            displaying movie statistics. The content of these widgets is dynamically populated
            based on the data loaded into the recommender system.

            The method ensures that if no data is loaded, it displays a placeholder message
            indicating that no movie data is available yet. This function is called during the
            initialization of the GUI to set up the movies tab.
            """
        # Create a tab for movies
        movie_tab = ttk.Frame(self.notebook)
        self.notebook.add(movie_tab, text="Movies")

        # Initialize a text widget for displaying movie titles and runtimes.
        # This widget is initially disabled to prevent user edits.
        self.movie_text = tk.Text(movie_tab, height=10, width=100, state='disabled')
        self.movie_text.pack(pady=10, padx=10,expand=True, fill='both')

        # Initialize a second text widget for displaying movie statistics.
        # Similar to the first, it is also disabled to prevent user edits.
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
        """
        Sets up the TV shows tab in the GUI.

        This method creates a tab within the notebook widget specifically for TV shows.
        It includes two text widgets: one for displaying TV show titles and their respective
        seasons, and another for showing statistical data about the TV shows. The content of
        these widgets is filled based on the data loaded into the recommender system. If no
        data is available, a placeholder message is displayed.

        Attributes:
            tv_tab (ttk.Frame): The tab frame for TV shows in the notebook.
            tv_text (tk.Text): Text widget for displaying TV show titles and seasons.
            tv_stats_text (tk.Text): Text widget for displaying statistics about TV shows.
        """
        # Create a tab for TV shows
        tv_tab = ttk.Frame(self.notebook)
        self.notebook.add(tv_tab, text="TV Shows")
        
        # Initialize a text widget for displaying TV show titles and seasons.
        # This widget is initially disabled to prevent user edits.
        self.tv_text = tk.Text(tv_tab, width=100, height=10, state='disabled')
        self.tv_text.pack(pady=10, padx=10, expand=True, fill='both')

        # Initialize a second text widget for displaying TV show statistics.
        # Similarly, it is also disabled to prevent user edits.
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
        """
            Sets up the books tab in the GUI.

            This method creates a tab within the notebook widget specifically for books.
            It includes two scrolled text widgets: one for displaying book titles and associated
            information, and another for showing statistical data about the books. The content of
            these widgets is filled based on the data loaded into the recommender system. If no
            data is available, a placeholder message is displayed.

            Attributes:
                tab (ttk.Frame): The tab frame for books in the notebook.
                books_text (scrolledtext.ScrolledText): Scrolled text widget for displaying book titles and information.
                books_stats_text (scrolledtext.ScrolledText): Scrolled text widget for displaying statistics about books.
            """
        # Create a new frame (tab) for books and add it to the notebook
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Books")

        # Initialize a scrolled text widget for displaying book titles and information.
        # This widget is initially disabled to prevent user edits.
        self.books_text = scrolledtext.ScrolledText(tab, width=100, height=10, state='disabled')
        self.books_text.pack(pady=10, padx=10, fill='both', expand=True)

        # Initialize a second scrolled text widget for displaying book statistics.
        # It is also disabled to prevent user edits.
        self.books_stats_text = scrolledtext.ScrolledText(tab, width=100, height=10, state='disabled')
        self.books_stats_text.pack(pady=10, padx=10, fill='both', expand=True)

        # Check if any book data is available in the recommender system
        if self.recommender.books:
            # Enable the book text widget, insert the book list, and then disable it again
            self.books_text.config(state='normal')
            self.books_text.insert('end', self.recommender.getBookList())
            self.books_text.config(state='disabled')
            # Enable the book statistics text widget, insert the statistics, and disable it again
            self.books_stats_text.config(state='normal')
            self.books_stats_text.insert('end', str(self.recommender.getBookStats()))
            self.books_stats_text.config(state='disabled')
        else:
            # If no book data or statistics are available, display a placeholder message
            self.books_text.config(state='normal')
            self.books_text.insert('end', 'No book data loaded yet.')
            self.books_stats_text.insert('end', 'No book statistics available.')

    def setup_search_tv_movies_tab(self):
        """
            Sets up the search tab for TV shows and movies in the GUI.

            This method creates a tab within the notebook widget specifically for searching TV shows
            and movies. It includes various entry fields for user inputs such as type, title, director,
            actor, and genre. A search button initiates the search based on the provided criteria, and
            results are displayed in a scrolled text widget.

            Attributes:
                tab (ttk.Frame): The tab frame for searching TV shows and movies in the notebook.
                type_combobox (ttk.Combobox): Dropdown menu for selecting the type (Movie or TV Show).
                title_entry (ttk.Entry): Entry widget for inputting the title.
                director_entry (ttk.Entry): Entry widget for inputting the director's name.
                actor_entry (ttk.Entry): Entry widget for inputting actor names.
                genre_entry (ttk.Entry): Entry widget for inputting the genre.
                results_text (scrolledtext.ScrolledText): Scrolled text widget for displaying search results.
            """
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Search TV/Movies")

        # Create entry fields and labels
        tk.Label(tab, text="Type:").pack(pady=(10, 0))
        self.type_combobox = ttk.Combobox(tab, values=["Movie", "TV Show"], state="readonly")
        self.type_combobox.pack(fill='x', padx=20)

        # Setup label and entry for inputting the title
        tk.Label(tab, text="Title:").pack()
        self.title_entry = ttk.Entry(tab)
        self.title_entry.pack(fill='x', padx=20)

        # Setup label and entry for inputting the director's name
        tk.Label(tab, text="Director:").pack()
        self.director_entry = ttk.Entry(tab)
        self.director_entry.pack(fill='x', padx=20)

        # Setup label and entry for inputting actor names

        tk.Label(tab, text="Actor:").pack()
        self.actor_entry = ttk.Entry(tab)
        self.actor_entry.pack(fill='x', padx=20)

        # Setup label and entry for inputting the genre

        tk.Label(tab, text="Genre:").pack()
        self.genre_entry = ttk.Entry(tab)
        self.genre_entry.pack(fill='x', padx=20)

        # Search button
        ttk.Button(tab, text="Search", command=self.search_shows).pack(pady=10)

        # Result area
        self.results_text = scrolledtext.ScrolledText(tab, width=100, height=15, state='disabled')
        self.results_text.pack(pady=10, padx=10, fill='both', expand=True)

    def setup_search_books_tab(self):
        """
            Sets up the search tab for books in the GUI.

            This method creates a tab within the notebook widget specifically for searching books.
            It includes entry fields for user inputs such as book title, author, and publisher.
            A search button initiates the search based on the provided criteria, and results are
            displayed in a scrolled text widget.

            Attributes:
                tab (ttk.Frame): The tab frame for searching books in the notebook.
                book_title_entry (ttk.Entry): Entry widget for inputting the book title.
                author_entry (ttk.Entry): Entry widget for inputting the author's name.
                publisher_entry (ttk.Entry): Entry widget for inputting the publisher's name.
                book_results_text (scrolledtext.ScrolledText): Scrolled text widget for displaying search results.
            """
        # Create a new frame (tab) for searching books and add it to the notebook
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Search Books")

        # Create entry fields and labels
        tk.Label(tab, text="Title:").pack()
        self.book_title_entry = ttk.Entry(tab)
        self.book_title_entry.pack(fill='x', padx=20)

        # Setup label and entry for inputting the author's name
        tk.Label(tab, text="Author:").pack()
        self.author_entry = ttk.Entry(tab)
        self.author_entry.pack(fill='x', padx=20)

        # Setup label and entry for inputting the publisher's name
        tk.Label(tab, text="Publisher:").pack()
        self.publisher_entry = ttk.Entry(tab)
        self.publisher_entry.pack(fill='x', padx=20)

        # Setup a button for initiating the search
        ttk.Button(tab, text="Search", command=self.search_books).pack(pady=10)

        # Result area
        self.book_results_text = scrolledtext.ScrolledText(tab, width=100, height=15, state='disabled')
        self.book_results_text.pack(pady=10, padx=10, fill='both', expand=True)

    def setup_recommendations_tab(self):
        """
            Sets up the recommendations tab in the GUI.

            This method creates a tab within the notebook widget specifically for obtaining recommendations.
            It includes a dropdown menu to select the type of media (Movie, TV Show, Book), an entry field
            to input the title of the media, and a button to trigger the recommendation process. The results
            are displayed in a scrolled text widget.

            Attributes:
                tab (ttk.Frame): The tab frame for recommendations in the notebook.
                recommendation_type (ttk.Combobox): Dropdown menu for selecting the type of media.
                recommendation_title (ttk.Entry): Entry widget for inputting the media title.
                recommendation_results (scrolledtext.ScrolledText): Scrolled text widget for displaying recommendation results.
            """
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
        """
        Retrieves and displays recommendations based on the user's input for media type and title.

        This method fetches recommendations by interacting with the 'recommender' system based on
        the media type and title specified by the user through the GUI. It displays an error message
        if the title field is empty, otherwise, it proceeds to fetch and display the recommendations.
        The results are shown in a scrolled text widget which is temporarily enabled for updates.

        Raises:
            tk.messagebox: Shows an error dialog if the title field is empty, prompting the user to enter a title.
        """
        # Get the selected media type and the entered title from the GUI components
        type = self.recommendation_type.get()
        title = self.recommendation_title.get()
        # Check if the title is not entered and display an error if so
        if not title:
            messagebox.showerror("Error", "Please enter a title to receive recommendations.")
            return
        # Obtain recommendations from the recommender system based on the input type and title
        results = self.recommender.getRecommendations(type, title)
        # Enable the results text widget, clear it, insert new results, and disable it again
        self.recommendation_results.config(state='normal')
        self.recommendation_results.delete(1.0, tk.END)# Clear existing contents
        self.recommendation_results.insert(tk.END, results)# Insert new results
        self.recommendation_results.config(state='disabled')# Disable the widget to prevent user edits

    def setup_buttons(self):
        """
            Sets up various operational buttons at the bottom of the GUI.

            This method adds a frame to the main window that contains buttons for loading shows,
            books, recommendations, viewing informational credits, and quitting the application.
            Each button is configured with appropriate commands linked to their respective functionalities.

            The layout ensures that the 'Quit' button is always on the far right, while other buttons
            are aligned to the left, providing an organized visual structure.
            """
        # Create a frame to hold the buttons and pack it at the bottom of the window
        frame = tk.Frame(self.root)
        frame.pack(side='bottom', fill='x')
        
        # Setup button for loading show data and define its position and padding
        tk.Button(frame, text="Load Shows", command=self.loadShows).pack(side='left',padx=30,pady=10)
        # Setup button for loading book data and define its position and padding
        tk.Button(frame, text="Load Books", command=self.loadBooks).pack(side='left',padx=130,pady=10)
        # Setup button for loading associations/recommendations and define its position and padding
        tk.Button(frame, text="Load Recommendations", command=self.loadAssociations).pack(side='left',padx=130,pady=10)
        # Setup button for displaying credit information and define its position and padding
        tk.Button(frame, text="Information", command=self.creditInfoBox).pack(side='left',padx=130,pady=10)
        # Setup a quit button that terminates the application and define its position and padding
        tk.Button(frame, text="Quit", command=self.root.quit).pack(side='right',padx=30,pady=10)

    def loadShows(self):
        """
            Loads and updates the show data within the GUI.

            This method is responsible for fetching and displaying data for both movies and TV shows.
            It retrieves the data using methods from the Recommender object, then updates the GUI components
            to show this data, specifically formatted movie and TV show lists and their respective statistics.
            The text widgets for both movies and TV shows are enabled for updates and then disabled to prevent user edits.
            """
        
        # Load show data from the Recommender object
        self.recommender.loadShows()  # Assuming this method populates self.recommender.shows

        # Update movies text area
        movies_info = self.recommender.getMovieList()  # Assuming this returns formatted movie list
        movie_stats = self.recommender.getMovieStats()  # Assuming this returns movie statistics

        # Update the movie text widget with movie information
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

        # Retrieve and display formatted TV show list and statistics
        tv_shows_info = self.recommender.getTVList()  # Assuming this returns formatted TV show list
        tv_stats = self.recommender.getTVStats()  # Assuming this returns TV show statistics

        # Update the TV show text widget with TV show information
        self.tv_text.config(state='normal')
        self.tv_text.delete(1.0, tk.END)
        self.tv_text.insert(tk.END, tv_shows_info)
        self.tv_text.config(state='disabled')

        # Update the TV show statistics text widget with formatted statistics
        self.tv_stats_text.config(state='normal')
        self.tv_stats_text.delete(1.0, tk.END)
        formatted_tv_stats = "\n".join(f"{key} : {value}" if not isinstance(value, dict) else f"{key}: \n" + "\n".join(f"  {k}  {v} " for k, v in value.items()) for key, value in tv_stats.items())
        self.tv_stats_text.insert(tk.END, formatted_tv_stats)
        self.tv_stats_text.config(state='disabled')
        
    def loadBooks(self):
        """
        Loads and updates the book data within the GUI.

        This method interacts with the Recommender object to fetch and display data for books.
        It retrieves a list of books and their respective statistics from the Recommender object,
        then updates the GUI components to show this data. The text widgets for displaying book
        information and statistics are temporarily enabled for updates and then disabled to prevent
        user edits.

        Assumes:
            - self.recommender.loadBooks() populates self.recommender.books
            - self.recommender.getBookList() returns a formatted list of books
            - self.recommender.getBookStats() returns statistics for books
        """
        # Load book data from the Recommender object
        self.recommender.loadBooks()

        # Retrieve formatted list of books from the Recommender object format book statistics from the Recommender object
        books_info = self.recommender.getBookList()  
        book_stats = self.recommender.getBookStats()
        
        # Update the book text area with the retrieved information
        self.books_text.config(state='normal')
        self.books_text.delete(1.0, tk.END)
        self.books_text.insert(tk.END, books_info)
        self.books_text.config(state='disabled')

        # Retrieve and format book statistics from the Recommender object
        # Update the book statistics text area with formatted statistics
        self.books_stats_text.config(state='normal')
        self.books_stats_text.delete(1.0, tk.END)
        formatted_stats = "\n".join(f"{key}:{value}" for key, value in book_stats.items())
        self.books_stats_text.insert(tk.END, formatted_stats)
        self.books_stats_text.config(state='disabled')

    def loadAssociations(self):
        """
        Loads association data for media recommendations from the Recommender object.

        This method is responsible for invoking the loading mechanism of association data
        which links various media types like books, movies, and TV shows based on user interactions
        or other criteria. This data is crucial for the recommendation engine to function properly.

        Note: This method assumes that `self.recommender.loadAssociations()` effectively populates
        the necessary data structures within the Recommender object for later access.
        """
        # Load association data which is critical for generating accurate recommendations
        self.recommender.loadAssociations()

    def creditInfoBox(self):
        """
            Displays an informational messagebox with credits for the application.

            This method shows a simple dialog box containing the names of the developers and the completion date
            of the project. It's used to provide acknowledgment and transparency regarding the development of
            the software.

            The information shown includes:
            - Developer names: Jaikishan Patel & Hrushikesha Mewada
            - Completion Date: 05-05-2024
            """
        # Show an information dialog box with credits
        messagebox.showinfo("Credits", "Developed by: Jaikishan Patel & Hrushikesha Mewada \nCompletion Date: 05-05-2024")

    def search_shows(self):
        """
        Searches for TV shows or movies based on user input and updates the GUI with the results.

        This method retrieves user inputs for type, title, director, actor, and genre from the GUI.
        It then uses these inputs to query the Recommender system for matching TV shows or movies.
        The results are displayed in a text widget which is temporarily enabled for updates.

        The method ensures that the results text widget is disabled after updating to prevent
        user modifications, maintaining the integrity of the displayed data.
        """
        # Retrieve the user inputs from the GUI components
        type = self.type_combobox.get() # Type of show (Movie or TV Show)
        title = self.title_entry.get() # Title of the show or movie
        director = self.director_entry.get() # Director's name
        actor = self.actor_entry.get() # Actor's name
        genre = self.genre_entry.get() # Genre of the show or movie

        # Use the recommender system to search for shows or movies that match the user inputs
        results = self.recommender.searchTVMovies(type, title, director, actor, genre)

        # Update the results text widget with the search results
        self.results_text.config(state='normal') # Enable the text widget for updates
        self.results_text.delete(1.0, tk.END) # Clear existing content in the widget

        self.results_text.insert(tk.END, results) # Insert new search results
        self.results_text.config(state='disabled') # Disable the text widget to prevent user edits

    def search_books(self):
        """
        Searches for books based on user input and updates the GUI with the results.

        This method retrieves user inputs for the book title, author, and publisher from the GUI.
        It then uses these inputs to query the Recommender system for matching books. The results
        are displayed in a text widget which is temporarily enabled for updates.

        After displaying the results, the text widget is disabled to prevent user modifications,
        ensuring the integrity and immutability of the displayed information.

        """
        # Retrieve the user inputs from the GUI components for the search criteria
        title = self.book_title_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()

        # Use the recommender system to search for books that match the user inputs
        results = self.recommender.searchBooks(title, author, publisher)
        # Update the book results text widget with the search results
        self.book_results_text.config(state='normal')
        self.book_results_text.delete(1.0, tk.END)
        self.book_results_text.insert(tk.END, results)
        self.book_results_text.config(state='disabled')

#main function 
if __name__ == '__main__':
    RecommenderGUI()
