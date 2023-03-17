import numpy as np
import pandas as pd


def writeDFToFilepathAsCSV(array, columns, filepath):
    df = pd.DataFrame(data=np.array(array), columns=columns)
    df.to_csv(filepath, index=False)
