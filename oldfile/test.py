import datetime
import time


def printer():
    print('hello')
    


def counter():
    current_year = datetime.date.today().year
    next_year = 2021

    while True:
        if current_year != next_year:
            print( current_year - next_year, end='\r')
        else:
            print('happy ')


# print(counter())
# x = datetime.date.today().year
# print(datetime.date.today().year)


































def timer():
    this_year = datetime.datetime.now().year
    new_year =  datetime.datetime(2022,1,1)

    delta = datetime.timedelta(microseconds=-0.0000005)
    soon = datetime.timedelta(seconds=10)

    while True:
        time_until = new_year -datetime.datetime.now()
        seconds_left = time_until.total_seconds()
        hours, remainder = divmod(seconds_left,3600)
        minute, seconds = divmod(remainder,60)

        if time_until < soon:
            if time_until < delta:
                print('Happy new year')
                break
            else:
                print(f'{int(seconds)}')

        else:
            print(f'{int(hours):02d}:{int(minute):02d}:{int(seconds):02d}', end='\r')
        time.sleep(1)

timer()
def countdown(args):
    while args:
        mins, secs = divmod(args, 60)
        time_format =  '{:02d} : {:02d}'.format(mins,secs)
        print(time_format, end='\r')
        time.sleep(1)
        args -= 1
    print('stop')

# countdown(10)
while True:
    current_year = datetime.datetime.now()
    next_year = datetime.datetime(2023,1,1,16, 26,5)

    if  current_year.minute == 30:
        print(next_year.minute)
        break
    
  
