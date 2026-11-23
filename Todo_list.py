"""3. To-do list in the terminal (2-3 hours)
A menu with options to add a task, show tasks, mark one as done, and quit. Keep tasks in a Python list at first.

Practises: lists, dictionaries and functions."""



def add_task(title, task_status):
    task = {"id": len(Task)+1, "title": title, "task_complected": task_status}
    Task.append(task)
      
def show_task(Task) :
    for value in Task:
        if value["task_complected"].strip() == "done":
            print( f"[✔]{value}")
        else :
            print(f"[x] {value}")

def task_done(Task):
    for task in Task:
        if task["task_complected"].strip() == "done":
            print(task)
    pass

Task = []

add_task("buy coursera course", "done")
add_task("study for exams ", "not done")
show_task(Task)
task_done(Task)
# this is checking if the git add show the changeor not 