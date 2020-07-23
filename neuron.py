import bittensor as bt
from protocol import LogicSynapse, MathQueryPayload
from constants import NETUID


class Neuron():
    def __init__(self):
        self.initialize(first_run = True)

    def initialize(self, first_run=False):
        if not first_run:
            previous_block = self.metagraph.block

        self.wallet = bt.wallet(name='test', hotkey='test')
        self.subtensor = bt.subtensor(network="test")
        self.metagraph = bt.metagraph(netuid = NETUID, network="test", sync = False, lite = False)
        self.metagraph.sync(subtensor = self.subtensor)

        if not first_run and previous_block == self.metagraph.block:
            bt.logging.critical(
                "METAGRAPH HASNT CHANGED\n"
                f"Last synced block: {previous_block.item()}")
            return
        
    async def forward_request_to_subnet(self, math_query_payload: MathQueryPayload):
        targeted_subnet_validator = self.metagraph.axons[68]
        d = bt.dendrite(wallet = self.wallet)

        syn = LogicSynapse(
            logic_question = math_query_payload.content
        )
        responses = await d(
            [targeted_subnet_validator],
            syn,
            deserialize = False,
        )
        bt.logging.info(f'Responses received: {responses}\n\n')
        return responses