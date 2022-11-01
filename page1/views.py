from django.shortcuts import render
import random
# Create your views here.

def show(request): 
    arr=["", "", ""]
    if request.method=='POST':
        s=request.POST["match"]
        temp = s.split(" vs ")
        print(temp)
        return render(request, "types_login.html", {'team1':temp[0], 'team2':temp[1], 'event_key':temp[2]})
    else:
        print(arr)
        return render(request, "types_login.html", {'team1':arr[0], 'team2':arr[1], 'event_key':arr[2]}) 
def auctioneerlogin(request):
    
    return render(request, "auctioneerlogin.html")
def bidderlogin(request):
    
    return render(request, "bidderlogin.html")
def newgame(request):
    n = random.randint(10000, 99999)
    return render(request, "newgame.html", {"n" : n})
def joinexistinggame(request):
    
    return render(request, "joinexistinggame.html")
def createnewteam(request):
    
    return render(request, "createnewteam.html")
def joinexistingteam(request):
    
    return render(request, "joinexistingteam.html")
def auctioneer_auctionwindow(request):

    return render(request, "auctioneer_auctionwindow.html")
def bidder_auctionwindow(request):

    return render(request, "bidder_auctionwindow.html")