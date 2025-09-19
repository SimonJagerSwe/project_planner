# Imports
import mock
import pytest
import sys

from .main import exit

def test_add_project_menu():
    ...
    # assert add_project_menu().choice("1") == ProgrammingProject.add_project_programming(programming_projects)

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

def test_add_everyday_project():
    mock_ep = {
        "name" : "Mock everyday 1",
        "start" : "1970-01-01",
        "finish" : "2055-12-31",
        "progress" : "99.9%",
        "status" : "Eternal"

    }
    mock_el = []

def test_view_projects():
    ...

def test_exit(monkeypatch):
    # Check lowercase y exits program
    monkeypatch.setattr("builtins.input", lambda _: "y")
    with pytest.raises(SystemExit) as input:
        exit()
    assert input.type == SystemExit

    # Check uppercase Y converts to lowercase and exits program
    monkeypatch.setattr("builtins.input", lambda _: "Y")
    with pytest.raises(SystemExit) as input:
        exit()
    assert input.type == SystemExit