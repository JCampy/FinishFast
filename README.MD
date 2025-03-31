# FinishFast Project Manager app

I created this project to show case a todo-like application that could help me manage my other projects but instead of going with a web app I decided to try a desktop app instead.

# How I made it

The application was created using entirely Python. I used customtkinter for the GUI design and decided on using Sqlite for the database. I went with this choice because I can achieve the same results as a hosted database but instead provide more usuability for a single user as this application is not dependent on users connecting with one another (SQLALCHEMY ORM was used to make the project easy to swap over to a hosted database). It was created with the idea of being a offline application for my personal use. I decided to not use a framework because I wanted to try and see what I could achieve on my own. **The Project is still a W.I.P!**

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
