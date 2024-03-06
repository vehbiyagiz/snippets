def month(df, some_date_col: str, result: str):
    """
    Returns the month of the selected date column
    :param some_date_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[some_date_col].dt.month

    return df
