#
# ATUALIZAR AS INFORMAÇÕES A PARTIR DE ARQUIVOS PDF


from base.base import Base


class PDF:

    def __init__(self, pdf):
        self.pdf = pdf

    def __repr__(self):
        return self.pdf

    def funcao(self):
        try:
            pass
        except AttributeError:
            Base.alertar_error_except(self, 'classPDF', 'funcao')


class PDFResult:

    def __init__(self, pdf):
        self.pdf = pdf

    def __repr__(self):
        return self.pdf
