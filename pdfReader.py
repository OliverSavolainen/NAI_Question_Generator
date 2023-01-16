import PyPDF2


class PDFReader:
    def __init__(self, filename, pages=None):
        if pages is None:
            pages = []
        self.filename = filename
        self.pages = pages

    def read(self):
        # creating a pdf File object of original pdf
        pdfFileObj = open(self.filename, 'rb')

        # creating a pdf Reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

        text = ""
        # rotating each page
        if len(self.pages) == 0:
            for page in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(page)
                textPage = pageObj.extractText()
                text += textPage

        else:
            for page in self.pages:
                pageObj = pdfReader.getPage(page)
                textPage = pageObj.extractText()
                text += textPage

        # closing the original pdf file object
        pdfFileObj.close()

        return text

