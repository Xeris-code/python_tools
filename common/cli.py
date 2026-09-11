import argparse
from typing import List

class CliArg():
    def __init__(self, key: str, help: str, required: bool = False, shortcut: str = None):
        self.key = key
        self.help = help
        self.required = required
        self.shortcut = shortcut

    def get_kwargs(self) -> dict:

        return {'help': self.help, 'required': self.required}

class DefaultArg(CliArg):
    def __init__(self, key: str, help: str, value: str, required: bool = False, shortcut: str = None):
        super().__init__(key, help, required=required, shortcut=shortcut)
        self.value = value

    def get_kwargs(self) -> dict:
        kwargs = super().get_kwargs()
        kwargs['default'] = self.value

        return kwargs

class StringArg(CliArg):
    def get_kwargs(self) -> dict:
        kwargs = super().get_kwargs()
        kwargs['type'] = str

        return kwargs

class BoolArg(CliArg):
    def get_kwargs(self) -> dict:
        kwargs = super().get_kwargs()
        kwargs['action'] = "store_true"

        return kwargs

class Cli():
    def __init__(self, description: str, args: List[CliArg] = None):
        self.parser = argparse.ArgumentParser(description = description, formatter_class=argparse.RawDescriptionHelpFormatter)
        for arg in args:
            self.add_arg(arg)
        self.args = self.parser.parse_args()

    def add_arg(self, arg: CliArg):

        keys = [f'-{arg.shortcut}', f'-{arg.key}'] if arg.shortcut else [f'-{arg.key}']

        self.parser.add_argument(*keys, **arg.get_kwargs())


script_arguments_list = {
    'compare': {
        'description': """Compare two excel files [file1 and file2] defined by script arguments.\nStored to './results' folder by default.""",
        'args': [
            StringArg("file1", "Compared file [file1].", required=True, shortcut="f1"),
            StringArg("file2", "Compared file [file2].", required=True, shortcut="f2"),
            DefaultArg("result", "Folder for report storage.", value="results", required=False, shortcut="r"),
            StringArg("sheet", "Specific excel sheet to be compared.", required=False, shortcut="st")
        ]
    }
}