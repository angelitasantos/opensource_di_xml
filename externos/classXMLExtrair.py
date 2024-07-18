#
# RETIRAR AS INFORMAÇÕES DO ARQUIVO XML (DI)


from xml.etree import cElementTree as ETree
import pynput

from base.base import Base
from base.classAno import AnoResult
from base.classProcedimento import ProcResult

from cliente.classCliente import CliResult
from externos.classXMLRoot import XMLRoot, XMLRootResult


class XMLExtrair:

    def __init__(self, xml):
        self.xml = xml

    def __repr__(self):
        return self.xml

    def extrair_dados_gerais(self, root, indice):
        try:
            for child in list(root):
                nDI = XMLRoot.get_text(self, child, 'numeroDI')
                viaTransporteNome = XMLRoot.get_text(
                    self, child, 'viaTransporteNome')
                sequencialRetificacao = XMLRoot.get_text(
                    self, child, 'sequencialRetificacao')
                Numero = XMLRoot.get_text(self, child, 'importadorNumero')
                imp_nome = XMLRoot.get_text(self, child, 'importadorNome')
                imp_cidade = XMLRoot.get_text(
                    self, child, 'importadorEnderecoMunicipio')
                imp_uf = XMLRoot.get_text(self, child, 'importadorEnderecoUf')
                dta = XMLRoot.get_text(
                    self, child, 'documentoChegadaCargaNumero')

                data_atual = AnoResult.data_atual

                if ProcResult.cod_proc == '23':
                    sigla_empresa = XMLRootResult.lista_sigla_empresa[indice]
                    num_empresa = XMLRootResult.lista_num_empresa[indice]
                    sigla_cliente = XMLRootResult.lista_sigla_cliente[indice]
                    num_cliente = XMLRootResult.lista_num_cliente[indice]
                else:
                    sigla_empresa = CliResult.dados_lista[10]
                    num_empresa = CliResult.dados_lista[1]
                    sigla_cliente = CliResult.dados_lista[8]
                    num_cliente = CliResult.dados_lista[0]

                cnpjp1 = Numero[0:2] + '.' + Numero[2:5] + '.' + Numero[5:8]
                cnpj = cnpjp1 + '/' + Numero[8:12] + '-' + Numero[-2:]
                num_DI = nDI[0] + nDI[1] + '/' + nDI[2:9] + '-' + nDI[-1]
                num_DTA = dta[0] + dta[1] + '/' + dta[2:9] + '-' + dta[-1]
                modal = viaTransporteNome
                seq_retif = sequencialRetificacao
                conf_retif = 'Sim' if seq_retif != '00' else 'Não'

            dados_gerais = [
                                cnpj,
                                imp_cidade,
                                imp_uf,
                                imp_nome,
                                AnoResult.ano_completo,
                                sigla_empresa,
                                num_empresa,
                                sigla_cliente,
                                num_cliente,
                                modal,
                                seq_retif,
                                num_DI,
                                num_DTA,
                                conf_retif,
                                data_atual
                            ]
            return dados_gerais
        except AttributeError:
            Base.alertar_error_except(
                self, 'classXMLExtrair', 'extrair_dados_gerais')

    def extrair_dados_adicoes(self, indice, caminho=[], arquivo=[]):
        try:
            caminho_xml = caminho[indice] + arquivo[indice]
            arquivos = [caminho_xml]
            for arquivo in arquivos:
                prstree = ETree.parse(arquivo)
                root = prstree.getroot()

                regimes = []
                exportadores = []
                cod_fund_legais = []
                fund_legais = []
                todas_LI = []

                for child in root.iter('adicao'):
                    nLI = XMLRoot.get_text(self, child, 'numeroLI')
                    atipico = XMLRoot.get_text(
                        self, child, 'iiRegimeTributacaoNome')
                    exportador = XMLRoot.get_text(
                        self, child, 'fornecedorNome')
                    cod_fund_legal = XMLRoot.get_text(
                        self, child, 'iiFundamentoLegalCodigo')
                    f_l_existe = []
                    camfl = 'declaracaoImportacao/adicao/iiFundamentoLegalNome'
                    for infoss in root.iterfind(camfl):
                        f_l_existe.append(infoss.text)
                    tfl = 'SEM FUNDAMENTO LEGAL'
                    fund_legal = tfl if f_l_existe == [] else XMLRoot.get_text(
                        self, child, 'iiFundamentoLegalNome')

                    num_LI = nLI[0] + nLI[1] + '/' + nLI[2:9] + '-' + nLI[-1]

                    regimes.append(atipico)
                    exportadores.append(exportador)
                    cod_fund_legais.append(cod_fund_legal)
                    fund_legais.append(fund_legal)
                    todas_LI.append(num_LI)

                qtd_regime, lista_regime, boolean = XMLRoot.get_lista(
                    self, regimes)
                qtd_exp, lista_exp, boolean = XMLRoot.get_lista(
                    self, exportadores)
                qtd_Tot_LI, lista_LI, boolean_LI = XMLRoot.get_lista(
                    self, todas_LI)
                qtd_cod, lista_cod_fund_legal, boolean = XMLRoot.get_lista(
                    self, cod_fund_legais)
                qtd_fund_legal, lista_fund_legal, boolean = XMLRoot.get_lista(
                    self, fund_legais)

                trib_atipica = 'Sim' if 'SUSPENSAO' in lista_regime else 'Não'
                drawback = 'Sim' if '16' in lista_cod_fund_legal else 'Não'

            dados_adicoes = [
                                qtd_exp,
                                lista_exp,
                                qtd_Tot_LI,
                                lista_LI,
                                boolean_LI,
                                trib_atipica,
                                lista_cod_fund_legal,
                                qtd_fund_legal,
                                lista_fund_legal,
                                drawback
                            ]
            return dados_adicoes
        except AttributeError:
            Base.alertar_error_except(
                self, 'classXMLExtrair', 'extrair_dados_adicoes')

    def extrair_dados_conhecimento(self, indice, caminho=[], arquivo=[]):
        try:
            caminho_xml = caminho[indice] + arquivo[indice]
            xmldata = caminho_xml
            prstree = ETree.parse(xmldata)
            root = prstree.getroot()

            lista_conhecimento = []
            all_conhecimentos = []
            cod_conhecimento = '28'

            for child in root.iter('documentoInstrucaoDespacho'):
                numero = XMLRoot.get_text(
                    self, child, 'numeroDocumentoDespacho')
                if child.tag == 'documentoInstrucaoDespacho':
                    for attr in child:
                        if attr.text == cod_conhecimento:
                            for child in child:
                                break

                            lista_conhecimento = numero.replace(' ', '')
                            all_conhecimentos.append(lista_conhecimento)

            conhecimentos = XMLRoot.get_replace_caracteres(
                self, all_conhecimentos)

            return conhecimentos
        except AttributeError:
            Base.alertar_error_except(
                self, 'classXMLExtrair', 'extrair_dados_conhecimento')

    def extrair_dados_faturas(self, indice, caminho=[], arquivo=[]):
        try:
            caminho_xml = caminho[indice] + arquivo[indice]
            xmldata = caminho_xml
            prstree = ETree.parse(xmldata)
            root = prstree.getroot()

            lista_fatura = []
            all_faturas = []
            cod_fatura = '01'

            for child in root.iter('documentoInstrucaoDespacho'):
                numero = XMLRoot.get_text(
                    self, child, 'numeroDocumentoDespacho')
                if child.tag == 'documentoInstrucaoDespacho':
                    for attr in child:
                        if attr.text == cod_fatura:
                            for child in child:
                                break

                            lista_fatura = numero.replace(' ', '')
                            all_faturas.append(lista_fatura)

            qtd_faturas = len(all_faturas)
            faturas = XMLRoot.get_replace_caracteres(self, all_faturas)

            return qtd_faturas, faturas
        except AttributeError:
            Base.alertar_error_except(
                self, 'classXMLExtrair', 'extrair_dados_faturas')


