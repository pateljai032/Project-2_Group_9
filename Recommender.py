import tkinter as tk
from tkinter import filedialog
import csv
from Book import Book
from Show import Show
from collections import Counter
from tkinter import messagebox


class Recommender:
    def __init__(self):
        self.books = {}
        self.shows = {}
        self.associations = {}

    def loadBooks(self):
        root = tk.Tk()
        root.withdraw()

        while True:
            file_path = filedialog.askopenfilename(title="Select a book file",
                                                   filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
            if file_path:
                try:
                    with open(file_path, newline='', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            book = Book(
                                row['bookID'],
                                row['title'],
                                float(row['average_rating']),
                                row['authors'],
                                row['isbn'],
                                row['isbn13'],
                                row['language_code'],
                                int(row['num_pages']),
                                int(row['ratings_count']),
                                row['publication_date'],
                                row['publisher']
                            )
                            self.books[book.get_ID()] = book
                    break
                except FileNotFoundError:
                    print("File not found. Please try again.")
                except KeyError as e:
                    print(f"Missing expected column: {e}. Please try again.")
                except ValueError as e:
                    print(f"Invalid data encountered: {e}. Please try again.")
                except Exception as e:
                    print(f"An error occurred: {e}. Please try again.")
            else:
                print("No file selected. Please select a file.")

        root.destroy()

    def loadShows(self):
        root = tk.Tk()
        root.withdraw()

        while True:
            file_path = filedialog.askopenfilename(title="Select a show file",
                                                   filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
            if file_path:
                try:
                    with open(file_path, newline='', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            show = Show(
                                row['show_id'],
                                row['title'],
                                float(row['average_rating']),
                                row['type'],
                                row['director'],
                                row['cast'],
                                row['country'],
                                row['date_added'],
                                row['release_year'],
                                row['rating'],
                                row['duration'],
                                row['listed_in'],
                                row['description']
                            )
                            self.shows[show.get_ID()] = show
                    break
                except FileNotFoundError:
                    print("File not found. Please try again.")
                except KeyError as e:
                    print(f"Missing expected column: {e}. Please try again.")
                except ValueError as e:
                    print(f"Invalid data encountered: {e}. Please try again.")
                except Exception as e:
                    print(f"An error occurred: {e}. Please try again.")
            else:
                print("No file selected. Please select a file.")

        root.destroy()

    def loadAssociations(self):
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        while True:
            file_path = filedialog.askopenfilename(title="Select an association file",
                                                   filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
            if file_path:
                try:
                    with open(file_path, newline='', encoding='utf-8') as csvfile:
                        reader = csv.reader(csvfile)
                        for row in reader:
                            id1, id2 = row

                            # Update dictionary for id1
                            if id1 not in self.associations:
                                self.associations[id1] = {}
                            if id2 in self.associations[id1]:
                                self.associations[id1][id2] += 1
                            else:
                                self.associations[id1][id2] = 1

                            # Update dictionary for id2
                            if id2 not in self.associations:
                                self.associations[id2] = {}
                            if id1 in self.associations[id2]:
                                self.associations[id2][id1] += 1
                            else:
                                self.associations[id2][id1] = 1
                    break
                except FileNotFoundError:
                    print("File not found. Please try again.")
                except Exception as e:
                    print(f"An error occurred: {e}. Please try again.")
            else:
                print("No file selected. Please select a file.")

        root.destroy()

    # Additional methods will be implemented based on further instructions

    def getMovieList(self):
        movies = [(show.get_title(), show.get_duration())
                  for show in self.shows.values()
                  if show.get_type_of_show() == 'Movie']

        # Determine column widths
        max_title_length = max(len("Title"), max(len(title) for title, _ in movies))
        max_runtime_length = max(len("Runtime"), max(len(runtime) for _, runtime in movies))

        # Prepare the header
        header = f"{'Title'.ljust(max_title_length)}  {'Runtime'.ljust(max_runtime_length)}"

        # Prepare the rows
        rows = [f"{title.ljust(max_title_length)}  {runtime.ljust(max_runtime_length)}"
                for title, runtime in movies]

        # Combine header and rows
        result = [header] + rows
        return "\n".join(result)

    def getTVList(self):
        # Filter TV shows
        tv_shows = [(show.get_title(), show.get_duration())
                    for show in self.shows.values()
                    if show.get_type_of_show() == 'TV Show']

        # Determine column widths
        max_title_length = max(len("Title"), max(len(title) for title, _ in tv_shows))
        max_seasons_length = max(len("Seasons"), max(len(duration) for _, duration in tv_shows))

        # Prepare the header
        header = f"{'Title'.ljust(max_title_length)}  {'Seasons'.ljust(max_seasons_length)}"

        # Prepare the rows
        rows = [f"{title.ljust(max_title_length)}  {duration.ljust(max_seasons_length)}"
                for title, duration in tv_shows]

        # Combine header and rows
        result = [header] + rows
        return "\n".join(result)

    def getBookList(self):
        # Prepare book data
        books = [(book.get_title(), book.get_authors()) for book in self.books.values()]

        # Determine column widths
        max_title_length = max(len("Title"), max(len(title) for title, _ in books))
        max_authors_length = max(len("Author(s)"), max(len(authors) for _, authors in books))

        # Prepare the header
        header = f"{'Title'.ljust(max_title_length)}  {'Author(s)'.ljust(max_authors_length)}"

        # Prepare the rows
        rows = [f"{title.ljust(max_title_length)}  {authors.ljust(max_authors_length)}"
                for title, authors in books]

        # Combine header and rows
        result = [header] + rows
        return "\n".join(result)

    def getMovieStats(self):
        movie_ratings = Counter()
        total_duration = 0
        director_counter = Counter()
        actor_counter = Counter()
        genre_counter = Counter()

        movie_count = 0
        for show in self.shows.values():
            if show.get_type_of_show() == 'Movie':
                movie_count += 1
                movie_ratings[show.get_rating()] += 1
                duration_str = show.get_duration()
                try:
                    duration_minutes = int(duration_str.split()[0])
                    total_duration += duration_minutes
                except ValueError:
                    continue
                director_counter.update(show.get_director().split(", "))
                actor_counter.update(show.get_cast().split(", "))
                genre_counter.update(show.get_listed_in().split(", "))

        if movie_count == 0:
            return "No movies found."

        rating_percentage = {
            rating: f"{count / movie_count * 100:.2f}%"
            for rating, count in movie_ratings.items()
        }
        average_duration = total_duration / movie_count
        most_directed = director_counter.most_common(1)
        most_directed_name = most_directed[0][0] if most_directed else "N/A"
        most_acted = actor_counter.most_common(1)
        most_acted_name = most_acted[0][0] if most_acted else "N/A"
        most_genres = genre_counter.most_common(1)

        
        
        stats = {
            "Rating Percentages": rating_percentage,
            "Average Duration (minutes)": f"{average_duration:.2f}",
            "Most Movie/Show Directed By": most_directed_name, #most_directed[0][0] if most_directed else "N/A",
            "Most Prolific Actor ": most_acted_name, #most_acted[0][0] if most_acted else "N/A",
            "Most Frequent Genre": most_genres[0][0] if most_genres else "N/A"
        }

        return stats


    def getTVStats(self):
        tv_ratings = Counter()
        total_seasons = 0
        actor_counter = Counter()
        genre_counter = Counter()

        tv_show_count = 0
        for show in self.shows.values():
            if show.get_type_of_show() == 'TV Show':
                tv_show_count += 1
                tv_ratings[show.get_rating()] += 1
                try:
                    seasons = int(show.get_duration().split()[0])
                    total_seasons += seasons
                except ValueError:
                    continue
                actor_counter.update(show.get_cast().split(", "))
                genre_counter.update(show.get_listed_in().split(", "))

        if tv_show_count == 0:
            return "No TV shows found."

        rating_percentage = {
            rating: f"{count / tv_show_count * 100:.2f}%"
            for rating, count in tv_ratings.items()
        }
        average_seasons = total_seasons / tv_show_count
        most_acted = actor_counter.most_common(1)
        most_genres = genre_counter.most_common(1)

        stats = {
            "Rating": rating_percentage,
            "\nAverage Number of Seasons": f"{average_seasons:.2f}",
            "\nMost Acted By": most_acted[0][0] if most_acted else "N/A",
            "\nMost Common Genre": most_genres[0][0] if most_genres else "N/A"
        }

        return stats

    def getBookStats(self):
        total_pages = 0
        author_counter = Counter()
        publisher_counter = Counter()

        book_count = len(self.books)
        for book in self.books.values():
            total_pages += book.get_num_pages()
            author_counter.update(book.get_authors().split(", "))
            publisher_counter[book.get_publisher()] += 1

        if book_count == 0:
            return "No books found."

        average_page_count = total_pages / book_count
        most_written = author_counter.most_common(1)
        most_published = publisher_counter.most_common(1)

        stats = {
            "Average Page Count ": f" {average_page_count:.2f} Pages",
            "\nMost Books Written By ":  most_written[0][0] if most_written else "N/A",
            "\nMost Books Published By ":  most_published[0][0] if most_published else "N/A"
        }

        return stats

    def searchTVMovies(self, media_type, title, director, actor, genre):
        # Validate media type
        if media_type not in ['Movie', 'TV Show']:
            messagebox.showerror("Error", "Please select 'Movie' or 'TV Show' from Type first.")
            return "No Results"

        # Validate search criteria
        if not any([title, director, actor, genre]):
            messagebox.showerror("Error",
                                 "Please enter information for the Title, Director, Actor, and/or Genre first.")
            return "No Results"

        # Search for matching shows
        matches = []
        for show in self.shows.values():
            if show.get_type_of_show() == media_type:
                if title and title not in show.get_title():
                    continue
                if director and director not in show.get_director():
                    continue
                if actor and actor not in show.get_cast():
                    continue
                if genre and genre not in show.get_listed_in():
                    continue
                matches.append(show)

        # Format output
        if not matches:
            return "No Results"

        max_title_length = max(len("Title"), max(len(show.get_title()) for show in matches))
        max_director_length = max(len("Director"), max(len(show.get_director()) for show in matches))
        max_actor_length = max(len("Actors"), max(len(show.get_cast()) for show in matches))
        max_genre_length = max(len("Genre"), max(len(show.get_listed_in()) for show in matches))

        header = f"{'Title'.ljust(max_title_length)}  {'Director'.ljust(max_director_length)}  {'Actors'.ljust(max_actor_length)}  {'Genre'.ljust(max_genre_length)}"
        rows = [
            f"{show.get_title().ljust(max_title_length)}  {show.get_director().ljust(max_director_length)}  {show.get_cast().ljust(max_actor_length)}  {show.get_listed_in().ljust(max_genre_length)}"
            for show in matches]

        result = [header] + rows
        return "\n".join(result)

    def searchBooks(self, title, author, publisher):
        # Validate search criteria
        if not any([title, author, publisher]):
            messagebox.showerror("Error", "Please enter information for the Title, Author, and/or Publisher first.")
            return "No Results"

        # Search for matching books
        matches = []
        for book in self.books.values():
            if title and title not in book.get_title():
                continue
            if author and author not in book.get_authors():
                continue
            if publisher and publisher not in book.get_publisher():
                continue
            matches.append(book)

        # Format output
        if not matches:
            return "No Results"

        max_title_length = max(len("Title"), max(len(book.get_title()) for book in matches))
        max_author_length = max(len("Author"), max(len(book.get_authors()) for book in matches))
        max_publisher_length = max(len("Publisher"), max(len(book.get_publisher()) for book in matches))

        header = f"{'Title'.ljust(max_title_length)}  {'Author'.ljust(max_author_length)}  {'Publisher'.ljust(max_publisher_length)}"
        rows = [
            f"{book.get_title().ljust(max_title_length)}  {book.get_authors().ljust(max_author_length)}  {book.get_publisher().ljust(max_publisher_length)}"
            for book in matches]

        result = [header] + rows
        return "\n".join(result)

    def getRecommendations(self, type_, title):
        recommendations = []
        if type_ in ['Movie', 'TV Show']:
            for show_id, show in self.shows.items():
                if show.get_title() == title:
                    associated_books = self.associations.get(show_id, {})
                    for book_id in associated_books:
                        book = self.books.get(book_id)
                        if book:
                            recommendations.append(book)
                    break
            else:
                messagebox.showwarning("Warning", "No recommendations for that title.")
                return "No results"
        elif type_ == 'Book':
            for book_id, book in self.books.items():
                if book.get_title() == title:
                    associated_shows = self.associations.get(book_id, {})
                    for show_id in associated_shows:
                        show = self.shows.get(show_id)
                        if show:
                            recommendations.append(show)
                    break
            else:
                messagebox.showwarning("Warning", "No recommendations for that title.")
                return "No results"
        else:
            messagebox.showwarning("Warning", "Invalid type specified.")
            return "No results"

        if not recommendations:
            messagebox.showwarning("Warning", "No recommendations found.")
            return "No results"

        max_title_length = max(len("Title"), max(len(rec.get_title()) for rec in recommendations))
        if recommendations and any(hasattr(rec, 'get_director') for rec in recommendations):
            max_director_length = max(len("Director"), max(len(rec.get_director()) for rec in recommendations if hasattr(rec, 'get_director')))
        else:
            max_director_length = len("Director")  # Default to the length of the string "Director" if no valid director data

        #max_director_length = max(len("Director"), max(len(rec.get_director()) for rec in recommendations if hasattr(rec, 'get_director')))

        if recommendations and any(hasattr(rec, 'get_cast') for rec in recommendations):
            max_actor_length = max(len("Actors"), max(len(rec.get_cast()) for rec in recommendations if hasattr(rec, 'get_cast')))
        else:
            max_actor_length = len("Actors")

        #max_actor_length = max(len("Actors"),max(len(rec.get_cast()) for rec in recommendations if hasattr(rec, 'get_cast')))

        if recommendations and any(hasattr(rec, 'get_listed_in') for rec in recommendations):
            max_genre_length = max(len("Genre"), max(len(rec.get_listed_in()) for rec in recommendations if hasattr(rec, 'get_listed_in')))
        else:
            max_genre_length = len("Genre")


        #max_genre_length = max(len("Genre"), max(len(rec.get_listed_in()) for rec in recommendations if hasattr(rec, 'get_listed_in')))

        if recommendations and any(hasattr(rec, 'get_authors') for rec in recommendations):
            max_author_length = max(len("Author"), max(len(rec.get_authors()) for rec in recommendations if hasattr(rec, 'get_authors')))
        else:
            max_author_length = len("Author")


        #max_author_length = max(len("Author"),max(len(rec.get_authors()) for rec in recommendations if hasattr(rec, 'get_authors')))

        if recommendations and any(hasattr(rec, 'get_publisher') for rec in recommendations):
            max_publisher_length = max(len("Publisher"), max(len(rec.get_publisher()) for rec in recommendations if hasattr(rec, 'get_publisher')))
        else:
            max_publisher_length = len("Publisher")

        #max_publisher_length = max(len("Publisher"), max(len(rec.get_publisher()) for rec in recommendations if hasattr(rec, 'get_publisher')))

        header = f"{'Title'.ljust(max_title_length)}  {'Director'.ljust(max_director_length)}  {'Actors'.ljust(max_actor_length)}  {'Genre'.ljust(max_genre_length)}  {'Author'.ljust(max_author_length)}  {'Publisher'.ljust(max_publisher_length)}"
        rows = []
        for rec in recommendations:
            title = rec.get_title().ljust(max_title_length)
            director = (rec.get_director().ljust(max_director_length) if hasattr(rec, 'get_director') else "").ljust(
                max_director_length)
            actors = (rec.get_cast().ljust(max_actor_length) if hasattr(rec, 'get_cast') else "").ljust(
                max_actor_length)
            genre = (rec.get_listed_in().ljust(max_genre_length) if hasattr(rec, 'get_listed_in') else "").ljust(
                max_genre_length)
            author = (rec.get_authors().ljust(max_author_length) if hasattr(rec, 'get_authors') else "").ljust(
                max_author_length)
            publisher = (
                rec.get_publisher().ljust(max_publisher_length) if hasattr(rec, 'get_publisher') else "").ljust(
                max_publisher_length)
            row = f"{title}  {director}  {actors}  {genre}  {author}  {publisher}"
            rows.append(row)

        result = [header] + rows
        return "\n".join(result)
    
    
    # def get_movie_ratings(self):
    #     """Calculate the percentage of each rating category for movies."""
    #     ratings = {}
    #     total_count = 0
    #     for movie in self.shows['movies']:
    #         ratings[movie['rating']] = ratings.get(movie['rating'], 0) + 1
    #         total_count += 1

    #     # Convert counts to percentages
    #     for rating in ratings:
    #         ratings[rating] = (ratings[rating] / total_count) * 100

    #     return ratings

    # def get_tv_ratings(self):
    #     """Calculate the percentage of each rating category for TV shows."""
    #     ratings = {}
    #     total_count = 0
    #     for show in self.shows['tv_shows']:
    #         ratings[show['rating']] = ratings.get(show['rating'], 0) + 1
    #         total_count += 1

    #     # Convert counts to percentages
    #     for rating in ratings:
    #         ratings[rating] = (ratings[rating] / total_count) * 100

    #     return ratings
