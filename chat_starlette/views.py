from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def room(request, room_name):
    return render(request, 'room_selection.html',
                  {'room_name': room_name})
