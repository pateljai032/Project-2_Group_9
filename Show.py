# Show.py

from Media import Media

class Show(Media):
    def __init__(self, show_id, title, average_rating, type_of_show, director,
                 cast, country, date_added, release_year, rating, duration,
                 listed_in, description):
        # Columns from data
        # - show_id: Unique identifier for the show
        # - title: Title of the show
        # - average_rating: Average rating of the show
        # - type_of_show: Type of the show (e.g., movie or series)
        # - director: Director(s) of the show
        # - cast: Actors in the show
        # - country: Country where the show was produced
        # - date_added: Date the show was added
        # - release_year: Year the show was released
        # - rating: Rating of the show (e.g., PG-13, R)
        # - duration: Duration of the show
        # - listed_in: Genres or categories of the show
        # - description: Description of the show

        super().__init__(show_id, title, average_rating)
        self.type_of_show = type_of_show
        self.director = director
        self.cast = cast
        self.country = country
        self.date_added = date_added
        self.release_year = release_year
        self.rating = rating
        self.duration = duration
        self.listed_in = listed_in
        self.description = description

    # Accessor methods
    def get_type_of_show(self):
        return self.type_of_show

    def get_director(self):
        return self.director

    def get_cast(self):
        return self.cast

    def get_country(self):
        return self.country

    def get_date_added(self):
        return self.date_added

    def get_release_year(self):
        return self.release_year

    def get_rating(self):
        return self.rating

    def get_duration(self):
        return self.duration

    def get_listed_in(self):
        return self.listed_in

    def get_description(self):
        return self.description

    # Mutator methods
    def set_type_of_show(self, type_of_show):
        self.type_of_show = type_of_show

    def set_director(self, director):
        self.director = director

    def set_cast(self, cast):
        self.cast = cast

    def set_country(self, country):
        self.country = country

    def set_date_added(self, date_added):
        self.date_added = date_added

    def set_release_year(self, release_year):
        self.release_year = release_year

    def set_rating(self, rating):
        self.rating = rating

    def set_duration(self, duration):
        self.duration = duration

    def set_listed_in(self, listed_in):
        self.listed_in = listed_in

    def set_description(self, description):
        self.description = description