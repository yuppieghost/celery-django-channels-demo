from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
channel_layer = get_channel_layer()


def send_channel_msg(channel_name, msg):
    async_to_sync(channel_layer.group_send)(channel_name, {
        'type': 'chat_message',
        'message': msg,
    })


send_channel_msg('chat_a','hello')