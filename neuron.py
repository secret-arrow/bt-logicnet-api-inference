import argparse
import logging
import bittensor as bt
from protocol import LogicSynapse
from constants import NETUID


class Neuron():
    def __init__(self):
        self.config = self.config()
        self.initialize(first_run = True)

    def config() -> bt.config:
        """
        Returns the configuration object.
        """
        parser = argparse.ArgumentParser(
            description = "Running the API Server for LogicNet Subnet 35..."
        )
        bt.wallet.add_args(parser)
        bt.subtensor.add_args(parser)
        bt.logging.add_args(parser)

        parser.add_argument("--auth_key", 
                            type = str, default = "",
                            help = "Auth key for authorization.")
        return bt.config(parser)

    def initialize(self, first_run=False):
        if not first_run:
            previous_block = self.metagraph.block

        self.wallet = bt.wallet(config = self.config)
        self.subtensor = bt.subtensor(config = self.config)
        self.metagraph = bt.metagraph(netuid = NETUID, sync = False, lite = False)
        self.metagraph.sync(subtensor = self.subtensor)
        self.version = self.parse_versions()

        if not first_run and previous_block == self.metagraph.block:
            logging.critical(
                "METAGRAPH HASNT CHANGED\n"
                f"Last synced block: {previous_block.item()}")
            return
        
    async def forward_request_to_subnet(self, math_query_payload):
        targeted_subnet_validator = 39
        d = bt.dendrite(wallet = self.wallet)

        syn = LogicSynapse(
            logic_question = math_query_payload.content
        )

        responses = await d(
            targeted_subnet_validator,
            syn,
            deserialize = True,
            timeout = 10)
        
        logging.info(f'Responses received: {responses}\n\n')
        result = responses[0].logic_answer
        return result


