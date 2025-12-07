class Book:
    """A class representing a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Constructor: initialize book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for readability."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
