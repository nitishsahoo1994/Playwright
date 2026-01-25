from datetime import datetime

def is_future_month(month_name, year):
    date_map = datetime.strptime(f"{month_name} {year}", "%B %Y")
    return date_map > datetime.now()


# Example
is_future = is_future_month("May", 2026)
print(is_future)