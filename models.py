import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Book:
    """Represents a book in the library."""
    
    def __init__(self, book_id: int, title: str, author: str, isbn: str, quantity: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
        self.date_added = datetime.now().strftime('%Y-%m-%d')
    
    def to_dict(self) -> Dict:
        """Convert book to dictionary."""
        return {
            'id': self.book_id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'quantity': self.quantity,
            'date_added': self.date_added
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        """Create book from dictionary."""
        book = Book(data['id'], data['title'], data['author'], data['isbn'], data['quantity'])
        book.date_added = data.get('date_added', datetime.now().strftime('%Y-%m-%d'))
        return book
    
    def __repr__(self) -> str:
        return f"Book(ID: {self.book_id}, Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Quantity: {self.quantity})"


class Member:
    """Represents a library member."""
    
    def __init__(self, member_id: int, name: str, email: str, phone: str, address: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.date_registered = datetime.now().strftime('%Y-%m-%d')
        self.books_issued = 0
    
    def to_dict(self) -> Dict:
        """Convert member to dictionary."""
        return {
            'id': self.member_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'date_registered': self.date_registered,
            'books_issued': self.books_issued
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Member':
        """Create member from dictionary."""
        member = Member(data['id'], data['name'], data['email'], data['phone'], data['address'])
        member.date_registered = data.get('date_registered', datetime.now().strftime('%Y-%m-%d'))
        member.books_issued = data.get('books_issued', 0)
        return member
    
    def __repr__(self) -> str:
        return f"Member(ID: {self.member_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone})"


class Borrowing:
    """Represents a book borrowing record."""
    
    def __init__(self, borrowing_id: int, member_id: int, book_id: int, quantity: int, due_date: str):
        self.borrowing_id = borrowing_id
        self.member_id = member_id
        self.book_id = book_id
        self.quantity = quantity
        self.borrow_date = datetime.now().strftime('%Y-%m-%d')
        self.due_date = due_date
        self.returned = False
        self.return_date = None
    
    def to_dict(self) -> Dict:
        """Convert borrowing to dictionary."""
        return {
            'id': self.borrowing_id,
            'member_id': self.member_id,
            'book_id': self.book_id,
            'quantity': self.quantity,
            'borrow_date': self.borrow_date,
            'due_date': self.due_date,
            'returned': self.returned,
            'return_date': self.return_date
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Borrowing':
        """Create borrowing from dictionary."""
        borrowing = Borrowing(data['id'], data['member_id'], data['book_id'], data['quantity'], data['due_date'])
        borrowing.borrow_date = data.get('borrow_date', datetime.now().strftime('%Y-%m-%d'))
        borrowing.returned = data.get('returned', False)
        borrowing.return_date = data.get('return_date')
        return borrowing
    
    def is_overdue(self) -> bool:
        """Check if the book is overdue."""
        if self.returned:
            return False
        due = datetime.strptime(self.due_date, '%Y-%m-%d')
        return datetime.now() > due
    
    def __repr__(self) -> str:
        status = "Returned" if self.returned else ("Overdue" if self.is_overdue() else "Active")
        return f"Borrowing(ID: {self.borrowing_id}, Member: {self.member_id}, Book: {self.book_id}, Quantity: {self.quantity}, Status: {status})"
