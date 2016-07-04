import botconfig
from slackteam import SlackTeam
from messagepattern import MessagePattern
from messagerule import MessageRule

# TODO: these could live in a class that is shared between rule generators.
# Each rule generator would have its own instance, though. That way they
# are independent of one another and can use different users/teams.
botuser = None
team = None

def greeting(message):
    msg1 = "Hello there! I'm just a little baby bot right now, and I can't do much, but one day I'll grow up big and strong!"
    msg2 = "Here are some of the things I'm going to be able to do:"
    msg3 = "/dailyspecials: provides a list of today's restaurant specials in Syracuse"
    msg4 = "/gitguru: annoy the crap out of... I mean, politely request the help of the gitguru"
    msg5 = "/remind: set a reminder for yourself. I'll send you a message whenever you asked to be reminded."
    msg6 = "/weather: get the current weather forecast"
    msg7 = "/suggest: send suggestions for exceptionbot improvements!"
    msg8 = "For now, if you have any suggestions for exceptionbot, send them to Courtney. When I grow up, I'll be able to take my own suggestions"

    botuser.send_message(message.get_prop("channel"), msg1)
    botuser.send_message(message.get_prop("channel"), msg2)
    botuser.send_message(message.get_prop("channel"), msg3)
    botuser.send_message(message.get_prop("channel"), msg4)
    botuser.send_message(message.get_prop("channel"), msg5)
    botuser.send_message(message.get_prop("channel"), msg6)
    botuser.send_message(message.get_prop("channel"), msg7)
    botuser.send_message(message.get_prop("channel"), msg8)

def build_greeting_rules(user):
    global team
    global botuser

    botuser = user
    team = SlackTeam()

    team.populate_user_list(user)
    team.populate_team_channels(user)
    botconfig.userid = team.get_user(botconfig.username)

    # If you private message the exceptionbot, he will send you a greeting.
    greeting_rule1 = MessageRule([
        MessagePattern("type", "equals", "message"),
        MessagePattern("user", "not equal", botconfig.userid),
        MessagePattern("channel", "not in", team.team_channels),
        MessagePattern("message", "contains", "help")], greeting)

    return [greeting_rule1]
