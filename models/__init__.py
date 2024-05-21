from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Importa os modelos após definir Base
from .pentaho_artifacts import PentahoArtifacts

__all__ = ["Base", "PentahoArtifacts"]
