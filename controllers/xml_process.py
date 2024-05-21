import xml.etree.ElementTree as ET
import pandas as pd


# Função para obter texto de um elemento, retornando uma string vazia se o elemento não existir
def get_text(element, tag):
    """
    Obtém o texto de um elemento XML especificado pela tag.

    Parâmetros:
    - element (ET.Element): O elemento XML onde procurar a tag.
    - tag (str): A tag do elemento cujo texto deve ser obtido.

    Retorna:
    - str: O texto do elemento, ou uma string vazia se o elemento não existir.
    """
    found = element.find(tag)
    return found.text if found is not None else ""


# Função principal para extrair informações do XML e criar o DataFrame
def extrair_dados_xml(caminho_arquivo: str) -> pd.DataFrame:
    """
    Extrai dados de um arquivo XML e cria um DataFrame do Pandas com as informações.

    Parâmetros:
    - caminho_arquivo (str): O caminho do arquivo XML a ser analisado.

    Retorna:
    - pd.DataFrame: Um DataFrame contendo as informações extraídas do XML.
    """

    try:
        # Parsing do arquivo XML
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()

        # Lista para armazenar as informações combinadas
        dados_combinados = []

        # Iterar sobre as transformações e extrair informações
        for transformation in root.findall("./transformations/transformation"):
            nome = get_text(transformation.find("info"), "name")
            trans_tipo = get_text(transformation.find("info"), "trans_type")
            diretorio = get_text(transformation.find("info"), "directory")

            # Dicionário para armazenar informações combinadas de uma transformação
            transformacao_info = {
                "name": nome,
                "transf_type": trans_tipo,
                "directory": diretorio,
                "step_input_connection": None,
                "step_input_sql": None,
                "step_output_connection": None,
                "step_output_schema": None,
                "step_output_table_name": None,
            }

            # Iterar sobre os steps da transformação e extrair informações
            for step in transformation.findall(".//step"):
                step_type = get_text(step, "type")
                if step_type == "TableInput":
                    transformacao_info["step_input_connection"] = get_text(
                        step, "connection"
                    )
                    transformacao_info["step_input_sql"] = get_text(step, "sql")
                elif step_type == "TableOutput":
                    transformacao_info["step_output_connection"] = get_text(
                        step, "connection"
                    )
                    transformacao_info["step_output_table_name"] = get_text(
                        step, "table"
                    )
                    transformacao_info["step_output_schema"] = get_text(step, "schema")

            # Adicionar as informações combinadas à lista
            dados_combinados.append(transformacao_info)

        # Criar DataFrame único
        df_dados_combinados = pd.DataFrame(dados_combinados)
        return df_dados_combinados

    except ET.ParseError:
        print("Erro ao fazer o parsing do arquivo XML.")
        return pd.DataFrame()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return pd.DataFrame()
