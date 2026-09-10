import json
import os
from typing import List, Optional
from models import Book, Member, Borrowing


class LibraryDatabase:
    """Handles persistent storage of library data."""
    
    def __init__(self, filename: str = 'library_data.json'):
        self.filename = filename
        self.data = self._load_data()
    
    def _load_data(self) -> Dict:
        """Load data from JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return self._get_default_data()
        return self._get_default_data()
    
    @staticmethod
    def _get_default_data() -> Dict:
        """Get default data structure."""
        return {
            'books': [],
            'members': [],
            'borrowings': [],
            'book_id_counter': 1,
            'member_id_counter': 1,
            'borrowing_id_counter': 1
        }
    
    def save_data(self) -> None:
        """Save data to JSON file."""
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def get_next_book_id(self) -> int:
        """Get next book ID."""
        book_id = self.data['book_id_counter']
        self.data['book_id_counter'] += 1
        return book_id
    
    def get_next_member_id(self) -> int:
        """Get next member ID."""
        member_id = self.data['member_id_counter']
        self.data['member_id_counter'] += 1
        return member_id
    
    def get_next_borrowing_id(self) -> int:
        """Get next borrowing ID."""
        borrowing_id = self.data['borrowing_id_counter']
        self.data['borrowing_id_counter'] += 1
        return borrowing_id
    
    def add_book(self, book: Book) -> None:
        """Add book to database."""
        self.data['books'].append(book.to_dict())
        self.save_data()
    
    def get_all_books(self) -> List[Book]:
        """Get all books."""
        return [Book.from_dict(book_data) for book_data in self.data['books']]
    
    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """Get book by ID."""
        for book_data in self.data['books']:
            if book_data['id'] == book_id:
                return Book.from_dict(book_data)
        return None
    
    def update_book(self, book: Book) -> None:
        """Update book in database."""
        for i, book_data in enumerate(self.data['books']):
            if book_data['id'] == book.book_id:
                self.data['books'][i] = book.to_dict()
                self.save_data()
                return
    
    def delete_book(self, book_id: int) -> bool:
        """Delete book from database."""
        for i, book_data in enumerate(self.data['books']):
            if book_data['id'] == book_id:
                self.data['books'].pop(i)
                self.save_data()
                return True
        return False
    
    def add_member(self, member: Member) -> None:
        """Add member to database."""
        self.data['members'].append(member.to_dict())
        self.save_data()
    
    def get_all_members(self) -> List[Member]:
        """Get all members."""
        return [Member.from_dict(member_data) for member_data in self.data['members']]
    
    def get_member_by_id(self, member_id: int) -> Optional[Member]:
        """Get member by ID."""
        for member_data in self.data['members']:
            if member_data['id'] == member_id:
                return Member.from_dict(member_data)
        return None
    
    def update_member(self, member: Member) -> None:
        """Update member in database."""
        for i, member_data in enumerate(self.data['members']):
            if member_data['id'] == member.member_id:
                self.data['members'][i] = member.to_dict()
                self.save_data()
                return
    
    def delete_member(self, member_id: int) -> bool:
        """Delete member from database."""
        for i, member_data in enumerate(self.data['members']):
            if member_data['id'] == member_id:
                self.data['members'].pop(i)
                self.save_data()
                return True
        return False
    
    def add_borrowing(self, borrowing: Borrowing) -> None:
        """Add borrowing record to database."""
        self.data['borrowings'].append(borrowing.to_dict())
        self.save_data()
    
    def get_all_borrowings(self) -> List[Borrowing]:
        """Get all borrowing records."""
        return [Borrowing.from_dict(borrowing_data) for borrowing_data in self.data['borrowings']]
    
    def get_borrowing_by_id(self, borrowing_id: int) -> Optional[Borrowing]:
        """Get borrowing record by ID."""
        for borrowing_data in self.data['borrowings']:
            if borrowing_data['id'] == borrowing_id:
                return Borrowing.from_dict(borrowing_data)
        return None
    
    def update_borrowing(self, borrowing: Borrowing) -> None:
        """Update borrowing record in database."""
        for i, borrowing_data in enumerate(self.data['borrowings']):
            if borrowing_data['id'] == borrowing.borrowing_id:
                self.data['borrowings'][i] = borrowing.to_dict()
                self.save_data()
                return
    
    def delete_borrowing(self, borrowing_id: int) -> bool:
        """Delete borrowing record from database."""
        for i, borrowing_data in enumerate(self.data['borrowings']):
            if borrowing_data['id'] == borrowing_id:
                self.data['borrowings'].pop(i)
                self.save_data()
                return True
        return False
