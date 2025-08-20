_tasks = []
_next_id = 1

def create_task(title, description):
  global _next_id
  task = {"id": _next_id, "title": title, "description": description}
  _tasks.append(task)
  _next_id += 1
  return task

def list_tasks():
  return list(_tasks)

def get_task(task_id):
  for t in _tasks:
    if t["id"] == task_id:
      return t
  return None    

  
