from abc import ABC, abstractmethod
total = 0
# superclass
class Item(ABC):
    # constructor
    def __init__(self, title, author, price, date_of_published, item):
        self.title = title
        self.author = author
        self.price = price
        self.date_of_published = date_of_published
        self.item = item

    # Getter for author
    def get_author(self):
        return self.author  
    
    def get_title(self):
        return self.title  
    
    def get_price(self):
        return self.price

    # To print item's information
    def retrieving(self):
        print(
            f"\nThe title of this {self.item} is {self.title} , It's author is {self.author} ,It cost {self.price} and "
            f"published in {self.date_of_published}")

    @abstractmethod
    def tax_calculation(self):
        pass

    def sold(self):
        return "item has been sold"

    @abstractmethod
    def available(self):
        pass


# Book subclass
class Book(Item):
    # constructor
    def __init__(self, title, author, price, date_of_published, item, number_of_pages, isbn, category):
        super().__init__(title, author, price, date_of_published, item)
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.category = category

    # book info method
    def book_info(self):
        super().retrieving()
        print(f"Number of pages in this book is {self.number_of_pages} from {self.category} category ,"
              f" It's ISBN = {self.isbn}")

    # Setters for book's information
    def set_info(self, title, author, price, date_of_published, item, number_of_pages, isbn, category):
        self.title = title
        self.author = author
        self.price = price
        self.date_of_published = date_of_published
        self.item = item
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.category = category

    def tax_calculation(self):
        return self.price + (self.price * 0.14)

    def sold(self):
        return "Book has been sold"

    # To print available books in store
    def available(self):
        print("=================================")
        for x in book_names:
            print(x.title)
        print("=================================")    
    
    # To add a new book to the book list
    def add_book(self, new_book):
        book_names.append(new_book)
    
    # Search method
    def search(self):
        author = input("Enter author name: ").lower().split()    
        y = None
        for item in book_names:
            if item.get_author().lower().split() == author:
                y = author
        if y == author: 
                print(f"Found a book for {author}")
        else:
                print(f"There is no book for {author} in store")  

    def info(self):
        name_of_book = input("Enter the name of book: ").lower().split()
        s = None
        for item in book_names:
            if item.get_title().lower().split()  == name_of_book:
                s = name_of_book
                break
        if s == name_of_book:
            print(f"{item.book_info()}")
        else:
            print("There is no item with this name in store")  

# magazine subclass
class Magazine(Item):
    # constructor
    def __init__(self, title, author, price, date_of_published, item, issue_number, editor):
        super().__init__(title, author, price, date_of_published, item)
        self.issue_number = issue_number
        self.editor = editor

    # To print magazine info
    def magazine_info(self):
        super().retrieving()
        print(f"Issue Number: {self.issue_number} , Editor: {self.editor}")

    def tax_calculation(self):
        return self.price + (self.price * 0.14)

    def sold(self):
        return "magazine has been sold"

    # To show the available magazines in store
    def available(self):
        print("=================================")
        for z in magazine_names:
            print(z.title)
        print("=================================")          

    # To add magazine to magazine list
    def add_magazine(self, new_magazine):
        magazine_names.append(new_magazine)

    # Setters for magazine's information
    def set_info(self, title, author, price, date_of_published, item, issue_number, editor):
        self.title = title
        self.author = author
        self.price = price
        self.date_of_published = date_of_published
        self.item = item
        self.issue_number = issue_number
        self.editor = editor
    
    # Search method
    def search(self):
        author = input("Enter author name: ")    
        y = None
        for item in book_names:
            if item.get_author() == author:
                y = author
        if y == author: 
                print(f"We found a book for {author}")
        else:
                print(f"we don't found any book for {author}") 

    def info(self):
        name_of_magazine = input("Enter the name of magazine: ").lower().split()
        s = None
        for item in magazine_names:
            if item.get_title().lower().split() == name_of_magazine:
                s = name_of_magazine
                break
        if s == name_of_magazine:
            print(f"{item.magazine_info()}")
        else:
            print("we don't have this item in store")                        
                                
class test:
    def __init__(self):
        pass

