from django.shortcuts import render, redirect, HttpResponse

def display_surveys(request):
    return HttpResponse('placeholder to display all the surveys created')

def make_new_survey(request):
    return HttpResponse('placeholder for users to add a new survey')
