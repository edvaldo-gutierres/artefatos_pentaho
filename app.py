# Importa bibliotecas Python
import os
import pandas as pd

# Importa módulos
from controllers.convert_xml_to_xls import xml_to_xls
from controllers.insert_xls_database import insert_xls_data

# Define a função principal main
def main() -> None:

    # Caminho para dos arquivos
    table_name = "data_engineer.tab_pentaho_artifacts"
    pasta_xml = "assets/raw/pentaho.xml"
    pasta_xls = "assets/trusted/pentaho.xlsx"
    pasta_xls_new = "assets/trusted/dados_banco.xlsx"

    # Extrai dados do xml e salva em excel
    xml_to_xls(filepath_xml=pasta_xml, filepath_xls=pasta_xls)

    # Insere os dados do excel no banco de dados
    insert_xls_data(filepath=pasta_xls, table_name=table_name)


# Verifica se o script está sendo executado diretamente (e não importado como um módulo em outro script)
if __name__ == "__main__":
    main()
