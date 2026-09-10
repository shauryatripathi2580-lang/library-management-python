# Library Management System - Python

A comprehensive library management system built in Python with command-line interface.

## Features

### 📚 Book Management
- Add new books with details (title, author, ISBN, quantity)
- View all books in the library
- Search books by title
- Search books by author
- Search books by ISBN
- Update book quantity
- Delete books from the system

### 👥 Member Management
- Register new library members
- Store member information (name, email, phone, address)
- View all registered members
- Search members by name
- Search members by email
- Delete member records
- Track member borrowing history

### 📖 Book Borrowing System
- Record book borrowings
- Track borrowing dates and due dates
- Record book returns
- Automatically update inventory
- View active borrowings
- **Identify overdue books**
- View member borrowing history
- Delete borrowing records

### 📊 Reports & Statistics
- Total unique books
- Total book quantity in inventory
- Total registered members
- Active borrowings count
- Overdue books count

## Project Structure

```
library-management-python/
├── models.py              # Data models (Book, Member, Borrowing)
├── database.py            # Database operations (JSON storage)
├── library_system.py      # Core library management logic
├── cli.py                 # Command-line interface
├── main.py                # Application entry point
├── library_data.json      # Data storage file (auto-created)
└── README.md              # Project documentation
```

## Installation

### Requirements
- Python 3.6 or higher
- No external dependencies required

### Setup

1. Clone the repository:
```bash
git clone https://github.com/shauryatripathi2580-lang/library-management-python.git
cd library-management-python
```

2. Run the application:
```bash
python main.py
```

## Usage

### Starting the Application
```bash
python main.py
```

### Main Menu
After starting, you'll see the main menu with options:
1. **Book Management** - Add, view, search, and delete books
2. **Member Management** - Register and manage library members
3. **Book Borrowing** - Record borrowing, returns, and view history
4. **Reports & Statistics** - View library statistics
5. **Exit** - Close the application

### Example Workflows

#### Adding a Book
1. Select "1" for Book Management
2. Select "1" for Add New Book
3. Enter book details:
   - Title: "The Great Gatsby"
   - Author: "F. Scott Fitzgerald"
   - ISBN: "978-0743273565"
   - Quantity: "5"

#### Registering a Member
1. Select "2" for Member Management
2. Select "1" for Register New Member
3. Enter member details:
   - Name: "John Doe"
   - Email: "john@example.com"
   - Phone: "1234567890"
   - Address: "123 Main St, City"

#### Recording a Borrowing
1. Select "3" for Book Borrowing
2. Select "1" for Record Book Borrowing
3. Enter:
   - Member ID: (e.g., 1)
   - Book ID: (e.g., 1)
   - Quantity: (e.g., 2)
   - Borrowing period in days: (default 14)

## Data Storage

All data is stored in `library_data.json` file in JSON format. The system automatically:
- Creates the file on first run
- Saves data after every operation
- Loads existing data when starting

Example data structure:
```json
{
  "books": [
    {
      "id": 1,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "isbn": "978-0743273565",
      "quantity": 5,
      "date_added": "2026-09-10"
    }
  ],
  "members": [],
  "borrowings": []
}
```

## Class Structure

### Models (models.py)
- **Book**: Represents a book with ID, title, author, ISBN, and quantity
- **Member**: Represents a library member with contact information
- **Borrowing**: Represents a book borrowing record with dates and status

### Database (database.py)
- **LibraryDatabase**: Handles all JSON file operations
- Methods for CRUD operations on books, members, and borrowings

### Library System (library_system.py)
- **LibraryManagementSystem**: Main business logic
- Book management methods
- Member management methods
- Borrowing management methods
- Statistics generation

### CLI (cli.py)
- **LibraryCLI**: Command-line interface
- Menu-driven navigation
- User input handling
- Data display in table format

## Key Features Explained

### Automatic ID Generation
Each book, member, and borrowing record gets a unique ID automatically.

### Book Quantity Management
- When a book is borrowed, the quantity decreases
- When a book is returned, the quantity increases
- System prevents borrowing more than available quantity

### Overdue Detection
Books are automatically marked as overdue based on current date vs. due date.

### Member History
Each member's borrowing history is tracked and can be viewed anytime.

## Future Enhancements

- 🗄️ Database integration (SQLite/PostgreSQL)
- 👤 User authentication and roles
- 📧 Email notifications for due dates
- 💰 Fine calculation system
- 🔍 Advanced search filters
- 📱 Web interface using Flask/Django
- 📊 Advanced reporting and analytics
- 📲 REST API

## License

Free to use and modify.

## Author

Created by Shaurya Tripathi
