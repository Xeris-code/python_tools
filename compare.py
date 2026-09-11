from sys import exit
from os import makedirs
from pathlib import Path

from common.script_base import ScriptBase
from common.cli import script_arguments_list as cli_list

from common.validation import validate_path, Collector
from common.helpers import make_path


class Compare(ScriptBase):
    def __init__(self):
        super().__init__( cli_list['compare']['description'], cli_list['compare']['args'])
        self.f1_dir = make_path(self.cli.args.f1)
        self.f2_dir = make_path(self.cli.args.f2)
        self.results_dir = make_path(self.cwd, self.cli.args.r)
        self.results_dir2 = make_path(self.cwd, Path("common/file"))

    def run(self):
        if not self.validate_input_paths(self.f1_dir, self.f2_dir):
            return
        if not self.validate_output_paths(self.results_dir):
            return

        print(f"Saving the report...")
        saved = True
        if saved:
            print(f"Files saved to: {self.results_dir}")
        else:
            print(f"error: report not saved correctly")
        super().run()

def main():
    compare = Compare()
    print(compare.cli.args)
    compare.run()

if __name__ == "__main__":
    exit(Compare().run())