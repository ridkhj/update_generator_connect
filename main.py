import extratorDeDados
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


participantesPatos, participantesPrincesa = extratorDeDados.openSheet(
    'assets\\sheets\\planilha_gerador.xltx')


def criar_pdf(nome_arquivo, participantes):
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = A4
    alturaAtual = 0
    # largura = 595.2755905511812
    # altura = 841.8897637795277
    if (len(participantes) > 3):
        for participante in participantes:

            nome = participante.name
            codigo = participante.code

            c.setFont(psfontname="Courier", size=10)
            c.drawString(x=30, y=800-alturaAtual, text=codigo +
                         "   " + nome + "   ", mode=2)
            alturaAtual = alturaAtual + 15

        if (alturaAtual > 600):
            c.showPage()
            alturaAtual = 0
        alturaAtual += 15

    for participante in participantes:

        nome = participante.name
        codigo = participante.code
        overdue = participante.overdue

        c.setFont(psfontname="Courier", size=10)
        c.drawString(x=17, y=800-alturaAtual, text=codigo +
                     "   " + nome + "   " + str(overdue), mode=2)
        c.drawString(x=17, y=780 - alturaAtual,
                     text="peso:          altura:          escolaridade:          faixa etária:          verificalão de nucleo familiar:          ", mode=2)
        c.drawImage(image='assets\\images\\coisasQueGosto.png',
                    x=0, y=570-alturaAtual, width=150, height=200)
        c.drawImage(image='assets\\images\\domiciliares.png',
                    x=125, y=570-alturaAtual, width=130, height=150)
        c.drawImage(image='assets\\images\\materiasFavoritas.png',
                    x=250, y=570-alturaAtual, width=130, height=150)
        c.drawImage(image='assets\\images\\Favoritas.png',
                    x=355, y=570-alturaAtual, width=130, height=125)

        alturaAtual = alturaAtual + 250
        if (alturaAtual >= 700):
            alturaAtual = 0
            c.showPage()

        # Salvando o PDF
    c.save()


if __name__ == "__main__":

    criar_pdf("atualizaçõesPatos.pdf", participantesPatos)
    criar_pdf("atualizaçõesPrincesa.pdf", participantesPrincesa)
