from typing import List, Optional
from datetime import datetime, timedelta
from models import Book, Member, Borrowing
from database import LibraryDatabase


class LibraryManagementSystem:
    """Main library management system."""
    
    def __init__(self, db_filename: str = 'library_data.json'):
        self.db = LibraryDatabase(db_filename)
    
    # ============ BOOK MANAGEMENT ============
    
    def add_book(self, title: str, author: str, isbn: str, quantity: int) -> Book:
        """Add a new book to the library."""
        book_id = self.db.get_next_book_id()
        book = Book(book_id, title, author, isbn, quantity)
        self.db.add_book(book)
        print(f"✓ Book added successfully: {book}")
        return book
    
    def view_all_books(self) -> List[Book]:
        """View all books in the library."""
        return self.db.get_all_books()
    
    def search_book_by_title(self, title: str) -> List[Book]:
        """Search books by title."""
        books = self.db.get_all_books()
        return [book for book in books if title.lower() in book.title.lower()]
    
    def search_book_by_author(self, author: str) -> List[Book]:
        """Search books by author."""
        books = self.db.get_all_books()
        return [book for book in books if author.lower() in book.author.lower()]
    
    def search_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """Search book by ISBN."""
        books = self.db.get_all_books()
        for book in books:
            if book.isbn == isbn:
                return book
        return None
    
    def delete_book(self, book_id: int) -> bool:
        """Delete a book from the library."""
        if self.db.delete_book(book_id):
            print(f"✓ Book ID {book_id} deleted successfully")
            return True
        print(f"✗ Book ID {book_id} not found")
        return False
    
    def update_book_quantity(self, book_id: int, new_quantity: int) -> bool:
        """Update book quantity."""
        book = self.db.get_book_by_id(book_id)
        if book:
            book.quantity = new_quantity
            self.db.update_book(book)
            print(f"✓ Book quantity updated: {book}")
            return True
        print(f"✗ Book ID {book_id} not found")
        return False
    
    # ============ MEMBER MANAGEMENT ============
    
    def register_member(self, name: str, email: str, phone: str, address: str) -> Member:
        """Register a new member."""
        member_id = self.db.get_next_member_id()
        member = Member(member_id, name, email, phone, address)
        self.db.add_member(member)
        print(f"✓ Member registered successfully: {member}")
        return member
    
    def view_all_members(self) -> List[Member]:
        """View all members."""
        return self.db.get_all_members()
    
    def search_member_by_name(self, name: str) -> List[Member]:
        """Search members by name."""
        members = self.db.get_all_members()
        return [member for member in members if name.lower() in member.name.lower()]
    
    def search_member_by_email(self, email: str) -> Optional[Member]:
        """Search member by email."""
        members = self.db.get_all_members()
        for member in members:
            if member.email == email:
                return member
        return None
    
    def delete_member(self, member_id: int) -> bool:
        """Delete a member."""
        if self.db.delete_member(member_id):
            print(f"✓ Member ID {member_id} deleted successfully")
            return True
        print(f"✗ Member ID {member_id} not found")
        return False
    
    # ============ BORROWING MANAGEMENT ============
    
    def record_borrowing(self, member_id: int, book_id: int, quantity: int, days: int = 14) -> Optional[Borrowing]:
        """Record a book borrowing."""
        member = self.db.get_member_by_id(member_id)
        book = self.db.get_book_by_id(book_id)
        
        if not member:
            print(f"✗ Member ID {member_id} not found")
            return None
        
        if not book:
            print(f"✗ Book ID {book_id} not found")
            return None
        
        if book.quantity < quantity:
            print(f"✗ Only {book.quantity} copies available")
            return None
        
        # Calculate due date
        due_date = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')
        
        # Create borrowing record
        borrowing_id = self.db.get_next_borrowing_id()
        borrowing = Borrowing(borrowing_id, member_id, book_id, quantity, due_date)
        
        # Update book quantity
        book.quantity -= quantity
        self.db.update_book(book)
        
        # Update member's books issued count
        member.books_issued += quantity
        self.db.update_member(member)
        
        # Add borrowing record
        self.db.add_borrowing(borrowing)
        
        print(f"✓ Borrowing recorded successfully: {borrowing}")
        return borrowing
    
    def return_book(self, borrowing_id: int) -> bool:
        """Record book return."""
        borrowing = self.db.get_borrowing_by_id(borrowing_id)
        
        if not borrowing:
            print(f"✗ Borrowing ID {borrowing_id} not found")
            return False
        
        if borrowing.returned:
            print(f"✗ This book has already been returned")
            return False
        
        # Update borrowing record
        borrowing.returned = True
        borrowing.return_date = datetime.now().strftime('%Y-%m-%d')
        self.db.update_borrowing(borrowing)
        
        # Update book quantity
        book = self.db.get_book_by_id(borrowing.book_id)
        if book:
            book.quantity += borrowing.quantity
            self.db.update_book(book)
        
        print(f"✓ Book returned successfully")
        return True
    
    def view_active_borrowings(self) -> List[Borrowing]:
        """View all active borrowings."""
        borrowings = self.db.get_all_borrowings()
        return [b for b in borrowings if not b.returned]
    
    def view_overdue_books(self) -> List[Borrowing]:
        """View all overdue books."""
        borrowings = self.db.get_all_borrowings()
        return [b for b in borrowings if b.is_overdue() and not b.returned]
    
    def get_member_borrowing_history(self, member_id: int) -> List[Borrowing]:
        """Get borrowing history for a member."""
        borrowings = self.db.get_all_borrowings()
        return [b for b in borrowings if b.member_id == member_id]
    
    def delete_borrowing_record(self, borrowing_id: int) -> bool:
        """Delete a borrowing record."""
        if self.db.delete_borrowing(borrowing_id):
            print(f"✓ Borrowing ID {borrowing_id} deleted successfully")
            return True
        print(f"✗ Borrowing ID {borrowing_id} not found")
        return False
    
    # ============ STATISTICS ============
    
    def get_library_stats(self) -> Dict:
        """Get library statistics."""
        books = self.db.get_all_books()
        members = self.db.get_all_members()
        borrowings = self.db.get_all_borrowings()
        active_borrowings = [b for b in borrowings if not b.returned]
        overdue_books = [b for b in borrowings if b.is_overdue() and not b.returned]
        
        total_books_quantity = sum(book.quantity for book in books)
        
        return {
            'total_unique_books': len(books),
            'total_book_quantity': total_books_quantity,
            'total_members': len(members),
            'active_borrowings': len(active_borrowings),
            'overdue_books': len(overdue_books)
        }
