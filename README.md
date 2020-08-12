

##CONVIN.AI 


#Backend Assignment 


#I HAVE used RESTFRAMEWORK for TaskTracker API


#Created Task and TaskTracker models as mentioned in the task. 


#Used SQLITE3 DataBase 


#Serialised: 'task_type','update_type','email' 


#For Particularly for 1,2,3,4 as IntergerField used ListComprehension inside IntegerField as 

###IntegerField(choices=list(zip(range(1, 5), range(1, 5))), unique=True)


# Celery with Django



## Learning points
- Celery configuration
- Write celery task in django app
- Call task asynchronously
- Execute task periodically

## Installation Steps
### Step 1 - Install python dependencies
`pip install -r requirements.txt`

### Step 2 - Migrate database
`python manage.py migrate`

### Step 3 - Run celery worker to receive tasks and execute
`celery -A convin worker -l info -Q celery,high`

### Step 4 - Run celery beat for sending task periodically to workers
`celery -A convin beat`

### Step 5 - Run command line events monitor
`celery -A convin events`

### Step 6 - Monitor celery tasks and workers using flower third party web tool
- `pip install flower`
- `celery -A convin flower`

###Step 7 - python manage.py runserver