class Publication:
    def __init__(self, name):
        self.name = name
    def print_information(self):
        print(f"Publication Name: {self.name}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}")

def main():
    donald_duck_magazine = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")
    compartment_no_6_book = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)

    print("Information for Donald Duck Magazine:")
    donald_duck_magazine.print_information()

    print("\nInformation for Compartment No. 6 Book:")
    compartment_no_6_book.print_information()
if __name__ == "__main__":
    main()