"""Page rendering functions for Bias Tracker

Includes use of User to authenticate and authorize.
"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render

from . import logic
from . import settings


@login_required(login_url='/accounts/login/')
def render_index_page(request):
    """render home/menu page with all further page choices"""
    page_fill = {}
    return render(request, 'bias_tracker/index.html', page_fill)


def process_login(request):
    """log in user or redirect to next page"""
    next = request.GET.get('next', '/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse('Inactive User.')
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    page_fill = {
        'redirect_to': next
    }
    return render(request, 'bias_tracker/login.html', page_fill)


@login_required(login_url='/accounts/login/')
def logout_return_home(request):
    """log out current user and return to home page"""
    logout(request)
    page_fill = {}
    return render(request, 'bias_tracker/index.html', page_fill)


@login_required(login_url='/accounts/login/')
def render_new_incident_log_page(request):
    """render incident log page."""
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
    """submit new incident and return to home page"""
    author = request.user
    subjects = request.POST.getlist('subjects')
    incident_date = request.POST['date']
    incident_time = request.POST['time']
    incident_type = request.POST['incident_type']
    descriptors = request.POST.getlist('descriptors')
    text_description = request.POST['description']
    logic.log_new_incident(
        author,
        subjects,
        incident_date,
        incident_time,
        incident_type,
        descriptors,
        text_description
    )
    page_fill = {}
    return render(request, 'bias_tracker/index.html', page_fill)


@login_required(login_url='/accounts/login/')
def render_self_stats(request):
    """take user and render author stats page"""
    author_id = request.user.id
    recorded_incident_total = logic.get_total_incidents_as_author(author_id)
    percent_exclusion_as_author = \
        logic.get_percent_exclusion_logged_as_author(author_id)
    percent_inclusion_as_author = \
        logic.get_percent_inclusion_logged_as_author(author_id)
    descriptor_counts = logic.create_descriptors_and_counts_as_author(
        author_id
    )
    page_fill = {
        'total': recorded_incident_total,
        'inclusion': percent_inclusion_as_author,
        'exclusion': percent_exclusion_as_author,
        'descriptors': descriptor_counts
    }
    return render(request, 'bias_tracker/self_stats.html', page_fill)


@login_required(login_url='/accounts/login/')
def render_subject_stats(request):
    """render blank page with subjects list.

    this renders page with only list of subjects.  user chooses subject to
    trigger js script to generate data.
    """
    subjects = logic.grab_subject_options
    page_fill = {'subjects': subjects}
    return render(request, 'bias_tracker/subject_stats.html', page_fill)


@login_required(login_url='/accounts/login/')
def get_subject_data(request):
    """extract subject id and find incident stats where id was subject."""
    subject_id = request.POST['subject']
    subject_name = logic.get_subject_name(subject_id)
    recorded_incident_total = logic.get_total_incidents_as_subject(subject_id)
    percent_exclusion_as_subject = \
        logic.get_percent_exclusion_logged_as_subject(subject_id)
    percent_inclusion_as_subject = \
        logic.get_percent_inclusion_logged_as_subject(subject_id)
    descriptor_counts = logic.create_json_ready_descriptors_and_counts(
        subject_id
    )
    subject_stats = logic.convert_subject_stats_to_json_obj(
        subject_name,
        recorded_incident_total,
        percent_exclusion_as_subject,
        percent_inclusion_as_subject,
        descriptor_counts
    )
    return JsonResponse(subject_stats)
