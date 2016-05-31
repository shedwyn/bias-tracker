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
    page_fill = {
        'trigger': 'default'
    }
    return render(request, 'bias_tracker/index.html', page_fill)


@login_required(login_url='/accounts/login/')
def logout_return_home(request):
    """logs out current user and returns to home page"""
    logout(request)
    page_fill = {
        'trigger': 'logout'
    }
    return render(request, 'bias_tracker/index.html', page_fill)


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
    return render(request, 'bias_tracker/incident_log.html', page_fill)


@login_required(login_url='/accounts/login/')
def submit_new(request):
    """submits new incident and returns to home page"""
    author = request.user
    subjects = request.POST.getlist('subjects')
    incident_type = request.POST['incident_type']
    descriptors = request.POST.getlist('descriptors')
    new_incident = logic.log_new_incident(
        author, subjects, incident_type, descriptors
    )
    page_fill = {'new_incident': new_incident, 'trigger': 'submit_new'}
    return render(request, 'bias_tracker/index.html', page_fill)


@login_required(login_url='/accounts/login/')
def self_stats(request):
    """take user and render page with Incl v. Excl stats for user"""
    author_id = request.user.id
    recorded_incident_total = logic.get_total_incidents_as_author(author_id)
    percent_exclusion_logged_as_author = \
        logic.get_percent_exclusion_logged_as_author(author_id)
    percent_inclusion_logged_as_author = \
        logic.get_percent_inclusion_logged_as_author(author_id)
    descriptor_counts = logic.get_descriptor_counts_as_author(author_id)
    # return descriptors as iterable dictionary, get key and put in html, get
    # val and put in html to match
    print(descriptor_counts)
    page_fill = {
        'total': recorded_incident_total,
        'inclusion': percent_inclusion_logged_as_author,
        'exclusion': percent_exclusion_logged_as_author,
        'descriptors': descriptor_counts
    }
    return render(request, 'bias_tracker/self_stats.html', page_fill)

# def render_edit_incident_log_page(request):
#     """takes incident id, finds incident in db, fills fields w data for that
#     incident.  user may change data and submit edited record.  'submit' sends
#     data to db and redirects to menu-page"""
#     pass
