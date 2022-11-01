from django.urls import path
from . import views

urlpatterns =[
    path('', views.show, name='show'),
    path('auctioneerlogin', views.auctioneerlogin, name='auctioneerlogin'),
    path('bidderlogin', views.bidderlogin, name='bidderlogin'),
    path('auctioneerlogin/newgame', views.newgame, name='newgame'),
    path('auctioneerlogin/joinexistinggame', views.joinexistinggame, name='joinexistinggame'),
    path('bidderlogin/createnewteam', views.createnewteam, name='createnewteam'),
    path('bidderlogin/joinexistingteam', views.joinexistingteam, name='joinexistingteam'),
    path('auctioneerlogin/joinexistinggame/auctioneer_auctionwindow', views.auctioneer_auctionwindow, name='auctioneer_auctionwindow'),
    path('bidderlogin/joinexistingteam/bidder_auctionwindow', views.bidder_auctionwindow, name='bidder_auctionwindow'),

]