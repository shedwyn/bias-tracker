"""Page rendering functions for Bias Tracker

Includes use of User to authenticate and authorize.
"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render

from . import logic


@login_required(login_url='/accounts/login/')
def render_index_page(request):
    """home/menu page with all choices of redirection available"""
    return render(request, 'bias_tracker/index.html', {})


@login_required(login_url='/accounts/login/')
def render_new_incident_log_page(request):
    """renders incident log page.

    user enters field data for database. 'submit' sends data to db, saves
    entries and redirects user to home/menu page.
    """

    subjects = logic.grab_subject_options
    descriptors = logic.grab_descriptor_options
    incident_type = logic.grab_type_options
    page_fill = {
        'subjects': subjects,
        'descriptors': descriptors,
        'incident_type': incident_type
    }
    print(page_fill)
    return render(request, 'bias_tracker/incident_log.html', page_fill)
#
#
# def render_edit_incident_log_page(request):
#     """takes incident id, finds incident in db, fills fields with data for that
#     incident.  user may change data and submit edited record.  'submit' sends
#     data to db and redirects to menu-page"""
#     pass
#
#
# def render_statistics_view_page(request):
#     """renders statistics view page - auto loads user's statistics on top
#     half of page, but allow single field choice for lower half.  When user
#     selects iSubject, reload lower page with stats for that iSubject
#     'return' button returns to menu-page"""
#     pass
#
#
# def render_add_new_isubject(request):
#     """may need page to add new iSubject"""
#     pass

# def render_menu_page(request):
#     """'home' page after log-in.  user has four choices:  create new incident
#     edit existing incident, see statistics, or log out. 'submit' will direct
#     to appropriate page'"""
#     # all other pages will return to this page if the original user //
#     # remains logged in
#     user_email_login = request.POST['login_name']
#     user_name = logic.get_db_name(user_email_login)
#     # take in email, see if it exists in db, if so, return user_name, if not
#     # produce error message
#
#     pass