# DVD subclass
class DVD(Item):
    # constructor
    def __init__(self, title, author, price, date_of_published, item, director, duration, genre):
        super().__init__(title, author, price, date_of_published, item)
        self.director = director
        self.duration = duration
        self.genre = genre

    # To print DVD info
    def dvd_info(self):
        super().retrieving()
        print(f"Director name: {self.director}\nDuration: {self.duration}\nGenre: {self.genre}")

    def tax_calculation(self):
        return self.price + (self.price * 0.14)

    def sold(self):
        return "DVD has been sold"

    # To show the available DVDs in store 
    def available(self):
        print("=================================")    
        for c in dvd_names:
            print(c.title)
        print("=================================")          

    # Setters for DVD's information
    def set_info(self, title, author, price, date_of_published, item, director, duration, genre):
        self.title = title
        self.author = author
        self.price = price
        self.date_of_published = date_of_published
        self.item = item
        self.director = director
        self.duration = duration
        self.genre = genre

    # To add DVD to DVDs list
    def add_dvd(self, new_dvd):
        dvd_names.append(new_dvd)

    # Search method
    def search(self):
        author = input("Enter author name: ")    
        y = None
        for item in book_names:
            if item.get_author() == author:
                y = author
        if y == author: 
                print(f"There is a DVD for {author}")
        else:
                print(f"we don't found any DVD for {author}")

    def info(self):
        name_of_dvd = input("Enter the name of DVD: ").lower().split()
        s = None
        for item in dvd_names:
            if item.get_title().lower().split()  == name_of_dvd:
                s = name_of_dvd
                break
        if s == name_of_dvd:
            print(f"{item.dvd_info()}")
        else:
            print("we don't have this item in store")                  

# class for shoppingcart
class ShoppingCart:
    total = 0
    def __init__(self):
        self.items = []
   
    # To add item to the cart
    def add_item(self, item_name):
        item = item_name
        self.items.append(item)
    # To remove item from cart
    def remove_item(self, item_index,item_price):
        x = self.items[item_index]
        self.items.remove(x)

    # To show the available items in cart
    def show(self):
        print(self.items) 
    # Check if cart is empty or not
    def empty(self):  
        if len(self.items) == 0 :
            return False
        else:
            return True 

# Set the total price to 0
total = 0

# Instances from book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 100, 1925, "book", 208, 9780743273565, "Tragedy")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 100, 1960, "book", 281, 9780061120084, "Domestic Fiction")
book3 = Book("1984", "George Orwell", 100, 1984, "book", 328, 9780452284234, "Science fiction")
book4 = Book("Pride and Prejudice", "Jane Austen", 100, 1813, "book", 400, 1843590543721, "Romantic novel of manners")
book5 = Book("The Catcher in the Rye", "J. D. Salinger", 100, 1951, "book", 309, 9780553149661, "realism")
book6 = Book("Harry Potter and the Sorcerer's Stone", "J. K. Rowling", 100, 1997, "book", 309, 1843590543721,
             "fantasy tale")
book7 = Book("The Lord of the Rings", "John Ronald Reuel Tolkien", 100, 1954, "book", 1178, 9780544003415,
             "Adventure fiction")
book8 = Book("Brave New World", "Aldous Huxley", 100, 1932, "book", 288, 9780060850524, "Dystopian Fiction")
book9 = Book("The Hobbit", "J. R. R. Tolkien", 100, 1937, "book", 310, 9780618002219, "Fantasy Adventure")
book10 = Book("Fahrenheit 451", "J. R. R. Tolkien", 100, 1953, "book", 158, 9780618257592, "Dystopian Science Fiction")



# Instances from DVD class
dvd1 = DVD("The Shawshank Redemption", "Stephen King", 100, "1994", "DVD", "Frank Darabont", "142 minutes", "Drama")
dvd2 = DVD("The Godfather", "Mario Puzo", 100, "1972", "DVD", "Francis Ford Coppola", "177 minutes", "Crime")
dvd3 = DVD("The Dark Knight", "Christopher Nolan", 100, "2008", "DVD", "Christopher Nolan", "152 minutes", "Action")
dvd4 = DVD("The Lord of the Rings: The Return of the King", "J.R.R. Tolkien", 100, "2003", "DVD", "Peter Jackson",
           "201 minutes", "Adventure")
