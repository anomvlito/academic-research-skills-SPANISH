import os

REPLACEMENTS = {
    # Directorios base
    "academic-paper": "articulo-academico",
    "academic-paper-reviewer": "revisor-articulo-academico",
    "academic-pipeline": "pipeline-academico",
    "deep-research": "investigacion-profunda",
    
    # Subdirectorios
    "/agents/": "/agentes/",
    "/references/": "/referencias/",
    "/templates/": "/plantillas/",
    "/examples/": "/ejemplos/",
    
    # Archivos base
    "SKILL.md": "HABILIDAD.md",
    "CHANGELOG.md": "HISTORIAL_DE_CAMBIOS.md",
    "MODE_REGISTRY.md": "REGISTRO_DE_MODOS.md",
    "CONTRIBUTING.md": "CONTRIBUCIONES.md",
    "POSITIONING.md": "POSICIONAMIENTO.md",
    "QUICKSTART.md": "INICIO_RAPIDO.md",
    "SECURITY.md": "SEGURIDAD.md",
    
    # Sufijos de archivos (para enlaces)
    "_agent.md": "_agente.md",
    "_protocol.md": "_protocolo.md",
    "_guide.md": "_guia.md",
    "_template.md": "_plantilla.md",
    "_example.md": "_ejemplo.md",
    "_report.md": "_informe.md",
    "_check.md": "_verificacion.md",
    "_standards.md": "_estandares.md",

    # Agentes (identificadores y referencias)
    "pipeline_orchestrator_agent": "agente_orquestador_pipeline",
    "state_tracker_agent": "agente_seguimiento_estado",
    "integrity_verification_agent": "agente_verificacion_integridad",
    "collaboration_depth_agent": "agente_profundidad_colaboracion",
    "intake_agent": "agente_admision",
    "draft_writer_agent": "agente_redactor_borrador",
    "argument_builder_agent": "agente_constructor_argumentos",
    "structure_architect_agent": "agente_arquitecto_estructura",
    "literature_strategist_agent": "agente_estratega_literatura",
    "peer_reviewer_agent": "agente_revisor_pares",
    "citation_compliance_agent": "agente_cumplimiento_citas",
    "abstract_bilingual_agent": "agente_resumen_bilingue",
    "revision_coach_agent": "agente_entrenador_revision",
    "visualization_agent": "agente_visualizacion",
    "formatter_agent": "agente_formateador",
    "devils_advocate_reviewer_agent": "agente_revisor_abogado_diablo",
    "domain_reviewer_agent": "agente_revisor_dominio",
    "editorial_synthesizer_agent": "agente_sintetizador_editorial",
    "eic_agent": "agente_editor_jefe",
    "field_analyst_agent": "agente_analista_campo",
    "methodology_reviewer_agent": "agente_revisor_metodologia",
    "perspective_reviewer_agent": "agente_revisor_perspectiva",
    "bibliography_agent": "agente_bibliografia",
    "claim_verifier_agent": "agente_verificador_afirmaciones",
    "compliance_agent": "agente_cumplimiento",
    "cross_model_da_agent": "agente_da_modelo_cruzado",
    "da_agent": "agente_abogado_diablo",
    "intent_classifier_agent": "agente_clasificador_intenciones",
    "literature_mapper_agent": "agente_mapeador_literatura",
    "meta_analysis_agent": "agente_meta_analisis",
    "monitoring_agent": "agente_monitoreo",
    "prisma_screener_agent": "agente_cribado_prisma",
    "report_compiler_agent": "agente_compilador_informes",
    "risk_of_bias_agent": "agente_riesgo_sesgo",
    "synthesis_agent": "agente_sintesis",
    "socratic_mentor_agent": "agente_mentor_socratico",

    # Protocolos y Tags
    "[PASSPORT-RESET": "[REINICIO-PASAPORTE",
    "resume_from_passport": "resume_desde_pasaporte",
    "stage=": "etapa=",
    "next=": "siguiente=",
    
    # Modos
    "mode: socratic": "modo: socratico",
    "mode: full": "modo: completo",
    "mode: quick": "modo: rapido",
    "mode: plan": "modo: plan",

    # UI / Checkpoints
    "Metrics:": "Métricas:",
    "Deliverables:": "Entregables:",
    "Next step:": "Siguiente paso:",
    "Ready to proceed?": "¿Listo para continuar?",
}

EXTENSIONS = {".md", ".py", ".json", ".yaml", ".txt", ".tex"}
SKIP_DIRS = {".git", "__pycache__", ".local-plans", "scratch"}

def process_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        return False
    
    new_content = content
    # Ordenamos por longitud de la clave para evitar reemplazos parciales incorrectos
    sorted_keys = sorted(REPLACEMENTS.keys(), key=len, reverse=True)
    for old in sorted_keys:
        new = REPLACEMENTS[old]
        new_content = new_content.replace(old, new)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

def main():
    modified_count = 0
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for file in files:
            if any(file.endswith(ext) for ext in EXTENSIONS):
                filepath = os.path.join(root, file)
                if process_file(filepath):
                    modified_count += 1
    print(f"\nTraducción global finalizada. Archivos modificados: {modified_count}")

if __name__ == "__main__":
    main()
EOF
