from django.shortcuts import render
import json
from datetime import datetime, timedelta
from collections import OrderedDict
import requests
from .models import playpts

# Create your views here.
def points_table(request):
    todays_date = (datetime.today()-timedelta(1)).strftime('%Y-%m-%d')
    uri_params = {'met': "Fixtures" , "APIkey": "a96bd2893448752400243e34ceaefdb6b6da2913273330a6251959e6b0fcd4c0", "from": todays_date , "to":todays_date }
    resp=requests.get("https://allsportsapi.com/api/cricket", params=uri_params)
    resp_dict=resp.json()
    list = []
    if resp_dict['success']==1 :
      for i in resp_dict['result'] :
          
          
          if i['league_name']=="IPL" :
            
            count = 0
            print("match " + i['event_home_team']+" vs "+i['event_away_team'] )
            
            for j in i['scorecard']:
              if count==0:
                x=j
              else:
                y=j
              count=count+1
            
            thisdict={}
            
            for j in i['scorecard'][x]:

                if(j['type']=='Batsman'):
                  points = (int)(j['R'])*1 + (int)(j['4s'])*1 + (int)(j['6s'])*2
                  if((int)(j['R'])>=25 and (int)(j['R'])<50):
                    points+=4
                  if((int)(j['R'])>=50 and (int)(j['R'])<75):
                    points+=8
                  if((int)(j['R'])>=75 and (int)(j['R'])<100):
                    points+=15
                  if((int)(j['R'])>=100 and (int)(j['R'])<125):
                    points+=20
                  if((int)(j['R'])>=125 and (int)(j['R'])<150):
                    points+=25
                  if((int)(j['R'])>=150 ):
                    points+=30
                  if((int)(j['R'])==0 and j['status']!="not out"):points+=-4
                  if(j['status']=="not out" and i['event_status']=="Finished"):points+=4
                  
                  if i['event_status']=="Finished" and (int)(j['R'])>6 :
                    sr=(float)(j['SR'])
                    if(sr<50):
                      points+=-12
                    if(sr<60.0 and sr>=50.0):
                      points+=-10
                    if(sr<70 and sr>=60):
                      points+=-8
                    if(sr<150 and sr>=130):
                      points+=8
                    if(sr<170 and sr>=150):
                      points+=10
                    if(sr<200 and sr>=170):
                      points+=12
                    if(sr>=200):
                      points+=16
                    
                  thisdict.update({j['player']:points})
                  
                if(j['type']=='Bowler'):
                  points= (int)(j['W'])*20
                  if i['event_status']=="Finished" :
                    w=(int)(j['W'])
                    er=(float)(j['ER'])
                    if(w==3):points+=8
                    if(w==4):points+=12
                    if(w==5):points+=25
                    if(er<=5.00):points+=12
                    if(er>5.00 and er<=6.00):points+=8
                    if(er>6.00 and er<=7.00):points+=4
                    if(er>7.00 and er<=8.00):points+=2
                    if(er>5.00 and er<=6.00):points+=8
                    if(er>=10.00 and er<11.00):points+=-4
                    if(er>=11.00 and er<12.00):points+=-8
                    if(er>=12.00):points+=-12
                  
                  thisdict.update({j['player']:points})
              
              

          



            
            for j in i['scorecard'][y]:
                if(j['type']=='Batsman'):
                  points = (int)(j['R'])*1 + (int)(j['4s'])*1 + (int)(j['6s'])*2
                  if((int)(j['R'])>=25 and (int)(j['R'])<50):
                    points+=4
                  if((int)(j['R'])>=50 and (int)(j['R'])<75):
                    points+=8
                  if((int)(j['R'])>=75 and (int)(j['R'])<100):
                    points+=15
                  if((int)(j['R'])>=100 and (int)(j['R'])<125):
                    points+=20
                  if((int)(j['R'])>=125 and (int)(j['R'])<150):
                    points+=25
                  if((int)(j['R'])>=150 ):
                    points+=30
                  if((int)(j['R'])==0 and j['status']!="not out"):points+=-4
                  if(j['status']=="not out"):points+=4
                  if i['event_status']=="Finished" and (int)(j['R'])>6 :
                    sr=(float)(j['SR'])
                    if(sr<50):
                      points+=-12
                    if(sr<60.0 and sr>=50.0):
                      points+=-10
                    if(sr<70 and sr>=60):
                      points+=-8
                    if(sr<150 and sr>=130):
                      points+=8
                    if(sr<170 and sr>=150):
                      points+=10
                    if(sr<200 and sr>=170):
                      points+=12
                    if(sr>=200):
                      points+=16
                  if j['player'] in thisdict.keys():
                    thisdict[j['player']]+=points
                  else:
                    thisdict.update({j['player']:points})
                  
                if(j['type']=='Bowler'):
                  points= (int)(j['W'])*20
                  if i['event_status']=="Finished" :
                    w=(int)(j['W'])
                    er=(float)(j['ER'])
                    if(w==3):points+=8
                    if(w==4):points+=12
                    if(w==5):points+=25
                    if(er<=5.00):points+=12
                    if(er>5.00 and er<=6.00):points+=8
                    if(er>6.00 and er<=7.00):points+=4
                    if(er>7.00 and er<=8.00):points+=2
                    if(er>5.00 and er<=6.00):points+=8
                    if(er>=10.00 and er<11.00):points+=-4
                    if(er>=11.00 and er<12.00):points+=-8
                    if(er>=12.00):points+=-12
                  if j['player'] in thisdict.keys():
                    thisdict[j['player']]+=points
                  else:
                    thisdict.update({j['player']:points})
                  




            
            #print(count)
            #if count==0 :



            sorted_values = sorted(thisdict.values()) # Sort the values
            sorted_dict = {}

            for i in sorted_values:
                for k in thisdict.keys():
                    if thisdict[k] == i:
                        sorted_dict[k] = thisdict[k]
                        break
            sorted_dict2 = dict( sorted(thisdict.items(),
                           key=lambda item: item[1],
                           reverse=True))
            count=1
            for i in sorted_dict2.keys():
                list.append(playpts(i ,str(sorted_dict2[i]), count))
                print(i + "                  "+str(sorted_dict2[i]))
                count=count+1
            # print('')
    else :
      print("Error, url not fetched")
    return render(request, "points_table.html", {'pts':list})