# Importa biblioteca
from sqlalchemy import Column, Integer, String, DateTime, Text
from . import Base

# from sqlalchemy.ext.declarative import declarative_base   # Vai entrar em desuso
from sqlalchemy.orm import declarative_base

# Definir a base para os modelos declarativos
Base = declarative_base()


# Definir uma classe modelo, que herda de 'Base'
class PentahoArtifacts(Base):
    __tablename__ = "tab_pentaho_artifacts"
    __table_args__ = {"schema": "data_engineer"}  # Define o esquema do banco de dados
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    transf_type = Column(String(50))
    directory = Column(String(255))
    step_input_connection = Column(String(255))
    step_input_sql = Column(Text)
    step_output_connection = Column(String(255))
    step_output_schema = Column(String(255))
    step_output_table_name = Column(String(255))
