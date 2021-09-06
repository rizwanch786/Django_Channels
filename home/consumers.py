from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
class TestConsumer(WebsocketConsumer):
    def connect(self):
       self.room_name = 'test_consumer'
       self.room_group_name = 'test_consumer_group'
       async_to_sync(self.channel_layer.group_add)(
           self. room_group_name,
           self.channel_name
           )
       self.accept()
       
       self.send(text_data = json.dumps({'status' : 'Connected from VS Code'}))

    def receive(self, text_data):
        print(text_data)
        self.send(text_data=json.dumps({"status": "We Got This"}))

    def disconnect(self, *args, **kwargs):
        # Called when the socket closes
        print('Disconnected')

    def send_notification(self, event):
        print('send_notification')
        # print(event['value'])
        data = json.loads(event['value'])
        self.send(text_data=json.dumps({'payload': data}))
        print('send_notification')

from channels.generic.websocket import AsyncJsonWebsocketConsumer
class NewConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = 'new_consumer'
        self.room_group_name = 'new_consumer_group'

        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({'ststus' : 'Connected fron new async json consumer'}))
    
    async def receive(self, text_data):
        await self.send(text_data=json.dumps({'status': 'We got this'}))
    
    async def disconnect(self, *args, **kwargs):
         print('Disconected')

    async def send_notification(self, event):
        data = json.loads(event['value'])
        await self.send(text_data=json.dumps({'payload': data}))
