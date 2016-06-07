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
conscious, really) gender bias.  She can then see statistics regarding incidence (positive or
negative) of occurance (or those she recorded) by iSubject, by location, or just overall.  Later
analysis with a cooler head enables her to see the incident for what it really was (bias or not)
and where she could have taken action that might have changed the end result of the incident
    * see also "Touchy-Feely Psychological Crap" section at bottom

## Specific Functionality
**What is _every_ specific page or interface and _every_ action the user can take?**
**Pick the minimum feature set for your product to work.**

* 1. allUser page 1
    * login screen
* 2. adminUser page 1
    * directional - choose to log incident or move to admin screen (only for admin)
* 3. partUser page 1
    * opt-in screen with explanation of how data can be used
* 3. partUser page 2
    * fields for details about incident
    * select whether s/he wants to receive tips upon submission about how to handle similar in future
    * select whether she wants to be specifically contacted by organization regarding this incident
    * actions available - enter data, submit;
* 4. partUser page 3
    * present suggestions for resolving negative incident or turning a negative more positive.  Needed: how to parse this, where is data, create my own db of tips by breaking down other
    forms
* 5. partUser page 4
    * page to rate organizational response to an incident
* 6. adminUser page 2
    * Review and Retrieve Data, divided by three sections
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

            ## Data Model

            **What are the "nouns" in your project? What do they represent? What do
            you need to save in the DB? What are the specific fields on each? How do
            you need to search for specific instances of nouns?**

            * iSubject
                * ID Num (unique)
                * Name
                * Gender
                * Minority Status (observed)
            * Incident
                * IDNum (unique)
                * iSubject ID (links to iSubject db) (list)
                * Incident Filing Date
                * Incident Date
                * Incident Time
                * Incident Type (pos/neg)
                * Incident Type Descriptors (list)
                * Subject Matter (limit to list)
                * Subject Stray (yes/no)
                * Text Box for Detail
                * Mitigation During (limit to list / ID links to other table?)
                * Mitigation After (limit to list / ID links to other table?)
                * Physical Location of Incident
                * Size of Group at Time of Incident
                * Leader of Group Where Incident Occurred



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
    ## Touchy-Feely Psychological Crap

    * By recording, and therefore quantifying, the incidents, the user can, upon later review, break
    the incident down into components of ownership:  what she owns, what the organization owns, and
    what the iSubject owns.  Once that has been done, she can study herself to see what improvements
    she can make, what recommendations she can make to her supervisors/organization, and that which
    is beyond her control.  By turning these upsetting incidents into "mere" data, something large,
    amorphous, and seemingly hopeless is minimized and compartmentalized into obvious conquerable steps.

    * The reason behind including the ability to record incidents representing INclusiveness is
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
