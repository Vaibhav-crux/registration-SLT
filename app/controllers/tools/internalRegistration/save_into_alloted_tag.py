from app.models.allotedTags import AllotedTags
from app.config.refreshSession import create_session  # Import create_session

def check_existing_in_alloted_tags(rfid_tag, vehicle_number):
    """Check if a record exists in AllotedTags."""
    db = create_session()
    try:
        existing_record = db.query(AllotedTags).filter(
            AllotedTags.rfidTag == rfid_tag,
            AllotedTags.vehicleNumber == vehicle_number
        ).first()
        return existing_record is not None
    finally:
        db.close()

        
def save_alloted_tag(**kwargs):
    """
    Save the Alloted Tag data into the database.
    
    :param **kwargs: Data to be saved into the AllotedTags table.
    """
    db = create_session()  # Create a new session using create_session

    try:
        # Create an AllotedTags instance with the given keyword arguments
        new_tag = AllotedTags(**kwargs)
        
        # Add and commit to the database
        db.add(new_tag)
        db.commit()
        db.refresh(new_tag)
        
        return new_tag
    except Exception as e:
        db.rollback()
        print(f"Error saving alloted tag: {e}")
        raise
    finally:
        db.close()  # Ensure the session is closed
