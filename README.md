
# Comercio Agrícola (Python) — Enunciado 2

Arquitectura de referencia y *starter kit* para cumplir los entregables del **enunciado 2** (aplicación web de comercio electrónico de productos agrícolas en Guatemala). Incluye:

- **Backend** en FastAPI (Python) con endpoints de productos y pedidos, pruebas unitarias (pytest) y Dockerfile.
- **Frontend** en React (Vite) para listar productos y crear pedidos, con Dockerfile.
- **Estrategia Git y CI/CD** con ramas **DEV**, **QA**, **PROD**, `Jenkinsfile`, `sonar-project.properties` y `docker-compose` para ejecutar Jenkins y SonarQube localmente.
- **Pruebas funcionales** (colección Postman + ambientes) y **pruebas de carga** (k6 + guía para ejecutar runner de Postman).
- **Plantillas de evidencias** para pegar capturas de pantalla y un **guion de video** (≤10 min).

> Nota: Este paquete es un punto de partida operativo. Puede desplegarse con Docker en entornos aislados; parametrice variables (tokens, credenciales y rutas) según su contexto.

## Estructura
```
backend/
frontend/
ops/
  docker-compose.yml
  Jenkinsfile
  git-strategy.md
  postman/
  k6/
  soapui/
docs/
scripts/
```

## Puesta en marcha rápida (DEV)
```bash
# 1) Clonar su repositorio y copiar este contenido o descomprimir el .zip
# 2) Levantar servicios de apoyo (opcional, para análisis CI): SonarQube y Jenkins
docker compose -f ops/docker-compose.yml up -d sonardb sonarqube jenkins

# 3) Backend (desarrollo)
cd backend
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# 4) Frontend (desarrollo)
cd ../frontend
npm install
npm run dev

# 5) Postman
#   - Importar postman/Comercio-Agricola.postman_collection.json
#   - Importar postman/env/DEV.postman_environment.json
#   - Ejecutar pruebas y pegar evidencias en docs/05-plantilla-evidencias.md
```

## Licencia
MIT (ajústela según su contexto institucional).
"# comercio-agricola" 
