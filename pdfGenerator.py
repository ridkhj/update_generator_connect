from main import participantes
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def criar_pdf(nome_arquivo):
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = letter

    # Adicionando texto
    c.drawString(100, altura - 100,
                 "Olá, este é um PDF gerado pelo ReportLab!")

    # Salvando o PDF
    c.save()


if __name__ == "__main__":
    criar_pdf("exemplo.pdf")
