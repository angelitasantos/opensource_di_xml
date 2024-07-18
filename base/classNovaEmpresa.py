#
# CRIAR PASTAS E GERAR ARQUIVOS MODELOS PARA NOVA EMPRESA


from datetime import date
import time
import pynput

from base.base import Base
from base.app import VarGerais, VarRede, VarSaude, VarAuditoria


class NovaEmpresa:

    def __init__(self, main):
        self.geral = main

    def __repr__(self):
        return self.main

    def criar_nova_empresa(self):
        try:
            if VarGerais.dir_rede == 'C:\\':
                criar_caminho = True
                return criar_caminho
            else:
                criar_caminho = False
                return criar_caminho
        except AttributeError:
            Base.alertar_error_except(
                self, 'classNovaEmpresa', 'criar_nova_empresa')

    def criar_novos_caminhos(self):
        try:
            Base.abrir_powershell(self)
            Base.executar_comando_cd(self, VarGerais.dir_rede)
            Base.executar_comando_mkdir(self, VarGerais.empresa)
            Base.executar_comando_cd(self, VarGerais.empresa)
            Base.executar_comando_mkdir(self, VarRede.pasta_arquivos_modelo)
            Base.executar_comando_mkdir(self, VarSaude.pasta_financeiro)
            Base.fechar_powershell(self)
        except AttributeError:
            Base.alertar_error_except(
                self, 'classNovaEmpresa', 'criar_novos_caminhos')

    def criar_pastas_internas(self):
        try:
            ano_atual = str(date.today().year)
            Base.abrir_powershell(self)
            Base.executar_comando_cd(self, VarGerais.dir_rede)
            Base.executar_comando_cd(self, VarGerais.empresa)
            auditoria_imp = VarAuditoria.caminho_auditoria_imp
            cimp = VarRede.caminho_imp
            cexp = VarRede.caminho_exp
            cdes = VarRede.caminho_desembaraco
            cpre = VarRede.caminho_pre_entry
            desembaraco_imp = cimp + ano_atual + '\\' + cdes
            desembaraco_exp = cexp + ano_atual + '\\' + cdes
            pre_entry_imp = cimp + ano_atual + '\\' + cpre
            pre_entry_exp = cexp + ano_atual + '\\' + cpre
            Base.executar_comando_mkdir(self, auditoria_imp)
            Base.executar_comando_mkdir(self, desembaraco_imp)
            Base.executar_comando_mkdir(self, desembaraco_exp)
            Base.executar_comando_mkdir(self, pre_entry_imp)
            Base.executar_comando_mkdir(self, pre_entry_exp)
            Base.fechar_powershell(self)
        except AttributeError:
            Base.alertar_error_except(
                self, 'classNovaEmpresa', 'criar_pastas_internas')

    def pesquisar_existe_arquivos_modelos(self, caminho_modelo):
        try:
            if caminho_modelo is None:
                existe_arquivos_modelos = False
                return existe_arquivos_modelos
            else:
                existe_em_massa, arquivo = Base.pesquisar_existe_arquivo(
                    self, caminho_modelo, VarRede.modelo_em_massa)
                existe_capa, arquivo = Base.pesquisar_existe_arquivo(
                    self, caminho_modelo, VarRede.modelo_capa)
                if existe_em_massa and existe_capa:
                    existe_arquivos_modelos = True
                    return existe_arquivos_modelos
                else:
                    time.sleep(Base.time_sleep_1)
                    msg1 = 'Os arquivos modelos não estão salvos!'
                    msg2 = 'Salve-os corretamente e refaça o procedimento.'
                    mensagem = f'{msg1}\n{msg2}'
                    Base.alertar_pyautogui(self, mensagem)
                    existe_arquivos_modelos = False
                    return existe_arquivos_modelos
        except AttributeError:
            Base.alertar_error_except(
                self, 'classNovaEmpresa', 'pesquisar_existe_arquivos_modelos')

    def copiar_arquivos(self, caminho_modelo):
        try:
            red = VarGerais.dir_rede
            amod = VarRede.pasta_arquivos_modelo
            mod = VarRede.modelo_financeiro
            sau = VarSaude.pasta_financeiro

            origem_em_massa = caminho_modelo + '\\' + VarRede.modelo_em_massa
            origem_capa = caminho_modelo + '\\' + VarRede.modelo_capa
            origem_financeiro = caminho_modelo + '\\' + mod
            ex_aq_m = NovaEmpresa.pesquisar_existe_arquivos_modelos(
                self, caminho_modelo)
            existe_arquivos_modelos = ex_aq_m
            if existe_arquivos_modelos:
                Base.abrir_powershell(self)
                Base.executar_comando_cd(self, red)
                destino_capa = red + VarGerais.empresa + '\\' + amod
                destino_financeiro = red + VarGerais.empresa + '\\' + sau
                Base.executar_hotkey_copiar(
                    self, origem_em_massa, destino_capa)
                Base.executar_hotkey_copiar(self, origem_capa, destino_capa)
                Base.executar_hotkey_copiar(
                    self, origem_financeiro, destino_financeiro)
                Base.fechar_powershell(self)
        except AttributeError:
            Base.alertar_error_except(
                self, 'classNovaEmpresa', 'copiar_arquivos')


class EmpresaResult:

    def __init__(self, geral):
        self.geral = geral

    def __repr__(self):
        return self.geral

    def criar_novas_pastas_arquivos(self):
        try:
            cria_caminho = NovaEmpresa.criar_nova_empresa(self)

            if cria_caminho is not None and cria_caminho is True:
                caminho = VarGerais.dir_rede + VarGerais.empresa
                print(caminho)
                existe_caminho, caminho = Base.pesquisar_existe_caminho_rede(
                    self, caminho)
                print(existe_caminho)
                if cria_caminho and not existe_caminho:
                    texto = 'Deseja criar as pastas para o cliente ?'
                    titulo = 'CONFIRMA'
                    botoes = ['SIM', 'NÃO']
                    cria_pastas = Base.confirmar_pyautogui(
                        self, texto, titulo, botoes)
                    if cria_pastas == 'SIM':
                        texto = 'Digite o caminho dos arquivos de modelo ...'
                        caminho_modelo = f'''{Base.digitar_pyautogui(
                            self, texto, "INFORME", "")}\\'''
                        exst = NovaEmpresa.pesquisar_existe_arquivos_modelos(
                            self, caminho_modelo)
                        existe_arquivos_modelos = exst

                        if (existe_arquivos_modelos
                                and caminho_modelo is not None):
                            mouse_listener = pynput.mouse.Listener(
                                suppress=True)
                            mouse_listener.start()
                            NovaEmpresa.criar_novos_caminhos(self)
                            NovaEmpresa.criar_pastas_internas(self)
                            NovaEmpresa.copiar_arquivos(self, caminho_modelo)
                            mouse_listener.stop()
                            Base.alertar_finalizado(self)
                            executar = 'EXECUTAR'
                            return executar
                        else:
                            executar = 'CANCELAR'
                            return executar
                    else:
                        executar = 'CANCELAR'
                        return executar
                else:
                    executar = 'EXECUTAR'
                    return executar
            else:
                executar = 'EXECUTAR'
                return executar
        except AttributeError:
            Base.alertar_error_except(
                self, 'classNovaEmpresa', 'criar_novas_pastas_arquivos')
