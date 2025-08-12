# Imports
import sys


# Main function
def main():
    start_menu()


def start_menu():
    print("What would you like to do?\n")
    print("1. Add new project")
    print("2. View programming projects")
    print("3. View everyday projects")
    print("4. View archived projects")
    print("5. Exit\n\n")
    validate_choice(str(input("Enter choice: ")))


def validate_choice(choice):
    if choice == "1":
        add_project()
    elif choice == "2":
        view_programming()
    elif choice == "3":
        view_everyday()
    elif choice == "4":
        view_archive()
    elif choice == "5":
        exit()
    else:
        print("Invalid option, use the number to select what to do")
        print("Returning to main menu...")
        start_menu()


def add_project():
    print("Adding project")


def view_programming():
    print("View programming projects")


def view_everyday():
    print("View everyday projects")


def view_archive():
    print("View project archive")


def exit():
    choice = input("Are you sure you want to quit? Y/N: ").lower()
    if choice == "y":
        sys.exit("Exiting program")
    elif choice == "n":
        start_menu()
    else:
        print("Invalid option, type 'Y' for yes or 'N for no")
        exit()


# Execute main
if __name__ == "__main__":
    main()