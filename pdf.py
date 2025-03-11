from PyPDF2 import PdfWriter, PdfReader
from pathlib import Path
from pikepdf import Pdf
import os

#Constantes y variables
DIRECTORIO_ACTUAL = Path(__file__).resolve().parent
DIRECTORIO_PDF = DIRECTORIO_ACTUAL.joinpath('PDFs')
PDFs = os.listdir(DIRECTORIO_PDF)

#Se instancia el pdf principal
combinado = PdfWriter()

#Se agregan los pdf como páginas
for pdf in PDFs:
    pagina = PdfReader(DIRECTORIO_PDF.joinpath(pdf))
    combinado.append(pagina)

#Se guarda el pdf sin comprimir
salida = open('salida.pdf', 'wb')
combinado.write(salida)
combinado.close()
salida.close()

#Se comprime el pdf resultante y se guarda
pdf = Pdf.open('salida.pdf')
pdf.save('salida_comprimida.pdf', compress_streams=True)
pdf.close()

#Mensaje de salida
print(f'Se unieron {len(PDFs)} archivos.')