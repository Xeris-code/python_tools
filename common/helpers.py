from pathlib import Path
from openpyxl import load_workbook

from typing import List

def list_excels(data_dir: Path):
    return sorted(
        p for p in data_dir.iterdir()
        if p.is_file() and p.suffix in (".xlsx", ".xlsm")
    )

#wb = load_workbook("", data_only=True)
#wb.save("name")


def make_path(*paths):
    list = [p for p in paths]
    return Path(*list)