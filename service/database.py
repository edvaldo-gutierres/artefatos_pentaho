from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
from models import PentahoArtifacts, Base
import logging

# Importa função de controle de variaveis
from controllers.env_controller import EnvironmentController

# Configura o log para depuração
logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Carrega as variáveis de ambiente
env_vars = EnvironmentController.load_environment_variables()

# Define os parâmetros de conexão
server = env_vars["server"]
database = env_vars["database"]
username = env_vars["username"]
password = env_vars["password"]


class DatabaseService:
    """Classe para gerenciar a conexão e sessões com o banco de dados."""

    def __init__(self):
        """
        Inicializa a classe DatabaseService.
        - Monta a string de conexão usando as variáveis de ambiente.
        - Cria o engine que gerencia a conexão com o banco de dados.
        - Cria um gerenciador de sessões (Session) vinculado ao engine.
        """
        # Define a string de conexão para o banco de dados usando o driver ODBC para SQL Server
        connection_string = (
            f"mssql+pyodbc://{username}:{password}@{server}/{database}"
            f"?driver=ODBC+Driver+17+for+SQL+Server"
        )

        # Cria um objeto Engine que faz a ponte entre o banco de dados e a aplicação
        self.engine = create_engine(connection_string)

        # Cria as tabelas no banco de dados se elas não existirem
        self.create_tables()

        # Configura o factory sessionmaker para criar novas sessões vinculadas ao engine
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        """Cria as tabelas no banco de dados se elas não existirem"""
        try:
            Base.metadata.create_all(self.engine)
            logging.info("As tabelas foram criadas com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao criar as tabelas: {e}")

    def get_session(self):
        """
        Retorna uma nova sessão do banco de dados.
        - As sessões são usadas para realizar operações de leitura e escrita no banco de dados.
        """
        return self.Session()

    def select_data_by_table_name(self, table_name: str):
        """
        Consulta todos os registros de uma tabela específica pelo nome da tabela.

        Parâmetros:
        - table_name (str): Nome da tabela a ser consultada.

        Retorna:
        - List[dict]: Lista de dicionários contendo os registros da tabela.
        """
        session = self.get_session()
        try:
            metadata = MetaData()
            table = Table(
                table_name, metadata, autoload_with=self.engine, schema="data_engineer"
            )
            stmt = select(table)
            results = session.execute(stmt).fetchall()
            keys = table.columns.keys()
            return [dict(zip(keys, row)) for row in results]
        except Exception as e:
            logging.error(f"Erro ao consultar os dados da tabela {table_name}: {e}")
            return []
        finally:
            session.close()
