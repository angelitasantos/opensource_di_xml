#
# ESCOLHER A AÇÃO PRINCIPAL

from base.base import Base
from base.classProcedimento import ProcResult
from classAcoes import Acoes


if __name__ == '__main__':
    if ProcResult.valida_proc:
        Acoes.escolher_procedimento(
            Base.self, ProcResult.procedimento, ProcResult.cod_proc)
