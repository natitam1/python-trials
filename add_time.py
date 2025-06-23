def add_time(start, duration, day_of_week=None):
    # Days of the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Convert to 24-hour format for calculation
    if period == "PM":
        start_hour += 12 if start_hour != 12 else 0
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Total minutes and calculate new time
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    new_hour_24 = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    days_later = total_minutes // (24 * 60)

    # Convert back to 12-hour format
    period = "AM" if new_hour_24 < 12 else "PM"
    new_hour_12 = new_hour_24 % 12
    if new_hour_12 == 0:
        new_hour_12 = 12

    # Build time string
    new_time = f"{new_hour_12}:{new_minute:02d} {period}"

    # Add day of the week if given
    if day_of_week:
        index = days.index(day_of_week.capitalize())
        new_day_index = (index + days_later) % 7
        new_day = days[new_day_index]
        new_time += f", {new_day}"

    # Add info about days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
print(add_time("3:00 PM", "3:10"))                      
