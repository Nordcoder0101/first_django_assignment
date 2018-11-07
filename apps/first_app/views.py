from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse("placeholder to display a list of blogs")

def new(request):
    print('worked')
    return HttpResponse('Placeholder to display a new form to create a new blog')

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f'placeholder to edit blog number: {number}')

def destroy(request, number):
    print('redirected')
    return redirect('/')