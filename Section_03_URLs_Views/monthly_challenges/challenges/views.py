from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Read a new book every week!",
    "may": "Try a new recipe every day!",
    "june": "Exercise for at least 30 minutes every day!",
    "july": "Learn a new language for at least 20 minutes every day!",
    "august": "Write a journal entry every day!",
    "september": "Practice meditation for at least 10 minutes every day!",
    "october": "Take a photo every day and create a photo journal!",
    "november": "Learn a musical instrument for at least 20 minutes every day!",
    "december": "Spread kindness and do a random act of kindness every day!"
}


def index(request):
    months = list(monthly_challenges.keys())
    month_list = "<ul>"
    for month in months:
        redirect_path = reverse("month-challenge", args=[month])
        month_list += f"<li> <a href='{redirect_path}'> {month.capitalize()} </a> </li>"
    month_list += "</ul>"
    return HttpResponse(month_list)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound("This month is not supported!")
    # return HttpResponse(challenge_text)
    return HttpResponse(response_data)


def monthly_challenges_by_number(request, month):

    if month > 12 or month < 1:
        return HttpResponseNotFound("Invalid month!")

    months = list(monthly_challenges.keys())
    forward_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[forward_month])

    return HttpResponseRedirect("/challenges/" + forward_month)
