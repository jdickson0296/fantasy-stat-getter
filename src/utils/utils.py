from os import path
import pandas as pd


def write_df_to_csv(data, file):
    """_summary_

    Args:
        data (_type_): _description_
        file (_type_): _description_
    """
    df = pd.DataFrame(data)
    if path.exists(file):
        df.to_csv(file, index=False, mode='a', header=False)
    else:
        df.to_csv(file, index=False, header=True)
