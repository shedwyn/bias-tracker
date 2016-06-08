## Project Name:  Bias Tracker
#### Developer:  Erin L. Fough
#### Course:  Day Boot Camp - Spring 2016

## High-Level Product
**What is your web app going to do?**
**How does a user interact with it on a high level?**

*2 types of users:  1) author, 2) administrator.  They can be one in the same.*
_NOTE:  subject will be used to describe the individual **about** whom the incident is
being filed_

* The author is able to record all incidents that appear as if they *could* be unconscious gender bias as an "Incident" and save to a database with a "type" field set to "exclusion".  She will also be able to record Incident of "type: inclusion".  This helps to pinpoint potential allies within the organization.  Additional fields are the date and time of the Incident, a text field for free-form detail, the names of all individuals who were the "subjects" creating or participating in the Incident, and a multiple choice field, "descriptor".  Descriptor field choices are common behaviors that exemplify the two types and are added to help the organization see what specific behaviors are being exhibited by the individual subjects.  In some cases, behaviors can be explained by cultural differences rather than being actual gender bias.

* The author can see what percentage of her logged Incidents were marked as exclusion or inclusion, as well as the numbers of times she tagged incidents with particular descriptor tags.

* Administrators will be able to see the same data as an author can see about her own logged incidents, but the data will pertain to the "subject" of reported Incidents:  
  * How many times that individual was the subject of any Incident
  * Percentages of Incidents that were marked inclusion v. exclusion
  * The count of named descriptors used to illustrate individual's behavior.


## Specific Functionality

**What is _every_ specific page or interface and _every_ action the user can take?**
**Pick the minimum feature set for your product to work.**

* 1. Login page - login screen *match name to db*
* 2. Home/Menu page
* 3. Log Incident page
* 4. Show statistics page for self as author
    * percentages of inclusive or exclusive logged incidents
    * count of different descriptors logged overall
* 5. Show statistics page for selected subjects
    * percentages of inclusive or exclusive logged incidents
    * count of different descriptors logged overall

## Data Model

**What are the "nouns" in your project? What do they represent? What do
you need to save in the DB? What are the specific fields on each? How do
you need to search for specific instances of nouns?**

* User
  * using Django's built-in User class to handle login, authentication, and to populate the "author" field of each Incident.

* Person
    * ID Num (unique) *automatic*
    * Name

* Incident Type Descriptors (list)
    * ID Num (unique) *automatic*
    * Descriptor

* Incident
    * IDNum (unique) *automatic*
    * Author ID *many to one*
    * Subject IDs *many to many*
    * Descriptors IDs *many to many*
    * Filing Date *automatic*
    * Incident Date
    * Incident Time *optional*
    * Incident Type *two options*
    * Text Detail

## Technical Components
**What are the "moving parts"?**
**What are the "modules" you're going to write?**

### Front-End

#### HTML and CSS
  * pages will be needed for every data entry point, including queries
  * Using Bootstrap to handle device sizing and appearance
  * write some css to override the Bootstrap defaults (color)

#### Javascript
  * to manage user input validation
  * on-screen error messages
  * handle data load for subject stats page
  * one module just to handle the subject stats page and another to add to any page requiring input validation and error messages

### Back-End

#### dbSqlite
  * Using built-in default with Django, no real direct interaction, Django will translate

#### Django/Python
  * will be web interface to SQL
  * create multiple relational databases & interact with db
  * calculate the statistics and transform data into correct formats.
  * modules for logic, views, storing the urls.  Logic does not, at this time, need to be broken down into multiple pieces.

## Timeline

#### In what order will you tackle your technical components?

* Django - write modules (models?) and set up framework
* Python - write the Python code assuming that we will get correctly formatted
inputs
    * set up dummy .csv files to dump output that will be going into Django for SQL db
* Javascript - write the necessary code to take raw input and correct/data test before handing
off to Django
* Python/js/Django - correcting for poor hand offs, making sure this works
* HTML/CSS - create user interface

#### Can you guess how long you'll take for each?

    * I am going to ** guess ** the following based strictly on the 3 weeks we have at the end
    of this class.  However, prior to the 3 weeks, the rough list of data to be collected will
    be developed (obviously not finalized) and, hopefully, some code work will begin.
    * 20% Django - ~ 3 PDXCD class days
    * 26% Python - ~ 4 PDXCD class days
    * 20% js - ~ 3 PDXCD class days
    * 13% Python/js/Django corrections - ~ 2 PDXCD class days
    * 13% HTML/CSS - ~ 2 PDXCD class days
    * 6% padding - ~ 1 PDXCD class days

#### What are the easy parts?

    * Django
    * HTML/CSS

#### What are the hard parts?

    * Python
    * Javascript
    * linking the two with Django

## Future Plans

* allow authors to review all individual Incidents and edit (add a new time stamp to track changes)
* display stats visually as graphs and pie charts
* add immediate feedback - program analyzes descriptors and upon submitting new incident, returns a page with "tips" on how to address specific behavior related to gender-bias
* allow administrators to add and remove authors and subjects
* add administrator fields to Incidents to record organization's response (if any) to a reported Incident.
* add location to Incident and related statistical output to track "where" Incidents happen
* adapt overall program to be used for other types of bias - racial, religious, etc.
* create mobile-specific app for logging Incident to main db.
