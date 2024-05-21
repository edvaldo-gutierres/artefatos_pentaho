# 🔌 Service

Pasta onde se encontram as funções criadas para conexão ao banco de dados.

## Arquivos e suas funcionalidades

## Estrutura do Projeto
A estrutura do projeto é a seguinte:
```
service/
├── __pycache__/
├── __init__.py
├── database.py
└── service.md
```

### Arquivos
- `__init__.py`: Arquivo de inicialização do módulo.
- `database.py`: Contém a implementação da classe `DatabaseService` que gerencia as conexões e sessões com o banco de dados.
- `service.md`: Documento com informações sobre o serviço.

## Pré-requisitos
- Um arquivo `.env` contendo as seguintes variáveis de ambiente:
  - `server`: Endereço do servidor SQL Server
  - `database`: Nome do banco de dados
  - `username`: Nome de usuário para autenticação
  - `password`: Senha para autenticação


## Uso
### DatabaseService
A classe `DatabaseService` é usada para gerenciar a conexão com o banco de dados e realizar operações.

#### Métodos
- `__init__()`: Inicializa a classe, configura a string de conexão e cria as tabelas no banco de dados.
- `create_tables()`: Cria as tabelas no banco de dados se elas não existirem.
- `get_session()`: Retorna uma nova sessão do banco de dados.
- `select_data_by_table_name(table_name: str)`: Consulta todos os registros de uma tabela específica pelo nome da tabela.


## Logs
O serviço está configurado para registrar logs de informações e erros, o que ajuda na depuração e no monitoramento das operações do banco de dados.
