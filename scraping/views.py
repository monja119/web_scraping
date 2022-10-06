from django.http import HttpResponse
from scraping.sites import *
from scraping.models import Site


def home(request):
    error = None
    # creating requires
    all_data = []

    # getting available sites
    for i in range(len(sites)):
        site_name = sites[i]
        content = []

        exists = False

        # affecting exists if exists
        for site in Site.objects.all():
            if site_name == site.title:
                exists = True
                break

        # updating or inserting new data
        if exists is True:
            # updating
            content = eval('{}Site().file_product'.format(site_name.capitalize()))
            for k in range(len(content)):
                all_data.append(content[k]['content'])

            # pushing new data
            Site.objects.filter(title=site_name).update(
                title=site_name,
                content=content
            )
        else:
            if content is not None:
                # making content
                content = eval('{}Site().file_product'.format(site_name.capitalize()))
                for k in range(len(content)):
                    all_data.append(content[k]['content'])

                # creating data
                site = Site()
                site.title = site_name
                site.content = content
                site.save()

    return HttpResponse(all_data)

