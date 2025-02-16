from datetime import datetime

input_file = "data/dates.txt"
output_file = "data/dates-wednesdays.txt"

date_formats = [
    "%d-%b-%Y",   # Example: 10-Mar-2006
    "%Y-%m-%d",   # Example: 2017-02-02
    "%Y/%m/%d %H:%M:%S",  # Example: 2005/06/15 18:51:14
    "%b %d, %Y"   # Example: Nov 03, 2005
]

def parse_date(date_str):
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Unknown date format: {date_str}")

with open(input_file, "r") as f:
    dates = f.readlines()

wednesday_count = sum(1 for date in dates if parse_date(date).weekday() == 2)

with open(output_file, "w") as f:
    f.write(str(wednesday_count))

print(f"Number of Wednesdays: {wednesday_count}")
