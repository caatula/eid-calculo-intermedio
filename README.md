# Evaluación Integrada de Desempeño (EID) - Cálculo Intermedio

## 1. Información del Proyecto
* **Curso:** Cálculo Intermedio MAT1188
* **Grupo:** 11
* **Integrantes y Cuentas de GitHub:**
  * Cristian Sáez - [@csaez69](https://github.com/csaez69)
  * Mathias Figueroa - [@MathiasF19](https://github.com/MathiasF19)
  * Catalina Durán - [@caatula](https://github.com/caatula)
  * Jaime Levil - [@jlevil2025-del](https://github.com/jlevil2025-del)
* **Tema:** Eje 2 - El papel del punto muestra: Punto medio y punto interior.
* **Pregunta Central:** *¿Por qué el punto muestra no tiene que ser necesariamente un extremo ni el punto medio?.

---

## 2. Requisitos y Dependencias

Para que el código ejecute correctamente y genere las escenas, se requieren dependencias tanto de Python como del sistema operativo.

### Entorno de Python
* **Python:** Versión 3.10 o superior.
* **Manim Community:** Versión 0.22.0.

Instalación de la librería de animación:
```bash
pip install -r requirements.txt
```
## 3. Escenas e Instrucciones de Ejecución

El proyecto consta de una única escena consolidada que incluye los 4 bloques del guion, llamada PuntoMuestraFinal.

Pasos para renderizar el video:
Clonar el repositorio y acceder a la carpeta del proyecto.

Crear y activar un entorno virtual:
```Bash
python3 -m venv env
source env/bin/activate
Instalar las dependencias de Python:
```

``` Bash
pip install -r requirements.txt
Renderizar la escena principal en Alta Definición (1080p a 60 fps):
```


```Bash
manim -pqh main.py PuntoMuestraFinal
```
_Nota_: _Si tu sistema tiene problemas con dvisvgm, puedes forzar el motor XeLaTeX añadiendo --compiler xelatex al final del comando._

El video renderizado sin voces se alojará en media/videos/main/1080p60/PuntoMuestraFinal.mp4. Las voces de los integrantes se inyectan posteriormente en postproducción utilizando Kdenlive.

## 4. Referencias Matemáticas

1. Apunte del curso: _Introducción a la integral_, MAT1188 (2026).

2. Stewart, J. (2012). _Cálculo de una variable: Trascendentes tempranas_ (7.a ed.). Cengage Learning.

3. Thomas, G. B., Weir, M. & Hass, J. (2010). _Cálculo: Una variable_ (12.a ed.). Pearson.