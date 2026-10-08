import os
from datetime import datetime as dt

class JournalManager:
    def create_file(self):
        try:
            if(notNull == True):
                with open("journal.txt", "x") as file:
                    file.write("Your Journal Entries:\n")
                    file.write("-----------------------------")
                    file.close()
        except FileExistsError:
            pass

    def add_entry(self, entry):
        if(entry == ""):
            print("Error: Journal entry can't be empty!")
            notNull = False
            return
        elif(notNull == True):
            with open("journal.txt", "a") as file:
                TimeStamp = dt.now().strftime("%d/%m/%y - %I:%M:%S %p")
                file.write(f"\n[{TimeStamp}]\n{entry}\n")
            print("\nEntry added successfully!")

    def view_entries(self):
        try:
            with open("journal.txt", "r") as file:
                entry = file.read()
            print(f"{entry}\n")
        except FileNotFoundError:
            print("Error: The Journal file does not exist. Please add a new entry first.")

    def search_entry(self, keyword):
        with open("journal.txt", "r") as file:
            found = False
            run = 0
            for entry in file:
                if keyword.lower() in entry.lower():
                    run += 1
                    if(run == 1):
                        print("\nMatching Entries:\n")
                        print("-----------------------------")
                    print(entry)
                    found = True
            if(found == False):
                print(f"\nNo entries were found for the keyword: {keyword}")

    def del_entries(self, decision):
        try:
            if(decision.lower() == "yes"):
                os.remove("journal.txt")
                print("All journal entries have been deleted.")
            elif(decision.lower() == "no"):
                print("Entries deletion terminated.")
            else:
                print("Invalid option")
                return
        except FileNotFoundError:
            print("No journal entries to delete.")

journal = JournalManager()
notNull = False
run = 0

while True:
    run += 1
    if(run == 1):
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
    print("\nPlease select an option:")
    print("\n1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search of an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    choice = input("User Input:\n")    

    match choice:
        case "1":
            journal.create_file()
            entry = input("\nEnter your journal entry:\n")
            journal.add_entry(entry)
        case "2":
            journal.view_entries()
        case "3":
            keyword = input("\nEnter a keyword or date to search: ")
            journal.search_entry(keyword)
        case "4":
            decision = input("\nAre you sure you want to delete all entries? (yes/no): ")
            journal.del_entries(decision)
        case "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        case _:
            print("Invalid option. Please select a valid option from the menu.")