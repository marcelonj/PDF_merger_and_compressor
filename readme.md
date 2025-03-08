# Mezclador y compresor de pdfs
## Descripción
El proyecto busca resolver el problema de unir varios pdfs de una sola página y luego comprimir el resultado.
El script funciona combinando los pdfs dentro de la carpeta PDFs, devolviendo dos pdfs: uno sin comprimir y uno comprimido.
## Instrucciones
1. Cree un entorno virtual con python.

```
python -m venv venv
```
>[!NOTE]
>Esto solo se debe hacer solo una vez, para usos posteriores se debe pasar directamente al paso 2

2. Active el entorno virtual.

```
venv/Scripts/activate
```
>[!NOTE]
>Los pasos 3 y 4 también solo se deben ejecutar solo la primera vez que se vaya a usar el script.
3. Instale las librerias necesarias.

```
pip install -r requirements.txt
```

4. Cree una carpeta llamada "PDFs".

```
mkdir PDFs
```

5. Agregue los pdfs que desea combinar en la carpeta "PDFs".
6. Ejecute el script.

```
python pdf.py
```
