# Mezclador y compresor de pdfs
## Descripción
El proyecto busca resolver el problema de unir varios pdfs de una sola página y luego comprimir el resultado.
El script funciona combinando los pdfs dentro de la carpeta PDFs, devolviendo dos pdfs: uno sin comprimir y uno comprimido.
## Instrucciones

1. Cree un entorno virtual con python.

```
python -m venv venv
```

2. Active el entorno virtual.

```
venv/Scripts/activate
```

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