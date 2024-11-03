class todo_view:
    def display_tasks(self, tasks):
        print("\nYour Todo List:")
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    def prompt_for_task(self):
        return input("\nEnter a new task: ")

    def prompt_for_removal(self):
        return int(input("\nEnter the task number to remove: ")) - 1
