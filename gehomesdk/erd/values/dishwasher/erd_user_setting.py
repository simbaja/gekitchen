from enum import Enum
from typing import NamedTuple, Optional

class UserSetting(Enum):
    DISABLE = 0
    ENABLE = 1
    INVALID = 255

class ErdUserSetting (NamedTuple):
    sound: UserSetting = UserSetting.DISABLE
    lock_control: UserSetting = UserSetting.DISABLE
    sabbath: UserSetting = UserSetting.DISABLE
    raw_value: Optional[str] = None
