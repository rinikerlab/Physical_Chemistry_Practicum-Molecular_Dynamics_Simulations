from typing import Iterable
import numpy as np
import pandas as pd

prepared_dihedral_names = ["time"]+["dihedral "+str(ind) for ind in range(1, 16)]

def read_rmsd_file(file_path:str, columns:Iterable[str]=["time", "rmsd"] )->pd.DataFrame:
  return pd.read_csv(file_path, comment="#", names=columns, delim_whitespace=True)

def read_cluster_file(file_path:str, columns:Iterable[str]=["clusterID", "clusterSize"] )->pd.DataFrame:
  return pd.read_csv(file_path, comment="#", names=columns, delim_whitespace=True)

def read_dihedral_file(file_path:str, columns:Iterable[str]=prepared_dihedral_names)->pd.DataFrame:
  return pd.read_csv(file_path, comment="#", names=columns, delim_whitespace=True)

def read_noe_file(file_path:str)->pd.DataFrame:
  return pd.read_csv(file_path, delim_whitespace=True)