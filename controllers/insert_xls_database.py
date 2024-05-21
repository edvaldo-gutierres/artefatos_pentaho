import pandas as pd
from service.database import DatabaseService
from models import PentahoArtifacts
from controllers.pentaho_artifacts_controller import truncate_table


def insert_xls_data(filepath: str, table_name: str) -> None:
    """
    Lê os dados de um arquivo Excel e insere-os na tabela do banco de dados.

    Parâmetros:
    - caminho_arquivo (str): O caminho do arquivo Excel contendo os dados.
    """
    # Inicializar o serviço de banco de dados
    db_service = DatabaseService()
    session = db_service.get_session()

    # Truncar a tabela antes de inserir os novos dados
    truncate_table(table_name)

    try:
        # Ler os dados do arquivo Excel em um DataFrame do Pandas
        df_dados = pd.read_excel(filepath)

        # Substituir valores NaN por valores padrão
        df_dados.fillna(
            {
                "name": "",
                "transf_type": "",
                "directory": "",
                "step_input_connection": "",
                "step_input_sql": "",
                "step_output_connection": "",
                "step_output_schema": "",
                "step_output_table_name": "",
            },
            inplace=True,
        )

        # Inicializar o serviço de banco de dados
        db_service = DatabaseService()
        session = db_service.get_session()

        # Iterar sobre os registros do DataFrame e inseri-los no banco de dados
        for _, row in df_dados.iterrows():
            new_artifact = PentahoArtifacts(
                name=row["name"],
                transf_type=row["transf_type"],
                directory=row["directory"],
                step_input_connection=row["step_input_connection"],
                step_input_sql=row["step_input_sql"],
                step_output_connection=row["step_output_connection"],
                step_output_schema=row["step_output_schema"],
                step_output_table_name=row["step_output_table_name"],
            )
            session.add(new_artifact)

        # Confirmar a transação
        session.commit()
        print("Dados inseridos com sucesso no banco de dados.")

    except Exception as e:
        print(f"Ocorreu um erro ao inserir os dados: {e}")

    finally:
        # Fechar a sessão
        session.close()


def insert_data(data: pd.DataFrame) -> None:
    """
    Insere dados de um DataFrame no banco de dados.

    Parâmetros:
    - data (pd.DataFrame): DataFrame contendo os dados a serem inseridos.
    """
    session = None  # Inicializa a variável session
    try:
        # Inicializar o serviço de banco de dados
        db_service = DatabaseService()
        session = db_service.get_session()

        # Iterar sobre os registros do DataFrame e inseri-los no banco de dados
        for _, row in data.iterrows():
            try:
                new_artifact = PentahoArtifacts(
                    name=row["name"],
                    transf_type=row["transf_type"],
                    directory=row["directory"],
                    step_input_connection=row["step_input_connection"],
                    step_input_sql=row["step_input_sql"],
                    step_output_connection=row["step_output_connection"],
                    step_output_schema=row["step_output_schema"],
                    step_output_table_name=row["step_output_table_name"],
                )
                session.add(new_artifact)
            except Exception as e:
                print(f"Erro ao inserir o registro: {row}")
                print(f"Erro: {e}")

        # Confirmar a transação
        session.commit()
        print("Dados inseridos com sucesso no banco de dados.")

    except Exception as e:
        print(f"Ocorreu um erro ao inserir os dados: {e}")

    finally:
        # Fechar a sessão apenas se ela foi criada
        if session:
            session.close()
