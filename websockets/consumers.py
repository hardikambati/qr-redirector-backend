import json

# 3rd party
from . import utility
from channels.generic.websocket import AsyncWebsocketConsumer


class Consumer(AsyncWebsocketConsumer):
    """
    Websocket connection code snippets
    """

    async def connect(self):
        await self.accept()
        encrypted_channel_id = utility.encrpyted_channel_id(self.channel_name)
        await self.send(text_data=json.dumps({'message': encrypted_channel_id}))


    async def disconnect(self, code):
        print(self.channel_name)
        print(f'[DISCONNECT] {code}')


    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data=json.dumps({'message': text_data}))


    async def redirect_event(self, event):
        message = event['message']

        print(f'[WEBSOCKET] {message}')
        
        str_message = json.dumps(message)
        await self.send(text_data=str_message)

        # await self.close()
