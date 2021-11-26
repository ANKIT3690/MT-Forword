import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hai {}!!</b>

<b>An advanced Auto file Forward Bot A.I

This Bot forward all files to One Public channel to Your Personal channel But you should be admin or owner otherwise it will not reach till your desire Destination
You can also forward files from other channel even if you are not an admin 
Forward files on your own risk

More details /help

© @thewarrriorsreal</b>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>Follow These Steps!!</b>

<b>• Currectly fill your Heroku Config vars</b> <code>FROM_CHANNEL</code> and <code>TO_CHANNEL</code> <b>and other Vars</b>

<b>• Then give admin permission in your personal telegram channel</b>

<b>• Then send any message In your personal telegram channel</b>

<b>• Then use /run command in your bot</b>

<b><u>Available Command</b></u>

* /start - <b>Bot Alive</b>

* /help - <b>more help</b>

* /run - <b>start forward</b>

* /about - <b>About Me</b>"""
  ABOUT_TXT = """<b><u>📃My Info</b></u>

<b>🤖Name :</b> <code>ᥴꪮꪀᥴꫀꪖꪶꫀᦔ 𝓽ꫀᥴꫝꪀꪮꪶꪮᧁ𝓲ꫀ𝘴</code>

<b>👨‍🎓Creator :</b> <code>@ANKIT3690</code>

<b>👨‍🎓Creator :</b> <code>@Saurav3BV6SA9LLElon7Musk</code>

<b>🎙️Language :</b> <code>Python3</code>

<b>📚Lybrary :</b> <code>Pyrogram v1.2.9</code>

<b>🛑Server :</b> <code>Heroku</code>

<b>📱Build :</b><code>V0.1</code>"""
