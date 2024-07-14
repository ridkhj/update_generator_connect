import extratorDeDados
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


participantes = extratorDeDados.openSheet(
    'assets\sheets\planilha_gerador.xltx')


def criar_pdf(nome_arquivo):
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = A4
    # largura = 595.2755905511812
    # altura = 841.8897637795277

    c.drawImage(image='assets/images/coisasQueGosto.png',
                x=0, y=590, width=150, height=200)
    c.drawImage(image='assets/images/tarefasDomiciliares.png',
                x=125, y=590, width=130, height=150)
    c.drawImage(image='assets/images/materiasFavoritas.png',
                x=250, y=590, width=130, height=150)
    c.drawImage(image='assets/images/atividadesFavoritas.png',
                x=450, y=590, width=130, height=150)

    # Salvando o PDF
    c.save()


if __name__ == "__main__":
    criar_pdf("exemplo.pdf")
