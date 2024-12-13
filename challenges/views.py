from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound   #imported http module
# Create your views here.

def monthly_challenges(request, month):  #this is a function based view processing request
    challenge_text = None
    if month == 'january':     #if and elif statements
        challenge_text = "Walk 20 minutes in the park for everyday."
    elif month == 'february':
        challenge_text = "Practice 1hr of django everyday."
    elif month == 'march':
        challenge_text = "Eat Vegan diet everyday."
    elif month == 'april':
        challenge_text = "Complete atleast 3 selfhelp books."
    else:
        return HttpResponseNotFound("Page not found!")
    return HttpResponse(challenge_text)   #returns a response to the server after processing the view