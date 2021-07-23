import datetime

logo = """
 ██████  █████  ██      ███████ ███    ██ ██████   █████  ██████          ███    ███  █████  ██   ██ ███████ ██████  ██     
██      ██   ██ ██      ██      ████   ██ ██   ██ ██   ██ ██   ██         ████  ████ ██   ██ ██  ██  ██      ██   ██ ██     
██      ███████ ██      █████   ██ ██  ██ ██   ██ ███████ ██████          ██ ████ ██ ███████ █████   █████   ██████  ██     
██      ██   ██ ██      ██      ██  ██ ██ ██   ██ ██   ██ ██   ██         ██  ██  ██ ██   ██ ██  ██  ██      ██   ██        
 ██████ ██   ██ ███████ ███████ ██   ████ ██████  ██   ██ ██   ██         ██      ██ ██   ██ ██   ██ ███████ ██   ██ ██     
                                                                                                                            
                                                                                                                            
"""

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

print(logo)

# Loop to get a year from the user
while True:
    try:
        year = int(input("Enter the year from the user: "))
        break
    except ValueError:
        print("Please enter an integer value for Year number eg. 2000.\n")

# Loop to get a month from the user
while True:
    try:
        month = int(input("Enter the month for the calander, 1-12: "))
        print("\n")
        break
    except ValueError:
        print("Please enter an integer value for Month number, Like 1 for January.\n")

   

def get_calander(year, month):
    # calender_text will contain the string of the calender
    calender_text = ""
    # Put month and year at the top of the calender
    calender_text += f"{' '*34} {MONTHS[month-1]} {str(year)} \n"
    # Add the days of the week labels to the calendar
    calender_text += "...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n"
    # The horizontal line string that separate weeks
    week_separator = ("+----------" * 7) + "+\n"
    # The blank rows have ten spaces in between the | day separators
    blank_row = ("|          " * 7) + "|\n"
    # Get the first date in the month.
    current_date = datetime.date(year,month, 1)
    # Roll back current_date until it is Sunday.
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)
    
    # Loop over each week in the month.
    while True:
        calender_text += week_separator
        # day_number_row is the row with the day number labels
        day_number_row = ''

        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += "|" + day_number_label + (" " * 8)
            # Go to next day
            current_date += datetime.timedelta(days=1)

        # Add the vertical line after Saturday
        day_number_row += "|\n"

        # Add the day number row and 3 blank rows to the calendar text
        calender_text += day_number_row
        for i in range(3):
            calender_text += blank_row

        # Check if done with the month
        if current_date.month != month:
            break
    
    # Add the horizontal line at the very bottom of the calendar.
    calender_text += week_separator
    return calender_text

calendar= get_calander(year, month)
print(calendar)

# Store Calendar as a text file
calendar_filename = f"calender_{year}_{month}.txt"
with open(calendar_filename, 'w') as cal_file:
    cal_file.write(calendar)

print(f'Saved to {calendar_filename}')
