import weechat
import zmq

weechat.register("zmq-notifier", "fitztrev", "0.1", "GPL",
                 "zmq-notifier - sends message notification to zeromq", "", "")

## Setup ZMQ
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5000")

## Setup weechat hooks
weechat.hook_signal("weechat_pv",        "send_message", "")
weechat.hook_signal("weechat_highlight", "send_message", "")


## Send messages to queue
def send_message(data, signal, message):
    socket.send("message " + message)
    return weechat.WEECHAT_RC_OK
