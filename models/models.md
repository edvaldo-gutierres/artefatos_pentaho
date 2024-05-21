# 📋 Models

Pasta onde se encontram as classes de banco de dados criadas, referentes às tabelas do banco.

## Arquivos e suas funcionalidades

### `__init__.py`
Este arquivo inicializa o pacote de modelos e define a base para os modelos declarativos do SQLAlchemy. Ele contém a definição de `Base`, que é utilizada como base para todos os modelos declarativos, e importa o modelo `PentahoArtifacts`.

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Importa os modelos após definir Base
from .pentaho_artifacts import PentahoArtifacts

__all__ = ["Base", "PentahoArtifacts"]
```

### `pentaho_artifacts.py`
Este arquivo define o modelo `PentahoArtifacts`, que representa a tabela `tab_pentaho_artifacts` no esquema `data_engineer` do banco de dados. A classe `PentahoArtifacts` herda de `Base` e mapeia as colunas da tabela para os atributos da classe.

```python
from sqlalchemy import Column, Integer, String, Text
from . import Base

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
```

## Dependências
Certifique-se de ter instalado as seguintes bibliotecas para o funcionamento adequado dos scripts:
- `sqlalchemy`

## Estrutura do Projeto
```plaintext
models/
├── __pycache__/
├── __init__.py
├── pentaho_artifacts.py
└── README.md
```

