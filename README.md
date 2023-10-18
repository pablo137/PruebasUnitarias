# ONECLICK
---
## Requerimientos
[![Node Version](https://img.shields.io/badge/Node-Ultimate-green)](https://nodejs.org/en/download)

[![git Version](https://img.shields.io/badge/Git-Download-red)](https://git-scm.com/downloads)

[![Visual-Code Version](https://img.shields.io/badge/Visual-Code-blue)](https://code.visualstudio.com/)

[![Visual-Code Version](https://img.shields.io/badge/Python-Lasted-white)](https://www.python.org/downloads/)



## Crear proyecto

<span style="color:chartreuse">Escojer una carpeta proyecto</span>

<span style="color:chartreuse">Apretar [Shift + click derecho] en la carpeta vacia</span>

<span style="color:chartreuse">Aparecera la opcion "Abrir la ventana de power Shell aqui" ingresar</span>

<span style="color:chartreuse">Aparecera una ventana de comando en la direccion actual de la carpeta del proyecto</span>

<span style="color:chartreuse">Poner el siguiente comando "git clone https://github.com/pablo137/AnalisisEstatico ." [copiar todo lo que esta entre comillas incluido el "."]</span>

<span style="color:chartreuse">Ahora poner el siguiente comando "CODE ." [Esto abrira el entorno de Visual Code]</span>

<span style="color:chartreuse">Dentro de Visual Code apreta "ctrl + ñ" [aparecera la terminal]</span>

<span style="color:chartreuse">En esta terminal se agregaran los comandos que a continuacion se mencionaran</span>

---
## Instalar Maquina Virtual, requerimientos y ejecucion de la aplicacion.
<span style="color:chartreuse">Una vez en el visual code en la linea de comando de la terminal poner las siguientes lineas</span>

## MAQUINA VIRTUAL

<span style="color:chartreuse">pip install virtualenv</span>

<span style="color:chartreuse">virtualenv venv</span>

<span style="color:chartreuse">venv/Scripts/Activate</span>

## REQUERIMIENTOS

<span style="color:chartreuse">pip install django</span>

<span style="color:chartreuse">pip install -r requirements.txt</span>

## EJECUTAR LA APLICACION

<span style="color:chartreuse">python manage.py makemigrations</span>

<span style="color:chartreuse">python manage.py migrate</span>

<span style="color:chartreuse">python manage.py runserver</span>

---

## EJECUTAR PYTEST
## EJECUTAR REPORTE GENERAL DE PRUEBAS
<span style="color:chartreuse">pytest -v</span>

## EJECUTAR REPORTE DE COVERAGE DE LAS PRUEBAS
<span style="color:chartreuse">pytest --cov=store/models --cov=store/views --cov-report=term-missing --cov-report=html</span>
