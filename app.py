import os
import pandas as pd
from controllers.convert_xml_to_xls import xml_to_xls
from controllers.insert_xls_database import insert_xls_data


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


# Chamar a função principal para criar o arquivo Excel
if __name__ == "__main__":
    main()
