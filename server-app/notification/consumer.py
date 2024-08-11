import json

from channels.generic.websocket import AsyncWebsocketConsumer

from django.template import Template, Context

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gangs", self.channel_name)
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard("gangs", self.channel_name)

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
        