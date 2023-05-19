import numpy as np
import pandas as pd


def writeDFToFilepathAsCSV(array, columns, filepath, sort=False):
    df = pd.DataFrame(data=np.array(array), columns=columns)
    if sort:
        df = df.sort_values(by=['Net Profit After Steam ($)'], axis=0, ascending=False)
    df.to_csv(filepath, index=False)
