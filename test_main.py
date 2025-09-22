# Imports
import mock
import pytest
import sys

from .main import main, initialize_project_lists, ProgrammingProject, add_project_menu, programming_projects, exit
mock_pp = {
        "name" : "Mock program 1",
        "start" : "1970-01-01",
        "finish" : "2055-12-31",
        "language" : "Assembly",
        "link" : "www.examplehub.com/mock_1",
        "progress" : "99.9%",
        "status" : "Eternal"
    }
mock_pl = []
mock_ep = {
        "name" : "Mock everyday 1",
        "start" : "1970-01-01",
        "finish" : "2055-12-31",
        "progress" : "99.9%",
        "status" : "Eternal"

    }
mock_el = []

def test_main_init():
    assert main() == initialize_project_lists()

def test_add_project_menu(monkeypatch):
    ...
    # monkeypatch.setattr("builtins.input", lambda _: "1")
    # assert add_project_menu() == ProgrammingProject.add_project_programming(programming_projects)

def test_add_programming_project():
    ...

def test_add_everyday_project():
    ...

def test_view_projects():
    ...

def test_exit_upper(monkeypatch):
    # Check lowercase y exits program
    monkeypatch.setattr("builtins.input", lambda _: "y")
    with pytest.raises(SystemExit) as input:
        exit()
    assert input.type == SystemExit

def test_exit_lower(monkeypatch):
    # Check uppercase Y converts to lowercase and exits program
    monkeypatch.setattr("builtins.input", lambda _: "Y")
    with pytest.raises(SystemExit) as input:
        exit()
    assert input.type == SystemExit