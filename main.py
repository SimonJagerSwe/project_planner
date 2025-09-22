# Imports
import datetime
import json
import os
import sys

from datetime import datetime


# Logo
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


# Project & archive files
pp_file = "programming_projects.json"
programming_projects = []
pa_file = "programming_archive.json"
programming_archive = []
ep_file = "everyday_projects.json"
everyday_projects = []
ea_file = "everyday_archive.json"
everyday_archive = []
fa_file = "full_archive.json"
full_archive = []

# Main function
def main():
        initialize_project_lists()
        print(f"{logo}\n\n\n")
        start_menu()


# Initialising archives from json-files
def initialize_project_lists():    
    with open(pp_file, "r") as file:
        p_projects = json.load(file)
        for project in p_projects:
            programming_projects.append(project)

    with open(pa_file, "r") as file:
        pa = json.load(file)
        for project in pa:
            programming_archive.append(project)
   
    with open(ep_file, "r") as file:
        e_projects = json.load(file)
        for project in e_projects:
            everyday_projects.append(project)
    
    with open(ea_file, "r") as file:
        ea = json.load(file)
        for project in ea:
            everyday_archive.append(project)

    with open(fa_file, "r") as file:
        fa = json.load(file)
        for project in fa:
            full_archive.append(project)

    return programming_projects, programming_archive, everyday_projects, everyday_archive, full_archive

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
    

    # Add programming project function
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
        
        start_menu()


# Everyday class, utilizing parameters from parent class
class EverydayProject(Project):
    def __init__(self, name, start, finish, progress, status):
        super().__init__(name, start, finish, progress, status)


    # Add everyday project function
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

        start_menu()


# Start menu
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


# Project adding menu
def add_project_menu():
    print("Select project type:\n")
    print("1. Programming project\n2. Everyday project\n3. Return to main menu\n4. Exit program\n\n")
    choice = str(input("Enter choice: "))    
    if choice == "1":
        clear_terminal()
        ProgrammingProject.add_project_programming(programming_projects)# print(f"This is the returned list of programming projects:\n{programming_projects}")
    elif choice == "2":
        clear_terminal()
        EverydayProject.add_project_everyday(everyday_projects)# print(f"This is the returned list of everyday projects:\n{everyday_projects}")
    elif choice == "3":
        clear_terminal()
        start_menu()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice, pick a number above")
        add_project_menu()


# Modifying programming projects, calling programming projects file and list
def modify_programming_project(pf, pl):
    pl.clear()
    with open(pf, "r") as file:
        projects = json.load(file)
        for i, project in enumerate(projects):
            print(f"{i + 1}. {project}\n")
            pl.append(project)
    
        choice = int(input("Chose project number to modify: "))
        project_to_change = projects[choice - 1]
        # print(project_to_change)
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

    start_menu()


# Modify everyday project, calling the everyday projects file and list
def modify_everyday_project(ef, el):
    el.clear()
    with open(ef, "r") as file:
        projects = json.load(file)
        for i, project in enumerate(projects):
            print(f"{i + 1}. {project}\n")
            el.append(project)

    choice = int(input("Chose project number to modify: "))
    project_to_change = projects[choice - 1]
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
    el.remove(project_to_change)
    el.append(changed_project)

    with open(ep_file, "w") as file:
        json.dump(el, file)

    start_menu()


# Project archiving
def archive_project(project_file, project_list, current_file, current_list, full_archive_file, full_archive_list):
    project_list.clear()
    current_list.clear()
    full_archive_list.clear()

    with open(project_file, "r") as file:
        projects = json.load(file)
        for i, project in enumerate(projects):
            print(f"{i + 1}. {project}\n")
            project_list.append(project)

    with open(current_file, "r") as file:
        projects = json.load(file)
        for project in projects:
            current_list.append(project)

    with open(full_archive_file, "r") as file:
        projects = json.load(file)
        for project in projects:
            full_archive_list.append(project)

    idx = int(input("Chose project number to archive: "))
    project_to_archive = project_list[idx - 1]

    project_list.remove(project_to_archive)
    with open(project_file, "w") as file:
        json.dump(project_list, file)

    current_list.append(project_to_archive)
    with open(current_file, "w") as file:
        json.dump(current_list, file)
        
    full_archive_list.append(project_to_archive)
    with open(full_archive_file, "w") as file:
        json.dump(full_archive_list, file)

    start_menu()


# View current programming projects
def view_programming():
    print("Viewing programming projects")
    try:
        with open(pp_file, "r") as file:
            projects = json.load(file)
            for i, project in enumerate(projects):
                print(f"{i + 1}. {project}\n")
    except:
        print("No programming projects available, returning to main menu...")
        start_menu()

    choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Modify project\n3. Archive project\n4. Return to main menu\n5. Exit program\n\nChoice: "))
    if choice == "1":
        clear_terminal()
        add_project_menu()
    elif choice == "2":
        clear_terminal()
        modify_programming_project(pp_file, programming_projects)
    elif choice == "3":
        clear_terminal()
        archive_project(pp_file, programming_projects, pa_file, programming_archive, fa_file, full_archive)
    elif choice == "4":
        clear_terminal()
        start_menu()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice")
        view_programming()


# View current everyday projects    
def view_everyday():
    print("Viewing everyday projects")
    try:
        with open(ep_file, "r") as file:
            projects = json.load(file)
            for i, project in enumerate(projects):
                print(f"{i + 1}. {project}\n")                
    except:
        print("No everyday projects available, returning to main menu...")
        start_menu()        

    choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Modify project\n3. Archive project\n4. Return to main menu\n5. Exit program\n\nChoice: "))
    if choice == "1":
        clear_terminal()
        add_project_menu()
    elif choice == "2":
        clear_terminal()
        modify_everyday_project(ep_file, everyday_projects)
    elif choice == "3":
        clear_terminal()
        archive_project(ep_file, everyday_projects, ea_file, everyday_archive, fa_file, full_archive)
    elif choice == "4":
        clear_terminal()
        start_menu()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice")
        view_everyday()


# Archive viewer menu
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


# Programming archive viewer
def view_archive_programming():
    print("Viewing programming archive")
    with open(pa_file, "r") as file:
        archive = json.load(file)
        for i, project in enumerate(archive):
            print(f"{i + 1}. {project}")
    choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Return to main menu\n3. Exit program\n\nChoice: "))
    if choice == "1":
        clear_terminal()
        add_project_menu()
    elif choice == "2":
        clear_terminal()
        start_menu()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        view_archive_programming()


# Everyday archive viewer
def view_archive_everyday():
    print("Viewing everyday project archive")
    with open(ea_file, "r") as file:
        archive = json.load(file)
        for i, project in enumerate(archive):
            print(f"{i + 1}. {project}")
    choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Return to main menu\n3. Exit program\n\nChoice: "))
    if choice == "1":
        clear_terminal()
        add_project_menu()
    elif choice == "2":
        clear_terminal()
        start_menu()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        view_archive_everyday()


# Full archive viewer
def view_full_archive():
    print("Viewing full archive")
    with open(fa_file, "r") as file:
        archive = json.load(file)
        for i, project in enumerate(archive):
            print(f"{i + 1}. {project}")
    choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Return to main menu\n3. Exit program\n\nChoice: "))
    if choice == "1":
        clear_terminal()
        add_project_menu()
    elif choice == "2":
        clear_terminal()
        start_menu()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        view_full_archive()


# Clear terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Exit program
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
