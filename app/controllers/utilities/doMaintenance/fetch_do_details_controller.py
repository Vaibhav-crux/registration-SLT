from app.config.refreshSession import create_session
from app.models.doMaintenance import DoData

def fetch_do_details(do_number: str):
    """
    Searches for the given DO Number in the database.

    :param do_number: The DO Number to search for.
    :return: The formatted result string if found, None otherwise.
    """
    session = create_session()
    try:
        result = session.query(DoData).filter_by(doNumber=do_number).first()

        if result:
            # Format the result data
            formatted_result = f"""
DO Number: {result.doNumber}
Weighbridge No: {result.weighbridgeNo}
Transporter: {result.transporter}
Permissido Nameon: {result.permissidoNameon}
Valid Through: {result.validThrough}
Validity Till: {result.validityTill}
Alloted Qty: {result.allotedQty}
Released Qty: {result.releasedQty}
Left Qty: {result.leftQty}
DO Address: {result.doAddress}
DO Route: {result.doRoute}
Sales Order: {result.salesOrder}
Customer ID: {result.customerId}
Mobile Number: {result.mobileNumber}
"""
            return formatted_result
        else:
            return None
    finally:
        session.close()