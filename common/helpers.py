from pathlib import Path
from openpyxl import load_workbook

def list_excels(data_dir: Path):
    return sorted(
        p for p in data_dir.iterdir()
        if p.is_file() and p.suffix in (".xlsx", ".xlsm")
    )

wb = load_workbook("", data_only=True)
wb.save("name")
results = Path("current_dir", "results/")
current_dir = Path.cwd()