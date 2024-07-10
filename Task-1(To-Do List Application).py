# Task List containing of all to-do tasks of user
task_list = []

# Function to add a task to task list
def add_task():
    task = input("Enter a task to add : ")
    task_list.append(task)
    print("Task added to task list successfully!")

# Function to update a new task in existing task list
def update_task():
    task_num = int(input("Enter the task number to update : "))
    new_task = input("Enter a new task : ")
    task_list[task_num - 1] = new_task
    print("Task",task_num,"updated to task list successfully!")

# Function to delete a task from task list
def delete_task():
    task_num = int(input("Enter the task number to delete : "))
    del task_list[task_num - 1]
    print("Task",task_num,"deleted from task list successfully!")

# Function to display all tasks from task list
def display_tasks():
    print("To-Do List :")
    count = 1
    for task in task_list :
        print("Task",count,":",task)
        count = count + 1

# Main Loop to execute above functions

while True :
    # Displays Menu for the To-Do List
    print("To-Do List Menu : ")
    print("Enter 1 : To Add Task")
    print("Enter 2 : To Update Task")
    print("Enter 3 : To Delete Task")
    print("Enter 4 : To Display All Tasks")
    print("Enter 5 : To Quit")
    
    choice = int(input("Enter your choice number : "))

    if choice==1 :
        add_task()
    elif choice==2 :
        update_task()
    elif choice==3 :
        delete_task()
    elif choice==4 :
        display_tasks()
    elif choice==5 : 
        break
    else :
        print("Invalid Choice. Try Again!")
     


