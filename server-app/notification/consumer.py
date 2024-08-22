import json

from channels.generic.websocket import AsyncWebsocketConsumer

from django.template import Template, Context

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print('client connected')
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard("all", self.channel_name)
        print('client disconnected')
        
    async def receive(self, text_data, bytes_data=None):
        user = self.scope['user']
        if (user_id := user.id):
            await self.channel_layer.group_add(user.username, self.channel_name)
            await self.send(text_data="Success")
        else:
            await self.send(text_data="Unathorized Access")
            await self.disconnect()

    async def send_notification(self, event):
        message = event["message"]

        template = Template('<div class="notification"><p>{{message}}</p></div>')
        context = Context({"message": message})
        rendered_notification = template.render(context)

        await self.send(    
            text_data=json.dumps(
                {
                    "type": "notification",
                    "message": rendered_notification
                }
            )
        )
        