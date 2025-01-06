from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def review(request):
    if request.method == 'POST':
        entered_username = request.POST['username']

        if entered_username == "" and len(entered_username) >= 50 :
            return render(request, "reviews/review.html", {
                "has_error":True
                })
        print(entered_username)
        return HttpResponseRedirect("/thank-you")


    return render(request, "reviews/review.html", {
        "has_error": False
    })

def thankyou(request):
    return render(request, "reviews/thankyou.html")
