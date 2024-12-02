import datetime
from dataclasses import dataclass
from typing import Optional, List

from app.models.subscription import Subscription


@dataclass
class User:
    id: str
    email: str
    username: str
    notification_email: bool
    setting_collection_order: str
    created_at: datetime
    confirmed_at: datetime
    confirmation_sent_at: datetime
    unconfirmed_email: Optional[str]
    certify_adult: bool
    possessions_count: int
    ad_home_banner: bool
    ad_native_home_first: bool
    ad_native_planning_perso: bool
    is_premium: bool
    subscriptions: List[Subscription]