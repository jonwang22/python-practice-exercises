def convert_to_military_time(time_str):
    # Split the time string into hours, minutes, seconds, and AM/PM
    time_parts = time_str.split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2][:2])  # Extract only the first two characters for seconds
    am_pm = time_parts[2][-2:]

    print(time_parts)
    print(hours)
    print(minutes)
    print(seconds)
    print(time_parts[2][-2:])

    # Adjust hours based on AM/PM
    if am_pm == "PM" and hours != 12:
        hours += 12
    elif am_pm == "AM" and hours == 12:
        hours = 0

    # Format the military time
    military_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    return military_time

# Example usage
am_pm_time = input()
military_time_result = convert_to_military_time(am_pm_time)
print("Military Time:", military_time_result)