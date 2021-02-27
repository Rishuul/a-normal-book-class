all_books = []
book_publisher = {}
class Books:
	
	
	def __init__(self,book_name):
		self.book_name = book_name
		all_books.append(book_name)

	def get_book(self,book_name):
		return "Book: "
		return book_name.title()

	def add_book(self,book_name):
		print(f'Adding {book_name}....')
		
		if book_name not in all_books:
			all_books.append(book_name)
			print(f'{book_name} added successfully!')
		else:
			print(f'{book_name} already exists! Use function "show_book()" to get all the book\'s names.')
		
	def show_all_books(self):
		print('List of all the books: ')
		for books in all_books:
			print('{}'.format(books))

	def remove_book(self,book_name):
		print(f'Books before removal: {all_books}')
		if book_name in all_books:
			all_books.remove(book_name)
			print(f'{book_name} removed successfully.')
			print(f'Books after removal: {all_books}')
		else:
			print(f'{book_name} is not added! Please use "add_book()" function to add the book or check the list of all the books by doing "show_all_books()"')
			print(f'No books removed : {all_books}')

	def add_publisher(self,book_name,publisher_name):
		if book_name in all_books:
			print(f'Registering {book_name} with {publisher_name}.....')
			book_publisher[book_name] = publisher_name
			print(f'{publisher_name} has been successfully registered with book {book_name}')
		else:
			print(f'{book_name} is not added in the books list, I cannot assign a publisher to it!')

	def get_publisher(self,book_name):
		if book_name in book_publisher:
			for publisher in book_publisher.values():
				print(f'Publisher for {book_name} is {publisher}')
		else:
			print(f'{book_name} has not been registered yet!')


book_class = Books('Chemistry')
book_class.add_book('World of Science')
book_class.add_book('HC Verma')
book_class.add_publisher('World of Science','DINESH')
book_class.get_publisher('HC Verma')
book_class.get_publisher('World of Science')
book_class.remove_book('HC Verma')
book_class.show_all_books()

print(book_publisher)