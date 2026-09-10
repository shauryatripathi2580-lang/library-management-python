from library_system import LibraryManagementSystem
from datetime import datetime, timedelta


class LibraryCLI:
    """Command Line Interface for Library Management System."""
    
    def __init__(self):
        self.library = LibraryManagementSystem()
        self.running = True
    
    def display_menu(self) -> None:
        """Display main menu."""
        print("\n" + "="*50)
        print("📚 LIBRARY MANAGEMENT SYSTEM 📚".center(50))
        print("="*50)
        print("\n1. Book Management")
        print("2. Member Management")
        print("3. Book Borrowing")
        print("4. Reports & Statistics")
        print("5. Exit")
        print("\n" + "-"*50)
    
    def book_menu(self) -> None:
        """Book management menu."""
        while True:
            print("\n--- BOOK MANAGEMENT ---")
            print("1. Add New Book")
            print("2. View All Books")
            print("3. Search Book by Title")
            print("4. Search Book by Author")
            print("5. Search Book by ISBN")
            print("6. Update Book Quantity")
            print("7. Delete Book")
            print("8. Back to Main Menu")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.view_all_books()
            elif choice == '3':
                title = input("Enter book title: ").strip()
                books = self.library.search_book_by_title(title)
                self.display_books(books)
            elif choice == '4':
                author = input("Enter author name: ").strip()
                books = self.library.search_book_by_author(author)
                self.display_books(books)
            elif choice == '5':
                isbn = input("Enter ISBN: ").strip()
                book = self.library.search_book_by_isbn(isbn)
                if book:
                    self.display_books([book])
                else:
                    print("✗ Book not found")
            elif choice == '6':
                book_id = int(input("Enter Book ID: ").strip())
                quantity = int(input("Enter new quantity: ").strip())
                self.library.update_book_quantity(book_id, quantity)
            elif choice == '7':
                book_id = int(input("Enter Book ID to delete: ").strip())
                self.library.delete_book(book_id)
            elif choice == '8':
                break
            else:
                print("✗ Invalid choice")
    
    def add_book(self) -> None:
        """Add a new book."""
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        isbn = input("Enter ISBN: ").strip()
        quantity = int(input("Enter quantity: ").strip())
        self.library.add_book(title, author, isbn, quantity)
    
    def view_all_books(self) -> None:
        """View all books."""
        books = self.library.view_all_books()
        self.display_books(books)
    
    def display_books(self, books) -> None:
        """Display books in table format."""
        if not books:
            print("No books found")
            return
        
        print("\n" + "-"*100)
        print(f"{'ID':<5} {'Title':<25} {'Author':<20} {'ISBN':<15} {'Quantity':<10} {'Date Added':<12}")
        print("-"*100)
        for book in books:
            print(f"{book.book_id:<5} {book.title:<25} {book.author:<20} {book.isbn:<15} {book.quantity:<10} {book.date_added:<12}")
        print("-"*100)
    
    def member_menu(self) -> None:
        """Member management menu."""
        while True:
            print("\n--- MEMBER MANAGEMENT ---")
            print("1. Register New Member")
            print("2. View All Members")
            print("3. Search Member by Name")
            print("4. Search Member by Email")
            print("5. Delete Member")
            print("6. Back to Main Menu")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                self.register_member()
            elif choice == '2':
                self.view_all_members()
            elif choice == '3':
                name = input("Enter member name: ").strip()
                members = self.library.search_member_by_name(name)
                self.display_members(members)
            elif choice == '4':
                email = input("Enter member email: ").strip()
                member = self.library.search_member_by_email(email)
                if member:
                    self.display_members([member])
                else:
                    print("✗ Member not found")
            elif choice == '5':
                member_id = int(input("Enter Member ID to delete: ").strip())
                self.library.delete_member(member_id)
            elif choice == '6':
                break
            else:
                print("✗ Invalid choice")
    
    def register_member(self) -> None:
        """Register a new member."""
        name = input("Enter member name: ").strip()
        email = input("Enter email: ").strip()
        phone = input("Enter phone number: ").strip()
        address = input("Enter address: ").strip()
        self.library.register_member(name, email, phone, address)
    
    def view_all_members(self) -> None:
        """View all members."""
        members = self.library.view_all_members()
        self.display_members(members)
    
    def display_members(self, members) -> None:
        """Display members in table format."""
        if not members:
            print("No members found")
            return
        
        print("\n" + "-"*120)
        print(f"{'ID':<5} {'Name':<20} {'Email':<25} {'Phone':<15} {'Address':<30} {'Date Registered':<15}")
        print("-"*120)
        for member in members:
            print(f"{member.member_id:<5} {member.name:<20} {member.email:<25} {member.phone:<15} {member.address:<30} {member.date_registered:<15}")
        print("-"*120)
    
    def borrowing_menu(self) -> None:
        """Book borrowing menu."""
        while True:
            print("\n--- BOOK BORROWING ---")
            print("1. Record Book Borrowing")
            print("2. Record Book Return")
            print("3. View Active Borrowings")
            print("4. View Overdue Books")
            print("5. View Member Borrowing History")
            print("6. Delete Borrowing Record")
            print("7. Back to Main Menu")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                self.record_borrowing()
            elif choice == '2':
                self.record_return()
            elif choice == '3':
                self.view_active_borrowings()
            elif choice == '4':
                self.view_overdue_books()
            elif choice == '5':
                member_id = int(input("Enter Member ID: ").strip())
                borrowings = self.library.get_member_borrowing_history(member_id)
                self.display_borrowings(borrowings)
            elif choice == '6':
                borrowing_id = int(input("Enter Borrowing ID to delete: ").strip())
                self.library.delete_borrowing_record(borrowing_id)
            elif choice == '7':
                break
            else:
                print("✗ Invalid choice")
    
    def record_borrowing(self) -> None:
        """Record book borrowing."""
        member_id = int(input("Enter Member ID: ").strip())
        book_id = int(input("Enter Book ID: ").strip())
        quantity = int(input("Enter quantity: ").strip())
        days = int(input("Enter borrowing period (days, default 14): ").strip() or "14")
        self.library.record_borrowing(member_id, book_id, quantity, days)
    
    def record_return(self) -> None:
        """Record book return."""
        borrowing_id = int(input("Enter Borrowing ID: ").strip())
        self.library.return_book(borrowing_id)
    
    def view_active_borrowings(self) -> None:
        """View active borrowings."""
        borrowings = self.library.view_active_borrowings()
        self.display_borrowings(borrowings)
    
    def view_overdue_books(self) -> None:
        """View overdue books."""
        borrowings = self.library.view_overdue_books()
        if not borrowings:
            print("✓ No overdue books")
        else:
            print("\n⚠️  OVERDUE BOOKS:")
            self.display_borrowings(borrowings)
    
    def display_borrowings(self, borrowings) -> None:
        """Display borrowings in table format."""
        if not borrowings:
            print("No borrowing records found")
            return
        
        print("\n" + "-"*130)
        print(f"{'ID':<5} {'Member ID':<10} {'Book ID':<10} {'Quantity':<10} {'Borrow Date':<15} {'Due Date':<15} {'Returned':<10}")
        print("-"*130)
        for borrowing in borrowings:
            status = "Yes" if borrowing.returned else ("OVERDUE" if borrowing.is_overdue() else "No")
            print(f"{borrowing.borrowing_id:<5} {borrowing.member_id:<10} {borrowing.book_id:<10} {borrowing.quantity:<10} {borrowing.borrow_date:<15} {borrowing.due_date:<15} {status:<10}")
        print("-"*130)
    
    def reports_menu(self) -> None:
        """Reports and statistics menu."""
        while True:
            print("\n--- REPORTS & STATISTICS ---")
            print("1. Library Statistics")
            print("2. Back to Main Menu")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                self.display_statistics()
            elif choice == '2':
                break
            else:
                print("✗ Invalid choice")
    
    def display_statistics(self) -> None:
        """Display library statistics."""
        stats = self.library.get_library_stats()
        
        print("\n" + "="*50)
        print("📊 LIBRARY STATISTICS 📊".center(50))
        print("="*50)
        print(f"Total Unique Books: {stats['total_unique_books']}")
        print(f"Total Book Quantity: {stats['total_book_quantity']}")
        print(f"Total Members: {stats['total_members']}")
        print(f"Active Borrowings: {stats['active_borrowings']}")
        print(f"Overdue Books: {stats['overdue_books']}")
        print("="*50)
    
    def run(self) -> None:
        """Run the CLI application."""
        while self.running:
            self.display_menu()
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                self.book_menu()
            elif choice == '2':
                self.member_menu()
            elif choice == '3':
                self.borrowing_menu()
            elif choice == '4':
                self.reports_menu()
            elif choice == '5':
                print("\n✓ Thank you for using Library Management System!")
                print("Goodbye!\n")
                self.running = False
            else:
                print("✗ Invalid choice. Please try again.")


if __name__ == "__main__":
    cli = LibraryCLI()
    cli.run()
