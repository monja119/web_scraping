import requests
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from scraping.sites import *


def home(request):
    amazon = Amazon().file_product
    return render(request, 'base.html', locals())


# <>