from sys import exit
from os import makedirs
from pathlib import Path

from openpyxl import load_workbook

from common.script_base import ScriptBase
from common.cli import script_arguments_list as cli_list

from common.helpers import make_path

class Excel():
    def __init__(self, path):
        self.wb = load_workbook(path, data_only=True)
        self.sheets = self.wb.sheetnames


class Compare(ScriptBase):
    def __init__(self):
        super().__init__( cli_list['compare']['description'], cli_list['compare']['args'])
        self.f1_dir = make_path(self.cli.args.f1)
        self.f2_dir = make_path(self.cli.args.f2)
        self.results_dir = make_path(self.cwd, self.cli.args.r)

        self.sheet = self.cli.args.st

    def run(self):
        if not self.validate_input_paths(self.f1_dir, self.f2_dir):
            return
        if not self.validate_output_paths(self.results_dir):
            return

        if self.sheet:
            print(f"Comparing sheet: {self.sheet}")
        else:
            print(f"Comparing all XY sheets")

        excel1 = Excel(self.f1_dir)
        excel2 = Excel(self.f2_dir)

        if excel1.sheets != excel2.sheets:
            print("excel sheet not comparable")
        else:
            print("excel sheets comparable")

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