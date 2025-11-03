
# Estrategia Git (DEV, QA, PROD)

- **DEV**: integración continua diaria. Se permiten PRs desde feature/* y fix/* con revisión 1+.
- **QA**: solo merges desde DEV con etiqueta de versión (ej. v1.0.0-rc.1). Se ejecutan pruebas integrales.
- **PROD**: solo *fast-forward* desde QA con etiqueta estable (ej. v1.0.0). Protección de rama activada.

## Flujo
1. `feature/*` → PR → `DEV`
2. `DEV` → tag `vX.Y.Z-rc.N` → PR → `QA`
3. `QA` → `PROD` con `vX.Y.Z` (release)
