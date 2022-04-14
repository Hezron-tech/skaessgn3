import numpy as np
today = np.datetime('today','D')
print("Today: ", today)


yesterday = np.datetime64('today', 'D')
- np.timedelta64(1, 'D')
tomorrow = np.datetime64('today', 'D')
+ np.timedelta64(1, 'D')

print("Tomorrow: ", tomorrow)

