import openpyxl
from participante import Participante


def openSheet(path):
    # Caminho para o arquivo carregado
    file_path = path

    # Carregar o arquivo .xltx
    workbook = openpyxl.load_workbook(file_path)

    # Selecionar a planilha ativa
    sheet = workbook.active

    # Fazer alterações, se necessário (exemplo: alterar o valor da célula A1)
    sheet['A1'] = 'Novo Valor'

    # Salvar as alterações como um novo arquivo .xlsx
    new_file_path = 'assets\sheets\planilha_gerador_modificado.xlsx'
    workbook.save(new_file_path)

    return extrairDados(new_file_path)


def extrairDados(path):
    arquivo = openpyxl.load_workbook(path)
    planilha = arquivo.active
    participantes = []

    auxCell = planilha.cell(2, 2)
    row = 2
    column = 2
    acessar = planilha.cell

    while (acessar(row, column).value != None):

        codigo = acessar(row, column).value
        nome = acessar(row, column+1).value
        status = acessar(row, column+2).value
        overdue = acessar(row, column+3).value
        participanteAuxiliar = Participante(codigo, nome, status, overdue)
        participantes.append(participanteAuxiliar)

        row = row + 1

    return participantes
