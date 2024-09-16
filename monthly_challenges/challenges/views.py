from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges={
    "january":"Start the year with a clean slate. Set your most important goals.",
    "february":"Listen to your inner voice. Keep a journal to better understand yourself.",
    "march":"Make your diet balanced. Movement is life! Find time for physical activity.",
    "april":"Renew connections with loved ones. Express your feelings.",
    "may":"Invest in your learning. Learn something new.",
    "june":"Enjoy the moment. Plan a vacation or simply set aside time to relax.",
    "july":"Analyze your expenses. Create a budget.",
    "august":" Let your imagination run wild. Try new creative hobbies.",
    "september":"Get your life in order. Plan your day.",
    "october":"Be grateful for everything you have. Keep a gratitude journal.",
    "november":"Take care of your physical and mental health.",
    "december":None
}

def index(request):
    
    months=list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months":months
    })

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound("This month is not supported")
    redirect_month=months[month-1]
    redirect_path=reverse("monthly_challenge",args=[redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(requests,month):
    try:
        challenge_text=monthly_challenges[month]
        return render(requests,"challenges/challenge.html",{
            "text":challenge_text,
            "month":month.capitalize(),
            "my_text":month+' '+'challenge'
        })
    except:
        raise Http404()
    