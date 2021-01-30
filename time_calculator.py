def add_time(start, duration, day_of_week=None):
    DAYS_OF_WEEK = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    # Convert to 24 hour time and integers
    start_hour, start_minute = start.split()[0].split(":")
    period = start.split()[1]
    if (period == "PM"):
        start_hour = int(start_hour) + 12
    else:
        start_hour = int(start_hour)
    start_minute = int(start_minute)

    duration_hour, duration_minute = duration.split(":")
    duration_hour = int(duration_hour)
    duration_minute = int(duration_minute)

    # Calculate initial ending time
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour
    end_day = 0

    # Convert to proper number of days, hours, minutes
    end_hour = end_hour + (end_minute // 60)
    end_minute = end_minute % 60
    end_day = end_day + (end_hour // 24)
    end_hour = end_hour % 24

    # Convert hour back to 12 hour time
    if end_hour > 12:
        end_hour = end_hour - 12
        end_period = 'PM'
    elif end_hour == 12:
        end_period = 'PM'
    elif end_hour == 0:
        end_hour = 12
        end_period = 'AM'
    else:
        end_period = 'AM'

    # Format and return the new time
    new_time = "{}:{:02d} {}".format(end_hour, end_minute, end_period)

    # If needed, calculate the ending day of the week
    if day_of_week:
        new_time += ", " + DAYS_OF_WEEK[(DAYS_OF_WEEK.index(day_of_week.lower()) + end_day) % 7].title()

    # If end_day > 0, add the number of days
    if end_day > 0:
        if end_day == 1:
            new_time += " (next day)"
        else:
            new_time += " ({} days later)".format(end_day)

    return new_time
