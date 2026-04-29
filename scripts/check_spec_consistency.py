#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def fail(message: str) -> None:
    ERRORS.append(message)


def expect_contains(rel_path: str, needle: str) -> None:
    text = read(rel_path)
    if needle not in text:
        fail(f"{rel_path}: missing expected text: {needle!r}")


def expect_contains_any(rel_path: str, *needles: str) -> None:
    """Pass if ANY of the given strings is present (supports bilingual docs)."""
    text = read(rel_path)
    if not any(n in text for n in needles):
        fail(f"{rel_path}: missing any of: {needles!r}")


def expect_absent(rel_path: str, needle: str) -> None:
    text = read(rel_path)
    if needle in text:
        fail(f"{rel_path}: forbidden text still present: {needle!r}")


def extract_section(text: str, start: str, end: str) -> str:
    start_idx = text.find(start)
    if start_idx == -1:
        fail(f"missing section start: {start!r}")
        return ""
    end_idx = text.find(end, start_idx + len(start))
    if end_idx == -1:
        fail(f"missing section end after {start!r}: {end!r}")
        return text[start_idx:]
    return text[start_idx:end_idx]


def check_relative_markdown_links(rel_path: str) -> None:
    text = read(rel_path)
    doc_path = ROOT / rel_path
    for raw_target in MARKDOWN_LINK_RE.findall(text):
        if raw_target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = raw_target.split("#", 1)[0]
        if not target:
            continue
        resolved = (doc_path.parent / target).resolve()
        if not resolved.exists():
            fail(f"{rel_path}: broken relative markdown link {raw_target!r}")


def check_mode_registry() -> None:
    rel_path = "MODE_REGISTRY.md"
    text = read(rel_path)
    expect_contains(rel_path, "Last updated: v3.6.5 (2026-04-27)")
    for heading in (
        "## deep-research (7 modes)",
        "## academic-paper (10 modes)",
        "## academic-paper-reviewer (6 modes)",
    ):
        if heading not in text:
            fail(f"{rel_path}: missing mode heading {heading!r}")


def check_claude_md() -> None:
    rel_path = ".claude/CLAUDE.md"
    expect_contains_any(rel_path, "integrity check (Stage 2.5)", "verificación de integridad (Etapa 2.5)")
    expect_contains_any(rel_path, "final integrity check (Stage 4.5)", "verificación de integridad final (Etapa 4.5)")
    expect_contains(rel_path, "**Suite version**: 3.6.5")
    for forbidden in (
        "6th independent reviewer",
        "Peer review gains 6th independent reviewer",
    ):
        expect_absent(rel_path, forbidden)


def check_reviewer_version_block() -> None:
    rel_path = "academic-paper-reviewer/SKILL.md"
    text = read(rel_path)
    frontmatter_match = re.search(
        r'metadata:\s*[\s\S]*?\n\s+version:\s"([^"]+)"\n\s+last_updated:\s"([^"]+)"',
        text,
    )
    if not frontmatter_match:
        fail(f"{rel_path}: could not parse frontmatter version/last_updated")
        return
    version, last_updated = frontmatter_match.groups()

    version_block_match = re.search(r"\| Skill Version \| ([^|]+) \|", text)
    updated_block_match = re.search(r"\| Last Updated \| ([^|]+) \|", text)
    if not version_block_match or not updated_block_match:
        fail(f"{rel_path}: missing Version Info table rows")
        return

    version_block = version_block_match.group(1).strip()
    updated_block = updated_block_match.group(1).strip()

    if version != version_block:
        fail(
            f"{rel_path}: frontmatter version {version!r} does not match Version Info block {version_block!r}"
        )
    if last_updated != updated_block:
        fail(
            f"{rel_path}: frontmatter last_updated {last_updated!r} does not match Version Info block {updated_block!r}"
        )


def check_pipeline_docs() -> None:
    for rel_path in (
        "academic-pipeline/SKILL.md",
        "academic-pipeline/agents/pipeline_orchestrator_agent.md",
    ):
        expect_absent(rel_path, "auto-continue in 5 seconds")
        expect_contains_any(
            rel_path,
            "One-line status + explicit continue/pause prompt",
            "Estado en una línea + confirmación explícita de continuar/pausar",
        )

    expect_contains_any(
        "academic-pipeline/agents/pipeline_orchestrator_agent.md",
        "Stage 2.5 can NEVER be skipped",
        "La Etapa 2.5 NUNCA puede omitirse",
    )
    expect_contains_any(
        "academic-pipeline/agents/pipeline_orchestrator_agent.md",
        "Stage 4.5 can NEVER be skipped",
        "La Etapa 4.5 NUNCA puede omitirse",
    )


