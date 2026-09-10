from typing import List
from common.cli import Cli, CliArg

class ScriptBase():
    def __init__(self, description: List[str], args: List[CliArg]):
        self.cli = Cli(description=description, args=args)

