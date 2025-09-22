# PROJECT PLANNER
#### Video Demo: <https://youtu.be/3Bj3TvIhM44>
#### Description:
The idea of this project is to create a program that will allow me to track my programming projects over time. It will also allow me to track my everyday projects, as one easily loses track of time while programming! Over time, the user can also create an archive over completed (or cancelled, should that be the case) projects, to look back at what they've done.

This is done by allowing the program to create .json-files for each type of project and project archive (a file for each kind of project and archive has already been created in order to comply with the Harvard CS50P requirements, later versions will not feature this, and instead allow the program to create them ).

Current version: 1.0.0  
Published 2025-09-22  
https://github.com/SimonJagerSwe/project_planner/



## **THE MENU SYSTEM**
The menus are navigated using numeric inputs, corresponding to the choices available for each menu.

### **MAIN MENU**
Upon starting the This menu is the first interface the user is faced with, and it will allow the user to do several things:
* Add new projects
* View programming projects
* View everyday projects
* View archived projects
* Exit the program

### **ADDING PROJECTS**
In this part of the menu, the user can add new projects to the active list of projects, either programming projects, or everyday projects. Other project types may be added later, subject to time.

### **VIEWING ACTIVE PROJECTS**
For both programming and everyday projects, you can view a list for each type, and from those viewing panels, a user can select to create a new project of the same type, or they can modify or archive each active project.

### **VIEWING ARCHIVED PROJECTS**
Chosing this option let's the user view either archived programming projects, archived everyday projects, or a combined archive of both.

### **MODIFYING PROJECTS**
When a certain project has been selected for modification, the user will be prompted to re-input project parameters. Just pressing Enter for a specific parameter will leave this parameter unchanged, letting the user move on to the next project parameter.

### **RETURNING TO MAIN MENU AND EXITING THE PROGRAM**
Each sub-menu of the program will provide the user with the options to either return to the main menu, or exiting the program, the exit function requiring confirmation from the user in order to avoid accidental termination of the program.

### **LIBRARIES AND PACKAGES**
This program has been designed to rely on Python's built-in packages for ease of use, however for testing purposes, the test_main.py also utilises Pytest for test automation and the mock-package to allow the test file to simulate pre-determined user input to certain menues in order to assert a specific required outcome of certain tests.


### **PROGRAM CREDITS**
All code in this project have been written, revised and tested by below copyright holder
© Simon Jäger, Lund, Sweden, 2025

TODO
