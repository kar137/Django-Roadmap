from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound   #imported http module

challenges = {
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

def monthly_challenges_by_number(request, month):
    return HttpResponse(month)

def monthly_challenges(request, month):  #this is a function based view processing request
    try:
        challenge_text = challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Page not found!")
       #returns a response to the server after processing the view