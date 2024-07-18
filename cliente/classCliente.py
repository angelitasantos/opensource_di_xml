#
# DEFINIR OS DADOS DO CLIENTE / PROCESSO


from base.base import Base
from base.app import VarGerais
from base.classAno import AnoResult
from base.classProcedimento import ProcResult

from cliente.classRede import Rede, RedeResult


class Cliente:

    def __init__(self, cliente):
        self.cliente = cliente

    def __repr__(self):
        return self.cliente

    if ProcResult.valida_proc and RedeResult.tipo_comex != 'Z':
        tipo_sigla = (VarGerais.filiais_exp if RedeResult.tipo_comex == 'E'
                      else VarGerais.filiais_imp)
        ref_sigla = (VarGerais.ref_filial if VarGerais.ref_filial != []
                     else tipo_sigla)

    def digitar_ref_cliente(self):
        try:
            texto = 'Digite o Número Ref. ' + VarGerais.cliente + ' ...'
            titulo = 'INFORME'
            padrao = ''
            ref_cliente = Base.digitar_pyautogui(self, texto, titulo, padrao)
            while ref_cliente == '':
                ref_cliente = Base.digitar_pyautogui(
                    self, texto, titulo, padrao)
            return ref_cliente
        except AttributeError:
            Base.alertar_error_except(
                self, 'classCliente', 'digitar_ref_cliente')

    def digitar_ref_empresa(self):
        try:
            texto = 'Digite o Número Ref. ' + VarGerais.empresa + ' ...'
            titulo = 'INFORME'
            padrao = ''
            ref_empresa = Base.digitar_pyautogui(self, texto, titulo, padrao)
            while ref_empresa == '':
                ref_empresa = Base.digitar_pyautogui(
                    self, texto, titulo, padrao)
            return ref_empresa
        except AttributeError:
            Base.alertar_error_except(
                self, 'classCliente', 'digitar_ref_empresa')

    def escolher_sigla_comex(self, tipo_comex):
        try:
            if Rede.proc_com_modal:
                ref_filial_processo = (VarGerais.filiais_exp
                                       if tipo_comex == 'E'
                                       else VarGerais.filiais_imp)

                if VarGerais.ref_filial == []:
                    texto = 'Escolha a Filial ' + VarGerais.cliente + ' ...'
                    titulo = 'OPÇÃO'
                    botoes = [item for item in VarGerais.filiais_nomes]
                    filial = Base.confirmar_pyautogui(
                        self, texto, titulo, botoes)
                    if filial is not None:
                        sigla_comex_index = VarGerais.filiais_nomes.index(
                            filial)
                        sigla_comex = ref_filial_processo[sigla_comex_index]
                        return sigla_comex, sigla_comex_index
                    else:
                        sigla_comex = filial = 'Z'
                        sigla_comex_index = 0
                        return sigla_comex, sigla_comex_index
                else:
                    if tipo_comex == 'I':
                        filial = VarGerais.filiais_nomes[0]
                        sigla_comex = VarGerais.filiais_imp[0]
                        sigla_comex_index = VarGerais.filiais_imp.index(
                            sigla_comex)
                        return sigla_comex, sigla_comex_index

                    elif tipo_comex == 'E':
                        filial = VarGerais.filiais_nomes[0]
                        sigla_comex = VarGerais.filiais_exp[0]
                        sigla_comex_index = VarGerais.filiais_exp.index(
                            sigla_comex)
                        return sigla_comex, sigla_comex_index
        except AttributeError:
            Base.alertar_error_except(
                self, 'classCliente', 'escolher_sigla_comex')

    def escolher_ref_interna(self, tipo_comex, tipo_sigla_index):
        try:
            ref_interna_processo = (VarGerais.ref_interna_exp
                                    if tipo_comex == 'E'
                                    else VarGerais.ref_interna_imp)
            if VarGerais.ref_filial == []:
                ref_interna = ref_interna_processo[tipo_sigla_index]
                return ref_interna
            else:
                ref_int_imp = VarGerais.ref_interna_imp[tipo_sigla_index]
                ref_int_exp = VarGerais.ref_interna_exp[tipo_sigla_index]
                ref_interna = (ref_int_imp if tipo_comex == 'I'
                               else ref_int_exp if tipo_comex == 'E' else '')
                return ref_interna
        except AttributeError:
            Base.alertar_error_except(
                self, 'classCliente', 'escolher_ref_interna')

    def retornar_info_cliente(self):
        try:
            sigla_comex, sigla_comex_index = Cliente.escolher_sigla_comex(
                self, RedeResult.tipo_comex)
            ref_int = Cliente.escolher_ref_interna(
                self, RedeResult.tipo_comex, sigla_comex_index)
            if sigla_comex != 'Z':
                ref_cli = Cliente.digitar_ref_cliente(self)
                ref_emp = Cliente.digitar_ref_empresa(self)
            else:
                ref_cli = ''
                ref_emp = ''
            return ref_cli, ref_emp, sigla_comex, sigla_comex_index, ref_int
        except AttributeError:
            Base.alertar_error_except(
                self, 'classCliente', 'retornar_info_cliente')

    def retornar_dados(self):
        try:
            if Rede.proc_com_modal:
                l_01, l_02, l_03, l_04, l_05 = Cliente.retornar_info_cliente(
                    self)
                ref_cliente = l_01
                ref_empresa = l_02
                sigla_comex = l_03
                sigla_comex_index = l_04
                ref_interna = l_05
                lista_dados_ref = [
                                        ref_cliente, ref_empresa,
                                        RedeResult.tipo_comex,
                                        RedeResult.tipo_comex_nome,
                                        RedeResult.tipo_movto,
                                        RedeResult.tipo_modal,
                                        RedeResult.tipo_modal_nome,
                                        RedeResult.caminho_movto,
                                        sigla_comex, sigla_comex_index,
                                        ref_interna
                                    ]
                return lista_dados_ref
            else:
                ref_cliente = ref_empresa = sigla_comex = 'Z'
                sigla_comex_index = ref_interna = 'Z'
                lista_dados_ref = [
                                        ref_cliente, ref_empresa,
                                        RedeResult.tipo_comex,
                                        RedeResult.tipo_comex_nome,
                                        RedeResult.tipo_movto,
                                        RedeResult.tipo_modal,
                                        RedeResult.tipo_modal_nome,
                                        RedeResult.caminho_movto,
                                        sigla_comex, sigla_comex_index,
                                        ref_interna
                                    ]
                return lista_dados_ref
        except AttributeError:
            Base.alertar_error_except(self, 'classCliente', 'retornar_dados')

    def apresentar_tela_dados(self, lista_dados_ref=[]):
        try:
            if lista_dados_ref[8] != 'Z':
                dados_dig_cli = f'Ref.{VarGerais.cliente}:{lista_dados_ref[0]}'
                dados_dig_emp = f'Ref.{VarGerais.empresa}:{lista_dados_ref[1]}'
                dados_dig_ref = f'{dados_dig_cli}\n{dados_dig_emp}'
                msg1 = f'Processo: {lista_dados_ref[2]} - {lista_dados_ref[3]}'
                dados_dig_tipo = f'{msg1}\nTipo: {lista_dados_ref[4]}'
                modal = f'Modal: {lista_dados_ref[6]}'
                caminho_rede = lista_dados_ref[7]
                caminho_processo = f'Caminho Rede: {caminho_rede}'

                msg2 = 'Confirma os dados digitados ?'
                msg3 = f'{dados_dig_tipo}\n{modal}\n\n{caminho_processo}'
                texto = f'{msg2}\n\n{dados_dig_ref}\n\n{msg3}'
                titulo = 'CONFIRMA'
                botoes = ['SIM', 'NÃO', 'CANCELAR']
                confirma_dados = Base.confirmar_pyautogui(
                    self, texto, titulo, botoes)
                return confirma_dados
        except AttributeError:
            Base.alertar_error_except(
                self, 'classCliente', 'apresentar_tela_dados')

    def tentar_confirmar(self, confirma_dados_ref):
        try:
            if Rede.proc_com_modal:
                confirma_dados = confirma_dados_ref
                while (VarGerais.tentativas <= VarGerais.total_tentativas
                       and confirma_dados == 'NÃO'):
                    var_dif = VarGerais.total_tentativas - VarGerais.tentativas
                    mensagem = f'Você tem {var_dif} tentativa(s)!!!'
                    Base.alertar_pyautogui(self, mensagem)
                    tipo_comex, tipo_comex_nome = Rede.escolher_tipo_comex(
                        self)

                    if tipo_comex != 'Z':
                        c_comex, c_mto, tp_mto = Rede.escolher_caminho_movto(
                            self, tipo_comex)
                        caminho_movto = c_mto
                        tipo_movto = tp_mto
                        if tipo_movto != 'Z':
                            tp_modal, tp_modal_nome = Rede.escolher_tipo_modal(
                                self)
                            tipo_modal = tp_modal
                            tipo_modal_nome = tp_modal_nome
                    else:
                        tipo_comex = tipo_comex_nome = tipo_movto = 'Z'
                        tipo_modal = tipo_modal_nome = 'Z'
                        caminho_movto = 'Z'

                    if tipo_comex != 'Z':
                        l1, l2, l3, l4, l5 = Cliente.retornar_info_cliente(
                            self)
                        ref_cliente = l1
                        ref_empresa = l2
                        sigla_comex = l3
                        sigla_comex_index = l4
                        ref_interna = l5
                        lista_dados_conf = [
                                                ref_cliente, ref_empresa,
                                                tipo_comex, tipo_comex_nome,
                                                tipo_movto, tipo_modal,
                                                tipo_modal_nome, caminho_movto,
                                                sigla_comex, sigla_comex_index,
                                                ref_interna
                                            ]
                        confirma_dados = Cliente.apresentar_tela_dados(
                            self, lista_dados_conf)
                    else:
                        confirma_dados = 'SIM'
                        lista_dados_conf = ['', '']
                    VarGerais.tentativas += 1

                    if confirma_dados == 'CANCELAR':
                        AnoResult.ano_processo = None
                        ProcResult.cod_proc = 0
                return confirma_dados, lista_dados_conf
        except AttributeError:
            Base.alertar_error_except(self, 'classCliente', 'tentar_confirmar')

    def confirmar_dados(self):
        try:
            lista_dados_ref = Cliente.retornar_dados(self)
            if Rede.proc_com_modal:
                confirma_dados_ref = Cliente.apresentar_tela_dados(
                    self, lista_dados_ref)

                if confirma_dados_ref == 'SIM':
                    AnoResult.ano_processo = AnoResult.ano_processo
                    ProcResult.cod_proc = ProcResult.cod_proc

                elif confirma_dados_ref == 'CANCELAR':
                    AnoResult.ano_processo = None
                    ProcResult.cod_proc = 0

                elif confirma_dados_ref == 'NÃO':
                    confirma = confirma_dados_ref
                    conf_tent, lista_dados_tent = Cliente.tentar_confirmar(
                        self, confirma)

                dados = (lista_dados_tent if confirma_dados_ref == 'NÃO'
                         else lista_dados_ref)
                return dados
        except AttributeError:
            Base.alertar_error_except(self, 'classCliente', 'confirmar_dados')


