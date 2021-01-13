from typing import Iterable
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def visualize_timeseries(time:Iterable, data:Iterable, title:str, y_label:str, x_label:str,
                         limit_structured:float=0.08, limit_disordered:float=0.12,
                         line_widht:float=0.3, figure_size:Iterable[float]=[12,6], dpi:int=100)->plt.Figure:
  figure, ax = plt.subplots(ncols=1, figsize=figure_size, dpi=dpi)
  ax.plot(time, data, lw=line_widht)
  ax.plot([time[0]-5, time[time.shape[0]-1]+5], [limit_structured, limit_structured], ls=":", c="black", label="limit_stucture")
  ax.plot([time[0]-5, time[time.shape[0]-1]+5], [limit_disordered, limit_disordered], ls=":", c="black", label="limit_disorder")
  ax.set_ylabel(y_label)
  ax.set_xlabel(x_label)
  ax.set_title(title)
  return figure

def visualize_dihedrals(data:pd.DataFrame, 
                        y_labels:str, x_labels:str, title:str,
                        ncols=4, nrows=3, figsize=[20,20]):
  
  #multiplot:
  torsion_names = list(data.columns)
  torsion_names.remove("time")
  fig, axes = plt.subplots(ncols=ncols, nrows=nrows, sharex=True, sharey=True, figsize=figsize)
  conc_axes = np.concatenate(axes)
  
  for ind, (torsion, ax) in enumerate(zip(torsion_names,conc_axes)):
      ax.scatter(data.time, data[torsion], s=0.3)
      ax.set_title(torsion)

      #labelling
      if(ind%ncols==0):
          ax.set_ylabel(y_labels)
      if(ind >= (nrows-1)*ncols):
          ax.set_xlabel(x_labels)
  fig.suptitle("DIHEDRALS", y=0.95)
  return fig


def visualize_cluster_sizes(cluster_ids:Iterable, cluster_sizes:Iterable, show_first_clusters:int, 
                            x_label:str, y_label:str, title:str):
    fig, ax = plt.subplots(ncols=1)
    ax.bar(cluster_ids[:show_first_clusters], height=cluster_sizes[:show_first_clusters])
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    
    return fig
