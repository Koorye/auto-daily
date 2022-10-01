from core import TimeSeries
from config import MyConfig


ts = TimeSeries(MyConfig())
print(ts.run())