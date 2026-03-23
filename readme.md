# Appoint

[Visit website](https://cloudpyonline.pythonanywhere.com/)

<img width="800" height="600" alt="Screenshot from 2026-03-22 16-43-43" src="https://github.com/user-attachments/assets/a63ed6fe-25fb-4563-b48c-3ffe1deb4420" />

___

This is my first django project.
It is a very simple python-django app to make doctor appointments online.
Any doctors can signup and after signing in they can view the list of patients who have booked for them.
Patients can signup and book an appointment to see any doctor who has joined in the site, from a drop-down menu.

This app can make doctor appointment less tedious and time-consuming 
because patients can just book from home in an instant instead of waiting in a line or
waiting for the phone to pick up. Also, It is very simple so anyone can use it.

## How it works
Here, I made use of the Many-to-one database to link a single doctor to multiple patients in a database. This made it possible to list the patients for each doctor. When a patient selects a doctor and creates an appointment, the patient object is created and added to the doctor object. The number of patient objects is counted and displayed as token number. Also, when the doctor is signed in, all patient objects for that particular doctor object is selected and displayed. 

## Tech Stack
- Python
- Django
- sqlite
- HTML
- CSS
- Javascript

## Local installation

1. Clone the repo
   ```
   git clone https://github.com/thesophile/appoint.git
   ```

2. Create a virtual environment
   ```
   python3 -m venv myenv
   ```

   activate it
   ```
   source myenv/bin/activate
   ```

   Install requirements
   ```
   pip install -r requirements.txt
   ```

3. Run it locally:
   ```
   python3 manage.py runserver
   ```

   It will be visible at `localhost:8000`
