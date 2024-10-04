# Appoint 

This is my first real django project.
It is a simple python-django app to make doctor appointments online.
Any doctors can signup and after signing in they can view the list of patients who have booked for them.
Patients can signup and book an appointment to see any doctor who has joined in the site, from a drop-down menu.

This app can make doctor appointment less tedious and time-consuming 
because patients can just book from home in an instant instead of waiting in a line or
waiting for the phone to pick up.

## How it works
Here, I made use of the Many-to-one database to link a single doctor to multiple patients in a database. This made it possible to list the patients for each doctor. When a patient selects a doctor and creates an appointment, the patient object is created and added to the doctor object. The number of patient objects is counted and displayed as token number. Also, when the doctor is signed in, all patient objects for that particular doctor object is selected and displayed. 
