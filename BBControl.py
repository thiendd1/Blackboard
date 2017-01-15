from BlackBoard import BlackBoard
from ActionAgent import ActionAgent
from CameraAgent import CameraAgent
import schedule
import time
from threading import Thread


class BlackBoardControl:
    black_board = None
    knowledge_sources = [];
    camera_agents = [];

    def __init__(self, black_board):
        """Init Controller for blackboard"""
        self.black_board = black_board
        self.knowledge_sources.append(ActionAgent(black_board))
        self.invoke_camera_agent()

        schedule.every(4).seconds.do(self.invoke_knowledge_source)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def invoke_knowledge_source(self):
        # """Invoke agents"""
        for agent in self.knowledge_sources:
            agent.execute_action()

    def invoke_camera_agent(self):
        """Invoke Camera agents"""

        camera1 = CameraAgent()
        self.camera_agents.append(camera1)
        camera2 = CameraAgent()
        self.camera_agents.append(camera2)
        camera3 = CameraAgent()
        self.camera_agents.append(camera3)

        count = 1
        t1 = None
        for agent in self.camera_agents:
            t1 = Thread(target=agent.execute_action, args=(count,))
            t1.start()
            count += 1


if __name__ == '__main__':
    blackboard = BlackBoard()
    control = BlackBoardControl(blackboard)
