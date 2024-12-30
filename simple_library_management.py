class Library:
    book_list=[]

    @classmethod
    def entry_book(self,book):
        self.book_list.append(book)
    @classmethod
    def find_book(self,id):
        for x in self.book_list:
            a=x.get_id()
            if a==id:
                return x
    @classmethod
    def display_books(self):
        for x in self.book_list:
            x.view_book_info()

class Book:
    def __init__(self,book_id,title,author):
        self.__book_id=book_id
        self.__title=title
        self.__author=author
        self.__availability=True

        Library.entry_book(self)
    def get_id(self):
        return self.__book_id
    def borrow_book(self):
        if self.__availability==True:
            self.__availability = False
            print(f"'{self.__title}' is successfully borrowed.")
        else:
            print(f'\'{self.__title}\' is currently unavailable. Try again later.')
        
    def return_book(self):
        if self.__availability==False:
            self.__availability=True
            print(f'\'{self.__title}\' is successfully returned.')
        else:
            print(f'You did not borrow \'{self.__title}\'. Enter your book id correctly next time, while returning books.')

    def view_book_info(self):
        if self.__availability:
            status="Available" 
        else: 
            status="Unavailable"
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {status}")


def main_Menu():
    while True:
        print("\n\n    Library Menu     ")
        print("---------------------")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit\n")
        x=int(input("Enter your choice: "))

        if x==1:
            print("\n\n    All Books in the Library    ")
            print("---------------------------------")
            Library.display_books()
        elif x==2:
            book_id=input("Enter the book id: ")
            book=Library.find_book(book_id)
            if book:
                book.borrow_book()
            else:
                print("Book ID is invalid. Please try again.")
        elif x==3:
            book_id=input("Enter the book id: ")
            book=Library.find_book(book_id)
            if book:
                book.return_book()
            else:
               print("Book id is invalid. Please try again.")
        elif x==4:
            print("Exiting the system. Thank you for using the Library.")
            break
        else:
            print("Your choice is invalid. Please select again.")



Book("7001","Shuvro Shomogro","Humayun Ahmed")
Book("7002","Nakshi Kathar Math","Jasimuddin")
Book("7003","Meghnaadbod Kabya","Michael Madhusudan Dutt")
Book("7004","Geetanjali","Rabindranath Tagore")
Book("7005","Amar Bondhu Rashed","Jafor Iqbal")
Book("7006","Pother Panchali","Bibhutibhushan Bandopadhyay")
Book("7007","Putul Nacher Itikotha","Manik Bandopadhyay")

print("\n-----------------------------")
print("|   Welcome to the Library  |")
print("-----------------------------")
main_Menu()
