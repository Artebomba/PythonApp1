
class library:
    
    def __init__(self, booksList, name):
        self.booksList = booksList
        self.name = name
        self.lendDict = {}
    
    def displayBooks(self):
        print(f'We have following books in our library \"{self.name}\" \n')
        for book in self.booksList:
            print(book)
    
    def addBook(self, book):
        if book in booksList:
            print ('Book already exists!')
        else:
            self.booksList.append(book)
            bookDatabase = open(database1, 'a')
            bookDatabase.write('\n')
            bookDatabase.write(book)
            print('Book added')
    
    def lendBook(self, book, user):
        if book in booksList:
            if book not in self.lendDict.keys():
                self.lendDict[book] = user
                print(f'{user} has lended a {book} book')
            else:
                print(f'{book} is already lended by {self.lendDict[book]}')
        else:
            print("We are very apologies! We don't have such a book.")
    
    def returnBook(self, book):
        if book in self.lendDict.keys():
            del self.lendDict[book]
            print(f'{book} returned successfully')
        else:
            print(f'{book} isn\'t belong to our library \"{self.name}\"')

def menu():
    print('Hello!')
    print('Choose number to continue: ')
    print('1 to display books')
    print('2 to lend a book')
    print('3 to add a book')
    print('4 to return a book')
    print('5 to quit')

def choice():
    choice=int(input('Enter menu choice: '))
    return choice

def main():
    
    menu()
    
    t=choice()
    if t==1:
        biblioteka.displayBooks()
    elif t==2:
        book = input("Enter a book: ")
        user = input("Enter your full name: ")
        biblioteka.lendBook(book, user)
    elif t==3:
        book = input("Enter a book: ")
        biblioteka.addBook(book)
    elif t==4:
        book = input("Enter a book: ")
        biblioteka.returnBook(book)
    elif t==5:
        exit
        
if __name__ == '__main__':
    booksList = []
    database1 = input("Enter the pass to the database file with extension: ")
    bookDatabase = open(database1, 'r')
    for i in bookDatabase:
        booksList.append(i)
    biblioteka = library(booksList, 'Kharcyzsk')
    
main()