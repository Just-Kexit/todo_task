# Todo List

Simple Django Todo List project with tasks and tags.

## Features

- Create, update and delete tasks  
- Mark tasks as completed or undo  
- Add deadline to tasks  
- Add multiple tags to tasks  
- Sidebar navigation (Home, Tags)  

## Pages

- `/` – Home page with task list  
- `/tags/` – Tag list page  

## How to run

```bash
git clone <repo-url>
cd todo-list
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver