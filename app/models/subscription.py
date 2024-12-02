import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Subscription:
    id: str
    user_id: str
    app: str
    product_id: str
    original_purchase_date: datetime
    expires_date: datetime
    auto_renewing: bool
    created_at: datetime
    updated_at: datetime
    cancellation_date: Optional[datetime] = None