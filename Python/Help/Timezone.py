from datetime import datetime
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S %Z%z"

# Current time in US/Eastern
now_us = datetime.now(timezone('US/Eastern'))
print(now_us.strftime(fmt))

print(datetime.now())