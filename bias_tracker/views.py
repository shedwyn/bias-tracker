from django.http import HttpResponse
from django.shortcuts import render
from . import logic


def render_login_page(request):
    """renders the home login page.  submitting the log in will redirect to
    menu-page"""
    return render(request, 'jokes/form.html', {})


def render_menu_page(request):
    """'home' page after log-in.  user has four choices:  create new incident
    edit existing incident, see statistics, or log out. 'submit' will direct
    to appropriate page'"""
    # all other pages will return to this page if the original user //
    # remains logged in
    # request will include login name, call logic operation that will//
    # send that information to db and return
    user_email_login = request.POST['email']
    user_name = logic.get_db_name(user_email_login)
    # take in email, see if it exists in db, if so, return user_name, if not//
    # produce error message

    pass

def render_new_incident_log_page(request):
    """renders incident log page.  user enters field data for database.
    'submit' sends data to db and redirects to menu-page"""
    pass


def render_edit_incident_log_page(request):
    """takes incident id, finds incident in db, fills fields with data for that
    incident.  user may change data and submit edited record.  'submit' sends
    data to db and redirects to menu-page"""
    pass


def render_statistics_view_page(request):
    """renders statistics view page - auto loads user's statistics on top
    half of page, but allow single field choice for lower half.  When user
    selects iSubject, reload lower page with stats for that iSubject
    'return' button returns to menu-page"""
    pass


def render_add_new_isubject(request):
    """may need page to add new iSubject"""
    pass
