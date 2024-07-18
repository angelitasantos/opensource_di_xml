## Automação Em PYTHON

### Processo: IMPORTAÇÃO / DESEMBARAÇO

#### Atualizar arquivo Excel com dados da DI via arquivo XML

- DI: Declaração de Importação

- retirar informações da DI (arquivo em xml) e preencher planilha de Excel com os dados coletados
    - CNPJ do cliente
    - nome do importador
    - nome do exportador
    - numero processo
    - modal
    - numero AWB/BL/CRT
    - numero e data da DI
    - numero(s) da(s) LI(s)
    - numero(s) da(s) fatura(s)
    - numero DTA/Termo de Entrada
    - se a importação é Drawback
    - se tem retificação de DI
    - se é importação atípica
    - peso bruto
    - canal
    - valor CIF
    - valor II (imposto de Importação)
    - data chegada / data saída
    - fundamento legal


- Siscomex Importação DI Web (arquivo xml) - necessita de certificado digital:
[Siscomex Importação DI Web](https://www1.siscomex.receita.fazenda.gov.br/siscomexImpweb-7/login_cert.jsp)


- bibliotecas utilizadas
    - os
    - time
    - datetime
    - pyautogui
    - pyperclip
    - openpyxl
    - pynput
    - pandas
    - locale
    - elementpath
    - xml.etree
    - pyinstaller


- processo para criar o executável encontra-se no arquivo: pyinstaller.txt
- para executar no terminal digitar: python main.py

- salvar os arquivos da pasta "files" dentro da pasta: 'C:\\REDE\\AUTOMACAO\\'
    - caminho a copiar os modelos para criar uma nova pasta
    - copiar os arquivos da pasta "files" para a pasta criada
