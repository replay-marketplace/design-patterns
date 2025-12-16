import sys

def add_task(task):
    with open('tasks.txt', 'a') as f:
        f.write(task + '\n')

def list_tasks():
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()
    for task in tasks:
        print(task)

def main():
    command = sys.argv[1]
    if command == 'add':
        task = sys.argv[2]
        add_task(task)
    elif command == 'list':
        list_tasks()

if __name__ == '__main__':
    main()