def check_readme_sections() -> None:
    rel_path = "README.md"
    text = read(rel_path)

    expect_contains(rel_path, "version-v3.6.5-blue")
    expect_contains(rel_path, "releases/tag/v3.6.5")
    expect_contains(rel_path, "### v3.6.5 (2026-04-27)")
    expect_contains(rel_path, "### v3.6.4 (2026-04-25)")
    expect_contains(rel_path, "### v3.6.3 (2026-04-23)")
    expect_contains(rel_path, "### v3.6.2 (2026-04-23)")
    expect_contains(rel_path, "### v3.5.1 (2026-04-22)")
    expect_contains(rel_path, "### v3.5.0 (2026-04-21)")
    expect_contains(rel_path, "### v3.4.0 (2026-04-20)")
    expect_contains(rel_path, "### v3.3.6 (2026-04-15)")
    expect_contains(rel_path, "### v3.3.5 (2026-04-15)")
    expect_contains(rel_path, "### v3.3.4 (2026-04-15)")
    expect_contains(rel_path, "### v3.3.3 (2026-04-15)")
    expect_contains(rel_path, "### v3.3.2 (2026-04-15)")
    # Headings: accept English or Spanish equivalents
    HEADING_PAIRS = [
        ("#### Deep Research (7 modes)", "#### Investigación Profunda (7 modos)"),
        ("#### Academic Paper (10 modes)", "#### Artículo Académico (10 modos)"),
        ("#### Academic Paper Reviewer (6 modes)", "#### Revisor de Artículo Académico (6 modos)"),
        ("### Deep Research (v2.8)", "### Investigación Profunda (v2.8)"),
        ("### Academic Paper (v3.0)", "### Artículo Académico (v3.0)"),
        ("### Academic Paper Reviewer (v1.8)", "### Revisor de Artículo Académico (v1.8)"),
        ("### Academic Pipeline (v3.6)", "### Pipeline Académico (v3.6)"),
    ]
    for en, es in HEADING_PAIRS:
        if en not in text and es not in text:
            fail(f"{rel_path}: missing heading {en!r} (or Spanish equivalent {es!r})")

    # Detect language to pick correct section markers
    if "#### Academic Paper (10 modes)" in text:
        paper_start = "#### Academic Paper (10 modes)"
        paper_end = "#### Academic Paper Reviewer (6 modes)"
        deep_start = "#### Deep Research (7 modes)"
        deep_end = "#### Academic Paper (10 modes)"
        reviewer_start = "#### Academic Paper Reviewer (6 modes)"
        reviewer_end = "#### Academic Pipeline (Orchestrator)"
    else:
        paper_start = "#### Artículo Académico (10 modos)"
        paper_end = "#### Revisor de Artículo Académico (6 modos)"
        deep_start = "#### Investigación Profunda (7 modos)"
        deep_end = "#### Artículo Académico (10 modos)"
        reviewer_start = "#### Revisor de Artículo Académico (6 modos)"
        reviewer_end = "#### Pipeline Académico (Orquestador)"

    paper_usage = extract_section(text, paper_start, paper_end)
    for expected_en, expected_es in [
        ("outline-only mode", "modo solo-esquema"),
        ("abstract-only mode", "modo solo-resumen"),
        ("disclosure mode", "modo declaración"),
    ]:
        if expected_en not in paper_usage and expected_es not in paper_usage:
            fail(f"{rel_path}: Academic Paper usage section missing {expected_en!r} (or Spanish equivalent)")
    for forbidden in ("bilingual-abstract mode", "writing-polish mode", "full-auto mode"):
        if forbidden in paper_usage:
            fail(f"{rel_path}: Academic Paper usage section still contains {forbidden!r}")

    deep_usage = extract_section(text, deep_start, deep_end)
    if "review mode" not in deep_usage and "modo revisión" not in deep_usage:
        fail(f"{rel_path}: Deep Research usage section missing 'review mode'")
    if "paper-review" in deep_usage:
        fail(f"{rel_path}: Deep Research usage section still contains 'paper-review'")

    reviewer_usage = extract_section(text, reviewer_start, reviewer_end)
    if "calibration mode" not in reviewer_usage and "modo calibración" not in reviewer_usage:
        fail(f"{rel_path}: reviewer usage section missing 'calibration mode'")

    for forbidden in (
        "6th independent reviewer",
        "Peer review gains 6th independent reviewer",
    ):
        expect_absent(rel_path, forbidden)
    # DOCX contract lines moved to docs/SETUP.md in v3.3.6; checked there instead.
    expect_contains_any(rel_path, "DOCX (via Pandoc when available)", "DOCX (vía Pandoc cuando esté disponible)")
    check_relative_markdown_links(rel_path)




