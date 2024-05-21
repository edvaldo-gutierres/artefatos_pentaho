import os
import pandas as pd
from controllers.xml_process import extrair_dados_xml


# Chama a função extrair_dados_xml e cria o arquivo excel
def xml_to_xls(filepath_xml: str, filepath_xls: str) -> None:
    """
    Extrai dados de um arquivo XML e salva em um arquivo Excel.

    Parâmetros:
    - filepath_xml (str): Caminho do arquivo XML a ser processado.
    - filepath_xls (str): Caminho onde o arquivo Excel será salvo.
    """

    try:

        # Chamar a função para extrair os dados e criar o DataFrame
        df_dados_combinados = extrair_dados_xml(filepath_xml)

        # Exibir o DataFrame
        # print(df_dados_combinados.head())

        # Verificar se o diretório de destino existe e criar se não existir
        diretorio_excel = os.path.dirname(filepath_xls)
        if not os.path.exists(diretorio_excel):
            os.makedirs(diretorio_excel)

        # Salvar o DataFrame em um arquivo Excel
        df_dados_combinados.to_excel(filepath_xls, index=False)

        print(f"Arquivo gerado com sucesso nas pasta {filepath_xls}")

    except FileNotFoundError:
        print(f"Arquivo XML não encontrado: {filepath_xml}")
    except Exception as e:
        print(
            f"Ocorreu um erro ao processar o arquivo XML ou ao salvar o arquivo Excel: {e}"
        )
