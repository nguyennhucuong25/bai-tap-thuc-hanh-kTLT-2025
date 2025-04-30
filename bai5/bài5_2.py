
import datetime as dt 
format = '%Y-%m-%dT%H:%M:%S' 
t1 = dt.datetime.strptime('2005-1-20T8:49:52', format) 
print('Day ' + str(t1.day)) 
print('Month ' + str(t1.month)) 
print('Minute ' + str(t1.minute)) 
print('Second ' + str(t1.second)) 
# Define todays date and time 
t2 = dt.datetime.now() 
diff = t2 - t1 
print('chênh lệch bao nhiêu ngày? ' + str(diff.days))
print("nguyễn như cường")   
print("MSSV: 235752020710047") 