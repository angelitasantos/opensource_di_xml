#
# ESCOLHER O PROCEDIMENTO


from base.base import Base
from base.classAno import AnoResult


class Proc:

    def __init__(self, procedimento):
        self.procedimento = procedimento

    def __repr__(self):
        return self.ano

    procedimento1 = 'CRIAR PASTAS/ARQUIVO'
    procedimento2 = 'ATUALIZAR PLANILHA'
    procedimento3 = 'HISTÓRICO'
    procedimento4 = 'AUDITORIA'

    subproc31 = 'PASTA DO PROCESSO'
    subproc32 = 'CAPA DO PROCESSO'
    subproc33 = 'PASTA MODELOS'
    subproc34 = 'EXCEL EM MASSA'
    subproc35 = 'PASTA COMEX'

    subproc41 = 'EADI USIFAST'
    subproc42 = 'SANTOS BRASIL'
    subproc43 = 'BH AIRPORT'
    subproc44 = 'GRU AIRPORT'
    subproc45 = 'VCP AIRPORT'
    subproc46 = 'CWB'

    def escolher_procedimento(self, historico):
        try:
            texto = 'Qual o procedimento deseja executar ?'
            titulo = 'OPÇÃO'
            if (historico == 'SIM'):
                botoes = [Proc.procedimento2,
                          Proc.procedimento3, Proc.procedimento4, 'SAIR']
                procedimento = Base.confirmar_pyautogui(
                    self, texto, titulo, botoes)
            elif (historico == 'NÃO'):
                botoes = [Proc.procedimento2,
                          Proc.procedimento1, Proc.procedimento3,
                          Proc.procedimento4, 'SAIR']
                procedimento = Base.confirmar_pyautogui(
                    self, texto, titulo, botoes)
            if procedimento is None:
                procedimento = 'SAIR'
                return procedimento
            else:
                return procedimento
        except AttributeError:
            Base.alertar_error_except(
                self, 'classProcedimento', 'escolher_procedimento')

    def escolher_subprocedimento_criar_pastas(self, procedimento):
        cod_proc = '1' if procedimento == Proc.procedimento1 else 9
        subproc11 = 'PROCESSO INDIVIDUAL'
        subproc12 = 'PROCESSOS EM MASSA'
        try:
            if cod_proc == '1':
                texto = 'Como deseja criar o(s) processo(s) ?'
                titulo = 'OPÇÃO'
                botoes = [subproc11, subproc12, 'VOLTAR']
                subproc = Base.confirmar_pyautogui(self, texto, titulo, botoes)
                cod_subproc = (cod_proc + '1' if subproc == subproc11
                               else cod_proc + '2' if subproc == subproc12
                               else 9)
                return cod_subproc
        except AttributeError:
            Base.alertar_error_except(
                self, 'classProcedimento',
                'escolher_subprocedimento_criar_pastas')

    def escolher_subprocedimento_atualizar(self, procedimento):
        cod_proc = '2' if procedimento == Proc.procedimento2 else 9
        subproc21 = 'DADOS DI (XML)'
        subproc22 = 'DADOS SAUDE'
        subproc23 = 'DI (XML) EM MASSA'
        try:
            if cod_proc == '2':
                texto = 'O que deseja atualizar ?'
                titulo = 'OPÇÃO'
                botoes = [subproc21, subproc22, subproc23, 'VOLTAR']
                subproc = Base.confirmar_pyautogui(self, texto, titulo, botoes)
                cod_subproc = (cod_proc + '1' if subproc == subproc21
                               else cod_proc + '2' if subproc == subproc22
                               else cod_proc + '3' if subproc == subproc23
                               else 9)
                return cod_subproc
        except AttributeError:
            Base.alertar_error_except(
                self, 'classProcedimento',
                'escolher_subprocedimento_atualizar')

    def escolher_subprocedimento_historico(self, procedimento):
        cod_proc = '3' if procedimento == Proc.procedimento3 else 9
        try:
            if cod_proc == '3':
                texto = 'O que deseja abrir ?'
                titulo = 'OPÇÃO'
                botoes = [Proc.subproc31, Proc.subproc32, Proc.subproc33,
                          Proc.subproc34, Proc.subproc35, 'VOLTAR']
                subproc = Base.confirmar_pyautogui(self, texto, titulo, botoes)

            match subproc:
                case Proc.subproc31:
                    cod_subproc = cod_proc + '1'
                case Proc.subproc32:
                    cod_subproc = cod_proc + '2'
                case Proc.subproc33:
                    cod_subproc = cod_proc + '3'
                case Proc.subproc34:
                    cod_subproc = cod_proc + '4'
                case Proc.subproc35:
                    cod_subproc = cod_proc + '5'
                case 'VOLTAR':
                    cod_subproc = 9
                case None:
                    cod_subproc = 9

            return cod_subproc
        except AttributeError:
            Base.alertar_error_except(
                self, 'classProcedimento',
                'escolher_subprocedimento_historico')

    def escolher_subprocedimento_auditoria(self, procedimento):
        cod_proc = '4' if procedimento == Proc.procedimento4 else 9
        try:
            if cod_proc == '4':
                texto = 'Qual local deseja auditar ?'
                titulo = 'OPÇÃO'
                botoes = [Proc.subproc41, Proc.subproc42, Proc.subproc43,
                          Proc.subproc44, Proc.subproc45, Proc.subproc46,
                          'VOLTAR']
                subproc = Base.confirmar_pyautogui(self, texto, titulo, botoes)

                match subproc:
                    case Proc.subproc41:
                        cod_subproc = cod_proc + '1'
                        construcao = Base.anunciar_em_construcao(
                            self) if cod_subproc == '41' else cod_subproc
                        cod_subproc = 9 if construcao == 'OK' else cod_subproc
                    case Proc.subproc42:
                        cod_subproc = cod_proc + '2'
                        construcao = Base.anunciar_em_construcao(
                            self) if cod_subproc == '42' else cod_subproc
                        cod_subproc = 9 if construcao == 'OK' else cod_subproc
                    case Proc.subproc43:
                        cod_subproc = cod_proc + '3'
                        construcao = Base.anunciar_em_construcao(
                            self) if cod_subproc == '43' else cod_subproc
                        cod_subproc = 9 if construcao == 'OK' else cod_subproc
                    case Proc.subproc44:
                        cod_subproc = cod_proc + '4'
                        construcao = Base.anunciar_em_construcao(
                            self) if cod_subproc == '44' else cod_subproc
                        cod_subproc = 9 if construcao == 'OK' else cod_subproc
                    case Proc.subproc45:
                        cod_subproc = cod_proc + '5'
                        construcao = Base.anunciar_em_construcao(
                            self) if cod_subproc == '45' else cod_subproc
                        cod_subproc = 9 if construcao == 'OK' else cod_subproc
                    case Proc.subproc46:
                        cod_subproc = cod_proc + '6'
                        construcao = Base.anunciar_em_construcao(
                            self) if cod_subproc == '46' else cod_subproc
                        cod_subproc = 9 if construcao == 'OK' else cod_subproc
                    case 'VOLTAR':
                        cod_subproc = 9
                    case None:
                        cod_subproc = 9

                return cod_subproc
        except AttributeError:
            Base.alertar_error_except(
                self, 'classProcedimento',
                'escolher_subprocedimento_auditoria')

    def escolher_codigo(self, procedimento):
        try:
            if procedimento == Proc.procedimento1:
                cod_procedimento = Proc.escolher_subprocedimento_criar_pastas(
                    self, procedimento)
            elif procedimento == Proc.procedimento2:
                cod_procedimento = Proc.escolher_subprocedimento_atualizar(
                    self, procedimento)
            elif procedimento == Proc.procedimento3:
                cod_procedimento = Proc.escolher_subprocedimento_historico(
                    self, procedimento)
            elif procedimento == Proc.procedimento4:
                cod_procedimento = Proc.escolher_subprocedimento_auditoria(
                    self, procedimento)
            elif procedimento == 'SAIR':
                cod_procedimento = 0

            return cod_procedimento
        except AttributeError:
            Base.alertar_error_except(
                self, 'classProcedimento', 'escolher_codigo')


