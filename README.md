Medication Management API

To install and run this app please git clone the project into a new directory. To run, this
project requires python 2.7 installed along with the pip dependency management. Next, navigate into
the outer directory for the project and run 'pip install -r requirements.txt' in a terminal.
This will install the dependencies required to run the application. To set up the model migrations, run
'python manage.py makemigrations medication_management' then 'python manage.py migrate'. This will create a
sqlite database for the app. After this, run 'python manage.py runserver [PORT]' replacing [PORT] with the
port that you want run the application on. The application will now be running on localhost (127.0.0.1:[PORT]).

The four endpoints available in this application are:
- Create a medication: /medication
    - Example JSON data: {'name': 'Warfarin'}

- Create a patient: /patient
    - Example JSON data: {'first_name': 'Steven', 'last_name': 'Test'}

- Add a medication to a patient's list of medications: /patient/<patient_id>/medication/add
    - Example JSON data: {'id': 1} with 'id' being the id of the medication

- Remove a medication from a patient's list of medications: /patient/<patient_id>/medication/remove
    - Example JSON data: {'id': 1} with 'id' being the id of the medication