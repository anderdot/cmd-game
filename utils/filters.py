def filter_common_keys(dic1, dic2):
    """Filters dictionaries to only keep shared keys.

    Args:
        dic1 (dict): First dictionary to filter.
        dic2 (dict): Second dictionary to filter.

    Returns:
        tuple: A tuple with two dictionaries, each containing only the keys shared between both.
    """
    common_keys = set(dic1.keys()) & set(dic2.keys())
    filtered_dic1 = {k: v for k, v in dic1.items() if k in common_keys}
    filtered_dic2 = {k: v for k, v in dic2.items() if k in common_keys}
    return filtered_dic1, filtered_dic2
