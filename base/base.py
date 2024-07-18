#
# DEFINIR AS BIBLIOTECAS QUE SERÃO UTILIZADAS E AS FUNÇÕES PADRÕES


import os
import time
import pyautogui
import pyperclip


class Base:

    def __init__(self, base):
        self.base = base

    def __repr__(self):
        return self.base

    self = 'self'
    time_sleep_1 = 1
    time_sleep_3 = 3

    def abrir_powershell(self):
        pyautogui.hotkey('win', 'r')
        time.sleep(Base.time_sleep_1)
        pyautogui.write('powershell')
        time.sleep(Base.time_sleep_1)
        pyautogui.press('enter')
        time.sleep(Base.time_sleep_1)

    def fechar_powershell(self):
        pyautogui.write('exit')
        time.sleep(Base.time_sleep_1)
        pyautogui.press('enter')
        time.sleep(Base.time_sleep_1)

    def executar_hotkey_colar(self):
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(Base.time_sleep_1)
        pyautogui.press('enter')
        time.sleep(Base.time_sleep_1)

    def executar_hotkey_copiar(self, destino, origem):
        copiar_item = f'Copy-Item "{destino}" "{origem}"'
        pyperclip.copy(copiar_item)
        time.sleep(Base.time_sleep_1)
        Base.executar_hotkey_colar(self)

    def executar_comando_cd(self, caminho_rede):
        time.sleep(Base.time_sleep_1)
        comando_cd = f'cd "{caminho_rede}"'
        pyperclip.copy(comando_cd)
        time.sleep(Base.time_sleep_1)
        Base.executar_hotkey_colar(self)
        time.sleep(Base.time_sleep_1)

    def executar_comando_mkdir(self, caminho):
        time.sleep(Base.time_sleep_1)
        comando_mkdir = f'mkdir "{caminho}"'
        pyperclip.copy(comando_mkdir)
        time.sleep(Base.time_sleep_1)
        Base.executar_hotkey_colar(self)
        time.sleep(Base.time_sleep_1)

    def abrir_pasta(self, pasta):
        pyautogui.hotkey('win', 'r')
        time.sleep(Base.time_sleep_1)
        pyperclip.copy(pasta)
        time.sleep(Base.time_sleep_1)
        Base.executar_hotkey_colar(self)
        pyautogui.hotkey('esc')
        time.sleep(Base.time_sleep_1)

    def alertar_pyautogui(self, mensagem):
        alerta = pyautogui.alert(
                                        text=mensagem,
                                        title='ALERTA !!!',
                                        button='OK'
                                    )
        return alerta

    def confirmar_pyautogui(self, texto, titulo, botoes=[]):
        confirma = pyautogui.confirm(
                                            text=texto,
                                            title=titulo,
                                            buttons=[
                                                        item for item in botoes
                                                    ]
                                        )
        return confirma

    def digitar_pyautogui(self, texto, titulo, padrao):
        digita = pyautogui.prompt(
                                        text=texto,
                                        title=titulo,
                                        default=padrao
                                    )
        return digita

    def alertar_finalizado(self):
        mensagem = 'PROCESSO FINALIZADO !!!'
        Base.alertar_pyautogui(self, mensagem)

    def alertar_error_except(self, arquivo, funcao):
        arquivo_funcao = f'ARQUIVO: {arquivo}.py\nCLASS/FUNÇÃO: {funcao}'
        mensagem = f'''Entre em contato com o ADMINISTRADOR !!!\n
                \nErro na execução do\n{arquivo_funcao}'''
        Base.alertar_pyautogui(self, mensagem)

    def anunciar_em_construcao(self):
        mensagem = 'PROCEDIMENTO EM CONSTRUÇÃO / ATUALIZAÇÃO !!!'
        alerta_construcao = Base.alertar_pyautogui(self, mensagem)
        return alerta_construcao

    def pesquisar_existe_caminho_rede(self, caminho):
        existe_caminho = os.path.exists(caminho)
        return existe_caminho, caminho

    def definir_tipo_arquivo(
            self, ref_cliente, tipo_arquivo, extensao_arquivo):
        arquivo = f'{ref_cliente} - {tipo_arquivo}{extensao_arquivo}'
        return arquivo

    def pesquisar_existe_arquivo(self, caminho, arquivo):
        caminho_arquivo = f'{caminho}\\{arquivo}'
        existe_arquivo = os.path.exists(caminho_arquivo)
        return existe_arquivo, arquivo

    def confirmar_atualizacao(self, texto):
        titulo = 'CONFIRMA'
        botoes = ['SIM', 'NÃO']
        atualiza = Base.confirmar_pyautogui(self, texto, titulo, botoes)
        return atualiza

    def procurar_arquivo(self, processo, lista_dados=[]):
        elemento_encontrado = None
        busca = processo
        lista = lista_dados
        for s in lista:
            if busca in s:
                elemento_encontrado = s
                break
        if elemento_encontrado:
            return elemento_encontrado
