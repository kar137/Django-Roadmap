from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

# Create your views here.

class ReviewView(FormView):   #inherits FormView from django
    form_class = ReviewForm
    template_name = "reviews/review.html"  #renders the template
    success_url = "thank-you"    #redirects if success post
    
    def form_valid(self, form):   #works out with valid form 
        form.save()                  #saves form to the database
        return super().form_valid(form)
    

class ThankyouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):    #works out with context info to be passed on to the template
        context = super().get_context_data(**kwargs)   #refers to the built in context
        context["message"] = "This Works!"      #adds extra context
        return context                           #returns context

class ReviewListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review           #refers to the model class
    context_object_name = "reviews"        #sets the context name for use in templates
    
class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
    
