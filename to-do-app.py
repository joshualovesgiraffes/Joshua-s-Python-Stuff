import time
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")

line01 = "*************************"  # header / footer
line02 = "*                       *"  # re-use
line03 = "*    Welcome to To do   *"
line04 = "*                       *"


def add_task(tasks):
    add_task_name = input("Please insert task name ...\n")
    tasks.append(add_task_name)
def load_tasks():
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    return []

def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as handle:
        json.dump(tasks, handle, indent=2)

# starts with blank
print('')
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)
print('')  # ends with blank

print("Tasks are saved in tasks.json file.")
print("")
tasks = load_tasks()

while True:
    time.sleep(1)
    choice = input("Please choose an action ...\n'add' | To add a task\n'remove' | To remove a task\n'view' | To view tasks\n'exit' | To exit\n\n")


    if choice == 'add':
        print("")
        add_task(tasks)
        save_tasks(tasks)
        print("")
    elif choice == 'remove':
        print("")
        remove_task_name = input("Please enter task name ...\n")
        tasks.remove(remove_task_name)
        save_tasks(tasks)
        print("")
        pass
    elif choice == 'view':
        print("")
        for i in tasks:
            print(i)
        print("")
        time.sleep(1)
        pass
    elif choice == 'exit':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        print("")