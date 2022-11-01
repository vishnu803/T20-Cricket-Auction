import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name ='test'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        arr = message.split(" ")
        if (arr[1]=="L") :
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':"bid",
                    'message':message
                }
            ) 
        else :
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':message,
                    'message':message
                }
            )  
    def call1(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type':'call1',
            'message':message
        }))
    def call2(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type':'call2',
            'message':message
        }))
    def call3(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type':'call3',
            'message':message
        }))
    def sold(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type':'sold',
            'message':message
        }))
    def unsold(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type':'unsold',
            'message':message
        }))
    def bid(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type':'bid',
            'message':message
        }))


