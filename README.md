## Bias-Tracker Project

  Bias Tracker allows the user to record, as in Incident, any interaction with another person at her organization that may have been demonstrating unconscious gender bias as well as marking more positive Incidents where the other person was acting more like an ally.  

  She can generate a page to see what types of incidents she logged over time, and which descriptor tags she gave to all Incidents, along with a count of the number of times any named descriptor was used.  She can see the same statistics as they relate to the other person involved, i.e. did "John" have more "good" or "bad" interactions with her?

  *[See Formal Proposal](Proposal_formal.md) for more detail, including desired upgrades*

## Setup

* [Limited Requirements Needed](requirements.txt) - just Django and your virtual environment, nothing else required at present

* You will need to create a superuser to begin. From there you can add to the separate Models of Person, User, and Descriptor as needed
  * I will be adding instructions on how to do this as soon as possible
* I am in the process of writing a module to populate the descriptors, but right now it can only be done manually through the admin screen.

## Pages

#### Index Page
  * Truly the "home" page - all the present user options appear as buttons
  * Buttons linking to:
    * Log New Incident page
    * Author Stats
    * Subject Stats
    * Login/Logout
  * When the user logs out a hidden <div> fills the index.page
  * Login is required on all pages

#### Log New Incident
  * Enter new incident fields and submit
    * program will add defaults into required fields if user leaves blank
  * Return home if traveled to page in error

#### View Stats for Author
  * Auto loads all stats for user who is presently logged in
  * Return home link at top of screen

#### View Stats for Subjects
  * Auto loads list of subjects
    * choosing subject from list will generate stats for that subject
  * Return home link at top of screen

#### Login/Logout
