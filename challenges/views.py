from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# def january(request):
#     return HttpResponse("this works!")

# def february(request):
#     return HttpResponse("February")

# we can also make views dynamically based on the name of the month in the url patterns

monthly_challenges = {
    "january" : "do this in jan",
    "february" : "do this in feb",
    "march" : "do this in mar",
    "april" : "do this in apr",
    "may" : "do this in may",
    "june" : "do this in jun",
    "july" : "do this in jul",
    "august" : "do this in aug",
    "september" : "do this in sep",
    "october" : "do this in oct",
    "november" : "do this in nov",
    "december" : None,

}

def index(request) :
    list_items = ""
    months = list(monthly_challenges.keys())
    # for month in months :
    #     month_path = reverse("month-challenge" , args=[month])
    #     list_items += f"<li><a  href= \"{month_path}\">{month.capitalize()} </a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    return render(request , "challenges/index.html" , {
        "months" : months

    })

def monthly_challenge(request , month):
    # if month == 'january' :
    #     challenge_text = "jan"
    # elif month == 'february' :
    #     challenge_text = "feb"
    # elif month == 'march' :
    #     challenge_text = "march"
    # else:

    try:
        challenge_text = monthly_challenges[month]
       
        #response_data = f"<h1>{challenge_text}</h1>" # f allows use to insert variables inside string in python 
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
        return render(request , "challenges/challenge.html" , {
            "text" : challenge_text,
            "mon" : month#.capitalize()
        }) #the third arg is a dictionary, in which we can set key - value pairs 
    except:
        return HttpResponseNotFound("<h1>this month is not supported</h1>")
   

def monthly_challenge_by_number(request , month) :
    months_list = list(monthly_challenges.keys())

    if month > len(months_list):
        return HttpResponseNotFound("invalid month number")

    redirect_month = months_list[month-1]

    redirect_path = reverse("month-challenge" , args = [redirect_month]) # args contains the list of dynamic element of the path 
    return HttpResponseRedirect(redirect_path)

