"""Git clean-фильтр: убирает результаты ячеек из .ipynb перед коммитом.

Читает ноутбук из stdin, пишет очищенный в stdout. Рабочая копия не меняется.
Подключение (один раз после клонирования):
    git config filter.nbstrip.clean "python tools/nbstrip.py"
"""
import json
import sys

nb = json.loads(sys.stdin.buffer.read().decode("utf-8"))
for cell in nb.get("cells", []):
    if cell.get("cell_type") == "code":
        cell["outputs"] = []
        cell["execution_count"] = None
    cell.get("metadata", {}).pop("execution", None)

out = json.dumps(nb, ensure_ascii=False, indent=1) + "\n"
sys.stdout.buffer.write(out.encode("utf-8"))
