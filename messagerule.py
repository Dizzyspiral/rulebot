class MessageRule:
    def __init__(self, patterns, action):
        self.patterns = patterns
        self.action = action

    def matches(self, message):
        for pattern in self.patterns:
            if not pattern.matches(message):
                return False

        return True
