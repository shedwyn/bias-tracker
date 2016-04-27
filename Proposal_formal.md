## Name
**What is the short name of your product or project?**
**Bias Tracker**

## High-Level Product
**What is your web app going to do?**
**How does a user interact with it on a high level?**

*2 types of users:  1) participant, 2) administrator.  They can be one in the same.*

**1) partUser** 
    *partUser* has a web form that asks for certain information about the incident being recorded.  *First and foremost will categorize as inclusive incident **(positive)** or exclusive incident **(negative)**.*
    *??Advanced??* Would use key words/choices in form to provide possible solutions to solve this incident in the future or steps to take to resolve - possibly use data already available at NCWIT.
    *Advanced* Method by which the partUser was was the loggee, not the logger, of an incident can rate his/her experience with the organization's response to this incident.
    *Advanced* phone app that can manage the incident logging form

**2) adminUser** 
    *adminUser* has a web form that allows them to bring up statistics *(need to decide what this will be initially)* about incidents for user.
    Base stat - ratio of inclusive v. exclusive

## Specific Functionality
**What is _every_ specific page or interface and _every_ action the user can take?**
**Pick the minimum feature set for your product to work.**
0.5) allUser page 0.5 - login screen
0.75) Directional screen?  Mainly for adminUser to choose to log an incident as partUser
    or go on to the adminUser page.
1) partUser page 1 - fields for details about incident.  Some fields may be linked to db with "tips" so when user submits, a new **window** pops up with those tips(should also indicate what partUser entered to elicit this(these) recommendation(s))
    actions available - enter data, submit;
    request for action?
2) partUser page 2 - *Advanced?* present suggestions for resolving negative incident or turning a 
    negative more positive.  Question:  What suggestions for reinforcing a positive incident?
3) *Advanced* partUser page 3 - page to rate organizational response to an incident
    Build in security from the start/permissions/log in
4) adminUser page 1 - Directory.  Choose to see statistics for 
    a) logger (one who recorded incident)
        1) location of incident (unclear how these subcategories could be broken down right now)
        2) time of incident
        3) ratios neg to pos
        4) calendar improvement (grid showing tracking over time) (d3 data visualization tool for JS)
        5) loggees involved in any recorded incident(s)
        6) *Advanced* meetings held with/about logger about incident(s)
        7) *Advanced* organization decision on categorization of incident as bias and what type on flagged incident(s) - i.e. bias - gender, bias - gender and race, not bias - interpersonal
        8) *Advanced* organization actions regarding incidents logged by this partUser - free-form answer? "most negative incidents related to meetings, changed meeting style to promote better inclusion"  default to None - not all incidents require recording
        9) *Advanced* organization response (default None) to logger's logging of incidents - room to give "points" that can be redeemed for prizes for logging N incidents a week/month/quarter 
        -early version to include a note section anyway
    b) loggee (one about whom an incident was recorded)
        1) location of incident (unclear how these subcategories could be broken down right now)
        2) time of incident
        3) ratios neg to pos
        4) calendar improvement (grid showing tracking over time)
        5) loggers involved in any recorded incident(s)
        6) *Advanced* meetings held with/about loggee about incident(s)
        7) *Advanced* organization decision on categorization of incident(s) as bias and what type on flagged incident(s) - i.e. bias - gender, bias - gender and race, not bias - interpersonal
        8) *Advanced* organization actions regarding incidents logged regarding this partUser - free-form answer? "most negative incidents related to meetings, changed meeting style to promote better inclusion"  default to None - not all incidents require recording
        9) *Advanced* organization response (default None) to loggee involvement (inclusion), improvement (negative) - room to give "points" that can be redeemed for prizes for being mentioned in N incidents a week/month/quarter, others for (subjective) enacting recommendations to promote inclusion and more for actually improving.
    c) aggregate of entire db of incidents
        1) statistics on locations/days/times of incident(s) (unclear how to use this, but it could be useful - does this seem to happen to a wider group at meetings?  Is it happening most often on Mondays?  *unclear - what other dynamics could be quantified?  ratio of women/men in group?  what about general minority makeup of teams, what are the "meetings" - product roll out?  code review?  stat of the company?  who was leading meeting?  Was it very structured (Roberts rules) or loose?*
        3) general ratios - pos to neg, marked as bias v. interpersonal, discussed formally v. not v discussed and actioned
        4) calendar improvement (grid showing tracking over time for different 
        5) *Advanced* satisfaction score from both logger and loggee on how any incident was handled

## Technical Components
**What are the "moving parts"?**
**What are the "modules" you're going to write?**
### Front-End
#### HTML and CSS
    forms will be needed for every data entry point, including queries
    Change windows or pop ups?
    HTML and CSS to formulate the output of the data queries?
        *I am very concerned about creating graphs and doing the statistical math*
#### Javascript
    to control the movement from screen to screen *(or is that HTML?)*
    to manage user inputs, including forcing answers when field data is a query tag
    data visualizations
    *Advanced* - what about security at this level?

### Back-End
*I'm not sure how the front and back ends communicate and what role each plays.  But I **think**:*
#### SQL
    create multiple relational databases
        a) user names
        b) incidents (related to 2 users)
        c) *Advanced* actions related to specific person(s) and/or incident(s)
        d) *Advanced* user privileges (security)
    not sure how this will relate to python and data mining - do I put the conditions in SQL or in python for once SQL hands over the data?  Where does SQL get used?  I know in the query developer for MS Access you can run filters so maybe it is more efficient to do some of the data limitation/mining with SQL as opposed to python?
#### Django
    not sure - this is supposed to help me create the databases and update them, do the "handing off" between Javascript and SQL?  or between Javascript to Python to SQL?
#### Python
    I think python is going to be used to calculate the statistics and transform the raw data into the proper out-put.  
    Where I can use python instead of Javascript, I would prefer, that way I only use Javascript for those things that can only be handled by Javascript.  I think it does data transformations and mining better than Javascript, but I have not worked with Javascript much.

### Timeline
**In what order will you tackle your technical components?**
**Can you guess how long you'll take for each?**
**What are the easy parts?**
**What are the hard parts?**


Work on the tough and crucial parts first.

## Submission
Create a _new_ git repo based on your project name [in GitHub](https://github.com/new).
Init that repository with a readme.
Write up your proposal as `proposal.md` and link to it from the readme.
I don't care that you learn all of the fancy parts of [writing Markdown documentation](https://help.github.com/articles/basic-writing-and-formatting-syntax/), but just get some basic sections that tackle the rubric above.

Message me with a link to your capstone repo before the proposal is due.