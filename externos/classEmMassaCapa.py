#
# GERAR CAPA DOS PROCESSOS A PARTIR DO ARQUIVO EM MASSA


import os
import time
from time import sleep
import pyperclip

from base.base import Base
from base.app import VarRede
from base.classProcedimento import ProcResult

from cliente.classRede import RedeResult
from cliente.classFiles import Files

from externos.classXMLRoot import XMLRootResult


class EmMassaCapa:

    def __init__(self, arquivos):
        self.arquivos = arquivos

    def __repr__(self):
        return self.arquivos

    try:
        arquivo_em_massa = VarRede.arquivo_em_massa
    except AttributeError:
        Base.alertar_error_except(Base.self, 'classEmMassaCapa', 'EmMassaCapa')

    def renomear_pasta(
            self, caminho_modelo, caminho_pc, arquivo_modelo, arquivo_novo):
        try:
            Base.abrir_powershell(self)
            copy_item = f'copy "{caminho_modelo}" "{caminho_pc}"'
            pyperclip.copy(copy_item)
            sleep(Base.time_sleep_1)
            Base.executar_hotkey_colar(self)
            pasta_nova = caminho_pc + '\\' + arquivo_modelo
            rename_item = f'Rename-Item "{pasta_nova}" "{arquivo_novo}"'
            pyperclip.copy(rename_item)
            sleep(Base.time_sleep_1)
            Base.executar_hotkey_colar(self)
            Base.fechar_powershell(self)
        except AttributeError:
            Base.alertar_error_except(
                self, 'classEmMassaCapa', 'renomear_pasta')

    def gerar_pastas_em_massa(
            self, lista_arquivo_capa=[], lista_caminho_pc=[],
            lista_capa_modelo=[], lista_caminho=[]):
        try:
            for indice, dados in enumerate(lista_arquivo_capa):
                l_01, arquivo_capa = Base.pesquisar_existe_arquivo(
                    Base.self, lista_caminho_pc[indice],
                    lista_arquivo_capa[indice])
                existe_arquivo_capa = l_01
                modelo = VarRede.caminho_modelo
                caminho_modelo = modelo + lista_capa_modelo[indice]
                if existe_arquivo_capa is False:
                    if not os.path.exists(lista_caminho_pc[indice]):
                        os.makedirs(lista_caminho_pc[indice])
                        EmMassaCapa.renomear_pasta(
                            self, caminho_modelo, lista_caminho_pc[indice],
                            lista_capa_modelo[indice],
                            lista_arquivo_capa[indice])
                    elif os.path.exists(lista_caminho_pc[indice]):
                        EmMassaCapa.renomear_pasta(
                            self, caminho_modelo, lista_caminho_pc[indice],
                            lista_capa_modelo[indice],
                            lista_arquivo_capa[indice])
                    elif os.path.exists(lista_caminho):
                        os.makedirs(lista_caminho_pc[indice])
                        EmMassaCapa.renomear_pasta(
                            self, caminho_modelo, lista_caminho_pc[indice],
                            lista_capa_modelo[indice],
                            lista_arquivo_capa[indice])
        except AttributeError:
            Base.alertar_error_except(
                self, 'classEmMassaCapa', 'gerar_pastas_em_massa')

    def criar_pastas_em_massa(self, confirma_atualizacao):
        try:
            l_01, arquivo_em_massa = Base.pesquisar_existe_arquivo(
                Base.self, VarRede.caminho_modelo, VarRede.arquivo_em_massa)
            existe_arquivo_em_massa = l_01
            modelo = VarRede.caminho_modelo
            caminho_arquivo_em_massa = modelo + VarRede.arquivo_em_massa

            if existe_arquivo_em_massa and confirma_atualizacao == 'SIM':
                try:
                    caminho_em_massa = XMLRootResult.listas_caminho_em_massa
                    EmMassaCapa.gerar_pastas_em_massa(
                        self, caminho_em_massa[8], caminho_em_massa[1],
                        caminho_em_massa[9], caminho_em_massa[0])
                    comex = RedeResult.tipo_comex
                    '' if comex == 'Z' else Files.abrir_pasta_comex(self)

                    mensagem = 'PASTAS CRIADAS !!!'
                    Base.alertar_pyautogui(self, mensagem)
                except AttributeError:
                    Base.alertar_error_except(
                        self, 'classEmMassaCapa', 'criar_pastas_em_massa if')

            elif not existe_arquivo_em_massa and confirma_atualizacao == 'SIM':
                mensagem = f'''Arquivo em Massa não está salvo na pasta !!!\n\n
                Caminho Rede: {caminho_arquivo_em_massa} \n\n
                Salve-o para continuar !!!'''
                Base.alertar_pyautogui(self, mensagem)
                Files.abrir_pasta_modelo(self)

            elif confirma_atualizacao == 'NÃO':
                mensagem = 'PASTAS NÃO CRIADAS !!!'
                Base.alertar_pyautogui(self, mensagem)
                time.sleep(Base.time_sleep_1)
            return confirma_atualizacao
        except AttributeError:
            Base.alertar_error_except(
                self, 'classEmMassaCapa', 'criar_pastas_em_massa')


class EmMassaCapaResult:

    def __init__(self, arquivos):
        self.arquivos = arquivos

    def __repr__(self):
        return self.arquivos

    comex = RedeResult.tipo_comex
    val_proc = ProcResult.valida_proc
    cod_proc = ProcResult.cod_proc
    valida_em_massa = comex != 'Z' and val_proc and cod_proc == '12'
