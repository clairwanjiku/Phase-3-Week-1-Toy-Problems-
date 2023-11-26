def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    result = f"{hour:02d}{minute:02d}"
    print(f"The 24-hour format is: {result}")
    return result
