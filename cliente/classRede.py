#
# DEFINIR O CAMINHO NA REDE


import time

from base.base import Base
from base.app import VarGerais, VarRede
from base.classAno import Ano, AnoResult
from base.classProcedimento import Proc, ProcResult


class Rede:

    def __init__(self, rede):
        self.rede = rede

    def __repr__(self):
        return self.rede

    dir = 'SIM' if ProcResult.cod_proc != '12' else 'NÃO'
    arq = 'SIM' if ProcResult.cod_proc != '23' else 'NÃO'
    mod = 'SIM' if ProcResult.cod_proc != '33' else 'NÃO'
    exc = 'SIM' if ProcResult.cod_proc != '34' else 'NÃO'
    cmx = 'SIM' if ProcResult.cod_proc != '35' else 'NÃO'
    auditoria = 'SIM' if ProcResult.procedimento != 'AUDITORIA' else 'NÃO'
    proc_com_modal = (dir == 'SIM' and mod == 'SIM' and exc == 'SIM'
                      and cmx == 'SIM' and arq == 'SIM' and auditoria == 'SIM')

    def escolher_tipo_comex(self):
        try:
            if (Ano.pesquisar_tipo_processo(self) == 'completo'
                    and ProcResult.procedimento != Proc.procedimento4):
                texto = 'Escolha uma Opção ...'
                titulo = 'OPÇÃO'
                botoes = ['IMPORTAÇÃO', 'EXPORTAÇÃO']
                tipo_comex_nome = Base.confirmar_pyautogui(
                    self, texto, titulo, botoes)
                tipo_comex = ('E' if tipo_comex_nome == 'EXPORTAÇÃO'
                              else 'I' if tipo_comex_nome == 'IMPORTAÇÃO'
                              else 'Z')
                return tipo_comex, tipo_comex_nome

            elif VarGerais.comex == 'IMPORTAÇÃO':
                tipo_comex = 'I'
                tipo_comex_nome = 'IMPORTAÇÃO'
                return tipo_comex, tipo_comex_nome

            elif VarGerais.comex == 'EXPORTAÇÃO':
                tipo_comex = 'E'
                tipo_comex_nome = 'EXPORTAÇÃO'
                return tipo_comex, tipo_comex_nome
        except AttributeError:
            Base.alertar_error_except(self, 'classRede', 'escolher_tipo_comex')

    def escolher_tipo_movto(self, procedimento, tipo_comex):
        try:
            if (Ano.pesquisar_tipo_processo(self) == 'completo'
                    and ProcResult.procedimento != Proc.procedimento4):
                if (procedimento == 'SIM' and AnoResult.historico_ano == "SIM"
                        and tipo_comex != 'E'):
                    tipo_movto = ''
                    return tipo_movto
                else:
                    texto = 'Escolha uma Opção ...'
                    titulo = 'OPÇÃO'
                    botoes = ['DESEMBARAÇO', 'PRE ENTRY']
                    tipo_movto_nome = Base.confirmar_pyautogui(
                        self, texto, titulo, botoes)
                    tipo_movto = ('PRE ENTRY' if tipo_movto_nome == 'PRE ENTRY'
                                  else 'DESEMBARAÇO'
                                  if tipo_movto_nome == 'DESEMBARAÇO' else 'Z')
                    return tipo_movto

            elif VarGerais.movto == 'DESEMBARAÇO':
                tipo_movto = 'DESEMBARAÇO'
                return tipo_movto

            elif VarGerais.movto == 'PRE_ENTRY':
                tipo_movto = 'PRE ENTRY'
                return tipo_movto
        except AttributeError:
            Base.alertar_error_except(self, 'classRede', 'escolher_tipo_movto')

    def escolher_tipo_modal(self):
        try:
            if (Rede.proc_com_modal
                    and ProcResult.procedimento != Proc.procedimento4):
                texto = 'Escolha uma Opção ...'
                titulo = 'OPÇÃO'
                botoes = ['AEREA', 'MARITIMA', 'RODOVIARIA']
                tipo_modal_nome = Base.confirmar_pyautogui(
                    self, texto, titulo, botoes)
                tipo_modal = ('R' if tipo_modal_nome == 'RODOVIARIA' else 'M'
                              if tipo_modal_nome == 'MARITIMA' else 'A'
                              if tipo_modal_nome == 'AEREA' else 'Z')
                tipo_modal_nome = (VarRede.modal_rodoviario
                                   if tipo_modal_nome == 'RODOVIARIA'
                                   else VarRede.modal_maritimo
                                   if tipo_modal_nome == 'MARITIMA'
                                   else VarRede.modal_aereo
                                   if tipo_modal_nome == 'AEREA' else 'Z')
                return tipo_modal, tipo_modal_nome

            elif ProcResult.procedimento == Proc.procedimento4:
                tipo_modal = 'Z'
                tipo_modal_nome = 'Z'
                return tipo_modal, tipo_modal_nome

            else:
                tipo_modal = 'Z'
                tipo_modal_nome = 'Z'
                return tipo_modal, tipo_modal_nome
        except AttributeError:
            Base.alertar_error_except(self, 'classRede', 'escolher_tipo_modal')

    def escolher_caminho_comex(self, tipo_comex):
        try:
            caminho_comex_exp = VarRede.caminho_rede + VarRede.caminho_exp
            caminho_comex_imp = VarRede.caminho_rede + VarRede.caminho_imp
            caminho_comex = (caminho_comex_imp if tipo_comex == 'I'
                             else caminho_comex_exp if tipo_comex == 'E'
                             else '')

            return caminho_comex
        except AttributeError:
            Base.alertar_error_except(
                self, 'classRede', 'escolher_caminho_comex')

    def escolher_caminho_movto(self, tipo_comex):
        try:
            c_cmx = Rede.escolher_caminho_comex(self, tipo_comex)
            anoc = AnoResult.ano_completo
            anoa = str(AnoResult.ano_atual) + '\\'
            if tipo_comex == 'Z':
                time.sleep(Base.time_sleep_1)

            elif tipo_comex == 'E':
                tp_mto = Rede.escolher_tipo_movto(
                    self, ProcResult.historico_proc, tipo_comex)
                if tp_mto == 'PRE ENTRY':
                    c_mto = c_cmx + tp_mto + '\\' + anoc + '\\'
                    return c_cmx, c_mto, tp_mto
                else:
                    c_mto = c_cmx + anoc + '\\'
                    return c_cmx, c_mto, tp_mto

            elif tipo_comex == 'I':
                tp_mto = Rede.escolher_tipo_movto(
                    self, ProcResult.historico_proc, tipo_comex)
                if (ProcResult.historico_proc == 'SIM'
                        and AnoResult.historico_ano == "SIM"):
                    c_mto = c_cmx + anoc + '\\'
                    return c_cmx, c_mto, tp_mto
                else:
                    # trocar o caminho dos processos
                    c_mto = c_cmx + tp_mto + '\\' + anoa + 'PROCESSOS' + '\\'
                    return c_cmx, c_mto, tp_mto
        except AttributeError:
            Base.alertar_error_except(
                self, 'classRede', 'escolher_caminho_movto')


