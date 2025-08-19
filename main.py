# Imports
# import csv
import datetime
import json
import os
import sys

from datetime import datetime


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
    def __init__(self, name, start, finish, progress, status):
        self.name = name
        self.start = start
        self.finish = finish
        self.progress = progress
        self.status = status
        

# Programming class, project parameters from parent class, and additional
class ProgrammingProject(Project):
    def __init__(self, name, start, finish, progress, status, language, link):
        super().__init__(name, start, finish, progress, status, language, link)
        self.language = language
        self.link = link
        
    def add_project_programming(pp):
        print("Add programming project from ProgrammingProject class...")
        print(pp)
        name = input("Project name: ")
        start = input("Project start date (if today, leave empty and press enter): ")
        if start == "":
            start = datetime.today().strftime("%Y-%m-%d")
        finish = input("Projected finish date (if today, leave empty and press enter): ")
        if finish == "":
            finish == datetime.today().strftime("%Y-%m-%d")
        language = input("Project language(s): ")
        link = input("Project link: ")
        progress = input("Project progress: ")
        status = input("Project status: ")
        project = {
            "name" : name,
            "start" : start,
            "finish" : finish,
            "language" : language,
            "link" : link,
            "progress" : progress,
            "status" : status
            }
        print(project)
    
        try:
            with open("programming_projects.json", "r") as file:
                data = json.load(file)
                print(f"Opening data from progamming_projects.json from ProgrammingProject function, result:\n{data}")
                # data.clear()
                # print(data)
        except:
            with open("programming_projects.json", "w") as file:
                data = json.dump({"name": "N/A"}, file)
                print(f"Initializing programming_projects.json from exception:\n{data}")
                # print(data)
                # data.clear()
                # print(data)

        # print(data)
        print(pp)
        pp.clear()
        # print(pp)
        # for p in data:
        #     print(p)
        #     pp.append(p)
        #    print(pp)
        if data:
            for _ in data:
                print(f"This is data:\n{_}")
            pp.append(data)
        pp.append(project)
        print(f"This is the full programming project list:\n{pp}")

        with open("programming_projects.json", "w") as file:
            json.dump(pp, file)

        print("Project added, returning to main menu...")
        return pp
        # start_menu()
        


# Everyday class, utilizing parameters from parent class
class EverydayProject(Project):
    def __init__(self, name, start, finish, progress, status):
        super().__init__(name, start, finish, progress, status)

    def add_project_everyday(ep):
        print("Adding everyday projecty from EverydayProject class...")
        name = input("Project name: ")
        start = input("Project start date (if today, leave empty and press enter): ")
        if start == "":
            start = datetime.today().strftime("%Y-%m-%d")
        finish = input("Project finish date (if today, leave empty and press enter): ")
        if finish == "":
            finish == datetime.today().strftime("%Y-%m-%d")
        progress = input("Project progress: ")
        status = input("Project status: ")
        project = {
            "name" : name,
            "start" : start,
            "finish" : finish,
            "progress" : progress,
            "status" : status
            }
        
        with open("everyday_projects.json", "r") as file:
            data = json.load(file)
        
        print(project)
        ep.append(data)
        ep.append(project)

        with open("everyday_projects.json", "w") as file:
            json.dump(ep, file)

        print("Project added, returning to main menu...")
        start_menu()


# Main function
while True:
    def main():    
        print(f"{logo}\n\n\n")
        start_menu()


    def start_menu():
        print("What would you like to do?\n")
        print("1. Add new project\n2. View programming projects\n3. View everyday projects\n4. View archived projects\n5. Exit program\n\n")
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
            clear_terminal()
            start_menu()


    def add_project_menu():
        print("Select project type:\n")
        print("1. Programming project\n2. Everyday project\n3. Return to main menu\n4. Exit program\n\n")
        choice = str(input("Enter choice: "))    
        if choice == "1":
            clear_terminal()
            ProgrammingProject.add_project_programming(programming_projects)
            print(f"This is the returned list of programming projects:\n{programming_projects}")
        elif choice == "2":
            clear_terminal()
            EverydayProject.add_project_everyday(everyday_projects)
            print(everyday_projects)
        elif choice == "3":
            clear_terminal()
            start_menu()
        elif choice == "4":
            exit()
        else:
            print("Invalid choice, pick a number above")
            add_project_menu()


    def view_programming():
        print("View programming projects")
        try:
            with open("programming_projects.json", "r") as file:
                projects = json.load(file)
                for i, project in enumerate(projects):
                    print(f"{i + 1}.", project)

        except:
            print("No programming projects available, returning to main menu...")
            start_menu()
            
        input("Press enter to return to main menu")
        start_menu()


    def view_everyday():
        print("Viewing everyday projects")
        try:
            with open("everyday_projects.json", "r") as file:
                projects = json.load(file)
                # print(projects)
                for i, project in enumerate(projects):
                    print(f"{i + 1}.", project)
                
        except:
            print("No everyday projects available, returning to main menu...")
            start_menu()

        input("Press enter to return to main menu")
        start_menu()


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


    def view_archive_programming():
        print("View programming archive")
        print(programming_archive)
        input("Press enter to return to main menu")
        start_menu()


    def view_archive_everyday():
        print("View everyday project archive")
        print(everyday_archive)
        input("Press enter to return to main menu")
        start_menu()


    def view_full_archive():
        print("Viewing full archive")
        print(full_archive)
        input("Press enter to return to main menu")
        start_menu()

    def modify_project(p):
        pass


    def clear_terminal():
        os.system("cls" if os.name == "nt" else "clear")


    def exit():
        choice = input("Are you sure you want to quit? Y/N: ").lower()
        if choice == "y":
            sys.exit("\nExiting program")
        elif choice == "n":
            start_menu()
        else:
            print("Invalid option, type 'Y' for yes or 'N' for no")
            exit()







# Execute main
    if __name__ == "__main__":
        main()