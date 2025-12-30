months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
        else:
            month_name, day_year = date.split(" ", 1)
            day, year = day_year.split(",")
            month = months.index(month_name) + 1
            day = int(day.strip())
            if 1 <= day <= 31:
                print(f"{year.strip()}-{month:02}-{day:02}")
                break
    except (ValueError, IndexError):
        pass
