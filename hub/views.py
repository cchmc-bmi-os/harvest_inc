from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
from .models import Fieldstats
import os

PROJECT = os.environ['PROJECT_NAME']
site = __import__("{}.models".format(PROJECT))


def ibemc_stats(request):
    query_string = ''
    try:
        query_string = request.GET['query_string']
    except:
        pass

    fs_list = Fieldstats.objects.filter(Q(field_name__icontains=query_string) | Q(field_label__icontains=query_string)).order_by('-ep')
    paginator = Paginator(fs_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    nb_records = site.models.subjects.Record.objects.all().count()

    try:
        stats = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        stats = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        stats = paginator.page(paginator.num_pages)

    return render(request, 'field_stats.html', {'stats': stats, 'query_string': query_string, 'nb_records': nb_records})
