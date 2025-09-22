# Imports
import json
import mock
import pytest
import sys

from .main import main, initialize_project_lists, ProgrammingProject, add_project_menu, programming_projects, exit

# def test_main_init():
#     assert main() == initialize_project_lists()

def test_add_project_menu(monkeypatch):
    ...
    # monkeypatch.setattr("builtins.input", lambda _: "1")
    # assert add_project_menu() == ProgrammingProject.add_project_programming(programming_projects)

def test_add_programming_project():
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
    mock_pl.append(mock_pp)

    with open("mock_programming_projects.json", "w") as file:
        json.dump(mock_pl, file)
    mock_pl.clear()

    with open("mock_programming_projects.json", "r") as file:
        mock_projects = json.load(file)
        for project in mock_projects:
            mock_pl.append(project)

    assert mock_pl[-1] == mock_pp

def test_add_everyday_project():
    mock_el = []
    mock_ep = {
        "name" : "Mock everyday 1",
        "start" : "1970-01-01",
        "finish" : "2055-12-31",
        "progress" : "99.9%",
        "status" : "Eternal"
    }
    mock_el.append(mock_ep)
    
    with open("mock_everyday_projects.json", "w") as file:
        json.dump(mock_el, file)
    mock_el.clear()

    with open("mock_everyday_projects.json", "r") as file:
        mock_projects = json.load(file)
        for project in mock_projects:
            mock_el.append(project)

    assert mock_el[-1] == mock_ep

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