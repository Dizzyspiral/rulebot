class MessagePattern:
    def __init__(self, prop, comparator, pattern): # It's probably not useful to keep this a tuple
        # A pattern is a tuple consisting of ("message property", "comparator", "text")
        # For example: message.get_prop("type") == "message"
        # Becomes: ("type", "equals", "message")
        # Rules are always AND'd - to get an OR, create a new ruleset with the alternate encoding
        # TODO: We need some error checking here to make sure we don't have short tuples
        self.message_prop = prop
        self.comparator = comparator
        self.pattern = pattern

    def matches(self, message):
        print("Checking pattern (" + self.tostring() + ")")

        prop = message.get_prop(self.message_prop)
        print("message[" + self.message_prop + "] = " + str(prop))

        # Should do string compare. Even better, these should be mapped somehow, so we remove the nested if's
        if self.comparator == "equals":
            if prop == self.pattern:
                return True

        elif self.comparator == "not equal":
            if prop != self.pattern:
                return True

        elif self.comparator == "contains":
            if prop.contains(self.pattern):
                return True

        elif self.comparator == "in":
            if prop in self.pattern:
                return True

        elif self.comparator == "not in":
            if prop not in self.pattern:
                return True

        elif self.comparator == "reverse in":
            if self.pattern in prop:
                return True

        else:
            print("Unrecognized comparator")

        print("Pattern did not match")
        return False

    def tostring(self):
        return str(self.message_prop) + ", " + str(self.comparator) + ", " + str(self.pattern)
