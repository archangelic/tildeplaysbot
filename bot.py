#!/usr/bin/env python3
import irc.bot

import tildeplays


class TVBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channels, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.chanlist = channels
        self.bot_nick = nickname

    def on_welcome(self, c, e):
        for channel in self.chanlist:
            c.join(channel)

    def on_pubmsg(self, c, e):
        self.process_command(c, e, e.arguments[0])

    def on_privmsg(self, c, e):
        self.process_command(c, e, e.arguments[0])

    def process_command(self, c, e, text):
        nick = e.source.nick
        res = tildeplays.run(nick, text)
        if res is not None:
            c.privmsg(e.target,str(res))



if __name__ == '__main__':
    channels = [
        '#tildeplays',
    ]
    bot = TVBot(channels, 'tildeplaysbot', 'localhost')
    bot.start()
