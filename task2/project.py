class Task:
    def __init__(self, name, description, status='Planned'):
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        print('Name:', self.name)
        print('Description:', self.description)
        print('Status:', self.status)

class Project:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)

    def update_task_status(self, name, new_status):
        for task in self.tasks:
            if task.name == name:
                task.status = new_status

    def get_tasks_by_status(self, status):
        return [i for i in self.tasks if i.status == status]

    def print_tasks(self):
        for task in self.tasks:
            task.display()
            print('-'*5)
