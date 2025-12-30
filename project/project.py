import sys
import csv
from datetime import datetime
from fpdf import FPDF

DATA_FILE = "scroll_logs.csv"

def main():
    while True:
        print("\n ScrollScriptor Menu")
        print("1. Add Entry")
        print("2. View Summary")
        print("3. Export to PDF")
        print("4. Filter by Date")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            export_to_pdf()
        elif choice == "4":
            filter_by_date()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

def add_entry():
    date = input("Date (YYYY-MM-DD): ").strip()
    entry = input("Enter your prophetic scroll entry: ").strip()
    with open(DATA_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, entry])
    print(" Entry added.")

def view_summary():
    try:
        with open(DATA_FILE, "r") as f:
            reader = csv.reader(f)
            print("\n Summary of Entries:")
            for row in reader:
                print(f"{row[0]} — {row[1]}")
    except FileNotFoundError:
        print("No entries found.")

def export_to_pdf():
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("Arial", "", fname="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="ScrollScriptor Export", ln=True, align="C")

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                line = f"{row[0]} — {row[1]}"
                pdf.cell(200, 10, txt=line, ln=True)

        pdf.output("scroll_export.pdf")
        print("Exported to scroll_export.pdf.")
    except Exception as e:
        print("Error exporting to PDF:", e)


def filter_by_date():
    date = input("Enter date to filter (YYYY-MM-DD): ").strip()
    try:
        with open(DATA_FILE, "r") as f:
            reader = csv.reader(f)
            matches = [row for row in reader if row[0] == date]
            if matches:
                print(f"Entries for {date}:")
                for m in matches:
                    print(m[1])
            else:
                print("No entries found for that date.")
    except FileNotFoundError:
        print("No entries found.")

if __name__ == "__main__":
    main()
