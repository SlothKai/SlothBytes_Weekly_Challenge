def convertTime(time):
    if "m" in time: # 12 hr format, change to 24 hr
        if "a" in time:
            if len(time) == 7: # single digit hour, am
                return time[:4]
            else:
                if time[0:2] == "12":
                    return "0" + time[2:5]
                return time[:5]
        else:
            # need check for double digit for proper string output
            if len(time) == 7: # single digit hour, pm
                temp = int(time[0]) + 12
                result = str(temp) + time[1:4]
            elif time[0:2] == "12":
                return time[0:5]
            else:
                temp = int(time[0:2]) + 12 
                result = str(temp) + time[2:5]
            return result
    else: # 24 hr format, change to 12 hr
        if len(time) == 4: # single digit hour
            hour = int(time[0])
            if hour == 0:
               return "12" + time[1:4] + " am"
            return time[0:4] + " am"
        else:
            hour = int(time[0:2])
            if hour > 12:
                hour -= 12
                end_prefix = " pm"
            elif hour == 12:
                end_prefix = " pm"
            else:
                end_prefix = " am"
            return str(hour) + time[2:5] + end_prefix

# Unit Testing
# rename file to test_sample.py and run pytest in cmd to run test. 
def test_convertTime():
    # 12-hour to 24-hour conversions
    assert convertTime("12:00 am") == "0:00"  # Midnight
    assert convertTime("12:00 pm") == "12:00"  # Noon
    assert convertTime("1:00 am") == "1:00"
    assert convertTime("11:59 am") == "11:59"
    assert convertTime("11:59 pm") == "23:59"

    # 24-hour to 12-hour conversions
    assert convertTime("0:00") == "12:00 am"  # Midnight
    assert convertTime("12:00") == "12:00 pm"  # Noon
    assert convertTime("1:00") == "1:00 am"
    assert convertTime("11:59") == "11:59 am"
    assert convertTime("13:00") == "1:00 pm"
    assert convertTime("23:59") == "11:59 pm"

    # Edge cases and boundary values
    assert convertTime("0:01") == "12:01 am"  # Just after midnight
    assert convertTime("12:01 am") == "0:01"
    assert convertTime("11:00 pm") == "23:00"
    assert convertTime("23:00") == "11:00 pm"

    # Random times
    assert convertTime("3:45 pm") == "15:45"
    assert convertTime("15:45") == "3:45 pm"
    assert convertTime("7:30 am") == "7:30"
    assert convertTime("7:30") == "7:30 am"
