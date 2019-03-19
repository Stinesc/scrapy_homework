from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json


class SocketConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)("jeans_scraping", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("jeans_scraping", self.channel_name)

    def foodprod_message(self, event):
        self.send(text_data=event['text'])

def ws_reload_page():
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        "jeans_scraping",
        {
            "type": "jeans_scraping.message",
            "text": json.dumps({'message': 'reload'}),
        }
    )
