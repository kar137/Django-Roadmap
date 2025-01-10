from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.views import View

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
        "form": form,
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():        #checks the validity of the data with built in is_valid method
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "reviews/review.html", {
        "form": form,
        })

def thankyou(request):
    return render(request, "reviews/thankyou.html")
