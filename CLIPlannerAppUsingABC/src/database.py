import csv

from .deadlined_reminders import DeadlinedReminder


def list_reminders():
    f = open("reminders.csv", "r")

    with f:
        reader = csv.reader(f)

        for row in reader:
            print()
            for e in row:
                print(e.ljust(32), end=' ')
        print()


def add_reminder(text, date, ReminderClass):

    reminder = ReminderClass(text, date)

    if not isinstance(reminder, DeadlinedReminder):
        raise TypeError('Invalid Reminder class')

    with open('reminders.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(reminder)
