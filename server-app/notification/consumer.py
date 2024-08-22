import json

from channels.generic.websocket import AsyncWebsocketConsumer

from django.template import Template, Context

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("all", self.channel_name)
        print('client connected')
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard("all", self.channel_name)
        print('client disconnected')
        
    async def receive(self, text_data, bytes_data=None):
        context = {
            'message': 'testing consumer',
        }
        user = self.scope['user']
        if (user_id := user.id):
            print('here')
            print(user.username)
            context.update({'user': str(user_id)})
        else:
            print('there')
            context.update({'user': None})
        await self.send(text_data=json.dumps(context))

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
        