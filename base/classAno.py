#
# ESCOLHER O ANO


from datetime import date
from base.base import Base
from base.app import VarGerais
from base.classNovaEmpresa import EmpresaResult


class Ano:

    def __init__(self, ano):
        self.ano = ano

    def __repr__(self):
        return self.ano

    executar = EmpresaResult.criar_novas_pastas_arquivos(Base.self)

    def pesquisar_tipo_processo(self):
        try:
            processo_ativo = None
            busca = VarGerais.processo
            for s in VarGerais.lista_processos:
                if busca in s:
                    processo_ativo = s
                    break
            if processo_ativo:
                return processo_ativo
        except AttributeError:
            Base.alertar_error_except(
                self, 'classAno', 'pesquisar_tipo_processo')

    def gerar_data_atual(self):
        try:
            data_atual = date.today()
            ano_atual = date.today().year
            data_formatada_br = data_atual.strftime('%d/%m/%Y')
            ano_anterior_default = ano_atual - 1
            return ano_atual, data_formatada_br, ano_anterior_default
        except AttributeError:
            Base.alertar_error_except(self, 'classAno', 'gerar_data_atual')

    def escolher_ano_anterior(self):
        try:
            ano_atual, data_atual, ano_anterior_default = Ano.gerar_data_atual(
                self)
            texto = '''Digite o Ano do Processo.\n
            Escreva quatro digítos para continuar.'''
            escolher_ano_anterior = Base.digitar_pyautogui(
                self, texto, 'INFORME', ano_anterior_default)
            if escolher_ano_anterior is not None:
                ano_anterior = escolher_ano_anterior
                len_escolha = len(escolher_ano_anterior)
                return ano_anterior, len_escolha
            else:
                ano_anterior = ''
                len_escolha = 4
                return ano_anterior, len_escolha
        except AttributeError:
            Base.alertar_error_except(
                self, 'classAno', 'escolher_ano_anterior')

    def validar_ano_anterior(self):
        try:
            ano_anterior, len_escolha = Ano.escolher_ano_anterior(self)
            if ano_anterior is not None:
                while len_escolha != 4:
                    try:
                        msg1 = 'Você não digitou um ANO válido!'
                        msg2 = 'Lembre-se de escrever os 4 digítos do ANO.'
                        mensagem = f'{msg1}\n{msg2}'
                        Base.alertar_pyautogui(self, mensagem)
                        ano_anterior, len_escolha = Ano.escolher_ano_anterior(
                            self)
                    except AttributeError:
                        Base.alertar_error_except(
                            self, 'classAno', 'validar_ano_anterior while')
                return ano_anterior
        except AttributeError:
            Base.alertar_error_except(self, 'classAno', 'validar_ano_anterior')

    def escolher_tipo_ano(self):
        try:
            texto = 'Escolha o Ano do Processo ...'
            titulo = 'OPÇÃO'
            botoes = ['ANO ATUAL', 'ANO ANTERIOR']
            tipo_ano = Base.confirmar_pyautogui(self, texto, titulo, botoes)
            return tipo_ano
        except AttributeError:
            Base.alertar_error_except(self, 'classAno', 'escolher_tipo_ano')

    def escolher_ano(self):
        try:
            tipo_ano = (Ano.escolher_tipo_ano(self)
                        if Ano.pesquisar_tipo_processo(self) == 'completo'
                        else 'ANO ATUAL')
            if tipo_ano == 'ANO ANTERIOR':
                ano_escolhido = (Ano.validar_ano_anterior(self)
                                 if Ano.pesquisar_tipo_processo(
                                     self) == 'completo' else 2023)
                return ano_escolhido
            elif tipo_ano == 'ANO ATUAL':
                ano_escolhido, dt_at, a_ant_def = Ano.gerar_data_atual(self)
                return ano_escolhido
        except AttributeError:
            Base.alertar_error_except(self, 'classAno', 'escolher_ano')


class AnoResult:

    def __init__(self, ano):
        self.ano = ano

    def __repr__(self):
        return self.ano

    def definir_variaveis_ano(self):
        try:
            if Ano.executar == 'EXECUTAR':
                ano_atual, data_atual, ano_ant_default = Ano.gerar_data_atual(
                    Base.self)
                ano_processo = Ano.escolher_ano(Base.self)
                ano_completo = str(ano_processo)
                ano_simples = str(ano_completo[-2:])
                valida_ano = ano_processo is not None and ano_processo != ''
                historico_ano = 'SIM' if str(
                    ano_processo) != str(ano_atual) else 'NÃO'
            else:
                ano_atual, data_atual, ano_ant_default = Ano.gerar_data_atual(
                    Base.self)
                ano_processo = ano_atual
                ano_completo = str(ano_processo)
                ano_simples = str(ano_completo[-2:])
                valida_ano = False
                historico_ano = 'NÃO'
            lst_var = [
                valida_ano,
                historico_ano,
                ano_atual,
                ano_processo,
                ano_completo,
                ano_simples,
                data_atual
            ]
            return lst_var
        except AttributeError:
            Base.alertar_error_except(
                self, 'classAno', 'definir_variaveis_ano')

    lst_var = definir_variaveis_ano(Base.self)
    valida_ano = lst_var[0]
    historico_ano = lst_var[1]
    ano_atual = lst_var[2]
    ano_processo = lst_var[3]
    ano_completo = lst_var[4]
    ano_simples = lst_var[5]
    data_atual = lst_var[6]
