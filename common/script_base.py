
from os import makedirs
from typing import List
from pathlib import Path

from common.cli import Cli, CliArg
from common.validation import Collector, validate_path

class ScriptBase():
    def __init__(self, description: List[str], args: List[CliArg]):
        self.cli = Cli(description=description, args=args)
        self.collector = Collector()
        self.cwd = Path.cwd()

    def run(self):
        pass

    def validate_input_paths(self, *inputs):
        report = validate_path(*[i for i in inputs])

        if report:
            for i in report:
                print(f'error: {i} does not exist')
            return False

        return True

    def validate_output_paths(self, *outputs):
        report = validate_path(*[o for o in outputs])
        print(report)
        if report:
            for i in report:
                user_confirmation = input(f"Output folder {i} does not exist. Do you want to create it? [y/n]")
                if user_confirmation.capitalize() == "Y":
                    print("Creating folder...")
                    makedirs(i)
                    if i.exists():
                        print(f"success: {i} created!")
                    else:
                        print(f"{i} not created succesfully. Script stopped!")
                        return False
                else:
                    print("error: script cancelled by user")
                    return False
        return True