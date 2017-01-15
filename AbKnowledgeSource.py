from abc import ABCMeta, abstractmethod

'''
Abstract class for KnowledgeSource
'''


class AbKnowledgeSource:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def is_enable(self):
        """This method check data is available for process"""
        pass

    def configure(self, blackboard):
        """Configuration for process data. DataSource, global variables ..."""
        pass

    def execute_action(self):
        """Implement action for data"""
        pass