
# ScrollScriptor: A CLI Journal and PDF Archiver

#### Video Demo: https://youtu.be/yLTjD2mj85U
#### Description:

ScrollScriptor is a command-line journaling application built in Python. It allows users to create, view, and export journal entries efficiently with persistent CSV storage and optional PDF output. Designed as a personal productivity tool, it supports quick entry creation, filtering by date, and summary exports in a professional layout.

This project was built as the final submission for Harvard’s CS50P course. It demonstrates command-line interaction, file I/O, PDF generation, and automated testing with pytest. It also uses `fpdf2` to support non-ASCII characters and generate styled certificates or reports.

---

## Features

1. **Add Entry**: Prompts user for date, title, and content. Appends entry to `scroll_data.csv`.
2. **View Summary**: Displays a chronological list of all entries saved.
3. **Export to PDF**: Creates `scroll_export.pdf` from saved entries using custom fonts and layout.
4. **Filter by Date**: Allows filtering the journal by a specific date (YYYY-MM-DD).
5. **Exit**: Cleanly ends the session.

---

## File Descriptions

- **`project.py`**
  Main script containing all core functions and user interface logic. It includes:
  - `main()` – Main menu loop
  - `add_entry()` – Gathers user input and saves entries
  - `view_summary()` – Prints all saved entries to screen
  - `export_to_pdf()` – Converts CSV data into a formatted PDF using `fpdf2`
  - `filter_by_date()` – Filters and displays entries by date

- **`test_project.py`**
  Contains unit tests using `pytest`. These test:
  - Entry creation and CSV writing (`test_add_entry`)
  - Data summary printing (`test_view_summary`)
  - PDF export file creation (`test_export_to_pdf`)

- **`requirements.txt`**
  Lists Python package dependencies. Currently includes:
  - `fpdf2` – Used for PDF generation

- **`scroll_data.csv`**
  Automatically created during runtime. Stores journal entries in the format:
  `date,title,content`

- **`scroll_export.pdf`**
  Generated on-demand. Contains all journal entries in a styled printable format.

---

## Design and Implementation Notes

- **Encoding**: Initially, the PDF export failed due to `latin-1` encoding issues. This was resolved by embedding a Unicode-compatible TrueType font (`DejaVuSans.ttf`) using `fpdf2`’s `add_font()` method.
- **Tests**: The `test_export_to_pdf()` function explicitly checks the existence of the PDF file after generation. Temporary file cleanup is handled to keep test environments clean.
- **Data Persistence**: A lightweight CSV format was chosen for simplicity and portability. This allows the application to run without needing a database or third-party storage service.
- **Interface**: The script uses a `while` loop and user input options to provide a simple text-based menu. This keeps the tool cross-platform and easy to run inside a terminal.
- **Dependencies**: No obscure external libraries are used. Everything is pip-installable via `requirements.txt`, ensuring ease of setup.

---

## How to Run

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the program:
   ```bash
   python project.py
   ```

3. Run tests:
   ```bash
   pytest test_project.py
   ```

---

## Conclusion

ScrollScriptor is a lightweight, extensible journaling utility for the terminal. Its clean file structure, strong test coverage, and PDF export capability make it suitable for quick journaling tasks, log-keeping, or personal diary management. This project was built entirely in Python as a demonstration of practical scripting, modular design, and command-line interactivity.
