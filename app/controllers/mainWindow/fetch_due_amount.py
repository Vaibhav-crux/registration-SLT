from datetime import datetime, time
from sqlalchemy import or_, and_
from app.config.refreshSession import create_session
from app.models.allotedTags import AllotedTags

def fetch_due_amount():
    session = create_session()

    try:
        alloted_tag = session.query(AllotedTags).filter_by(due=True).all()
        due=0
        for data in alloted_tag:
            due=due+int(data.total)

        if due:
            return str(due*10)
        else:
            return "0"
    except Exception as e:
        print(f"Error fetching due amount: {e}")
        return "Unknown Amount"
    
    finally:
        session.close()