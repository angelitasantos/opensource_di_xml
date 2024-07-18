#
# ESCOLHER O ARQUIVO DE MODELO


from time import sleep
import pyautogui
import pyperclip

from base.base import Base
from base.app import VarGerais, VarRede
from base.classAno import AnoResult
from base.classProcedimento import ProcResult

from cliente.classRede import Rede, RedeResult
from cliente.classCliente import CliResult


class Files:

    def __init__(self, arquivos):
        self.arquivos = arquivos

    def __repr__(self):
        return self.arquivos

    if CliResult.valida_cliente:
        ref_cliente = CliResult.dados_lista[0]
        ref_empresa = CliResult.dados_lista[1]
        tipo_comex = CliResult.dados_lista[2]
        tipo_comex_nome = CliResult.dados_lista[3]
        tipo_movto = CliResult.dados_lista[4]
        tipo_modal = CliResult.dados_lista[5]
        tipo_modal_nome = CliResult.dados_lista[6]
        caminho_movto = CliResult.dados_lista[7]
        tipo_sigla = CliResult.dados_lista[8]
        tipo_ref = CliResult.dados_lista[10]
        capa_bs = VarRede.capa_base
        apelido = VarGerais.apelido
        file_imp = f'{capa_bs}{tipo_modal_nome} {apelido} - 0000.xlsx'
        file_exp = f'{capa_bs}Exportação {VarGerais.apelido}0000.xlsx'
        capa_modelo = file_exp if tipo_comex == 'E' else file_imp

    def definir_variaveis(self):
        try:
            tp_sgl = Files.tipo_sigla
            tp_ref = Files.tipo_ref
            ano = AnoResult.ano_simples
            apel = VarGerais.apelido
            comex = Files.tipo_comex
            ref_cli = Files.ref_cliente
            ref_emp = Files.ref_empresa
            capa = VarRede.capa_base
            mod_nm = Files.tipo_modal_nome
            pasta_imp = f'{tp_sgl}-{ref_cli} - {tp_ref}-{ref_emp}-{ano}'
            pasta_exp = f'{tp_ref}-{ref_emp}-{ano} - {tp_sgl}-{ref_cli}'
            pasta = pasta_exp if Files.tipo_comex == 'E' else pasta_imp

            pasta_int_imp = VarGerais.pasta_interna_imp
            pasta_int_exp = VarGerais.pasta_interna_exp
            pasta_interna = pasta_int_exp if comex == 'E' else pasta_int_imp

            caminho = Files.caminho_movto
            processo = caminho + pasta
            processo_pc = caminho + pasta + '\\' + pasta_interna

            file_imp_new = f'{capa}{mod_nm} {apel} - {tp_sgl} - {ref_cli}.xlsx'
            file_exp_new = f'{capa}Exportação {apel} - {tp_sgl}{ref_cli}.xlsx'
            capa_novo = file_exp_new if comex == 'E' else file_imp_new

            return caminho, pasta, pasta_interna, processo, processo_pc, Files.capa_modelo, capa_novo
        except AttributeError:
            Base.alertar_error_except(self, 'classFiles', 'definir_variaveis')

    def abrir_pasta_modelo(self):
        try:
            Base.abrir_pasta(self, VarRede.caminho_modelo)
        except AttributeError:
            Base.alertar_error_except(self, 'classFiles', 'abrir_pasta_modelo')

    def abrir_pasta_processo(self, caminho):
        try:
            existe_caminho, caminho = Base.pesquisar_existe_caminho_rede(
                self, caminho)
            if existe_caminho:
                Base.abrir_pasta(self, caminho)
            else:
                mensagem = 'A pasta deste processo não foi encontrada !!!'
                Base.alertar_pyautogui(self, mensagem)
                sleep(Base.time_sleep_1)
        except AttributeError:
            Base.alertar_error_except(
                self, 'classFiles', 'abrir_pasta_processo')

    def abrir_pasta_comex(self):
        try:
            caminho_comex = Rede.escolher_caminho_comex(
                self, RedeResult.tipo_comex)
            ano = AnoResult.ano_completo
            # trocar o caminho dos processos
            caminho_imp = caminho_comex + RedeResult.tipo_movto + '\\' + ano + '\\' + 'PROCESSOS' + '\\'
            caminho_exp = caminho_comex
            comex = RedeResult.tipo_comex
            caminho_movto = caminho_exp if comex == 'E' else caminho_imp
            Base.abrir_pasta(self, caminho_movto)
        except AttributeError:
            Base.alertar_error_except(self, 'classFiles', 'abrir_pasta_comex')

    def abrir_excel_em_massa(self):
        try:
            l_01, arquivo_em_massa = Base.pesquisar_existe_arquivo(
                Base.self, VarRede.caminho_modelo, VarRede.arquivo_em_massa)
            existe_arquivo_em_massa = l_01
            modelo = VarRede.caminho_modelo
            caminho_em_massa = modelo + '\\' + VarRede.arquivo_em_massa

            if existe_arquivo_em_massa:
                pyautogui.hotkey('win', 'r')
                sleep(Base.time_sleep_1)
                pyperclip.copy(caminho_em_massa)
                Base.executar_hotkey_colar(self)
                sleep(Base.time_sleep_1)
            else:
                mensagem = 'O arquivo em massa não foi encontrado !!!'
                Base.alertar_pyautogui(self, mensagem)
                Files.abrir_pasta_modelo(self)
                sleep(Base.time_sleep_1)
        except AttributeError:
            Base.alertar_error_except(
                self, 'classFiles', 'abrir_excel_em_massa')

    def abrir_arquivo_capa(self, caminho, arquivo):
        try:
            existe_arquivo_capa, arquivo_capa = Base.pesquisar_existe_arquivo(
                Base.self, caminho, arquivo)

            if existe_arquivo_capa:
                pyautogui.hotkey('win', 'r')
                sleep(Base.time_sleep_1)
                pyperclip.copy(caminho + '\\' + arquivo)
                Base.executar_hotkey_colar(self)
                sleep(Base.time_sleep_1)
            else:
                mensagem = 'O arquivo deste processo não foi encontrado !!!'
                Base.alertar_pyautogui(self, mensagem)
                sleep(Base.time_sleep_1)
        except AttributeError:
            Base.alertar_error_except(self, 'classFiles', 'abrir_arquivo_capa')

    def criar_nova_pasta(self, caminho):
        try:
            Base.executar_comando_mkdir(self, caminho)
        except AttributeError:
            Base.alertar_error_except(self, 'classFiles', 'criar_novas_pastas')

    def copiar_novo_arquivo(self, caminho, arquivo):
        try:
            modelo = VarRede.caminho_modelo + Files.capa_modelo
            Base.executar_hotkey_copiar(self, modelo, caminho)
            rename_item = f'Rename-Item "{caminho}\\{Files.capa_modelo}" "{arquivo}"'
            pyperclip.copy(rename_item)
            sleep(Base.time_sleep_1)
            Base.executar_hotkey_colar(self)
            Base.fechar_powershell(self)
        except AttributeError:
            Base.alertar_error_except(
                self, 'classFiles', 'copiar_novo_arquivo')


