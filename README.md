# Bias-Tracker Purpose and Function

*[See Formal Proposal](general_notes/Proposal_formal.md)*


##Background

* I found myself in the position of truly being the minority in an environment created for the majority when I enrolled in an intensive programming vocational learning "bootcamp" in 2016.  Having once been 1/10 of the non-black employees at a historically black organization, I thought I had experienced being the "minority" but it is quite different to truly be the minority in a world structured for someone else.

* One thing I started to do was write down when an incident of possible gender bias occurred, so I could look back at it with a cooler head and determine if it really was bias in action.  I also decided to record when someone else was kind to me, or inclusive, because it only felt "fair" to record both types of interactions.  When I counted, I found that there were far more inclusive incidents than exclusive.  The idea for this web application was born in that moment.

* When I can take something unpleasant and dissect it, I feel empowered.  When I break it down into component parts, it is just like code - I can see where my function breaks between the input and the output, shall we say?  


## Function

* The user may record any incident of (potential) unconscious gender bias that she witnesses at her organization.  Data recorded includes the filing date, the occurrence date and time, the individual or individuals who exhibited any of the behavior described, tags of specific types of exclusionary behavior, and a short description of what happened in her own words.

* The user may also record any incident where the other individual exhibited inclusive behavior - thus being a potential ally.  Data recorded includes the incident filing date, the event date and time, the individual or individuals who exhibited any of the behavior described, tags of specific types of exclusionary behavior, and a short description of what happened in her own words.

* The user may see the following usage statistics for her own use:
  * total number of incidents recorded
  * percentages of inclusion v. exclusion incidents she has recorded
  * descriptors she recorded and the number of times each descriptor was used

* The user may see the following statistics for any individual subject:
  * total number of incidents recorded in which individual was (one of) the subject(s)
  * percentages of inclusion v. exclusion incidents in which individual was (one of) the subject(s)
  * number of times any given descriptors were used in those incidents where the individual was (one of) the subject(s)


## Future Plans

* tiered authentication to limit access to subject data only to those with staff access
* allow authors to review all individual Incidents and edit (add a new time stamp to track changes)
* display stats visually as graphs and pie charts
* add immediate feedback
  * program analyzes descriptors and upon submitting new incident, returns a page with "tips" on how to address specific behavior related to gender-bias
* allow administrators to add and remove authors and subjects
* add administrator fields to Incidents to record organization's response (if any) to a reported Incident.
* add location to Incident and related statistical output to track "where" Incidents happen
* adapt overall program to be used for other types of bias - racial, religious, etc.
* create mobile-specific app for logging Incident to main db.
* points/rewards system for recording incidents, being part of a positive inclusive incident, and/or showing overall improvement as an individual
