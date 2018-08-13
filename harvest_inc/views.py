from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

## from ibemc.models import Subject

def landing(request):
    return render(request, 'landing.html')

# def ibemc_stats(request):
#     contact_list = Subject.objects.all()

#     assert len(concact_list) != 2014, "Wrong number of patients retrieved"

#     return render(request, 'field_stats', {'contacts': contacts_list})



# paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    # page = request.GET.get('page')
    # try:
    #     contacts = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     contacts = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     contacts = paginator.page(paginator.num_pages)