dvd5 = DVD("Pulp Fiction", "Quentin Tarantino", 100, "1994", "DVD", "Quentin Tarantino", "154 minutes", "Crime")
dvd6 = DVD("Forrest Gump", "Winston Groom", 100, "1994", "DVD", "Robert Zemeckis", "142 minutes", "Drama")
dvd7 = DVD("Inception", "Christopher Nolan", 100, "2010", "DVD", "Christopher Nolan", "148 minutes", "Action")
dvd8 = DVD("The Matrix", "Lana Wachowski, Lilly Wachowski", 100, "1999", "DVD", "Lana Wachowski, Lilly Wachowski",
           "136 minutes", "Action")
dvd9 = DVD("Interstellar", "Jonathan Nolan", 100, "2014", "DVD", "Christopher Nolan", "169 minutes",
           "Adventure")
dvd10 = DVD("The Silence of the Lambs", "Thomas Harris", 100, "1991", "DVD", "Jonathan Demme", "118 minutes", "Crime")


# Instances from DVD class
magazine1 = Magazine("National Geographic", "Andrew Evans", 100, 1888, "magazine", 5478965412365, "Nathan Lump")
magazine2 = Magazine("Time", " Marc Benioff", 100, 1923, "magazine", 9874512347895, "Sam Jacobs")
magazine3 = Magazine("Vogue", "Anna Wintour", 100, 1892, "magazine", 9784120657892, "Dame Anna Wintour ")
magazine4 = Magazine("The New Yorker", "Harold Ross", 100, 1925, "magazine", 9124578632014, "David Remnick")
magazine5 = Magazine("Scientific American", "John Horgan", 100, 1845, "magazine", 9412578463254, "Laura Helmuth")
magazine6 = Magazine("Sports Illustrated", " Henry Luce", 100, 1954, "magazine", 9532647812985, "Mark Pesavento")
magazine7 = Magazine("People", " Geraldine Brooks", 100, 2008, "magazine", 2369784512365, "Wendy Naugle ")
magazine8 = Magazine("Python Automation", "Linda Martinez", 100, 2023, "magazine", 9845632014568, "Kate Roberts")
magazine9 = Magazine("Python Robotics", "Mike Adams", 100, 2023, "magazine", 9412368742569, "Larry Parker")
magazine10 = Magazine("Python Game Development", "Nancy King", 100, 2023, "magazine", 9236547810925,
                      "Oliver Reed")

# DVD's list (DVDs that available in store)
dvd_names = [dvd1,dvd2,dvd3,dvd4,dvd5,dvd6,dvd7,dvd8,dvd9,dvd10]

# magazine's list (magazines that available in store)
magazine_names = [magazine1,magazine2,magazine3,magazine4,magazine5,magazine6,magazine7,magazine8,magazine9,magazine10]

# Book's list (books that available in store)
book_names = [book1,book2,book3,book4,book5,book6,book7,book8,book9,book10]


