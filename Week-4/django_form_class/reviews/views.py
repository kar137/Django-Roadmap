from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm

# Create your views here.

def review(request):
    if request.method == 'POST':
        form = ReviewForm()
        if form.is_valid():        #checks the validity of the data with built in is_valid method
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")

    form = ReviewForm()
    
    return render(request, "reviews/review.html", {
        "form": form,
    })

def thankyou(request):
    return render(request, "reviews/thankyou.html")
