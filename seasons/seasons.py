import sys
from datetime import date, datetime
import inflect


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date format. Please use YYYY-MM-DD.")


def calculate_minutes(birth_date):
    return (date.today() - birth_date).days * 24 * 60


def minutes_to_words(minutes):
    p = inflect.engine()
    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"


def main():
    birth_str = input("Date of Birth (YYYY-MM-DD): ")
    birth_date = parse_date(birth_str)
    print(minutes_to_words(calculate_minutes(birth_date)))


if __name__ == "__main__":
    main()
