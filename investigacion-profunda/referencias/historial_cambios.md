## [2.9.1] - 2026-04-22

### Added

- **Opt-in reading-check probe** in Mentor Socrático. Gated by `ARS_SOCRATIC_READING_PROBE=1`. See `agents/agente_mentor_socratico.md` §"Optional Reading Probe Layer" and `HABILIDAD.md` §"Opt-in Reading Probe (v3.5.1)".

### Version

- 2.9.0 → 2.9.1 (patch; opt-in, default OFF).

---

# Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.4 | 2026-03-27 | Report compiler now consumes optional Style Profile (from articulo-academico intake) and runs Writing Quality Check checklist before finalizing reports. Style Profile applied as soft guide for Executive Summary and Synthesis sections; discipline conventions take priority. Writing Quality Check catches overused AI-typical terms, em dash overuse, throat-clearing openers, and monotonous sentence rhythm. See `articulo-academico/referencias/writing_quality_verificacion.md` and `shared/style_calibration_protocolo.md` |
| 2.3 | 2026-03-08 | Added systematic-review mode (7th mode): PRISMA 2020 compliant pipeline with agente_riesgo_sesgo (RoB 2 + ROBINS-I), agente_meta_analisis (effect sizes, heterogeneity, GRADE, narrative synthesis), 2 new templates (PRISMA protocol + report), systematic_review_toolkit reference. Added agente_monitoreo (post-pipeline literature monitoring with digests, retraction alerts, author tracking) + literature_monitoring_strategies reference. Enhanced agente_mentor_socratico with 4 convergence signals, 4-type question taxonomy, and auto-end triggers. Added Quick Mode Selection Guide to HABILIDAD.md |
| 2.2 | 2026-03-05 | Added synthesis anti-patterns, Socratic quantified thresholds & auto-end conditions, reference existence verification (DOI + WebSearch), enhanced ethics reference integrity check (50% + Retraction Watch), mode transition matrix, cross-agent quality alignment definitions |
| 2.1 | 2026-03 | Added IRB decision tree, EQUATOR reporting guidelines, preregistration guide + template; enhanced ethics_review_agent with human subjects dimension; enhanced research_architect_agent with ethics/EQUATOR/preregistration integration; enhanced methodology_patterns with EQUATOR cross-references |
| 2.0 | 2026-02 | Added socratic mode (10th agent), failure paths, mode selection guide, Traspaso protocol, 2 new examples, 3 new references |
| 1.0 | 2026-02 | Initial release: 9 agents, 5 modes, 6-phase pipeline |
