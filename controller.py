class todo_controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self):
        task = self.view.prompt_for_task()
        self.model.add_task(task)
        self.update_view()

    def remove_task(self):
        task_index = self.view.prompt_for_removal()
        self.model.remove_task(task_index)
        self.update_view()

    def update_view(self):
        tasks = self.model.get_tasks()
        self.view.display_tasks(tasks)

    def run(self):
        while True:
            action = input("\nEnter 'a' to add a task, 'r' to remove a task, or 'q' to quit: ").lower()
            if action == 'a':
                self.add_task()
            elif action == 'r':
                self.remove_task()
            elif action == 'q':
                print("Exiting the Todo List application.")
                break
            else:
                print("Invalid input. Please try again.")
