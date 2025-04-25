from datetime import datetime
from Database import Database, Tasks
import uuid

class TasksModel:
        
        def __init__(self, database):
            self.db = database
    
        @classmethod
        def create_task(cls, database, project_id, title, task_data, priority, difficulty, task_color):
            # Create a new task and return its data
            db = database
            if title is None or project_id is None:
                raise ValueError('Title and owner must be provided')
            else:
                with db.get_session() as session:
                    new_task = Tasks(
                        taskID=str(uuid.uuid4()),
                        completed=False,
                        projectID=project_id,
                        task_name=title,
                        task_data=task_data,
                        priority=priority,
                        difficulty=difficulty,
                        task_color= task_color,
                        date_created=datetime.now()
                    )
                    session.add(new_task)
                    print('Task Created!')
    
                    # Return task object data as a dictionary 
                    task_data = {
                        'taskID': new_task.taskID,
                        'completed' : new_task.completed,
                        'projectID': new_task.projectID,
                        'task_name': new_task.task_name,
                        'task_data': new_task.task_data,
                        'priority' : new_task.priority,
                        'difficulty' : new_task.difficulty,
                        'task_color' : new_task.task_color,
                        'date_created': new_task.date_created
                    }
                    return task_data

        # get all task for current user and current project
        @staticmethod       
        def get_tasks(database, project_id):
            with database.get_session() as session:
                tasks = session.query(Tasks).filter_by(projectID=project_id).all()
            return tasks
        
        # return the number of current task for project
        @staticmethod
        def get_num_of_task(database, project_id):
            with database.get_session() as session:
                num_task = session.query(Tasks).filter_by(projectID=project_id).all()
            return len(num_task)
        
        # delete task
        @staticmethod
        def delete_task(database, project_id, taskID):
            with database.get_session() as session:
                task = session.query(Tasks).filter_by(projectID=project_id, taskID=taskID).first()
                session.delete(task)

        # change task name
        @staticmethod
        def update_task(database, project_id, title):
            with database.get_session() as session:
                task = session.query(Tasks).filter_by(projectID=project_id).first()
                task.task_name = title

        @staticmethod
        def completed_tasks(database, project_id):
            with database.get_session() as session:
                task = session.query(Tasks).filter_by(projectID=project_id, completed=True).all()
            return len(task)
        
        @staticmethod
        def delete_all_tasks(database, project_id):
            with database.get_session() as session:
                tasks = session.query(Tasks).filter_by(projectID=project_id).all()
                for task in tasks:
                    session.delete(task)
                