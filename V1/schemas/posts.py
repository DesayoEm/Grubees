from pydantic import BaseModel
from datetime import datetime

class Posts(BaseModel):
    id: str
    user_id: str  # reference back to user
    created_at: datetime
    last_updated: datetime