from datetime import datetime
from Database import Database, Projects
import uuid
class ProjectsModel:
    
    def __init__(self, database):

        self.db = database

    @classmethod
    def create_project(cls, database, title, owner):
        #Create a new project and return its values
        db = database
        if title is None or owner is None:
            raise ValueError('Title and owner must be provided')
        else:
            
            with db.get_session() as session:
                new_project = Projects(
                    projectID=str(uuid.uuid4()),
                    project_name=title,
                    userID=owner,
                    date_created=datetime.now()
                )
                session.add(new_project)
                print('Project Created!')

                # Return project data as a dictionary 
                project_data = {
                    'projectID': new_project.projectID,
                    'project_name': new_project.project_name,
                    'userID': new_project.userID,
                    'date_created': new_project.date_created
                }
                return project_data
    
    # Get users projects
    @staticmethod
    def get_projects(database, user_id):

        with database.get_session() as session:
            projects = session.query(Projects).filter_by(userID=user_id).all()
        return projects
    
    def num_of_projects(self, user_id):
        with self.db.get_session() as session:
            projects = session.query(Projects).filter_by(userID=user_id).all()
        return len(projects)

    # Delete project
    def delete_project(self, project_id):
        with self.db.get_session() as session:
            project = session.query(Projects).filter_by(projectID=project_id).first()
            session.delete(project)

    # Update project
    def update_project(self, project_id, title):
        with self.db.get_session() as session:
            project = session.query(Projects).filter_by(projectID=project_id).first()
            project.project_name = title
        session.commit()



    
