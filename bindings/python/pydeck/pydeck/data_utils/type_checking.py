def is_pandas_df(obj):
    """Check if an object is a Pandas dataframe

    The benefit here is that Pandas doesn't have to be included
    in the dependencies for pydeck

    The drawback of course is that the Pandas API might change and break this function
    """
    return obj.__class__.__module__ == 'pandas.core.frame' and obj.to_records and obj.to_dict
