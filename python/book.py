class Publisher:
	def __init__(self, name):
		self.name = name

class Book(Publisher):
	def __init__(self, name, title, author):
		super().__init__(name) # Invoking the base class (Publisher) constructor
		self.title = title
		self.author = author

	def display_info(self):
		print("Publisher:", self.name)

		print("Title:", self.title)
		print("Author:", self.author)

class Python(Book):
	def __init__(self, name, title, author, price, no_of_pages):
		super().__init__(name, title, author) # Invoking the base class (Book) constructor
		self.price = price
		self.no_of_pages = no_of_pages

	def display_info(self): # Method overriding
		super().display_info() # Invoking the base class (Book) method
		print("Price:", self.price)
		print("Number of Pages:", self.no_of_pages)

# Example usage:
python_book = Python("O'Reilly","Python Crash Course","Eric Matthes", 29.99,544)
python_book.display_info()
