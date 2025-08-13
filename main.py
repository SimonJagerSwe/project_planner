# Imports
import os
import sys

class Project:
    def __init__(self, name, start, finish, progress, status, language, link):
        self.name = name
        self.start = start
        self.finish = finish
        self.progress = progress
        self.status = status
        self.language = language
        self.link = link

class ProgrammingProject(Project):
    def __init__(self, name, start, finish, progress, status, language, link):
        super().__init__(name, start, finish, progress, status, language, link)
        


class EverydayProject(Project):
    def __init__(self, name, start, finish, progress, status):
        super().__init__(name, start, finish, progress, status)



# Main function
def main():
    programming_projects = []
    everyday_projects = []
    programming_archive = []
    everyday_archive = []
    start_menu()


def start_menu():
    print("What would you like to do?\n")
    print("1. Add new project\n2. View programming projects\n3. View everyday projects\n4. View archived projects\n5. Exit program\n\n")
    validate_choice(str(input("Enter choice: ")))


def validate_choice(choice):
    if choice == "1":
        add_project_menu()
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


def add_project_menu():
    clear_terminal()
    print("Select project type:\n")
    print("1. Programming project\n2. Everyday project\n3. Return to main menu\n4. Exit program\n\n")
    choice = str(input("Enter choice: "))
    if choice == "1":
        add_project_programming()
    elif choice == "2":
        add_project_everyday()
    elif choice == "3":
        start_menu()
    elif choice == "4":
        exit()



def add_project_programming():
    clear_terminal()
    project = ProgrammingProject()
    


def add_project_everyday():
    project = EverydayProject()


def view_archive():
    clear_terminal()
    print("Select which archive to view:\n")
    print("1. Programming projects\n2. Everyday projects\n")


def view_programming():
    clear_terminal()
    print("View programming projects")


def view_everyday():
    clear_terminal()
    print("View everyday projects")



def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def exit():
    choice = input("Are you sure you want to quit? Y/N: ").lower()
    if choice == "y":
        sys.exit("\nExiting program")
    elif choice == "n":
        start_menu()
    else:
        print("Invalid option, type 'Y' for yes or 'N for no")
        exit()







# Execute main
if __name__ == "__main__":
    main()