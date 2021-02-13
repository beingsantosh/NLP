from datetime import datetime, timedelta
import time
t1 = datetime.now()

time.sleep(3)

t = datetime.now()

print(str(t.year)+'_'+str(t.month)+'_'+str(t.day)+'_'+str(t.hour)+'_'+str(t.minute)+'_'+str(t.second))

print(timedelta(hours=1))