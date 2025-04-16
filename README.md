# Recomendador de Desodorantes según pH de Piel

Este es un programa en Python que recomienda una marca de desodorante basada en el pH de la piel y si la persona tiene piel sensible. Utiliza la API de Google Generative AI (Gemini-Pro) para generar la recomendación.

## Cómo funciona

1. El usuario ingresa su pH (valor entre 0 y 14).
2. Indica si tiene piel sensible o no.
3. La aplicación envía esta información a la API de Google junto con un prompt predefinido.
4. Se recibe una recomendación de marca de desodorante y una breve justificación.
5. Se muestra la respuesta en pantalla.

## Requisitos

- Python 3.8 o superior
- Cuenta de Google Cloud con acceso a la API de Generative AI (Gemini-Pro)
- Dependencias indicadas en `requirements.txt`

## Instalación

1. Clona este repositorio.
2. Instala las dependencias con:
   ```
   pip install -r requirements.txt
   ```
3. Coloca tu API Key en la variable `GOOGLE_API_KEY` dentro del archivo `recomendador.py`.

## Uso

Ejecuta el script con:
```
python recomendador.py
```
Sigue las instrucciones en pantalla.

## Archivos del proyecto

- `recomendador.py` — Código fuente principal.
- `requirements.txt` — Dependencias del proyecto.
- `README.md` — Instrucciones de uso.
- `.gitignore` — Para excluir archivos innecesarios.

## Nota

La clave API se incluye directamente en el script solo con fines de prueba. En producción se recomienda usar variables de entorno.