class CliResult:

    def __init__(self, cliente):
        self.cliente = cliente

    def __repr__(self):
        return self.cliente

    def definir_variaveis_cliente(self):
        try:
            if (RedeResult.valida_rede
                    and ProcResult.valida_proc and AnoResult.valida_ano
                    and Rede.proc_com_modal is True):
                dados_lista = Cliente.confirmar_dados(Base.self)

            elif (ProcResult.valida_proc
                    and AnoResult.valida_ano and Rede.proc_com_modal is False):
                dados_lista = Cliente.retornar_dados(Base.self)
            else:
                dados_lista = ['', '']
            if dados_lista is not None:
                valida_cliente = (False if dados_lista == ['', '']
                                  else dados_lista[0] is not None
                                  and dados_lista[1] is not None)
                valida_filial = (False if dados_lista == ['', '']
                                 else False if dados_lista[8] == 'Z' else True)

                return valida_cliente, valida_filial, dados_lista
            else:
                valida_cliente = False
                valida_filial = False
                dados_lista = ['', '']
                return valida_cliente, valida_filial, dados_lista
        except AttributeError:
            Base.alertar_error_except(
                self, 'classCliente', 'definir_variaveis_cliente')

    valida_cliente, valida_filial, dados_lista = definir_variaveis_cliente(
        Base.self)
