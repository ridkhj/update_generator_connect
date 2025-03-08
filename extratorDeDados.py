import openpyxl
from participante import Participante


def openSheet(path):
    # Caminho para o arquivo carregado
    file_path = path
    # Carregar o arquivo .xltx
    workbook = openpyxl.load_workbook(file_path)
    # Selecionar a planilha ativa
    sheet = workbook.active

    # Salvar as alterações como um novo arquivo .xlsx
    new_file_path = 'assets\\sheets\\planilha_gerador_modificado.xlsx'
    workbook.save(new_file_path)

    return extrairDados(new_file_path)


def extrairDados(path):
    arquivo = openpyxl.load_workbook(path)
    planilha = arquivo.active
    participantesPatos = []
    participantesPricesa = []

    row = 2
    column = 2
    acessar = planilha.cell

    while (acessar(row, column).value != None):

        codigo = acessar(row, column).value
        nome = acessar(row, column+1).value
        status = acessar(row, column+2).value

        numeroAtual = int(codigo[-5:])
        print(status)

        participanteAuxiliar = Participante(codigo, nome, status)

        if status != "Enviado" and status != "Devolvido à Igreja Parceira":

            if ((numeroAtual > 0 and numeroAtual <= 87)
                or (numeroAtual > 137 and numeroAtual <= 153)
                or (numeroAtual > 169 and numeroAtual <= 175)
                or (numeroAtual > 225 and numeroAtual <= 250)
                or (numeroAtual > 310 and numeroAtual <= 325)
                    or numeroAtual == 346):

                participantesPatos.append(participanteAuxiliar)
            else:
                participantesPricesa.append(participanteAuxiliar)
        row += 1

    return participantesPatos, participantesPricesa
