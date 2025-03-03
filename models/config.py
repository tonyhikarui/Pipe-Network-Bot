import random
from typing import Literal
import secrets
import string

from better_proxy import Proxy
from pydantic import BaseModel, PositiveInt, ConfigDict, Field


class Account(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    email: str
    password: str = Field(default_factory=lambda: ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(random.randint(10, 14))))
    twitter_token: str = ""
    proxy: Proxy


class Config(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    class DelayBeforeStart(BaseModel):
        min: int
        max: int

    accounts_to_register: list[Account] = []
    accounts_to_farm: list[Account] = []
    referral_codes: list[str] = []

    delay_before_start: DelayBeforeStart
    show_points_stats: bool

    keepalive_interval: float
    heartbeat_interval: float

    threads: PositiveInt
    module: str = ""
