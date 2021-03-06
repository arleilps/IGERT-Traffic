from datetime import datetime, date, time, timedelta
import statistics

#small traffic
#Speeds from traffic sensors
#vertices: 100
#snapshots: 8641
#sampling rate: 5 min.

small_traffic = {}
small_traffic["path"] = "data/small_traffic/"
small_traffic["num_snaps"]=8640

#Large traffic
#Speeds from traffic sensors
#vertices: 1923
#snapshots: 8641
#sampling rate: 5 min.

traffic = {}
traffic["path"] = "data/traffic/"
traffic["num_snaps"]=8640

def check_time_range_traffic(file_id, days, hours):
	"""
		Checks if file id matches a subset of (week)days and hours
	"""
	start_time = datetime.strptime("1/04/11 00:00", "%d/%m/%y %H:%M")
	file_time = start_time + timedelta(minutes=int(file_id)*5)
   
	check_day = False
    
	for d in days:
		if file_time.weekday() == d:
			check_day = True
			break
    
	if check_day is False:
		return False
    
	check_hour = False
    
	for h in hours:
		if file_time.hour == h:
			check_hour = True
			break
            
	return check_hour