def check_setup_docs() -> None:
    expect_contains_any(
        "docs/SETUP.md",
        "Direct `.docx` generation uses [Pandoc]",
        "La generación directa de `.docx` usa [Pandoc]",
    )
    expect_contains_any(
        "docs/SETUP.md",
        "Direct `.docx` generation requires Pandoc, and PDF generation requires `tectonic`",
        "La generación directa de `.docx` requiere Pandoc, y la generación de PDF requiere `tectonic`",
    )
    check_relative_markdown_links("docs/SETUP.md")


def check_docx_contract() -> None:
    expect_contains_any(
        "academic-paper/SKILL.md",
        "LaTeX/DOCX-via-Pandoc/PDF output",
        "salida LaTeX/DOCX-vía-Pandoc/PDF",
    )
    expect_contains_any(
        "academic-paper/agents/formatter_agent.md",
        "If Pandoc is available, generate the `.docx` file directly",
        "Si Pandoc está disponible, genera el archivo `.docx` directamente",
    )
    expect_contains_any(
        "academic-paper/agents/formatter_agent.md",
        "If Pandoc is unavailable, provide complete markdown + DOCX conversion instructions",
        "Si Pandoc no está disponible, proporciona instrucciones completas de conversión a DOCX",
    )
    expect_contains_any(
        "academic-pipeline/SKILL.md",
        "DOCX via Pandoc when available, otherwise conversion instructions",
        "DOCX vía Pandoc cuando esté disponible, de lo contrario instrucciones de conversión",
    )
    expect_contains_any(
        "academic-pipeline/agents/pipeline_orchestrator_agent.md",
        "DOCX via Pandoc when available (otherwise instructions)",
        "DOCX vía Pandoc cuando esté disponible (de lo contrario instrucciones)",
    )
    for rel_path in (
        "academic-pipeline/SKILL.md",
        "academic-pipeline/agents/pipeline_orchestrator_agent.md",
    ):
        expect_absent(rel_path, "Auto-produce MD + DOCX")


def check_reference_docs() -> None:
    expect_contains_any(
        "academic-pipeline/references/passport_as_reset_boundary.md",
        "# Passport as Reset Boundary (v3.6.3)",
        "# Passport como Límite de Reinicio (v3.6.3)",
    )
    expect_contains_any(
        "academic-pipeline/references/passport_as_reset_boundary.md",
        "## `resume_from_passport` mode contract",
        "## Contrato del modo `resume_from_passport`",
    )
    expect_contains_any(
        "academic-pipeline/references/passport_as_reset_boundary.md",
        "## Iron rules",
        "## Reglas de Hierro",
    )
    # Unified PASSPORT-RESET tag format across protocol doc + orchestrator emission + checkpoint template.
    # Divergence here breaks cross-session machine-stable handoff.
    tag_format = "[PASSPORT-RESET: hash=<hash>, stage=<completed>, next=<next>]"
    expect_contains(
        "academic-pipeline/references/passport_as_reset_boundary.md",
        tag_format,
    )
    expect_contains(
        "academic-pipeline/agents/pipeline_orchestrator_agent.md",
        tag_format,
    )


def main() -> int:
    check_mode_registry()
    check_claude_md()
    check_reviewer_version_block()
    check_pipeline_docs()
    check_readme_sections()
    check_setup_docs()
    check_docx_contract()
    check_reference_docs()

    if ERRORS:
        print("Spec consistency check failed:")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("Spec consistency check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
