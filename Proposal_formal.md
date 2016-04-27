## Project Name:  Bias Tracker
#### Developer:  Erin L. Fough
#### Course:  Day Boot Camp - Spring 2016

## High-Level Product
**What is your web app going to do?**
**How does a user interact with it on a high level?**

*2 types of users:  1) participant, 2) administrator.  They can be one in the same.*

* **1) partUser** 
    * *partUser* has a web form that asks for certain information about the incident being recorded.  _First and foremost will categorize as inclusive incident **(positive)** or exclusive incident **(negative)**._
    * *??Advanced??* Would use key words/choices in form to provide possible solutions to solve this incident in the future or steps to take to resolve - possibly use data already available at NCWIT.
    * *Advanced* Method by which the partUser was was the loggee, not the logger, of an incident can rate his/her experience with the organization's response to this incident.
    * *Advanced* phone app that can manage the incident logging form

* **2) adminUser** 
    * *adminUser* has a web form that allows them to bring up statistics *(need to decide what this will be initially)* about incidents for user.
    * Base stat - ratio of inclusive v. exclusive

## Specific Functionality
**What is _every_ specific page or interface and _every_ action the user can take?**
**Pick the minimum feature set for your product to work.**
* 1. allUser page 0.5 - login screen
* 2. Directional screen?  Mainly for adminUser to choose to log an incident as partUser
    or go on to the adminUser page.
* 3. partUser page 1 - fields for details about incident.  Some fields may be linked to db with "tips" so when user submits, a new **window** pops up with those tips(should also indicate what partUser entered to elicit this(these) recommendation(s))
    * actions available - enter data, submit;
    * request for action?
* 4. partUser page 2 - *Advanced?* present suggestions for resolving negative incident or turning a 
    negative more positive.  Question:  What suggestions for reinforcing a positive incident?
* 5. *Advanced* partUser page 3 - page to rate organizational response to an incident
* 6. adminUser page 1 - Directory.  Choose to see statistics for 
    * a) logger (one who recorded incident)
        * location of incident (unclear how these subcategories could be broken down right now)
        * time of incident
        * ratios neg to pos
        * calendar improvement (grid showing tracking over time) 
        * loggees involved in any recorded incident(s)
        * *Advanced* meetings held with/about logger about incident(s)
        * *Advanced* organization decision on categorization of incident as bias and what type on flagged incident(s) - i.e. bias - gender, bias - gender and race, not bias - interpersonal
        * *Advanced* organization actions regarding incidents logged by this partUser - free-form answer? "most negative incidents related to meetings, changed meeting style to promote better inclusion"  default to None - not all incidents require recording
        * *Advanced* organization response (default None) to logger's logging of incidents - room to give "points" that can be redeemed for prizes for logging N incidents a week/month/quarter 
        -early version to include a note section anyway
    * b) loggee (one about whom an incident was recorded)
        * location of incident (unclear how these subcategories could be broken down right now)
        * time of incident
        * ratios neg to pos
        * calendar improvement (grid showing tracking over time)
        * loggers involved in any recorded incident(s)
        * *Advanced* meetings held with/about loggee about incident(s)
        * *Advanced* organization decision on categorization of incident(s) as bias and what type on flagged incident(s) - i.e. bias - gender, bias - gender and race, not bias - interpersonal
        * *Advanced* organization actions regarding incidents logged regarding this partUser - free-form answer? "most negative incidents related to meetings, changed meeting style to promote better inclusion"  default to None - not all incidents require recording
        * *Advanced* organization response (default None) to loggee involvement (inclusion), improvement (negative) - room to give "points" that can be redeemed for prizes for being mentioned in N incidents a week/month/quarter, others for (subjective) enacting recommendations to promote inclusion and more for actually improving.
    * c) aggregate of entire db of incidents
        * statistics on locations/days/times of incident(s) (unclear how to use this, but it could be useful - does this seem to happen to a wider group at meetings?  Is it happening most often on Mondays?  *unclear - what other dynamics could be quantified?  ratio of women/men in group?  what about general minority makeup of teams, what are the "meetings" - product roll out?  code review?  stat of the company?  who was leading meeting?  Was it very structured (Roberts rules) or loose?*
        * general ratios - pos to neg, marked as bias v. interpersonal, discussed formally v. not v discussed and actioned
        * calendar improvement (grid showing tracking over time for different 
        * *Advanced* satisfaction score from both logger and loggee on how any incident was handled

## Technical Components
**What are the "moving parts"?**
**What are the "modules" you're going to write?**
### Front-End
#### HTML and CSS
    * forms will be needed for every data entry point, including queries
    * Change windows or pop ups?
    * HTML and CSS to formulate the output of the data queries?
        * *I am very concerned about creating graphs and doing the statistical math*
    * to control the movement from screen to screen *(or is that HTML?)*
#### Javascript
    * to manage user inputs, including forcing answers when field data is a query tag
    * data visualizations - Chris J suggested specifically using D3 data visualization tool

### Back-End
*I'm not sure how the front and back ends communicate and what role each plays.  But I 
**think**:*
#### SQL
    * create multiple relational databases
        * user names
        * incidents (related to 2 users)
        * *Advanced* actions related to specific person(s) and/or incident(s)
        * *Advanced* user privileges (security)
    * not sure how this will relate to python and data mining - 
        * do I put the conditions in SQL or in python for once SQL hands over the data?  
        * Where does SQL get used?  
        I know in the query developer for MS Access you can run filters so maybe it is 
        more efficient to do some of the data limitation/mining with SQL as opposed to python?
#### Django
    * Assist JS with some of the execution of the graphs and charts
    * will be web interface to SQL and probably eliminate need to write all the SQL for database
    creation listed above in SQL section
    * still a little fuzzy on how I set this up
#### Python
    * to be used to calculate the statistics and transform the raw data into the proper out-put. 
    * create the classes that will work with Django to dip into the db and retrieve the data 
    requested from the web app
## Timeline

#### In what order will you tackle your technical components?

* python - write the python tranformational code assuming that we will get correctly formatted 
inputs
    * set up dummy .csv files to dump output that will be going into django for SQL db
* javascript - write the necessary code to take raw input and correct/data test before handing 
off to django
* django - create framework to connect js & python, develop db portion
* python/js/django - correcting for poor hand offs, making sure this works
* HTML/CSS - create user interface

#### Can you guess how long you'll take for each?

    * I am going to ** guess ** the following based strictly on the 3 weeks we have at the end
    of this class.  However, prior to the 3 weeks, the rough layout of information to be asked 
    will be developed (obviously not finalized) and, hopefully, some code work will begin.
    * 35% python - ~5 PDXCD class days
    * 20% js - ~ 3 PDXCD class days
    * 15% django - ~ 2 PDXCD class days
    * 15% python/js/django corrections - ~ 2 PDXCD class days
    * 10% HTML/CSS - ~ 2 PDXCD class days
    * 5% padding - ~ 1 PDXCD class days

#### What are the easy parts?

    * Django
    * HTML/CSS 

#### What are the hard parts?

    * python (base of entire app)
    * js
    * linking the two with django