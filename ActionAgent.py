from KnowledgeSourceBase import KnowledgeSourceBase


class ActionAgent (KnowledgeSourceBase):

    def is_enable(self):
        pass

    def configure(self, blackboard):
        pass

    def execute_action(self):
        print self.blackboard.name
        self.send_email()

    def send_email(self):
        print "Send email to PIC ! \n"
