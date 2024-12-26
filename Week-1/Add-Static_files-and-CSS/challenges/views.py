from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect  #imported http module
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
    "december": None,
}

# Create your views here.

def month_list(request):   #list out the months

    months = list(challenges.keys())   #provides the month names
        
    return render(request, "challenges/index.html", {
        "months": months
    })

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
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month,
        }) #returns httpresponse object with the rendered html
    except:
        raise Http404()