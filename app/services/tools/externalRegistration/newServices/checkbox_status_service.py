def update_due_checkbox_status(payment_mode: str) -> bool:
    """
    Determine if the 'Due' checkbox should be enabled or disabled based on the selected payment mode.

    :param payment_mode: The current payment mode selected.
    :return: True if the checkbox should be enabled, False otherwise.
    """
    if payment_mode == "Cash":
        return False  # Disable the checkbox if payment mode is 'Cash'
    else:
        return True   # Enable the checkbox for all other payment modes
