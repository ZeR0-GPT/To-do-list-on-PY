from todo_database import create_connection

def add_task(task):
    conn = create_connection()
    conn.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def complete_task(task_id):
    conn = create_connection()
    conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = create_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = create_connection()
    cursor = conn.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return rows