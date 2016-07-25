## Inclusion/Exclusion Incident Tracker Project

  Tracker allows the user to record, as an Incident, any interaction with another person at his/her organization that had some significance to him/her in terms of making the person feel included in the group or excluded.  This might be something that made him feel particularly left-out, or made her feel warmly welcomed.  

  The user can generate a page to see what types of incidents the user logged over time, and which descriptor tags were given in all Incidents, along with a count of the number of times any named descriptor was used.  The user can see the same statistics as they relate to the other person involved, i.e. did "Chris" have more "positive/inclusive" or "negative/exclusive" interactions with her?

  *[See Formal Proposal](Proposal_formal.md) for more detail, including desired upgrades*


* [Requirements](## Requirements)
* [Admin Setup](## Admin Setup) - *written for Windows 7 using PowerShell*
  * [Initialize DB](### Initialize the SQLite DB - PostGreSQL)
  * [Superuser](### Create Superuser)
  * [Manual Instantiate](### Add Person(s) and Descriptors Manually)
  * [Auto Instantiate](### Instantiate Person(s) and Descriptors Automatically)
* [Pages](## Page)
  * [Index Page](### Index Page)
  * [New Incident](### Log New Incident)
  * [Author Stats](### View Stats for Author)
  * [Subject Stats](### View Stats for Subjects)
  * [Logout/Login](### Login/Logout)

## Requirements

* [Limited Requirements Needed](requirements.txt)

## Admin Setup

* Save files in permanent location
  * This Django project only contains one app and both are named the same.  The
  outer folder "bias_tracker" contains the manage.py folder needed to run the
  Django project.  The inner "bias_tracker" folder contains the files needed for
  the app itself.
* Initialize virtual environment *(optional)*

### Initialize the SQLite DB - PostGreSQL

* Open and review settings.py
  * check the DATABASES default settings to make sure they are correct for YOUR database.  Right now they default to my elfough settings

* In shell/terminal "bias_tracker" APP folder
  * > python ..\\manage.py createmigrations bias_tracker

* In shell/terminal "bias_tracker" PROJECT folder
  * > python manage.py migrate

### Create Superuser
* In shell/terminal "bias_tracker" PROJECT folder
  * > python manage.py createsuperuser
  * follow steps to set up your user name and password

### Add Person(s) and Descriptors Manually
* In shell/terminal "bias_tracker PROJECT folder
  * > python manage.py runserver

* In browser window run your local server but add "/admin" to the address
* Use the links to add
  * Person - these are the subjects of the incident
  * Descriptor - these are the tags that should be added to help with statistical analysis.  Trying to create code to fish key words out of a text field is more difficult than planting the key words as an option field on the form itself.

### Instantiate Person(s) and Descriptors Automatically
* This will populate the Person model with "Organization" and "Individual" only.
  * If you want to add additional Persons, follow the steps for Manual above
* This will populate the Descriptors model with (currently) one of two lists of descriptors, which will be described in the instructions below
  * If you want to add or edit Descriptors, follow the steps for Manual above
* In shell/terminal "bias_tracker" PROJECT folder
  * run Django shell - > python manage.py shell
  * >>>from bias_tracker import set_defaults
  * >>>main()
  * follow instructions to load appropriate default data.

## Pages

### Index Page
  * Truly the "home" page - all the present user options appear as buttons
  * Buttons linking to:
    * Log New Incident page
    * Author Stats
    * Subject Stats
    * Login/Logout
  * When the user logs out a hidden <div> fills the index.page
  * Login is required on all pages

### Log New Incident
  * Enter new incident fields and submit
    * program will add defaults into required fields if user leaves blank
  * Return home if traveled to page in error

### View Stats for Author
  * Auto loads all stats for user who is presently logged in
  * Return home link at top of screen

### View Stats for Subjects
  * Auto loads list of subjects
    * choosing subject from list will generate stats for that subject
  * Return home link at top of screen

### Login/Logout
