class SlackTeam:
    def __init__(self):
        self.usernames_by_id = {}
        self.userids_by_name = {}
        self.team_channels = {}

    # The user list will be popualted from the perspective of the helper_user
    # Subsequent calls to this method only grow the list with any new information
    def populate_user_list(self, helper_user):
        data = helper_user.api_call("users.list")

        # Apparently there can be a case that this does not return any members - perhaps if the API call is unsuccessful
        if "members" in data:
            for member in data["members"]:
                self.usernames_by_id[member["id"]] = member["name"]
                self.userids_by_name[member["name"]] = member["id"]

    def get_user(self, user):
        if user in self.usernames_by_id:
            return self.usernames_by_id[user]
        elif user in self.userids_by_name:
            return self.userids_by_name[user]
        else:
            return None

    # The team channels will be populated from the perspective of the helper_user
    # Subsequent calls to this method only grow the list with any new information
    def populate_team_channels(self, helper_user):
        for channel in helper_user.api_call("channels.list")["channels"]:
            self.team_channels[channel["id"]] = channel["name"]

        for channel in helper_user.api_call("groups.list")["groups"]:
            self.team_channels[channel["id"]] = channel["name"]

