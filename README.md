# Projeto Python para gestão de artefatos do pentaho

O objetivo do projeto é ler o arquivo XML exportado do pentaho e inserir os dados em uma tabela no banco de dados.

# Exportação Arquivo XML


# Estrutura de Pasta

A estrutura de pastas foi organizada seguindo princípios de orientação a objetos, conforme preferência do autor.

* **assets/**: Pasta onde se encontram os arquivos estáticos XML e Excel.
* **controller/**: Pasta onde se encontram todas as funções criadas, referentes à transformação de dados, operações de banco de dados e automatizações.
* **model/**: Pasta onde se encontram as classes de banco de dados criadas, referentes às tabelas do banco.
* **service/**: Pasta onde se encontram as funções criadas para conexão ao banco de dados.


# Banco de dados e ORM
A tecnologia de banco de dados utilizada foi o SQL Server, e o ORM utilizado foi o sqlalchemy.


# Ambiente
Para instalar as dependências do projeto, execute o comando
```bash
pip install -r requirements.txt
```