from django.shortcuts import render, redirect, HttpResponse

def create_new_user(request):
    return HttpResponse('placeholder for users to create a new user')

def login(request):
    return HttpResponse('placeholder for users to login')

def display_users(request):
    return HttpResponse('placeholder to later display all the list of users')
