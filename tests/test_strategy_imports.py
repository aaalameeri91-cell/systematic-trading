import ast
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
STRATEGY_FILES = [
    REPO_ROOT / "static/strategies/earnings-quality-factor.py",
    REPO_ROOT / "static/strategies/how-to-use-lexical-density-of-company-filings.py",
    REPO_ROOT / "static/strategies/value-and-momentum-factors-across-asset-classes.py",
]


def _imports_algorithmimports(path: Path) -> bool:
    module = ast.parse(path.read_text())
    return any(
        isinstance(node, ast.ImportFrom) and node.module == "AlgorithmImports"
        for node in module.body
    )


def test_quantconnect_strategies_import_algorithmimports():
    for path in STRATEGY_FILES:
        assert _imports_algorithmimports(path), f"{path.name} is missing AlgorithmImports"
