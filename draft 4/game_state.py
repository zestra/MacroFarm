class State:
    def __init__(self, states):
        self.states = states
        self.index = 0
        self.current = self.states[self.index]

    def update(self):
        self.index += 1
        if self.index == len(self.states):
            self.index = 0
        self.current = self.states[self.index]