# Patrón de Reproducibilidad de Artefactos (v3.3.5+)

## Por qué existe este documento

ARS produce artefactos de investigación (borradores, revisiones, etc.). Dentro de un año, es posible que desees reproducir uno. El Pasaporte de Materiales (Esquema 9) captura QUIÉN lo produjo y CUÁNDO, pero no CON QUÉ. ¿Qué LLM? ¿Qué versión de ARS? ¿Qué archivos de habilidad?

El sub-bloque `repro_lock` llena ese vacío. Este patrón asegura que los artefactos lleven su configuración registrada — no como un mecanismo de repetición determinista, sino como un rastro de documentación honesto.

## Lo que este patrón NO ES (leer primero)

1. **Los resultados de los LLM no son reproducibles byte a byte, incluso a temperatura 0.** Los proveedores de modelos actualizan los pesos sin cambiar el ID del modelo.
2. **Las consultas a APIs externas en vivo se registran como versiones de protocolo, no como instantáneas.** Las respuestas de APIs como Semantic Scholar pueden cambiar de un día para otro.
3. **No se capturan las mutaciones de prompts a mitad de la ejecución.** Los hashes se toman cuando se carga la habilidad, no por cada llamada de agente.

Este patrón te da DOCUMENTACIÓN DE CONFIGURACIÓN suficiente para INVESTIGAR la divergencia — no para PREVENIRLA.

## El bloque de un vistazo

```yaml
repro_lock:
  schema_version: "1.0"                    # versión del esquema del bloqueo
  stochasticity_declaration: "Los resultados de los LLM no son reproducibles byte a byte. Este archivo documenta la configuración, no es una garantía de repetición determinista."
  ars_version: "3.3.5"                     # versión de la suite
  model:
    family: claude
    id: claude-opus-4-7
    weight_stable: false                    # siempre falso hasta que exista una atestación firmada
  prompts:
    hash_timing: skill-load
    skill_md_hash: "sha256:..."            # hash de HABILIDAD.md
    agents_bundle_hash: "sha256:..."       # hash del paquete de prompts de agentes
```

## Racional de los campos

### declaración_de_estocasticidad (stochasticity_declaration)
Es OBLIGATORIA. Omitirla hace que el bloqueo sea deshonesto por implicación.

### hash_de_lista_de_materiales (list_hash)
Hash de un manifiesto ordenado de los archivos de la sesión. Si el usuario edita un material entre ejecuciones, el hash cambia.

## Línea roja de honestidad

Este patrón permite la DOCUMENTACIÓN HONESTA. No permite la REPETICIÓN exacta. La configuración bloqueada te dice qué se ejecutó; no puede decirte qué se ejecutaría de nuevo exactamente igual.

Esta distinción importa: la documentación permite que un tercero investigue qué sucedió y pregunte si la divergencia es esperada o alarmante. La repetición requeriría modelos con pesos congelados, planificadores deterministas y datos externos cacheados — nada de lo cual controla ARS hoy.
