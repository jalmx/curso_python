from task import Task


class TaskController:

    def __init__(self):
        if not Task.table_exists():
            Task.create_table()

    def create_task(self, name, description):
        Task.create(name=name, description=description)

    def change_state(self, id):
        task = Task.get(Task.id == id)
        if task:
            task.state = True
            task.save()

    def show_tasks(self):
        text_complete = "Tasks Done:\n"
        text_incomplete = "Task Incomplete:\n"
        count_complete = 1
        count_incomplete = 1
        for task in Task.select():
            if task.state:
                text_complete += f"{count_complete}.- {task.name } - description: {task.description} - (COMPLETE)\n"
                count_complete += 1
            else:
                text_incomplete += f"{count_incomplete}.- [{task.id}] {task.name } - description: {task.description} - (NOT COMPLETE)\n"
                count_incomplete += 1
        print(text_complete)
        print(text_incomplete)


if __name__ == "__main__":
    opt = 0
    controller = TaskController()
    while True:
        print("APP TASK")
        print("1. Add Task")
        print("2. Change status Task")
        print("3. Show Task")
        opt = int(input())

        if opt == 1:
            print("ADD TASK")
            name = input("Name task: ")
            description = input("Description task: ")
            controller.create_task(name=name, description=description)
        elif opt == 2:
            print("CHANGE STATUS")
            id = int(input("Give ID task to change: "))
            controller.change_state(id)
        elif opt == 3:
            controller.show_tasks()
