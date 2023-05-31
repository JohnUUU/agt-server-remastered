import argparse
import random
from src.agt_agents.agents.base_agents.bosii_agent import BOSIIAgent
from src.agt_agents.agents.local_games.bosii_arena import BOSIIArena


class RandomAgent(BOSIIAgent):
    def setup(self):
        self.COMPROMISE, self.STUBBORN = 0, 1
        self.GOOD_MOOD, self.BAD_MOOD = 0, 1
        self.actions = [self.COMPROMISE, self.STUBBORN]

    def get_action(self):
        return random.choice(self.actions)

    def update(self):
        return None


if __name__ == "__main__":
    ##### EDIT THIS #####
    ip = '192.168.1.16'
    port = 1234

    #### DO NOT TOUCH THIS #####
    parser = argparse.ArgumentParser(description='My Agent')
    parser.add_argument('agent_name', type=str, help='Name of the agent')
    parser.add_argument('--run_server', action='store_true',
                        help='Connects the agent to the server')

    args = parser.parse_args()

    agent = RandomAgent(args.agent_name)
    if args.run_server:
        agent.connect(ip=ip, port=port)
    else:
        arena = BOSIIArena(
            num_rounds=1000,
            timeout=1,
            players=[
                agent,
                RandomAgent("Agent_1"),
                RandomAgent("Agent_2"),
                RandomAgent("Agent_3"),
                RandomAgent("Agent_4")
            ]
        )
        arena.run()