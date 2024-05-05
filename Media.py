# Media.py

class Media:
    def __init__(self, ID, title, average_rating):
        self.ID = ID
        self.title = title
        self.average_rating = average_rating

    # Accessor methods
    def get_ID(self):
        return self.ID

    def get_title(self):
        return self.title

    def get_average_rating(self):
        return self.average_rating

    # Mutator methods
    def set_ID(self, ID):
        self.ID = ID

    def set_title(self, title):
        self.title = title

    def set_average_rating(self, average_rating):
        self.average_rating = average_rating