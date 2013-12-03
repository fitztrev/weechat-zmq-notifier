## Weechat ZeroMQ Notifier

I run Weechat inside tmux on a remote server. I miss being able to see desktop notifications of certain events. So I made this.

It's a Weechat plugin that sends notifications of highlights or private messages to zeromq on the server.

On your local machine, you run the client which connects to it. Whenever a new message is received, it'll pass it along to your Notification Center.

Still a work-in-progress.