# To Enter the username and password
x = input("Enter your username: ").strip().lower()
y = input("Enter password: ").strip()
if x == "ahmed" and int(y) == 123456 :

    command = 3
    print("\nWelcome back admin\n")
    while command != 4:
        # The interface of admin
        print("1-Books\n2-DVDs\n3-Magazines\n4-To go to customer view\n5-To Exit the program")
        try:
            command = int(input("Select section you want: "))
        except ValueError :
            print("ERROR Invaild input please enter an integer input")
        except Exception as e:
            print("An unexcpected error", e)    
        print("===============================")

        if command == 1:
                print("1-Available books\n2-Update a book information \n3-add book to store\n4-Delete a book from store")
                while True:
                    try:    
                        function = int(input("Type the opertaion number: "))
                        if 1 <= function <=4:
                            break
                    except ValueError :
                        print("ERROR Invaild input please enter an integer input: ")
                    except Exception as e:
                        print("An unexcpected error", e)  
                    print("===============================")
                if function == 1 :
                    print("The available books in bookstore: ")
                    book1.available()
            
                elif function == 2 : 
                        while True:
                            try:
                                # The order of book
                                order_of_book = int(input("Enter the order of book from 1 to 10: "))
                                if 1<= order_of_book<=10:
                                    break
                                else:
                                    print("out of range")
                            except ValueError :
                                print("ERROR Invaild input please enter an integer input: ")
                            except Exception as e:
                                print("An unexcpected error", e)  

                        # The updated information
                        new_title = input("Enter new title: ")
                        new_author = input("Enter the new name of author: ")
                        new_price = input("Enter the new price: ")
                        new_date_of_publish = input("Enter the date of publish: ")
                        new_item = input("Enter the item: ")
                        new_no_of_pages = input("Enter the no. of pages: ")
                        new_isbn = input("Enter the new isbn: ")
                        new_category = input("Enter the category: ")
                        print("===============================")
                        # Updating procedures
                        if order_of_book == 1:
                            book1.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_no_of_pages,
                                        new_isbn, new_category)

                        elif order_of_book == 2:
                            book2.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_no_of_pages,
                                        new_isbn, new_category)

                        elif order_of_book == 3:
                            book3.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_no_of_pages,
                                        new_isbn, new_category)

                        elif order_of_book == 4:
                            book4.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_no_of_pages,
                                        new_isbn, new_category)

                        elif order_of_book == 5:
                            book5.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_no_of_pages,
                                        new_isbn, new_category)

                        elif order_of_book == 6:
                            book6.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_no_of_pages,
                                        new_isbn, new_category)

                        elif order_of_book == 7:
                            book7.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_no_of_pages,
                                        new_isbn, new_category)

                        elif order_of_book == 8:
                            book8.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_no_of_pages,
                                        new_isbn, new_category)

                        elif order_of_book == 9:
                            book9.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_no_of_pages,
                                        new_isbn, new_category)

                        elif order_of_book == 10:
                            book10.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_no_of_pages,
                                            new_isbn, new_category)

                
                elif function == 3 :
                  # To add new book
                  # New book's information
                    n_title = input("Enter new title: ")
                    n_author = input("Enter the new name of author: ")
                    n_price = input("Enter the new price: ")
                    n_date_of_publish = input("Enter the date of publish: ")
                    n_item = input("Enter the item: ")
                    nno_of_pages = input("Enter the no. of pages: ")
                    n_isbn = input("Enter the new isbn: ")
                    n_category = input("Enter the category: ")
                    print("===============================")
                    # Instance for new book
                    book11 = Book(n_title, n_author, n_price, n_date_of_publish, n_item, nno_of_pages, n_isbn, n_category)

                    # Add new book to list
                    book11.add_book(book11)

            
                elif function == 4 :
                    book1.available()
                    i = 0
                    # To delete books from store
                    x = 9
                    # Enter the index of book
                    try:
                        index = int(input(f"Please enter the index of the book from 0 to {x - i}: "))
                        book_names.pop(index)
                    except ValueError :
                        print("ERROR Invaild input please enter an integer input: ")
                    except Exception as e:
                        print("An unexcpected error", e)     
                    print("===============================")
       
        elif command == 2 :
                print("1-Available DVDs\n2-Update a DVD information \n3-add DVD to store\n4-Delete a DVD from store")
                while True:
                    try:    
                        function = int(input("Type the operation number: "))
                        if 1 <= function <=4:
                            break
                    except ValueError :
                        print("ERROR Invaild input please enter an integer input")
                    except Exception as e:
                        print("An unexcpected error", e)    
                    print("===============================")
           
            # To show the available DVDs
                if function == 1:
                    print("The available DVDs in bookstore: ")
                    dvd1.available()
                    print("===============================")

                elif function ==2: 
                       
                        while True:
                            try:
                                # Order of DVD
                                order_of_dvd = int(input("Enter the order of DVD from 1 to 10: "))
                                if 1<= order_of_dvd<=10:
                                    break
                                else:
                                    print("out of range")
                            except ValueError :
                                print("ERROR Invaild input please enter an integer input: ")
                            except Exception as e:
                                print("An unexcpected error", e)  

                        # The updated information
                        n_title = input("Enter new title: ")
                        n_author = input("Enter the new name of author: ")
                        n_price = input("Enter the new price: ")
                        n_date_of_publish = input("Enter the date of publish: ")
                        n_item = input("Enter the item: ")
                        n_director = input("Enter the director name: ")
                        n_duration = input("Enter the duration: ")
                        n_genre = input("Enter the genre: ")
                        print("===============================")

                        # Updating procedures
                        if order_of_dvd == 1:
                            dvd1.set_info(n_title, n_author, n_price, n_date_of_publish, n_item, n_director, n_duration, n_genre)

                        elif order_of_dvd == 2:
                            dvd2.set_info(n_title, n_author, n_price, n_date_of_publish, n_item, n_director, n_duration, n_genre)

                        elif order_of_dvd == 3:
                            dvd3.set_info(n_title, n_author, n_price, n_date_of_publish, n_item, n_director, n_duration, n_genre)

                        elif order_of_dvd == 4:
                            dvd4.set_info(n_title, n_author, n_price, n_date_of_publish, n_item, n_director, n_duration, n_genre)

                        elif order_of_dvd == 5:
                            dvd5.set_info(n_title, n_author, n_price, n_date_of_publish, n_item, n_director, n_duration, n_genre)

                        elif order_of_dvd == 6:
                            dvd6.set_info(n_title, n_author, n_price, n_date_of_publish, n_item, n_director, n_duration, n_genre)

                        elif order_of_dvd == 7:
                            dvd7.set_info(n_title, n_author, n_price, n_date_of_publish, n_item, n_director, n_duration, n_genre)

                        elif order_of_dvd == 8:
                            dvd8.set_info(n_title, n_author, n_price, n_date_of_publish, n_item, n_director, n_duration, n_genre)

                        elif order_of_dvd == 9:
                            dvd9.set_info(n_title, n_author, n_price, n_date_of_publish, n_item, n_director, n_duration, n_genre)

                        elif order_of_dvd == 10:
                            dvd10.set_info(n_title, n_author, n_price, n_date_of_publish, n_item, n_director, n_duration, n_genre)


                elif function == 3:
                    # To add new DVD
                        # new DVD information
                        n_title = input("Enter new title: ")
                        n_author = input("Enter the new name of author: ")
                        n_price = input("Enter the new price: ")
                        n_date_of_publish = input("Enter the date of publish: ")
                        n_item = input("Enter the item: ")
                        n_director = input("Enter the director name: ")
                        n_duration = input("Enter the duration: ")
                        n_genre = input("Enter the genre: ")
                        print("===============================")

                        # instance for new DVD
                        dvd11 = DVD(n_title, n_author, n_price, n_date_of_publish, n_item, n_director, n_duration, n_genre)

                        # add new dvd to list
                        dvd11.add_dvd(dvd11)

        
                elif function == 4 :
                    dvd1.available()
                    i = 0
                    # To delete DVDs from store
                
                    x = 9
                    # Enter the index of DVD
                    try:
                        index = int(input(f"Please enter the index of the DVD from 0 to {x - i}: "))
                        dvd_names.pop(index)
                    except ValueError :
                        print("ERROR Invaild input please enter an integer input: ")
                    except Exception as e:
                        print("An unexcpected error", e) 
                    print("===============================")

        elif command == 3 :
            
            print("1-Available magazines\n2-Update a magazine information \n3-add magazine to store\n4-Delete a magazine from store")
            while True:
                try:    
                        function = int(input("Type the operation number: "))
                        if 1 <= function <=4:
                            break
                except ValueError :
                        print("ERROR Invaild input please enter an integer input")
                except Exception as e:
                        print("An unexcpected error", e)  
                print("===============================")
            
            if function == 1 :
            # Show the available magazines
                print("The available magazines in bookstore: ")
                magazine1.available()
                print("===============================")
        
            elif function == 2 :
                    while True:
                            try:
                                # order of magazine
                                order_of_magazine = int(input("Enter the order of magazine from 1 to 10: "))
                                if 1<= order_of_magazine<=10:
                                    break
                                else:
                                    print("out of range")
                            except ValueError :
                                print("ERROR Invaild input please enter an integer input: ")
                            except Exception as e:
                                print("An unexcpected error", e)

                    # updated information
                    new_title = input("Enter new title: ")
                    new_author = input("Enter the new name of author: ")
                    new_price = input("Enter the new price: ")
                    new_date_of_publish = input("Enter the date of publish: ")
                    new_item = input("Enter the item: ")
                    new_issue_number = input("Enter the issue number: ")
                    new_editor = input("Enter editor name: ")
                    print("===============================")

                    # updated procedures
                    if order_of_magazine == 1:
                        magazine1.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_issue_number,
                                        new_editor)
                       
                    elif order_of_magazine == 2:
                        magazine2.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_issue_number,
                                        new_editor)
                        
                    elif order_of_magazine == 3:
                        magazine3.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_issue_number,
                                        new_editor)
                        
                    elif order_of_magazine == 4:
                        magazine4.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_issue_number,
                                        new_editor)                        

                    elif order_of_magazine == 5:
                        magazine5.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_issue_number,
                                        new_editor)
                    
                    elif order_of_magazine == 6:
                        magazine6.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_issue_number,
                                        new_editor)
                       
                    elif order_of_magazine == 7:
                        magazine7.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_issue_number,
                                        new_editor)
                    
                    elif order_of_magazine == 8:
                        magazine8.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_issue_number,
                                        new_editor)
                    
                    elif order_of_magazine == 9:
                        magazine9.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_issue_number,
                                        new_editor)
                    
                    elif order_of_magazine == 10:
                        magazine10.set_info(new_title, new_author, new_price, new_date_of_publish, new_item, new_issue_number,
                                            new_editor)
                        
            elif function == 3: 
                # add new magazine               
                    # new magazine's information
                    new_title = input("Enter new title: ")
                    new_author = input("Enter the new name of author: ")
                    new_price = input("Enter the new price: ")
                    new_date_of_publish = input("Enter the date of publish: ")
                    new_item = input("Enter the item: ")
                    new_issue_number = input("Enter the issue number: ")
                    new_editor = input("Enter editor name: ")
                    print("===============================")

                    # Instance for new magazine
                    magazine11 = Magazine(new_title, new_author, new_price, new_date_of_publish, new_item, new_issue_number,
                                        new_editor)

                    # add magazine to magazine list
                    magazine11.add_magazine(magazine11)

            
            elif function == 4:
                magazine1.available()
                i = 0
                # To delete DVDs from store
                x = 9
                # Enter the index of DVD
                try:
                    index = int(input(f"Please enter the index of the maagzine from 0 to {x - i}: "))
                    magazine_names.pop(index)
                except ValueError :
                    print("ERROR Invaild input please enter an integer input: ")
                except Exception as e:
                    print("An unexcpected error", e) 
                print("===============================")

        elif command == 5:
          # To exit the store  
            print("========= Good Bye Admin =========")
            exit()        
                

