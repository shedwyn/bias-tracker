## Project Name:  Bias Tracker
#### Developer:  Erin L. Fough
#### Course:  Day Boot Camp - Spring 2016

## High-Level Product
**What is your web app going to do?**
**How does a user interact with it on a high level?**

*2 types of users:  1) participant, 2) administrator.  They can be one in the same.*
_NOTE:  iSubject will be used to describe the individual **about** whom the incident is
being filed_

* It is easier to speak of this in terms of the goal behind the product.  Simply, this program is 
being developed to give the person who feels she is experiencing unconscious gender bias in an 
organizational setting a sense of control.  How?

* The user is able to record all incidents that appear as if they *could* be unconscious (or
conscious) gender bias.  She can then see statistics regarding incidence (positive or
negative) of occurance (of those she recorded) by iSubject, by location, or just overall.  Later
analysis with a cooler head enables her to see the incident for what it really was (bias or not)
and where she could have taken action that might have changed the end result of the incident
    * see also "Touchy-Feely Psychological Crap" section at bottom

## Specific Functionality

**What is _every_ specific page or interface and _every_ action the user can take?**
**Pick the minimum feature set for your product to work.**

* 1. allUser page - login screen
* 2. Directional screen?  Mainly for adminUser to choose to log an incident as partUser
    or go on to the adminUser page.
* 3. partUser page 1 - fields for details about incident.
    * actions available - enter data, submit;
* 4. adminUser page 1 - Directory.  Choose to see statistics for 
    * see ratios of pos to neg in past month overall (graphical)
    * see ratios for specific iSubject (graphical)
    * see ratios for location type (graphical)

## Technical Components
**What are the "moving parts"?**
**What are the "modules" you're going to write?**

### Front-End
#### HTML and CSS
    * forms will be needed for every data entry point, including queries
    * Change windows or pop ups?
    * HTML and CSS to formulate the output of the data queries?
    * to control the movement from screen to screen
#### Javascript
    * to manage user inputs, including forcing answers when field data is a query tag
    * data visualizations - Chris J suggested specifically using D3 data visualization tool

### Back-End
#### SQL
    * create multiple relational databases
        * user names
        * incidents (related to 2 users)
    * not sure how this will relate to Python and data mining - 
        * do I put the conditions in SQL or in Python for once SQL hands over the data?  
        * Where does SQL get used?  
        I know in the query developer for MS Access you can run filters so maybe it is 
        more efficient to do some of the data limitation/mining with SQL as opposed to Python?
#### Django
    * Assist JS with some of the execution of the graphs and charts
    * will be web interface to SQL and probably eliminate need to write all the SQL for database
    creation listed above in SQL section
#### Python
    * to be used to calculate the statistics and transform the raw data into the proper out-put. 
    * create the classes that will work with Django to dip into the db and retrieve the data 
    requested from the web app

## Timeline

#### In what order will you tackle your technical components?

* Django - write modules and set up framework
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

## Touchy-Feely Psychological Crap

* By recording, and therefore quantifying, the incidents, the user can, upon later review, break
the incident down into components of ownership:  what she owns, what the organization owns, and 
what the iSubject owns.  Once that has been done, she can study herself to see what improvements
she can make, what recommendations she can make to her supervisors/organization, and that which
is beyond her control.  By turning these upsetting incidents into "mere" data, something large, amorphous, and seemingly hopeless is minimized and compartmentalized into obvious conquerable steps.

* "Positively representing unconscious gender bias" is really a ridiculous statement. In truth, 
the reason behind including the ability to record incidents representing inclusiveness is 
meant to give the user additional information to frame their interaction with others in the 
workplace/classroom.  This to, can be a source of empowerment.  Not every interaction is negative.
In studying the positive interactions she can, over time, learn specifically what the other person does to be inclusive, and incorporate those actions into her own life.  It also prevents the user 
from unconsciously developing an incorrect visualization of the organizational setting because she 
is only remembering the negative interactions.  It can also help her to identify potential allies 
in the organization who might be receptive to taking a greater role in improving inclusiveness and working to end gender bias.

* The advanced features will allow an organization to better map where/how/when they are 
succeeding and ditto where they have the opportunity to make improvement.  Ideally there will
be a way for user to connect to resources that allow her to gradually become better at 
handling these incidents sooner (each time).  Theoretically, identifying a developing situation
that might result in bad behaviour early enough in the interaction may allow the user to turn
the situation around.  By, for example, asking a pointed question early on, or deliberately moving into the person's line of sight, or bravely and deliberately stopping a meeting organizer from 
moving to the next topic when her questions have not been answered successfully.