class RedeResult:

    def __init__(self, rede):
        self.rede = rede

    def __repr__(self):
        return self.rede

    def definir_variaveis_rede(self):
        try:
            if ProcResult.valida_proc:
                tipo_comex, tipo_comex_nome = Rede.escolher_tipo_comex(
                    Base.self)
                if tipo_comex != 'Z':
                    c_cmx, c_mto, tp_mto = Rede.escolher_caminho_movto(
                        self, tipo_comex)
                    caminho_comex = c_cmx
                    caminho_movto = c_mto
                    tipo_movto = tp_mto
                    if tipo_movto != 'Z' and Rede.proc_com_modal:
                        tipo_modal, tipo_modal_nome = Rede.escolher_tipo_modal(
                            self)
                    else:
                        tipo_modal = tipo_modal_nome = 'Z'
                else:
                    tipo_comex = tipo_comex_nome = tipo_movto = 'Z'
                    tipo_modal = tipo_modal_nome = caminho_comex = 'Z'
                    caminho_movto = 'Z'
            else:
                tipo_comex = tipo_comex_nome = tipo_movto = 'Z'
                tipo_modal = tipo_modal_nome = caminho_comex = 'Z'
                caminho_movto = 'Z'

            if Rede.proc_com_modal and tipo_comex != 'Z':
                valida_rede = (tipo_comex != 'Z' and tipo_movto != 'Z'
                               and tipo_modal != 'Z')
            else:
                valida_rede = tipo_comex != 'Z' and tipo_movto != 'Z'
            lst = [
                valida_rede, tipo_comex, tipo_comex_nome, tipo_movto,
                tipo_modal, tipo_modal_nome, caminho_comex, caminho_movto
            ]
            return lst
        except AttributeError:
            Base.alertar_error_except(
                self, 'classRede', 'definir_variaveis_rede')

    lst = definir_variaveis_rede(Base.self)

    valida_rede = lst[0]
    tipo_comex = lst[1]
    tipo_comex_nome = lst[2]
    tipo_movto = lst[3]
    tipo_modal = lst[4]
    tipo_modal_nome = lst[5]
    caminho_comex = lst[6]
    caminho_movto = lst[7]
