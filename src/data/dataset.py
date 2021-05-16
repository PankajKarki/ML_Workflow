import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris

def get_data() -> pd.DataFrame:
    """ Read dataset into pandas dataframe.
    Returns:
        pandas.DataFrame
    """

    iris = load_iris(as_frame=True)
    dataset = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
    columns=iris['feature_names'] + ['target'])
    dataset.rename(
    columns=lambda colname: colname.strip(' (cm)').replace(' ', '_'),
    inplace=True
    )

    return dataset


def get_target_names() -> list:
    """Get target class names.
    Returns:
        List[Text]: list of target class names
    """
    return load_iris(as_frame=True).target_names.tolist()

