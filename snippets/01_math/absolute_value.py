def absolute_value(df, numeric_col: str, result: str):
    """
    Returns the absolute value of a number. The absolute value of a number is the number without its sign.
    :param numeric_col: Name of the column whose absolute values are to be calculated.
    :param result: Name of the resulting column where the absolute values will be stored.
    """
    import numpy as np

    df[result] = np.absolute(df[numeric_col])

    return df
