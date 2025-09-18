# Imports
import pytest
import sys

from .main import add_project_menu, programming_projects, ProgrammingProject, everyday_projects, EverydayProject, Project, exit

'''
@pytest.fixture
def project_manager():
    return Project

@pytest.fixture
def programming_manager():
    return ProgrammingProject

@pytest.fixture
def everyday_manager():
    return EverydayProject
'''
def test_add_project_menu():
    ...
    # print(add_project_menu)
    # assert add_project_menu(choice = "1") == ProgrammingProject.add_project_programming(programming_projects)

def test_add_programming_project(programming_manager):
    ...

def test_add_everyday_project(everyday_manager):
    ...

def test_view_projects():
    ...

def test_exit():
    assert exit() == sys.exit()
# test_add_project_menu()