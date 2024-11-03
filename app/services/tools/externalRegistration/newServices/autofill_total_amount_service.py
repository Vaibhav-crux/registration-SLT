def calculate_total_amount(vehicle_type: str) -> int:
    """
    Determine the total amount based on the vehicle type.

    :param vehicle_type: The type of vehicle.
    :return: 200 if vehicle_type is PDV, TOV, or TVV, otherwise 250.
    """
    # List of vehicle types that have a total amount of 200
    special_vehicle_types = ["PDV", "TOV", "TVV"]
    
    # Return 200 if the vehicle type is in the special list, otherwise return 250
    if vehicle_type in special_vehicle_types:
        return 200
    else:
        return 250
