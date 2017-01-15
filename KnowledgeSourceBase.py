from AbKnowledgeSource import AbKnowledgeSource
from BlackBoard import BlackBoard


class KnowledgeSourceBase (AbKnowledgeSource):
    blackboard = None

    def __init__(self, blackboard):
        print "init blackboard"
        self.blackboard = blackboard

    def is_enable(self):
        return True

    def configure(self, blackboard):
        self.blackboard = blackboard
        pass

    def execute_action(self):
        pass
