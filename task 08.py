# Converts a number into hours and minutes

  
def conv(number):
    minutes = number % 60
    #print("minute",minutes)
    hour = number // 60
    #print("hour",hour)
    if hour == 1:
        desc_hour=" hour"
    else:
        desc_hour=" hours"
    if minutes == 1:
        desc_minutes=" minute"
    else:
        desc_minutes=" minutes"  
     
    print(hour, desc_hour,",", minutes, desc_minutes )
      
conv(62)