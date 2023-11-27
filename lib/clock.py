def convert_to_24_hour(hour, minute, period):
    
     # Check if the period is "pm" and adjust the hour accordingly
    if period.lower() == "pm" and hour != 12:
        hour += 12
        
         # For "am", convert 12 to 0
    elif period.lower() == "am" and hour == 12:
        hour = 0
# Return the time in 24-hour format 
    return f"{hour:02d}{minute:02d}"
