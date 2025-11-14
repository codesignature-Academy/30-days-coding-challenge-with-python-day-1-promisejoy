print("⏰ Welcome to the Time Converter!")

minutes = int(input("Enter total minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(minutes, "minutes is equal to", hours, "hour(s) and", remaining_minutes, "minute(s).")