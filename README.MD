# FinishFast Project Manager app

I created this project to show case an application that could help me manage my other projects but instead of going with a web app I decided to try a desktop app instead.

# How I made it

The application was created using entirely Python. I used customtkinter for the GUI design and decided on using Sqlite for the database. I went with this choice because I can achieve the same results as a hosted database but instead provide more usuability for a single user as this application is not dependent on users connecting with one another (SQLALCHEMY ORM was used to make the project easy to swap over to a hosted database). It was created with the idea of being a offline application for my personal use. I decided to not use a framework because I wanted to try and see what I could achieve on my own. I used mostly customtkinter for the GUI but still used aspects of normal tkinter to round out some features. **The Project is still a W.I.P!**

# Features

- Add, view, update, and delete projects.
- Dynamic grid layout for displaying projects.
- Project overview page with detailed information.
- Modern and responsive GUI using CustomTkinter.
- Offline functionality with SQLite database.
- Easily adaptable to a hosted database using SQLAlchemy ORM.

# Lessons learned

**GUI Design with CustomTkinter:**
Learned how to create a modern and responsive desktop application interface using CustomTkinter.
Gained experience in designing layouts, managing widgets, and handling user interactions in a desktop environment.

**Database Integration with SQLite and SQLAlchemy:**
Understood how to set up and interact with a local SQLite database for storing and managing project data.
Learned how to use SQLAlchemy ORM to simplify database operations and make the application flexible for future database migrations (e.g., switching to a hosted database).

**Session Management:**
Explored how to manage database sessions effectively, ensuring efficient resource usage and avoiding common pitfalls like DetachedInstanceError.

**Database Relationships:**
Focused on the relationships between tables within my database to ensure every relationship was set to the correct type.

**Dynamic Grid Layouts:**
Implemented a dynamic grid system to display projects, which adjusts automatically based on the number of projects.
Learned how to calculate grid positions and handle layout updates dynamically.

**Event-Driven Programming:**
Gained experience in handling user actions (e.g., button clicks) and linking them to backend operations, such as querying the database and updating the UI.

**Building Without a Framework:**
Developed a deeper understanding of how to structure an application without relying on a framework.
Learned how to manage application logic, database interactions, and UI updates independently.

**Problem-Solving and Debugging:**
Encountered and resolved challenges like session management, grid layout issues, and efficient data retrieval.
Improved debugging skills by using print statements and systematically analyzing issues.

**CRUD Fundamentals:**
Strengthened knowledge of CRUD (Create, Read, Update, Delete) operations and how they are implemented in a desktop application.

**Personal Growth:**
This project has been a great opportunity to push my limits, experiment with new tools, and build something practical for personal use.

# Some Screen shots of the application running

**Login screen ↓**

![Project Screenshot](images/ff%20-%20login.PNG)

**Sign up screen ↓**

![Project Screenshot](images/ff%20-%20signup.PNG)

**Main view of project ↓**

![Project Screenshot](images/ff%20-%20main%20view.PNG)

**Adding a project ↓**

![Project Screenshot](images/ff%20-%20adding%20project.PNG)

**Note adding window ↓**

![Project Screenshot](images/ff%20-%20note%20window.PNG)

**Main view with a note and a project ↓**

![Project Screenshot](images/ff%20-%20main%20view%20note%20project.PNG)

**Project window ↓**

![Project Screenshot](images/ff%20-%20projects%20view.PNG)

**Adding task window ↓**

![Project Screenshot](images/ff%20-%20task%20window.PNG)

**Project window with task ↓**

![Project Screenshot](images/ff%20-%20project%20view%20with%20task.PNG)

**Task information window ↓**

![Project Screenshot](images/ff%20-%20task%20information.PNG)

# 🙌 Acknowledgments

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the modern and customizable Tkinter widgets.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the standard Python GUI toolkit.
- [SQLite](https://www.sqlite.org/index.html) for the lightweight, serverless database engine.
- [SQLAlchemy](https://www.sqlalchemy.org/) for the powerful and flexible ORM.
- [Python](https://www.python.org/) for being the foundation of this project.
- Thanks to the open-source community for documentation, tutorials, and inspiration!
