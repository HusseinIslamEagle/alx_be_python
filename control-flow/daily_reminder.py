# daily_reminder.py

# سؤال المستخدم عن المهمة
task = input("Enter your task: ")

# سؤال المستخدم عن أولوية المهمة
priority = input("Priority (high/medium/low): ").lower()

# سؤال المستخدم إذا كانت المهمة محددة بوقت
time_bound = input("Is it time-bound? (yes/no): ").lower()

# إنشاء التذكير باستخدام Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

# تعديل الرسالة إذا كانت المهمة محددة بوقت
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# طباعة التذكير النهائي
print("\nReminder:", reminder)
