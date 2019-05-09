
from chat import cele


@cele.task
def mutiply(x, y):
    return x * y


@cele.task
def add(x, y):
    return x + y +1


from . import tests

@cele.task
def hello():
    tests.send_channel_msg('chat_a','hello')

