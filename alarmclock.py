import datetime
import time
import os  # for beep sound (works on Linux/Mac) or use winsound on Windows

# For Windows beep sound
try:
    import winsound
    use_winsound = True
except ImportError:
    use_winsound = False

# Function to set alarm
def set_alarm():
    print("Set the alarm time (24-hour format):")
    hour = int(input("Hour (0-23): "))
    minute = int(input("Minute (0-59): "))
    second = int(input("Second (0-59): "))
    return hour, minute, second

# Get alarm time
alarm_hour, alarm_minute, alarm_second = set_alarm()
print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}:{alarm_second:02d}")

# Loop to check the time
while True:
    now = datetime.datetime.now()
    if (now.hour == alarm_hour and
        now.minute == alarm_minute and
        now.second == alarm_second):
        print("Wake up! Alarm ringing...")

        # Play beep sound
        if use_winsound:
            for i in range(5):  # beep 5 times
                winsound.Beep(2500, 1000)  # frequency, duration(ms)
        else:
            # Linux/Mac alternative
            for i in range(5):
                os.system('say "Alarm ringing"')  # macOS voice
        break
    time.sleep(1)
