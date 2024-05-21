from service.database import DatabaseService
from sqlalchemy import text


def truncate_table(table_name: str) -> None:
    """
    Trunca a tabela especificada.

    Parâmetros:
    - table_name (str): Nome da tabela a ser truncada.
    """
    db_service = DatabaseService()
    session = db_service.get_session()
    try:
        session.execute(text(f"TRUNCATE TABLE {table_name}"))
        session.commit()
        print(f"Tabela {table_name} truncada com sucesso.")
    except Exception as e:
        print(f"Erro ao truncar a tabela {table_name}: {e}")
        session.rollback()
    finally:
        session.close()
