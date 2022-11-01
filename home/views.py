from django.http import HttpRequest
from django.shortcuts import render
import requests
from datetime import datetime, timedelta
from .models import matches

# Create your views here.
def home(request):
    todays_date = (datetime.today()).strftime('%Y-%m-%d')
    uri_params = {'met': "Fixtures" , "APIkey": "a96bd2893448752400243e34ceaefdb6b6da2913273330a6251959e6b0fcd4c0", "from": todays_date , "to":todays_date }
    resp=requests.get("https://allsportsapi.com/api/cricket", params=uri_params)
    resp_dict=resp.json()
    list = []
    count = 0
    for i in resp_dict['result']:
            if((i['event_live']=='0')&(i['event_date_start']==todays_date)):
                list.append(matches(i['event_home_team'], i['event_away_team'], count, i['event_key']));    
                count=count+1
    return render( request, 'index.html', {'req' : list})