class ProcResult:

    def __init__(self, procedimento):
        self.procedimento = procedimento

    def __repr__(self):
        return self.procedimento

    def definir_variaveis_proc(self):
        try:
            if AnoResult.valida_ano:
                procedimento = Proc.escolher_procedimento(
                    Base.self, AnoResult.historico_ano)
                if procedimento != 'SAIR':
                    cod_proc = Proc.escolher_codigo(Base.self, procedimento)

                    while cod_proc == 9 and procedimento != 'SAIR':
                        procedimento = Proc.escolher_procedimento(
                            Base.self, AnoResult.historico_ano)
                        cod_proc = Proc.escolher_codigo(
                            Base.self, procedimento)

                    cod_proc = cod_proc
                    historico_proc = 'SIM' if procedimento == 3 else 'NÃO'
                else:
                    historico_proc = 'NÃO'
                    cod_proc = 0
            else:
                historico_proc = 'NÃO'
                cod_proc = 0
                procedimento = ''

            valida_proc = (AnoResult.valida_ano and procedimento != 0
                           and procedimento is not None and cod_proc != 0
                           and cod_proc is not None)
            return valida_proc, cod_proc, procedimento, historico_proc
        except AttributeError:
            Base.alertar_error_except(
                self, 'classProcedimento', 'definir_variaveis_proc')

    vproc, cproc, proc, hist_proc = definir_variaveis_proc(Base.self)
    valida_proc = vproc
    cod_proc = cproc
    procedimento = proc
    historico_proc = hist_proc
