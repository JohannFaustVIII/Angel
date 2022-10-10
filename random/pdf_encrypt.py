from PyPDF3 import PdfFileReader, PdfFileWriter

input_file = input("Input file: ")

with open(input_file, "rb") as pdf_in_file:
    pdf_read = PdfFileReader(pdf_in_file)

    pdf_write = PdfFileWriter()
    pdf_write.appendPagesFromReader(pdf_read)
    pdf_write.encrypt(input("Encrypt password: "))

    output_file = input("Output file: ")
    with open(output_file, "wb") as pdf_out_file:
        pdf_write.write(pdf_out_file)