class XMLExtResult:

    def __init__(self, xml):
        self.xml = xml

    def __repr__(self):
        return self.xml

    def definir_variaveis_extrair_xml(self):
        try:
            if CliResult.valida_cliente:
                if (ProcResult.cod_proc == '11'
                        or ProcResult.cod_proc == '12'
                        or ProcResult.cod_proc == '21'
                        or ProcResult.cod_proc == '23'):
                    mouse_listener = pynput.mouse.Listener(suppress=True)
                    mouse_listener.start()
                    lista_root = XMLRoot.listar_arquivos_xml(
                        Base.self, XMLRootResult.lista_caminho,
                        XMLRootResult.lista_caminho_pc,
                        XMLRootResult.lista_arquivo_txt,
                        XMLRootResult.lista_arquivo_xml)
                    lista_root = XMLRoot.listar_arquivos_xml(
                        Base.self, XMLRootResult.lista_caminho,
                        XMLRootResult.lista_caminho_pc,
                        XMLRootResult.lista_arquivo_txt,
                        XMLRootResult.lista_arquivo_xml)
                    mouse_listener.stop()
                else:
                    lista_root = []
            else:
                lista_root = []
            if lista_root == []:
                lista_root = ['Z']
            return lista_root
        except AttributeError:
            Base.alertar_error_except(
                self, 'classXMLExtrair', 'definir_variaveis_extrair_xml')
