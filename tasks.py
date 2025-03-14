import time

tasks = []

def add_task():
    task_name = input("Enter the task name: ")
    task_time = input("Enter the task time in seconds: ")
    task = {"name": task_name, "time": int(task_time)}
    tasks.append(task)
    print("Task added successfully!")

def run_scheduler():
    print("Task scheduler started!")
    while tasks:
        task = tasks.pop(0)
        print(f"Running task: {task['name']}")
        time.sleep(task["time"])
        print(f"Task {task['name']} completed!")
    print("All tasks completed!")

def main():
    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. Run scheduler")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            run_scheduler()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
