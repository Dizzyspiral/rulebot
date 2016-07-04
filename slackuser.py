from slackclient import SlackClient

class SlackUser:
    def __init__(self, username, token):
        self.username = username
        self.userid = None # We eventually want to fill this out
        self.token = token
        if self.token:
            self.authenticate()

    # Authenticates the user with the server
    def authenticate(self):
        self.sc = SlackClient(self.token)
        self.authenticated = True

        data = self.sc.api_call("api.test")

        if data["ok"] == False:
            self.authenticated = False
            print("Unable to authenticate user " + str(self.username) + " with Slack\n")

    # Connects the user to the Real-Time Messaging (RTM) service
    def connect(self):
        self.sc.rtm_connect()
        self.connected = True

    def get_new_messages(self):
        if self.connected:
            return self.sc.rtm_read()
        else:
            print("User " + str(self.username) + " is not connected to the RTM service, and therefore cannot get messages\n")

    def send_message(self, chan, message):
        # If we're just going to directly use sc.api_call, we shouldn't even bother having a api_call class method
        resp = self.sc.api_call("chat.postMessage", as_user="true:", channel=chan, text=message)
        print("Sent message. Response: " + str(resp))

    # Can we make this accept args?
    def api_call(self, message):
        if self.authenticated:
            return self.sc.api_call(message)
        else:
            print("User " + str(self.username) + " is not authenticated, and therefore cannot make API calls\n")

