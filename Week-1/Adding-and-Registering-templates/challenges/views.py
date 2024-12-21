from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect  #imported http module
from django.urls import reverse
from django.template.loader import render_to_string  #converts anything to string

challenges = {  #dictionary to store challenges
    "january": "Learn the basics of Data Structures and Algorithms.",
    "february": "Build a simple CRUD application using Django.",
    "march": "Master advanced Python concepts like decorators and generators.",
    "april": "Solve 30 competitive programming problems on a popular platform like LeetCode.",
    "may": "Build a personal portfolio website using HTML, CSS, and JavaScript.",
    "june": "Learn the basics of SQL and practice queries on sample datasets.",
    "july": "Understand REST APIs and integrate one into a Python project.",
    "august": "Develop a small AI-powered project, such as a chatbot or recommendation system.",
    "september": "Contribute to an open-source project on GitHub.",
    "october": "Master Git and GitHub workflows, including branching and pull requests.",
    "november": "Prepare for technical interviews by practicing 50 coding problems.",
    "december": "Review and document all the projects completed throughout the year."
}

# Create your views here.

def month_list(request):   #list out the months
    list_items = ""
    months = list(challenges.keys())   #provides the month names

    for month in months:     #looping through months
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month]) #args is a type of identifier-->[array]
        list_items += f"<li><a href='{month_path}'> {capitalized_month}</a></li>" #anchor tag for creating links
        
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenges_by_number(request, month):
    months = list(challenges.keys())
    if month > len(months):     #checking month is greater than given keys
        return HttpResponseNotFound("Invalid Month!")

    redirect_month = months[month-1]  #index starts from 0 
    redirect_path = reverse("month-challenge", args= [redirect_month])  #reverse function to redirect path challenges/january

    return HttpResponseRedirect(redirect_path)  #redirects this to monthly_challenges view's url

def monthly_challenges(request, month):  #this is a function based view processing request
    try:
        challenge_text = challenges[month]    #accessing value from dictionary
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Page not found!</h1>") #returns a response to the server after processing the view