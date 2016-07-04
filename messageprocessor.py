import time # So we can sleep for one second between polling for messages
from slackmessage import SlackMessage

class MessageProcessor:
    def __init__(self, user):
        self.user = user

    def load_rules(self, rules):
        self.rules = rules

    def check_rules(self, message):
        for rule in self.rules:
            if rule.matches(message):
                rule.action(message)

    def message_loop(self):
        while True:
            messages = self.user.get_new_messages()

            for message in messages:
                self.check_rules(SlackMessage(message))

            time.sleep(1)

