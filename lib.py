import json
import os

FILE = "lib.txt"

# Load & Save functions
def load_books():
    if os.path.exists(FILE):
        try:
            with open(FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return []

def save_books(books):
    with open(FILE, 'w') as f:
        json.dump(books, f, indent=4)

# Add a book
def add_book(books):
    book = {
        'title': input("Enter title: ").strip(),
        'author': input("Enter author: ").strip(),
        'year': input("Enter year: ").strip(),
        'genre': input("Enter genre: ").strip(),
        'read': input("Have you read it? (yes/no): ").strip().lower() == 'yes'
    }
    books.append(book)
    save_books(books)
    print(f'✅Successfuly Added "{book["title"]}".')

# Remove a book 
def remove_book(books):
    title = input("Enter title to remove: ").strip().lower()
    updated_books = [b for b in books if b['title'].lower() != title]
    
    if len(updated_books) < len(books):
        save_books(updated_books)
        print(f'☑️ Removed "{title}".')
    else:
        print(f'🔍 No book found with title "{title}".')

    return updated_books 

# Search books
def search_books(books):
    while True:
        field = input("Search by 'title' or 'author': ").strip().lower()
        if field in ['title', 'author']:
            break
        print("❌ Invalid field. Please enter 'title' or 'author'.")

    term = input(f"Enter {field}: ").strip().lower()
    results = [b for b in books if term in b[field].lower()]

    if results:
        for b in results:
            print(f'{b["title"]} by {b["author"]} ({b["year"]}) - {b["genre"]} [{"Read" if b["read"] else "Unread"}]')
    else:
        print(f"❌ No books found with '{term}' in {field}.")

# Display books
def display_books(books):
    if books:
        for b in books:
            print(f'{b["title"]} by {b["author"]} - {b["genre"]} [{"Read" if b["read"] else "Unread"}]')
    else:
        print("📚 Library is empty.")

# Statistics
def show_stats(books):
    total = len(books)
    read_count = sum(b['read'] for b in books)
    print(f"📚 Total books: {total}, Read: {read_count} ({(read_count/total*100):.2f}%)" if total else "📖 No books in library.")

# Main Menu
def main():
    books = load_books()
    options = {
        "1": add_book,
        "2": remove_book,
        "3": search_books,
        "4": display_books,
        "5": show_stats
    }

    while True:
        print("\n📖 Library Menu\n1. Add\n2. Remove\n3. Search\n4. Show all\n5. Stats\n6. Exit")
        choice = input("Choose: ").strip()
        if choice == "6":
            print("🥰Have a Nice Day!"); break
        elif choice in options:
            books = options[choice](books) or books  
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    main()