class FilesResult:

    def __init__(self, arquivos):
        self.arquivos = arquivos

    def __repr__(self):
        return self.arquivos

    def definir_variaveis_files(self):
        try:
            if CliResult.valida_cliente:
                valida_files = (CliResult.valida_cliente
                                and RedeResult.valida_rede
                                and ProcResult.valida_proc
                                and AnoResult.valida_ano)
                if valida_files:
                    if CliResult.dados_lista[8] != 'Z':
                        caminho, pasta, pasta_interna, processo, processo_pc, capa_modelo, capa_novo = Files.definir_variaveis(Base.self)
                        l_01, arquivo_capa = Base.pesquisar_existe_arquivo(
                            Base.self, processo_pc, capa_novo)
                        existe_arquivo_capa = l_01
                    else:
                        caminho, pasta, pasta_interna, processo, processo_pc, capa_modelo, capa_novo = Files.definir_variaveis(
                            Base.self)
                        existe_arquivo_capa = False
                        arquivo_capa = 'Z'
                else:
                    caminho, pasta, pasta_interna, processo, processo_pc,
                    capa_modelo, capa_novo = Files.definir_variaveis(Base.self)
                    existe_arquivo_capa = False
                    arquivo_capa = 'Z'
                return caminho, pasta, pasta_interna, processo, processo_pc, capa_modelo, capa_novo, existe_arquivo_capa, arquivo_capa, valida_files
            else:
                caminho = pasta = pasta_interna = processo = processo_pc = 'Z'
                capa_modelo = capa_novo = existe_arquivo_capa = 'Z'
                arquivo_capa = valida_files = 'Z'
                return caminho, pasta, pasta_interna, processo, processo_pc, capa_modelo, capa_novo, existe_arquivo_capa, arquivo_capa, valida_files
        except AttributeError:
            Base.alertar_error_except(
                self, 'classFiles', 'definir_variaveis_files')

    caminho, pasta, pasta_interna, processo, processo_pc, capa_modelo, capa_novo, existe_arquivo_capa, arquivo_capa, valida_files = definir_variaveis_files(Base.self)
