# 🛠️ Controllers

Diretório onde se encontram todas as funções criadas, referentes à transformação de dados, operações de banco de dados e automatizações.

## Arquivos e suas funcionalidades

### `__init__.py`
Arquivo de inicialização do pacote. Geralmente vazio, mas essencial para que o Python trate o diretório como um pacote.

### `convert_xml_to_xls.py`
Este script contém a função `xml_to_xls`, que extrai dados de um arquivo XML e os salva em um arquivo Excel. Ele utiliza a função `extrair_dados_xml` do módulo `xml_process.py` para criar um DataFrame a partir do XML e, em seguida, salva o DataFrame em um arquivo Excel no caminho especificado.

### `env_controller.py`
Este script gerencia as variáveis de ambiente do projeto. Utiliza a biblioteca `dotenv` para carregar variáveis de ambiente de um arquivo `.env` e retorna um dicionário contendo essas variáveis.

### `insert_xls_database.py`
Este script contém duas funções principais para inserir dados em um banco de dados a partir de um arquivo Excel:
- `insert_xls_data`: Lê os dados de um arquivo Excel e insere-os em uma tabela do banco de dados, truncando a tabela antes de inserir os novos dados.
- `insert_data`: Insere dados de um DataFrame no banco de dados.

### `pentaho_artifacts_controller.py`
Este script contém a função `truncate_table`, que trunca a tabela especificada no banco de dados. Ele utiliza o serviço de banco de dados para obter uma sessão e executar o comando SQL de truncamento.

### `xml_process.py`
Este script contém funções para processar e extrair dados de arquivos XML. As principais funções são:
- `get_text`: Obtém o texto de um elemento XML especificado por uma tag.
- `extrair_dados_xml`: Extrai dados de um arquivo XML e cria um DataFrame do Pandas com as informações extraídas. Esta função é utilizada pelo script `convert_xml_to_xls.py`.

## Dependências
Certifique-se de ter instalado as seguintes bibliotecas para o funcionamento adequado dos scripts:
- `pandas`
- `openpyxl`
- `sqlalchemy`
- `python-dotenv`
- `xml.etree.ElementTree`

## Estrutura do Projeto
```plaintext
controllers/
├── __pycache__/
├── __init__.py
├── convert_xml_to_xls.py
├── env_controller.py
├── insert_xls_database.py
├── pentaho_artifacts_controller.py
├── README.md
└── xml_process.py
```

