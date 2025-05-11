## MadyPro Household Services Application - v2
This repo contains the code for Modern Application Development II Project.

### Project Statement: 
Develop a multi-user application where the customers can book services offered by service professionals. The admin manages the services, service professionals, and customers.

### Frameworks and Libraries Used
- Flask: for creating controllers, and endpoint routing
- VueJS CLI: used to build user interface
- SQLAlchemy: for creating models, and establishing connection between models and controllers
- Bootstrap: to make the app aesthetically pleasing
- SQLite: used as a database
- Redis: for caching and as a message broker in Celery
- Celery: for async batch jobs and scheduling


### How To Run This Application
- Clone the project:<br>
`git clone https://github.com/devgupta1907/flaskvue.git`

- Create a virtual environment: <br>
`python -m venv env`

- Activate the virtual environment: <br>
`source backend/env/Scripts/activate`

- Install the required dependencies (for backend): <br>
`cd backend && pip install -r requirements.txt`

- Install the required dependencies (for frontend): <br>
`cd frontend && npm install`

- Run the following codes in the vscode terminal:
`cd backend/ && python3 app.py`
`sudo service redis-server start`
`~/go/bin/MailHog`
`cd backend/ && celery -A app:celery_app worker -l INFO`
`cd backend/ && celery -A app:celery_app beat -l INFO`
`cd frontend/ && npm run dev`

- <b>Note:</b> You might face some issues in running the application. In that case, just ping me either on Instagram or LinkedIn.