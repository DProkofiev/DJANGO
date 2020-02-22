from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse


def main_view(request):

    return render(request, 'firstsiteapp/index.html', context={})