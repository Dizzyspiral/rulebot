class SlackMessage:
    def __init__(self, message):
        self.message = message

    def get_prop(self, prop):
        if prop in self.message:
            return self.message[prop]

    def is_direct_message(self, team):
        if not self.get_prop("channel") in team.team_channels:
            return True

        return False

    def is_channel_message(self, team):
        if self.get_prop("channel") in team.team_channels:
            return True

        return False

    def is_from_user(self, user):
        message_user = self.get_prop("user")
        if message_user == user.username or message_user == user.userid:
            return True

        return False
