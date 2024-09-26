from app.config.refreshSession import create_session
from app.models.doMaintenance import DoData

def delete_do_number_from_db(do_number):
    session = create_session()
    try:
        record = session.query(DoData).filter_by(doNumber=do_number).first()
        if record:
            session.delete(record)
            session.commit()
            return True, "DO Number successfully deleted"
        return False, "DO Number not found"
    finally:
        session.close()