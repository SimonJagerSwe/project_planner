# Imports
import os
import sys


programming_projects = []
everyday_projects = []
programming_archive = []
everyday_archive = []
full_archive = []
logo = """            ******************************************************************************
            ******************************************************************************
            *********************************             ********************************
            ***************************** 		      ****************************
            *************************			          ************************
            *********************				      ********************
            ******************                                          ******************
            *****************              PROJECT  PLANNER              *****************
            *****************                     BY                     *****************
            *****************                SIMON  JÄGER                *****************
            *****************                   © 2025                   *****************
            ******************                                          ******************
            *********************				      ********************
            *************************			          ************************
            ***************************** 		      ****************************
            *********************************             ********************************
            ******************************************************************************
            ******************************************************************************"""

# Project class, initializing project parameters 
class Project:
    def __init__(self, name, start, finish, progress, status, language, link):
        self.name = name
        self.start = start
        self.finish = finish
        self.progress = progress
        self.status = status
        self.language = language
        self.link = link


# Programming class, utilizing all project parameters from parent class
class ProgrammingProject(Project):
    def __init__(self, name, start, finish, progress, status, language, link):
        super().__init__(name, start, finish, progress, status, language, link)
        
    def add_project_programming():
        print("Add programming project from ProgrammingProject class")
        


# Everyday class, utilizing select parameters from parent class
class EverydayProject(Project):
    def __init__(self, name, start, finish, progress, status):
        super().__init__(name, start, finish, progress, status)

    def add_project_everyday():
        print("Adding everyday projecty from EverydayProject class")



# Main function
def main():    
    start_menu()


def start_menu():    
    print(logo)
    print("\n\n\nWhat would you like to do?\n")
    print("1. Add new project\n2. View programming projects\n3. View everyday projects\n4. View archived projects\n5. Exit program\n\n")
    # validate_choice(str(input("Enter choice: ")))
    choice = str(input("Enter choice: "))
    if choice == "1":
        clear_terminal()
        add_project_menu()
    elif choice == "2":
        clear_terminal()
        view_programming()
    elif choice == "3":
        clear_terminal()
        view_everyday()
    elif choice == "4":
        clear_terminal()
        view_archive()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice, pick a number above")
        # print("Returning to main menu...")
        clear_terminal()
        start_menu()



def add_project_menu():
    # project = Project()
    print("Select project type:\n")
    print("1. Programming project\n2. Everyday project\n3. Return to main menu\n4. Exit program\n\n")
    choice = str(input("Enter choice: "))    
    if choice == "1":
        clear_terminal()
        # add_project_programming(ProgrammingProject.__init__)
        # project = ProgrammingProject()
        # project.add_project_programming(project.__init__)
        ProgrammingProject.add_project_programming()
    elif choice == "2":
        clear_terminal()
        EverydayProject.add_project_everyday()
    elif choice == "3":
        clear_terminal()
        start_menu()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice, pick a number above")
        add_project_menu()



# def add_project_programming():    
#     # project = ProgrammingProject()
#     print("Add programming project from regular function")
    


# def add_project_everyday():
#     print("Add everyday project from regular function")


def view_archive():
    print("Select which archive to view:\n")
    print("1. Programming projects archive\n2. Everyday projects archive\n3. Full achive\n4. Return to main menu\n5. Exit program\n\n")
    choice = str(input("Enter choice: "))
    if choice == "1":
        clear_terminal()
        view_archive_programming()
    elif choice == "2":
        clear_terminal()
        view_archive_everyday()
    elif choice == "3":
        clear_terminal()
        view_full_archive()
    elif choice == "4":
        clear_terminal()
        start_menu()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice, pick a number above")
        view_archive()



def view_programming():
    print("View programming projects")
    print(programming_projects)


def view_everyday():
    print("View everyday projects")
    print(everyday_projects)


def view_archive_programming():
    print("View programming archive")
    print(programming_archive)


def view_archive_everyday():
    print("View everyday project archive")
    print(everyday_archive)


def view_full_archive():
    print("Viewing full archive")
    print(full_archive)


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