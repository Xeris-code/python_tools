
import sys
from pathlib import Path

from common.script_base import ScriptBase
from common.cli import script_arguments_list as cli_list

from common.validation import validate_paths, Collector


class Compare(ScriptBase):
    def __init__(self):
        super().__init__( cli_list['compare']['description'], cli_list['compare']['args'])




def main():
    compare = Compare()
    print(compare.cli.args)

    filesCollector = Collector()
    validate_paths(Path("fofo/ghgrg.py"), Path("aefaef"), collector=filesCollector)
    print(filesCollector.collection)


if __name__ == "__main__":
    sys.exit(main())