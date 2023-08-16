#Khaled Dafi
#16/8/2023
#yes i can make computer understand me!
#make sure to input 24 hours 
from datetime import datetime, timedelta


class Activity:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration


def plan_day():
    wake_up_time = input("What time do you wake up? (HH:MM AM/PM): ")
    sleep_duration = int(input("How many hours do you sleep? "))

    activities = []
    activities.append(Activity("Sleep", sleep_duration))

    work_duration = int(input("How many hours do you work? "))
    activities.append(Activity("Work", work_duration))

    other_activity_count = int(input("How many other activities do you have? "))
    for _ in range(other_activity_count):
        activity_name = input("Enter activity name: ")
        activity_duration = int(input(f"How many hours do you spend on {activity_name}? "))
        activities.append(Activity(activity_name, activity_duration))

    total_duration = sum(activity.duration for activity in activities)
    remaining_time = 24 - total_duration

    activities.append(Activity("Free Time", remaining_time))

    sorted_activities = sorted(activities, key=lambda x: x.duration, reverse=True)

    current_time = wake_up_time
    for activity in sorted_activities:
        end_time = update_time(current_time, activity.duration)
        print(f"{current_time} - {end_time} : {activity.name} ({activity.duration} hours)")
        current_time = end_time


def update_time(current_time, duration):
    time_obj = datetime.strptime(current_time, "%I:%M %p")
    end_time_obj = time_obj + timedelta(hours=duration)
    end_time = end_time_obj.strftime("%I:%M %p")
    return end_time


if __name__ == "__main__":
    plan_day()
