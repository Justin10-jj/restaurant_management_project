import datetime
def is_restaurant_open():
    now=datetime.datetime()
    current_time=now.time()
    current_day=now.weekday()
    weekday_hours=(datetime.time(9,0),datetime.time(22,0))
    weekend_hours=(datetime.time(10,0),datetime.time(23,0))

    if current_day<5:
        open_time,close_time=weekday_hours
    else:
        open_time,close_time=weekend_hours
    return open_time<=current_day<=close_time