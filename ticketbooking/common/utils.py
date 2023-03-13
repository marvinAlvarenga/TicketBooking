from datetime import datetime

from pytz import timezone

from ticketbooking.common.env import env


def now() -> datetime:
    return datetime.now(tz=timezone(env.TIME_ZONE))
