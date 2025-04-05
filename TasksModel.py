from datetime import datetime
from Database import Database, Tasks
import uuid

class TasksModel:
        
        def __init__(self, database):
            self.db = database
    
        @classmethod
        def create_task(cls, database, title, owner, project_id):
            # Create a new task and return its data
            db = database
            if title is None or owner is None:
                raise ValueError('Title and owner must be provided')
            else:
                with db.get_session() as session:
                    new_task = Tasks(
                        taskID=str(uuid.uuid4()),
                        task_name=title,
                        userID=owner,
                        projectID=project_id,
                        date_created=datetime.now()
                    )
                    session.add(new_task)
                    print('Task Created!')
    
                    # Return task object data as a dictionary 
                    task_data = {
                        'taskID': new_task.taskID,
                        'task_name': new_task.task_name,
                        'userID': new_task.userID,
                        'projectID': new_task.projectID,
                        'date_created': new_task.date_created
                    }
                    return task_data

        # get all task for current user and current project
        @staticmethod       
        def get_tasks(database, user_id, project_id):
            with database.get_session() as session:
                tasks = session.query(Tasks).filter_by(userID=user_id, projectID=project_id).all()
            return tasks
        
        # return the number of current task for project
        @staticmethod
        def get_num_of_task(database, user_id, project_id):
            with database.get_session() as session:
                num_task = session.query(Tasks).filter_by(userID=user_id, projectID=project_id).all()
            return len(num_task)
        
        # delete task
        @staticmethod
        def delete_task(database, user_id, project_id):
            with database.get_session() as session:
                task = session.query(Tasks).filter_by(userID=user_id, projectID=project_id).first()
            session.delete(task)

        # change task name
        @staticmethod
        def update_task(database, user_id, project_id, title):
            with database.get_session() as session:
                task = session.query(Tasks).filter_by(userID=user_id, projectID=project_id).first()
                task.task_name = title
                