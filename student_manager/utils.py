def get_key_by_value(dictionary: dict, target_value: str):
    """
    Get the key associated with a specific value in a dictionary.

    Returns:
    - The key associated with the target value, or None if not found.
    """
    for key, value in dictionary.items():
        if value.lower() == target_value.lower():
            return key
    return None
