from datetime import datetime, timedelta

class Library:
    def __init__(self):
        # Dictionary to store books
        self.books = {
            1: {"title": "Python Basics", "available": True},
            2: {"title": "Data Structures", "available": True},
            3: {"title": "Algorithms", "available": True}
        }
        
        # Issued book records
        self.issued_books = {}

    def display_books(self):
        print("\n📚 Available Books:")
        for book_id, info in self.books.items():
            status = "Available" if info["available"] else "Issued"
            print(f"{book_id}. {info['title']} - {status}")

    def issue_book(self):
        self.display_books()
        try:
            book_id = int(input("\nEnter Book ID to issue: "))
            
            if book_id not in self.books:
                print("❌ Invalid Book ID!")
                return
            
            if not self.books[book_id]["available"]:
                print("❌ Book already issued!")
                return
            
            student_name = input("Enter student name: ")
            duration_days = int(input("Enter duration (in days): "))
            
            issue_date = datetime.now()
            due_date = issue_date + timedelta(days=duration_days)
            
            self.books[book_id]["available"] = False
            self.issued_books[book_id] = {
                "student": student_name,
                "issue_date": issue_date,
                "due_date": due_date
            }
            
            print(f"✅ Book issued to {student_name}")
            print(f"📅 Due Date: {due_date.strftime('%Y-%m-%d')}")

        except ValueError:
            print("❌ Invalid input!")

    def return_book(self):
        try:
            book_id = int(input("\nEnter Book ID to return: "))
            
            if book_id not in self.issued_books:
                print("❌ This book was not issued!")
                return
            
            record = self.issued_books[book_id]
            return_date = datetime.now()
            due_date = record["due_date"]
            
            # Fine calculation (₹10 per week, progressive)
            late_days = (return_date - due_date).days
            fine = 0
            
            if late_days > 0:
                weeks_late = (late_days // 7) + 1
                fine = weeks_late * 10
            
            # Update records
            self.books[book_id]["available"] = True
            del self.issued_books[book_id]
            
            print("\n📄 Return Summary:")
            print(f"Student: {record['student']}")
            print(f"Return Date: {return_date.strftime('%Y-%m-%d')}")
            
            if fine > 0:
                print(f"⚠️ Late return! Fine: ₹{fine}")
            else:
                print("✅ Returned on time. No fine.")

        except ValueError:
            print("❌ Invalid input!")

    def show_issued_books(self):
        print("\n📖 Issued Books:")
        if not self.issued_books:
            print("No books currently issued.")
            return
        
        for book_id, record in self.issued_books.items():
            print(f"{book_id}. {self.books[book_id]['title']}")
            print(f"   Student: {record['student']}")
            print(f"   Due Date: {record['due_date'].strftime('%Y-%m-%d')}")


def main():
    library = Library()
    
    while True:
        print("\n====== 📚 LIBRARY MENU ======")
        print("1. View Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View Issued Books")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            library.display_books()
        elif choice == "2":
            library.issue_book()
        elif choice == "3":
            library.return_book()
        elif choice == "4":
            library.show_issued_books()
        elif choice == "5":
            print("👋 Exiting Library System. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")


# Run the system
main()