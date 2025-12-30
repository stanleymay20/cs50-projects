import pytest
from project import add_entry, view_summary, export_to_pdf, filter_by_date
import os

def setup_module(module):
    with open("scroll_logs.csv", "w") as f:
        f.write("2025-07-07,Scroll entry one\n")
        f.write("2025-07-08,Scroll entry two\n")

def test_export_to_pdf():
    export_to_pdf()
    assert os.path.exists("scroll_export.pdf")

def test_add_entry():
    add_entry_test_line = "2025-07-09,New Test Entry"
    with open("scroll_logs.csv", "a") as f:
        f.write(f"{add_entry_test_line}\n")
    with open("scroll_logs.csv", "r") as f:
        lines = f.read()
        assert "New Test Entry" in lines

def test_filter_by_date(capfd):
    import builtins
    input_values = ["2025-07-08"]
    builtins_input = builtins.input
    builtins.input = lambda _: input_values.pop(0)
    try:
        filter_by_date()
        out, _ = capfd.readouterr()
        assert "Scroll entry two" in out
    finally:
        builtins.input = builtins_input
