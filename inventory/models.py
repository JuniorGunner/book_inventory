class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password


class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages


class Review:  # TODO: bound book info to review post (title, author, etc.)
    def __init__(self, title, text, date_time):
        self.title = title
        self.text = text
        self.date_time = date_time
