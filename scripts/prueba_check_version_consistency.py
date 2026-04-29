"""Unit tests for check_version_consistency.py."""
from __future__ import annotations

import subprocess
import textwrap
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts._test_helpers import run_script

SCRIPT = Path(__file__).resolve().parent / "check_version_consistency.py"


def _run(root: Path) -> subprocess.CompletedProcess:
    return run_script(SCRIPT, "--path", str(root))


def _write_skill(root: Path, name: str, version: str) -> None:
    skill_dir = root / name
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "HABILIDAD.md").write_text(
        textwrap.dedent(
            f"""\
            ---
            name: {name}
            description: "fixture"
            metadata:
              version: "{version}"
              last_updated: "2026-04-22"
              status: active
              data_access_level: raw
              task_type: open-ended
            ---

            # {name}
            """
        ),
        encoding="utf-8",
    )


def _write_claude_md(
    root: Path,
    suite_version: str,
    table_rows: list[tuple[str, str]],
) -> None:
    claude_dir = root / ".claude"
    claude_dir.mkdir(parents=True, exist_ok=True)
    rows = "\n".join(
        f"| `{name}` v{ver} | purpose | modes |" for name, ver in table_rows
    )
    text = (
        "# Academic Research Skills\n"
        "\n"
        "## Descripción General de Habilidades\n"
        "\n"
        "| Skill | Purpose | Key Modes |\n"
        "|-------|---------|-----------|\n"
        f"{rows}\n"
        "\n"
        "## Version Info\n"
        f"- **Versión de la suite**: {suite_version} (per HISTORIAL_DE_CAMBIOS.md)\n"
    )
    (claude_dir / "CLAUDE.md").write_text(text, encoding="utf-8")


def _write_changelog(root: Path, latest_version: str) -> None:
    (root / "HISTORIAL_DE_CAMBIOS.md").write_text(
        textwrap.dedent(
            f"""\
            # Changelog

            ## [{latest_version}] - 2026-04-22

            ### Added
            - fixture entry
            """
        ),
        encoding="utf-8",
    )


def _write_aligned_fixture(root: Path) -> None:
    """Everything lines up — baseline for PASS cases and drift mutations."""
    skills = [
        ("investigacion-profunda", "2.9.0"),
        ("articulo-academico", "3.1.0"),
        ("articulo-academico-reviewer", "1.8.1"),
        ("pipeline-academico", "3.5.0"),
    ]
    for name, ver in skills:
        _write_skill(root, name, ver)
    _write_claude_md(root, suite_version="3.5.0", table_rows=skills)
    _write_changelog(root, latest_version="3.5.0")


def _write_aligned_fixture_v351(root: Path) -> None:
    """v3.5.1 suite: investigacion-profunda 2.9.1, pipeline-academico 3.5.1."""
    skills = [
        ("investigacion-profunda", "2.9.1"),
        ("articulo-academico", "3.1.0"),
        ("articulo-academico-reviewer", "1.8.1"),
        ("pipeline-academico", "3.5.1"),
    ]
    for name, ver in skills:
        _write_skill(root, name, ver)
    _write_claude_md(root, suite_version="3.5.1", table_rows=skills)
    _write_changelog(root, latest_version="3.5.1")


class TestVersionConsistency(unittest.TestCase):
    def test_all_aligned_passes(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_aligned_fixture(root)
            result = _run(root)
            self.assertEqual(
                result.returncode, 0,
                msg=f"stdout={result.stdout!r} stderr={result.stderr!r}",
            )

    def test_all_aligned_v351_passes(self) -> None:
        """v3.5.1 suite (investigacion-profunda 2.9.1, pipeline-academico 3.5.1) must pass."""
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_aligned_fixture_v351(root)
            result = _run(root)
            self.assertEqual(
                result.returncode, 0,
                msg=f"stdout={result.stdout!r} stderr={result.stderr!r}",
            )

    def test_table_version_drift_fails(self) -> None:
        """Table lists investigacion-profunda v2.9.0 but HABILIDAD.md says 2.8.0 — must fail."""
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_aligned_fixture(root)
            _write_skill(root, "investigacion-profunda", "2.8.0")
            result = _run(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("investigacion-profunda", result.stdout)
            self.assertIn("2.9.0", result.stdout)
            self.assertIn("2.8.0", result.stdout)

    def test_suite_version_vs_changelog_drift_fails(self) -> None:
        """CLAUDE.md suite version != CHANGELOG latest entry — must fail."""
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_aligned_fixture(root)
            _write_changelog(root, latest_version="3.4.0")
            result = _run(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("3.5.0", result.stdout)
            self.assertIn("3.4.0", result.stdout)
            self.assertIn("CHANGELOG", result.stdout)

    def test_pipeline_version_vs_suite_drift_fails(self) -> None:
        """pipeline-academico version in table must equal suite version."""
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_aligned_fixture(root)
            # Drop pipeline to 3.4.0 in both table and HABILIDAD.md, keep suite at 3.5.0.
            # This isolates invariant 3 (pipeline tracks suite) from invariant 1
            # (HABILIDAD.md == table).
            _write_skill(root, "pipeline-academico", "3.4.0")
            _write_claude_md(
                root,
                suite_version="3.5.0",
                table_rows=[
                    ("investigacion-profunda", "2.9.0"),
                    ("articulo-academico", "3.1.0"),
                    ("articulo-academico-reviewer", "1.8.1"),
                    ("pipeline-academico", "3.4.0"),
                ],
            )
            result = _run(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("pipeline-academico", result.stdout)

    def test_skill_missing_frontmatter_fails(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_aligned_fixture(root)
            (root / "investigacion-profunda" / "HABILIDAD.md").write_text(
                "# investigacion-profunda\n\nNo frontmatter here.\n",
                encoding="utf-8",
            )
            result = _run(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("investigacion-profunda", result.stdout)

    def test_skill_listed_in_table_but_missing_on_disk_fails(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_aligned_fixture(root)
            import shutil
            shutil.rmtree(root / "articulo-academico-reviewer")
            result = _run(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("articulo-academico-reviewer", result.stdout)

    def test_missing_suite_version_in_claude_md_fails(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_aligned_fixture(root)
            (root / ".claude" / "CLAUDE.md").write_text(
                textwrap.dedent(
                    """\
                    # Academic Research Skills

                    ## Descripción General de Habilidades

                    | Skill | Purpose | Key Modes |
                    |-------|---------|-----------|
                    | `investigacion-profunda` v2.9.0 | x | y |
                    | `articulo-academico` v3.1.0 | x | y |
                    | `articulo-academico-reviewer` v1.8.1 | x | y |
                    | `pipeline-academico` v3.5.0 | x | y |

                    ## Version Info
                    - No suite version line here.
                    """
                ),
                encoding="utf-8",
            )
            result = _run(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("Versión de la suite", result.stdout)


if __name__ == "__main__":
    unittest.main()
