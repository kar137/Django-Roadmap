from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

# Create your views here.

class ReviewView(CreateView):   #inherits CreateView from django
    model = Review        #sets the model class for which form will be created
    form_class = ReviewForm         #refers to the form class and inputs labels and error messages
    template_name = "reviews/review.html"  #renders the template
    success_url = "thank-you"    #redirects if success post
    
    # def form_valid(self, form):   #works out with valid form 
    #     form.save()                  #saves form to the database
    #     return super().form_valid(form)
    

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        fav_id = request.session["favorite_review"]
        context["is_fav"] = fav_id == str(loaded_review.id)
        return context

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)

    
