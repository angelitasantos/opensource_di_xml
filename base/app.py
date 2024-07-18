#
# DEFINIR AS VARIÁVEIS


from openpyxl import load_workbook
from base.base import Base


class ExcelExterno:

    def __init__(self, excel):
        self.excel = excel

    def __repr__(self):
        return self.excel

    nome_arquivo = 'main_variaveis.xlsx'
    dir_arquivo = 'C:\\REDE\\AUTOMACAO\\'
    caminho_arquivo = dir_arquivo + nome_arquivo
    l_01, l_02 = Base.pesquisar_existe_arquivo(
        Base.self, dir_arquivo, nome_arquivo)
    existe_arquivo_main_variaveis = l_01
    arquivo_main_variaveis = l_02

    mensagem = f'''O arquivo:
    \n{nome_arquivo}\nnão está salvo no local correto !!!
    \nSalve-o corretamente e refaça o procedimento !!!'''

    if not existe_arquivo_main_variaveis:
        Base.alertar_pyautogui(Base.self, mensagem)

    else:
        workbook = load_workbook(caminho_arquivo, data_only=True)
        var_gerais = workbook['var_gerais']
        var_rede = workbook['var_rede']
        var_saude = workbook['var_saude']
        var_auditoria = workbook['var_auditoria']
        listas = workbook['listas']
        m_row = listas.max_row

    def listar_dados(self, m_row, listas, coluna):
        exportados = []
        for i in range(2, m_row + 1):
            cell_obj = listas.cell(row=i, column=coluna)
            exportados.append(cell_obj.value)
        return exportados


class VarGerais:

    def __init__(self, variaveis_geral):
        self.variaveis_geral = variaveis_geral

    def __repr__(self):
        return self.variaveis_geral

    try:
        dir_rede = ExcelExterno.var_gerais['C3'].value
        dir_financeiro = ExcelExterno.var_gerais['C4'].value
        grupo = ExcelExterno.var_gerais['C5'].value
        lista_empresas = [
                                'EMPRESA 1',
                                'EMPRESA 2',
                                'EMPRESA 3'
                            ]
        empresa = ExcelExterno.var_gerais['C6'].value
        cliente = ExcelExterno.var_gerais['C7'].value
        apelido = ExcelExterno.var_gerais['C8'].value

        filiais_nomes = ExcelExterno.listar_dados(
            Base.self, ExcelExterno.m_row, ExcelExterno.listas, 2)
        filiais_imp = ExcelExterno.listar_dados(
            Base.self, ExcelExterno.m_row, ExcelExterno.listas, 3)
        filiais_exp = ExcelExterno.listar_dados(
            Base.self, ExcelExterno.m_row, ExcelExterno.listas, 4)
        ref_filial = []
        ref_interna_imp = ExcelExterno.listar_dados(
            Base.self, ExcelExterno.m_row, ExcelExterno.listas, 5)
        ref_interna_exp = ExcelExterno.listar_dados(
            Base.self, ExcelExterno.m_row, ExcelExterno.listas, 6)

        pasta_interna_imp = ExcelExterno.var_gerais['C9'].value
        pasta_interna_exp = ExcelExterno.var_gerais['C10'].value

        total_tentativas = int(ExcelExterno.var_gerais['C11'].value)
        tentativas = int(ExcelExterno.var_gerais['C12'].value)

        lista_processos = [
                                'auditoria',
                                'importação-desembaraço',
                                'importação-pre-entry',
                                'exportação-desembaraço',
                                'exportação-pre-entry',
                                'importação-histórico',
                                'exportação-histórico',
                                'completo'
                            ]
        processo = ExcelExterno.var_gerais['C13'].value
        comex = ExcelExterno.var_gerais['C14'].value
        movto = ExcelExterno.var_gerais['C15'].value
    except AttributeError:
        Base.alertar_error_except(Base.self, 'app', 'VarGerais')


class VarRede:

    def __init__(self, variaveis_rede):
        self.variaveis_rede = variaveis_rede

    def __repr__(self):
        return self.variaveis_rede

    try:
        caminho_rede = VarGerais.dir_rede + VarGerais.grupo + '\\'
        caminho_imp = 'IMPORTAÇÃO\\Clientes\\' + VarGerais.apelido + '\\'
        caminho_exp = 'EXPORTAÇÃO\\Clientes\\' + VarGerais.cliente + '\\'
        caminho_desembaraco = 'DESEMBARAÇO' + '\\'
        caminho_pre_entry = 'PRE ENTRY' + '\\'
        pasta_arquivos_modelo = 'CAPAS MODELO ' + VarGerais.cliente + '\\'
        caminho_modelo = caminho_rede + pasta_arquivos_modelo

        capa_base = ExcelExterno.var_rede['C3'].value
        arquivo_em_massa = ExcelExterno.var_rede['C4'].value
        modelo_capa = ExcelExterno.var_rede['C5'].value
        modelo_em_massa = ExcelExterno.var_rede['C6'].value
        modelo_financeiro = ExcelExterno.var_rede['C7'].value

        modal_aereo = ExcelExterno.var_rede['C8'].value
        modal_maritimo = ExcelExterno.var_rede['C9'].value
        modal_rodoviario = ExcelExterno.var_rede['C10'].value
    except AttributeError:
        Base.alertar_error_except(Base.self, 'app', 'VarRede')


class VarSaude:

    def __init__(self, variaveis_saude):
        self.variaveis_saude = variaveis_saude

    def __repr__(self):
        return self.variaveis_saude

    try:
        caminho_financeiro = ExcelExterno.var_saude['C3'].value
        caminho_rede = VarGerais.dir_financeiro + caminho_financeiro
        pasta_financeiro = ExcelExterno.var_saude['C4'].value

        arquivo_saude = ExcelExterno.var_saude['C5'].value
        arquivo_saude_backup = ExcelExterno.var_saude['C6'].value
        arquivo_saude_base = ExcelExterno.var_saude['C7'].value
        arquivo_saude_processos = ExcelExterno.var_saude['C8'].value

        caminho_completo = caminho_rede + arquivo_saude
        empresa_banco1 = ExcelExterno.var_saude['C9'].value
        empresa_banco2 = ExcelExterno.var_saude['C10'].value
        banco1 = ExcelExterno.var_saude['C11'].value
        banco2 = ExcelExterno.var_saude['C12'].value
        require_cols = [1, 3, 4, 6, 7, 8, 9, 10]
    except AttributeError:
        Base.alertar_error_except(Base.self, 'app', 'VarSaude')


class VarAuditoria:

    def __init__(self, variaveis_auditoria):
        self.variaveis_auditoria = variaveis_auditoria

    def __repr__(self):
        return self.variaveis_auditoria

    try:
        pasta_auditoria = ExcelExterno.var_auditoria['C3'].value
        rede = VarRede.caminho_rede
        caminho_auditoria_imp = rede + VarRede.caminho_imp + pasta_auditoria
        if VarGerais.processo == 'importação-desembaraço':
            caminho_auditoria_imp

        porto_santos = ExcelExterno.var_auditoria['C4'].value
        porto_seco_betim = ExcelExterno.var_auditoria['C5'].value
        arq_aud_porto_santos = ExcelExterno.var_auditoria['C6'].value
        arq_aud_porto_seco_betim = ExcelExterno.var_auditoria['C7'].value
        bh_airport = ''
        arq_aud_bh_airport = ''
        gru_airport = ''
        arq_aud_gru_airport = ''
        vcp_airport = ''
        arq_aud_vcp_airport = ''
        cwb = ''
    except AttributeError:
        Base.alertar_error_except(Base.self, 'app', 'VarAuditoria')
