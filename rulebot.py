import botconfig
from slackuser import SlackUser
from messageprocessor import MessageProcessor
import greetingrules

def main():
    botuser = SlackUser(botconfig.username, botconfig.token)
    botuser.authenticate()
    botuser.connect()

    greeting_rules = greetingrules.build_greeting_rules(botuser)

    # Let each MessageProcessor load multiple rule sets? That way, we can still
    # have multiple message processors (potentially) that each start on their 
    # own threads (for example, if we want to set up multiple bots). We should
    # just never have more than one MessageProcessor that uses the same user, 
    # because I'm not sure what the behavior would be, but expect it would be
    # a race condition for the two MessageProcessors, and whichever called
    # user.get_next_message() first would dequeue the message wrt to the other
    # MessageProcessors
    rulebot_message_processor = MessageProcessor(botuser)
    rulebot_message_processor.load_rules(greeting_rules)
    rulebot_message_processor.message_loop()

if __name__ == '__main__':
    main()

