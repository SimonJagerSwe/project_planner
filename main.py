# Imports
# import csv
import datetime
import json
import os
import sys

from datetime import datetime


programming_projects = []
pp_file = "programming_projects.json"
everyday_projects = []
ep_file = "everyday_projects.json"
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
        name = input("Project name: ")
        start = input("Project start date (if today, leave empty and press enter): ")
        if start == "":
            start = datetime.today().strftime("%Y-%m-%d")
        finish = input("Projected finish date (if today, leave empty and press enter): ")
        if finish == "":
            finish = datetime.today().strftime("%Y-%m-%d")
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
        pp.append(project)

        with open(pp_file, "w") as file:
            json.dump(pp, file)


# Everyday class, utilizing parameters from parent class
class EverydayProject(Project):
    def __init__(self, name, start, finish, progress, status):
        super().__init__(name, start, finish, progress, status)

    def add_project_everyday(ep):
        name = input("Project name: ")
        start = input("Project start date (if today, leave empty and press enter): ")
        if start == "":
            start = datetime.today().strftime("%Y-%m-%d")
        finish = input("Project finish date (if today, leave empty and press enter): ")
        if finish == "":
            finish = datetime.today().strftime("%Y-%m-%d")
        progress = input("Project progress: ")
        status = input("Project status: ")
        project = {
            "name" : name,
            "start" : start,
            "finish" : finish,
            "progress" : progress,
            "status" : status
            }        
        ep.append(project)

        with open(ep_file, "w") as file:
            json.dump(ep, file)


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
            print(f"This is the returned list of everyday projects:\n{everyday_projects}")
        elif choice == "3":
            clear_terminal()
            start_menu()
        elif choice == "4":
            exit()
        else:
            print("Invalid choice, pick a number above")
            add_project_menu()

    
    def modify_programming_project(pf, pl):
        # print(pf)
        # print(pl)
        pl.clear()
        # print(pl)
        with open(pf, "r") as file:
            projects = json.load(file)
            for i, project in enumerate(projects):
                print(f"{i + 1}. {project}")
                pl.append(project)
        
            choice = int(input("Chose project number to modify: "))
            # print(f"Project number: {choice}")
            project_to_change = projects[choice - 1]
            print(project_to_change)
            print("If project variable is to be unchanged, just press Enter")           
            name = input("Project name: ")
            if name == "":
                name = project_to_change["name"]
            start = input("Project start date: ")
            if start == "":
                start = project_to_change["start"]
            finish = input("Projected finish date: ")
            if finish == "":
                finish = project_to_change["finish"]
            language = input("Project language(s): ")
            if language == "":
                language = project_to_change["language"]
            link = input("Project link: ")
            if link == "":
                link = project_to_change["link"]
            progress = input("Project progress: ")
            if progress == "":
                progress = project_to_change["progress"]
            status = input("Project status: ")
            if status == "":
                status = project_to_change["status"]
            changed_project = {
                "name" : name,
                "start" : start,
                "finish" : finish,
                "language" : language,
                "link" : link,
                "progress" : progress,
                "status" : status
                }
            print(f"Project to change: {project_to_change}")
            print(f"Project changed to: {changed_project}")
            pl.remove(project_to_change)
            pl.append(changed_project)
            print(pl)

            with open(pp_file, "w") as file:
                json.dump(pl, file)


    def modify_everyday_project(ef, el):
        # print(ef)
        # print(el)
        el.clear()
        # print(el)
        with open(ef, "r") as file:
            projects = json.load(file)
            for i, project in enumerate(projects):
                print(f"{i + 1}. {project}")
                el.append(project)
    
        choice = int(input("Chose project number to modify: "))
        # print(f"Project number: {choice}")
        project_to_change = projects[choice - 1]
        print(project_to_change)
        print("If project variable is to be unchanged, just press Enter") 
        name = input("Project name: ")
        if name == "":
            name = project_to_change["name"]
        start = input("Project start date: ")
        if start == "":
            start = project_to_change["start"]
        finish = input("Project finish date: ")
        if finish == "":
            finish = project_to_change["finish"]
        progress = input("Project progress: ")
        if progress == "":
            progress = project_to_change["progress"]
        status = input("Project status: ")
        if status == "":
            status = project_to_change["status"]
        changed_project = {
            "name" : name,
            "start" : start,
            "finish" : finish,
            "progress" : progress,
            "status" : status
            }
        print(f"Project to change: {project_to_change}")
        print(f"Project changed to: {changed_project}")
        el.remove(project_to_change)
        el.append(changed_project)
        print(el)

        with open(ep_file, "w") as file:
            json.dump(el, file)


    def view_programming():
        print("View programming projects")
        try:
            with open(pp_file, "r") as file:
                projects = json.load(file)
                for i, project in enumerate(projects):
                    print(f"{i + 1}. {project}")
        except:
            print("No programming projects available, returning to main menu...")
            start_menu()
    
        choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Modify or archive project\n3. Return to main menu\n4. Exit program\n\nChoice: "))
        if choice == "1":
            add_project_menu()
        elif choice == "2":
            modify_programming_project(pp_file, programming_projects)
        elif choice == "3":
            start_menu()
        elif choice == "4":
            exit()
        else:
            print("Invalid choice")
            view_programming()

        
    def view_everyday():
        print("Viewing everyday projects")
        try:
            with open(ep_file, "r") as file:
                projects = json.load(file)
                for i, project in enumerate(projects):
                    print(f"{i + 1}. {project}")
                
        except:
            print("No everyday projects available, returning to main menu...")
            start_menu()

        choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Modify or archive project\n3. Return to main menu\n4. Exit program\n\nChoice: "))
        if choice == "1":
            add_project_menu()
        elif choice == "2":
            modify_everyday_project(ep_file, everyday_projects)
        elif choice == "3":
            start_menu()
        elif choice == "4":
            exit()
        else:
            print("Invalid choice")
            view_everyday()


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
        choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Modify or archive project\n3. Return to main menu\n4. Exit program\n\nChoice: "))
        if choice == "1":
            add_project_menu()
        elif choice == "2":
            modify_programming_project()
        elif choice == "3":
            start_menu()
        elif choice == "4":
            exit()
        else:
            print("Invalid choice")
            view_archive_programming()


    def view_archive_everyday():
        print("View everyday project archive")
        print(everyday_archive)
        choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Modify or archive project\n3. Return to main menu\n4. Exit program\n\nChoice: "))
        if choice == "1":
            add_project_menu()
        elif choice == "2":
            modify_everyday_project()
        elif choice == "3":
            start_menu()
        elif choice == "4":
            exit()
        else:
            print("Invalid choice")
            view_archive_everyday()


    def view_full_archive():
        print("Viewing full archive")
        print(full_archive)
        choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Return to main menu\n3. Exit program\n\nChoice: "))
        if choice == "1":
            add_project_menu()
        elif choice == "2":
            start_menu()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice")
            view_full_archive()


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