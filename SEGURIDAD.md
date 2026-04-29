# Política de Seguridad

## Versiones soportadas

Solo la última versión en la rama `main` recibe correcciones de seguridad.

| Versión | Soportada |
|---------|-----------|
| Última (`main`) | Sí |
| Versiones anteriores | No |

## Reportar una vulnerabilidad

Si encuentras un problema de seguridad (ej. inyección de prompts, exposición de credenciales, filtración no intencionada de datos a través de llamadas a la API), **no abras un problema público**.

En su lugar, utiliza el **reporte privado de vulnerabilidades** de GitHub:

1. Ve a la página de [Security Advisories](https://github.com/Imbad0202/academic-research-skills/security/advisories).
2. Haz clic en **"Report a vulnerability"**.
3. Rellena los detalles — lo que encontraste, cómo reproducirlo y el impacto potencial.

Recibirás una respuesta en un plazo de 7 días. Si se acepta el reporte, se emitirá una corrección y se dará crédito en las notas de la versión. Si se rechaza, recibirás una explicación.

## Alcance

Los siguientes están dentro del alcance para los reportes de seguridad:

- **Inyección de prompts** — entradas que causan que los agentes omitan las restricciones de la REGLA DE HIERRO, las compuertas de integridad o los protocolos éticos.
- **Filtración de credenciales** — configuraciones o comportamientos de los agentes que exponen claves API (`ARS_CROSS_MODEL`, clave API de Semantic Scholar, etc.).
- **Filtración de datos** — comportamientos de los agentes que envían datos de investigación del usuario a servicios externos no deseados.
- **Omisión de compuertas de integridad** — entradas que saltan las verificaciones de bloqueo de la Etapa 2.5 o la Etapa 4.5.

Los siguientes están **fuera de alcance**:

- Problemas de calidad de la salida de la IA (alucinaciones, argumentos débiles) — estos son limitaciones de la investigación, no vulnerabilidades de seguridad.
- Solicitudes de características o errores generales — utiliza [Issues](https://github.com/Imbad0202/academic-research-skills/issues) en su lugar.
