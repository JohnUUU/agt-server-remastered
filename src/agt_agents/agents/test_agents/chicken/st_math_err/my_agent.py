from src.agt_agents.agents.base_agents.chicken_agent import ChickenAgent
from src.agt_agents.agents.local_games.chicken_arena import ChickenArena
import argparse


class MathBreaker(ChickenAgent):
    def setup(self):
        self.SWERVE, self.CONTINUE = 0, 1
        self.actions = [self.SWERVE, self.CONTINUE]

    def get_action(self):
        a = 1 / 0
        return a

    def update(self):
        return None


if __name__ == "__main__":
    #### DO NOT TOUCH THIS #####
    parser = argparse.ArgumentParser(description='My Agent')
    parser.add_argument('agent_name', type=str, help='Name of the agent')
    parser.add_argument('--run_server', action='store_true',
                        help='Connects the agent to the server')
    parser.add_argument('--ip', type=str, default='127.0.0.1',
                        help='IP address (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=8080,
                        help='Port number (default: 8080)')

    args = parser.parse_args()

    agent = MathBreaker(args.agent_name)
    if args.run_server:
        agent.connect(ip=args.ip, port=args.port)
    else:
        arena = ChickenArena(
            num_rounds=1000,
            timeout=1,
            players=[
                agent,
                MathBreaker("Agent_1"),
                MathBreaker("Agent_2"),
                MathBreaker("Agent_3"),
                MathBreaker("Agent_4")
            ]
        )
        arena.run()
