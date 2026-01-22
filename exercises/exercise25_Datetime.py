"""
from datetime import datetime, timezone, timedelta, UTC
from zoneinfo import ZoneInfo

# 1. 获取当前datetime
now = datetime.now()
print(f'当前datetime:{now}')
print(f'类型是:{type(now)}')

# 2. 获取指定datetime
custom_time = datetime(2025, 12, 31, 23, 59, 59)
print(f'指定datetime:{custom_time}')
print('=' * 50)

# 3. datetime转时间戳
dt = datetime(2026, 1, 1, 0, 0, 0)
ts = dt.timestamp()
print(f'datetime转为时间戳:{ts}')

# 4. 时间戳转datetime
# 4.1 转本地时间
local_time = datetime.fromtimestamp(ts)
print(f'时间戳转本地时间:{local_time}')

# 4.2 转UTC时间 (UTC时间指UTC+0:00时区的时间)
# utc_time = datetime.utcfromtimestamp(ts)
utc_time = datetime.fromtimestamp(ts, UTC)
print(f'时间戳转UTC时间:{utc_time}')
print('=' * 50)

# 5. 字符串转datetime
my_str = '2025-12-31 00:00:00'
str2dt = datetime.strptime(my_str, '%Y-%m-%d %H:%M:%S')
print(f'字符串转datetime:{str2dt}')

# 6. datetime转字符串
my_dt = datetime(2025, 12, 31, 23, 59, 59)
dt2str = my_dt.strftime('%Y-%m-%d %H:%M:%S')
print(f'datetime转字符串:{dt2str}')
print('=' * 50)

# 7. datetime加减
# 7.1 datetime加减timedelta
dt0 = datetime(2026, 1, 1, 0, 0, 0)
dt1 = dt0 + timedelta(days=2, hours=12)
dt2 = dt0 - timedelta(days=3, minutes=15)
print(f'原时间:{dt0}')
print(f'做加法后的时间:{dt1}')
print(f'做减法后的时间:{dt2}')

# 7.2 datetime之间的减法
delta = dt1 - dt0
print(f'偏移量1:{delta}')
print('=' * 50)

# 8. 时区转换
# 8.1 给本地时间声名时区
naive_dt = datetime(2026, 1, 1, 0, 0, 0)
print(f'本地时间:{naive_dt}')
dt_sh = dt.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
print(f'给本地时间声名时区：{dt_sh}')

# 8.2 转成目标时区
dt_ny = dt_sh.astimezone(ZoneInfo("America/New_York"))
print(f'转成目标时区:{dt_ny}')
"""
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    naive_dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    m = re.match(r'UTC([+-])(\d{1,2}):(\d{2})', tz_str)
    if not m:
        raise ValueError(f'Invalid timezone format: {tz_str}')

    sign, hours, minutes = m.groups()
    offset = timedelta(hours=int(hours), minutes=int(minutes))
    if sign == '-':
        offset = -offset

    tz = timezone(offset)
    aware_dt = naive_dt.replace(tzinfo=tz)

    return aware_dt.timestamp()
      
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

