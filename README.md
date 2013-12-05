## Weechat ZeroMQ Notifier

[![Build Status](https://travis-ci.org/fitztrev/weechat-zmq-notifier.png?branch=master)](https://travis-ci.org/fitztrev/weechat-zmq-notifier)

I run Weechat inside tmux on a remote server. I miss being able to see desktop notifications of certain events. So I made this.

It's a Weechat plugin that sends notifications of highlights or private messages to ZeroMQ on the server.

On your local machine, you run the client which connects to it. Whenever a new message is received, it'll pass it along to your Notification Center.

The client works on both Mac OS X and Ubuntu.

## Usage

#### On the remote machine where Weechat is running

```
$ sudo apt-get install python-zmq
$ ln -s zmq-notifier.py ~/.weechat/python/autoload/zmq-notifier.py
```

Then, restart Weechat.

#### On your local machine where you want to receive notifications

*For Mac OS X:*

```
$ gem install terminal-notifier
$ brew install zmq
$ pip install pyzmq
$ ./irc-notifier <hostname|ip>
```

*For Ubuntu:*

```
$ sudo apt-get install python-zmq
$ ./irc-notifier <hostname|ip>
```