if True :
    # Instance of shoppingcart class
    cart = ShoppingCart()

    # Customer interface
    print("Hello to our bookstore")

    command = 3
    while command != 4:
        print("================")
        print("1-Books\n2-DVDs\n3-Magazines\n4-Checkout")
        print("================")
        command = int(input("Select the section you want from 1 to 4: "))

        if command == 1:
            print("1-Available books\n2-Search for a book\n3-know more about specific book\n4-Buying a book")
            while True:
                try:
                    function = int(input("Type the operation number: "))
                    if 1 <= function <=4:
                            break
                except ValueError :
                    print("ERROR Invaild input please enter an integer input: ")
                except Exception as e:
                        print("An unexcpected error", e)  
            print("===============================")

            if function == 1:
                # Show the available books
                book1.available()
            
            # To search about book
            elif function == 2:
                type_of_search = int(input("Search by\n1-Title\n2-author "))    
                
                if type_of_search == 1:
                    y = None
                    x = input("Enter the book name you want to search: ").lower().split()
                    for wanted in book_names:
                        if wanted.get_title().lower().split() == x:
                            y = wanted.get_title().lower().split()
                    if y == x:
                        print("Available in store")
                    else:
                        print("Sorry we don't have this item")
                elif type_of_search == 2:    
                    book1.search()
                else:
                    print("Invaild input")        
                                         
            elif function == 3:
                # To know about book information
                print("The available books:")
                book1.available()
                book1.info()
                   
            elif function == 4:
                book1.available()
                # Buying books
                while True:
                    order = int(input("The order of Book in the shelf from 0 to 9: "))
                    if 0<=order <=9:
                        break
                    else:
                        print("out of range")
                book_new = book_names[order]
                cart.add_item(book_new.title)
                total += 100

  
        elif command == 2:
            print("1-Available DVDs\n2-Search for a DVD\n3-know more about specific DVD\n4-Buying a DVD")
            function = int(input("Type the operation number: "))

            if function == 1:
                # show the available DVDs
                dvd1.available()

            elif function == 2:
                # to search for dvd
                type_of_search = int(input("Search by\n1-Title\n2-author ")) 
                if type_of_search == 1 :
                    y = None
                    x = input("Enter the DVD name you want to search: ").lower().split()
                    for wanted in dvd_names:
                        if wanted.get_title().lower().split() == x:
                            y = wanted.get_title().lower().split()
                    if y == x:
                        print("Available in store")
                    else:
                        print("Sorry we don't have this item")
                elif type_of_search == 2 :
                    dvd1.search()
                else:
                    print("Invaild input")                  

            elif function == 3:
                # To know about DVD information
                print("The available DVDs: ")
                dvd1.available()
                dvd1.info()
                
            elif function == 4:
                dvd1.available()
                # Buying DVDs    
                while True:
                    order = int(input("The order of DVD in the shelf from 0 to 9: "))
                    if 0<=order <=9:
                        break
                    else:
                        print("out of range")
                dvd_new = dvd_names[order]
                cart.add_item(dvd_new.title)
                total += 100

        elif command == 3:
            print("1-Available magazines\n2-Search for a magazine\n3-know more about specific magazine\n4-Buying a magazine")
            function = int(input("Type the operation number: "))

            # show the available Magazine in store
            if function == 1:
                magazine1.available()

            elif function == 2:              
                # to search for magazine
                try:
                 type_of_search = int(input("Search by\n1-Title\n2-author ")) 
                except ValueError :
                    print("'ERROR' incorrect input please enter an integer")
                except Exception as e:
                    print("An unexcpected error",e)
                if type_of_search == 1 :
                    y = None
                    x = input("Enter the magazine name you want to search: ").lower().split()
                    for wanted in magazine_names:
                        if wanted.get_title().lower().split() == x:
                            y = wanted.get_title().lower().split()
                    if y == x:
                        print("Available in store")
                    else:
                        print("Sorry we don't have this item")
                elif type_of_search == 2:
                    magazine1.search()  
                else:
                    print("Invaild input")                

            elif function == 3:
                # To know about any magazine information
                print("The available magazines")
                magazine1.available()
                magazine1.info()
            elif function == 4:
                # Buying magazines
                magazine1.available()
                while True:
                    order = int(input("The order of magazine in the shelf from 0 to 9: "))
                    if 0<=order <=9:
                            break
                    else:
                        print("out of range")
                magazine_new = magazine_names[order]
                cart.add_item(magazine_new.title)
                total += 100

        elif command == 4:       
            if cart.empty(): 
                # To remove any item from cart
                while True :
                                # Show the final items in cart
                                print("The final items in the cart:")
                                cart.show()
                                n = input("do you want to remove any item from cart? y for yes n for no: ")
                                if n == "n" :
                                    break
                                elif n =="y" :
                                    break
                                else:
                                    print("invalid input")
                if n == "y":
                    while n != "n":
                        try: 
                           m = int(input("Which item you want to remove? Enter order: "))
                           cart.remove_item(m)
                        except IndexError:
                          print("OUt of range")  
                        
                        total -= 100
                        # if there is more than one item want to remove
                        while True :
                                n = input("do you want to remove any item from cart? y for yes n for no: ")
                                if n == "n" :
                                    break
                                elif n =="y" :
                                    break
                                else:
                                    print("invalid input")
                        

            # Show the final items in cart after editing
            print("The final items in the cart:")
            cart.show()
            # Print the final price
            print(f"final price will be {total} $")
            print("========= Thank you for visiting our site =========")
