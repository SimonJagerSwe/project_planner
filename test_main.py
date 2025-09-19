# Imports
import mock
import pytest
import sys

from .main import add_project_menu, programming_projects, ProgrammingProject, everyday_projects, EverydayProject, Project, exit
'''
def test_add_project_menu():
    assert add_project_menu().choice("1") == ProgrammingProject.add_project_programming(programming_projects)

def test_add_programming_project(programming_manager):
    ...

def test_add_everyday_project(everyday_manager):
    ...

def test_view_projects():
    ...

@pytest.fixture
def prompt():
    return "y"
'''

def test_exit(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    with pytest.raises(SystemExit) as input:
        exit()
    assert input.type == SystemExit
    