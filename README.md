# Reconocimiento de Placas con I.A.

## Descripcion

Captura la imagen de la camara y manda a EasyOCR a detectar el texto en la imagen 

## Pre-Requisitos

- [Python 3](https://www.python.org/downloads/)
- [Virtual Env de Python](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- [Git](https://git-scm.com/)

## Pasos de Instalacion

1. Clonar El Repositorio
```bash
git clone https://github.com/pxnditxyr/text-recognition-easyocr
```
2. Creacion del Entorno Virtual

En Windows

```bash
python -m venv env
```

En linux

```bash
python3 -m venv env
```

3. Activar el entorno virtual

En Windows

```bash
.\env\Scripts\activate
```

En Linux

```bash
./env/bin/activate
```

4. Instalacion de Librerias

```bash
pip install -r requirements.txt
```

5. Modificacion de la libreria

Ingrese al archivo dentro de `env/lib/python3.11/site-packages/easyocr/utils.py` y en las siguientes lineas modifique

```python
if ratio<1.0: 
     ratio = calculate_ratio(width,height) 
     img = cv2.resize(img,(model_height,int(model_height*ratio)), interpolation=Image.ANTIALIAS) 
 else: 
     img = cv2.resize(img,(int(model_height*ratio),model_height),interpolation=Image.ANTIALIAS) 
 return img,ratio 
```

Por:

```python
if ratio<1.0: 
     ratio = calculate_ratio(width,height) 
     img = cv2.resize(img,(model_height,int(model_height*ratio)), interpolation=Image.LANCZOS) 
 else: 
     img = cv2.resize(img,(int(model_height*ratio),model_height),interpolation=Image.LANCZOS) 
 return img,ratio 
```

## Pruebas

1. Correr el main

```bash
python main.py
```
