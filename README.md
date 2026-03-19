# - API de Frases Motivadoras - ✏️ 

Una API sencilla construida con FastAPI que devuelve frases motivadoras.
Proyecto de aprendizaje para practicar el desarrollo de APIs en Python.

## Tecnologías usadas

- Python
- FastAPI
- Uvicorn

## Requisitos

- Python 3.8 o superior
- pip

## Instalación

1. Clona el repositorio
git clone https://github.com/tuusuario/frases-api.git

2. Crea el entorno virtual
python -m venv venv

3. Actívalo
venv\Scripts\activate

4. Instala las dependencias
pip install -r requirements.txt

5. Crea tu archivo .env basándote en .env.example
cp .env.example .env

## Ejecución

uvicorn main:app --reload

Abre en el navegador: http://localhost:8000/docs

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /frases | Ver todas las frases |
| GET | /frases/aleatoria | Obtener una frase aleatoria |
| POST | /frases | Añadir una frase nueva |
| DELETE | /frases/{id} | Eliminar una frase |

## Autora

Lily — proyecto de aprendizaje personal
