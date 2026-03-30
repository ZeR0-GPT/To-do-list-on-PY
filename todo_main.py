from todo_database import create_table
from todo import add_task, complete_task, delete_task, get_all_tasks

def main():
    create_table()
    while True:
        print("\n1. Add Task  2. Complete Task  3. Delete Task  4. View All  5. Quit")
        choice = input("Choose: ")
        if choice == "1":
            task = input("Task: ")
            add_task(task)
            print("Task added!")
        elif choice == "2":
            task_id = int(input("Task ID to complete: "))
            complete_task(task_id)
            print("Marked as complete!")
        elif choice == "3":
            task_id = int(input("Task ID to delete: "))
            delete_task(task_id)
            print("Deleted!")
        elif choice == "4":
            for row in get_all_tasks():
                status = "Done" if row[2] == 1 else "Ongoing"
                print(f"[{row[0]}] {row[1]} {status}")
        elif choice == "5":
            break

if __name__ == "__main__":
    main()