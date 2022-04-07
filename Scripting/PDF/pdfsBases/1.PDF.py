import PyPDF2 as pdf

archivo = 'Scripting/PDF/pdfsBases/pdfUnido_1.pdf'

with open(archivo, 'rb') as miArchivo:
    print(miArchivo)
    print(type(miArchivo))

    # pasar esta informacion binaria
    # a un formato operable para pdf
    archivoPdf = pdf.PdfFileReader(miArchivo)
    print(archivoPdf)
    print(type(archivoPdf))

    #Informcacion archivo pdf
    print(f'Info del archivo {archivo} es: {archivoPdf.getDocumentInfo()}')
    print(f'Destinatario del archivo {archivo} es: {archivoPdf.getNamedDestinations()}')


    # Numero de paginas
    print(f'Numero de paginas del archivo {archivo} es: {archivoPdf.getNumPages()}')

    #Obtener una pagina en especifico
    pagina = archivoPdf.getPage(0)
    print(pagina)
    print(type(pagina))

    # Rotar una pagina
    # Sentido antihorario
    pagina.rotateCounterClockwise(90)

    ## Escribir pdf
    writerPdf = pdf.PdfFileWriter()
    writerPdf.addPage(pagina)
    writerPdf.addBlankPage()

    with open('Scripting/PDF/pdfBlanco.pdf', 'wb') as pdfSalida:
        writerPdf.write(pdfSalida)
