### COMPLETED AND CLEANED ####
# this project was made using no refrences, I am sure there are more efficient ways to do this in terms of runtime.->
# But given my current knowledge. 

def add_time(time, add_time, day=None):
  '''from a given start time and day(optional), add xx:yy AM/PM time. Gives back what time and day it will be'''
  given_t = [*time]
  plus_t = [*add_time]
  days_list = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    'Sunday'
  ]
  #collects proper indexes in both time and add_time
  if len(given_t) == 8:
    ghour = int(f'{given_t[0]}{given_t[1]}')
    gminutes = int(f'{given_t[3]}{given_t[4]}')
    gam_pm = (f'{given_t[6]}{given_t[7]}').lower()
  else:
    ghour = int(f'{given_t[0]}')
    gminutes = int(f'{given_t[2]}{given_t[3]}')
    gam_pm = (f'{given_t[5]}{given_t[6]}').lower()
  if len(plus_t) == 6:
    adhour = int(f'{plus_t[0]}{plus_t[1]}{plus_t[2]}')
    adminutes = int(f'{plus_t[4]}{plus_t[5]}')
  elif len(plus_t) == 5:
    adhour = int(f'{plus_t[0]}{plus_t[1]}')
    adminutes = int(f'{plus_t[3]}{plus_t[4]}')
  else:
    adhour = int(plus_t[0])
    adminutes = int(f'{plus_t[2]}{plus_t[3]}')
  fhour = int(f'{(ghour + adhour)}')
  fminutes = int(f'{(gminutes + adminutes)}')

  # deal with changing hour based on 59 min and above
  while fminutes >= 59:
    fminutes -= 60
    fhour += 1
  if fminutes <= 0:
    fminutes += 60
    fhour -= 1

  days_tick = 0
  halfday = 12
  #deals with finding days later and days_in_hour1 comes into play with the am/pm
  days_in_hour1 = (fhour / 24)
  days_tick = int(-(-days_in_hour1 // 1))
  loop_count =0
  if fhour < 48 and int(days_in_hour1) <= 1:
    if days_in_hour1 >= 1.5:
      days_tick = days_tick
    else:
      days_tick = ('next day')
  while fhour >= halfday:
    loop_count += 1
    if gam_pm == 'am':
      gam_pm = ('pm')
    else:
      gam_pm = 'am'
    fhour -= 12
    continue

  # properly sets 00:00 to 12:00
  if fhour == 0:
    fhour = 12

  # finds which day of the week the added time will lead to.
  if day:
    day = day.strip().title()
    given_day_pos = int(days_list.index(day))
    if type(days_tick) is int:
      x = int(given_day_pos + days_tick)
      while x > len(days_list):
        given_day_pos = 0
        x = int(((given_day_pos + days_tick) // 7) - 2)
      day = (days_list[x])
    if type(days_tick) is str:
      x = int(given_day_pos + 1)
      if int(days_in_hour1) < 1:
        x = 0
      while x >= len(days_list):
        given_day_pos = 0
        x = int(((given_day_pos + 1) // 7))
      day = (days_list[x])

  # this loop deals with resetting changes from noon+ back to the same day till midnight
  while day == None:
    if gam_pm == 'am' and loop_count == 1:
      break
    elif (days_in_hour1) >= 0.51 and loop_count == 1:
      return (f'{fhour}:{fminutes:02} {gam_pm.upper()}')
    break
    
  # returns time when a day is given and is end-time is later that 48 hour:
  if day and 2 > (days_in_hour1) >= 1.5: 
      return (f'{fhour}:{fminutes:02} {gam_pm.upper()}, {day} ({days_tick} days later)')
  # returns time when end-time is in the same day
  elif day and int(days_in_hour1) == 0:
      return (f'{fhour}:{fminutes:02} {gam_pm.upper()}, {day}')
    
  # returns time when day is specified and time is 24+ hours
  elif day  and int(days_in_hour1) <= 1:
      return (f'{fhour}:{fminutes:02} {gam_pm.upper()}, {day} ({days_tick})')

  # returns end-time that is past middnight but time is less than 48 hours
  if days_tick == ('next day') and (days_in_hour1) > 0.5:
      return (f'{fhour}:{fminutes:02} {gam_pm.upper()} ({days_tick})')
    
  #returns end-time when a day is given and time is  48+ hours
  if day:
      return (f'{fhour}:{fminutes:02} {gam_pm.upper()}, {day} ({days_tick} days later)')

  # returns time when am/pm change has occured while still being in the same day
  elif days_tick ==('next day'):
      return (f'{fhour}:{fminutes:02} {gam_pm.upper()}')

  # returns time when day is NOT specified and time duration is beyond 48+
  else:
      return (f'{fhour}:{fminutes:02} {gam_pm.upper()} ({days_tick} days later)')


####### below are my trial and error code scraps that ######

# def add_time(time, add_time, day=None):
#     given_t = [*time]
#     plus_t = [*add_time]
#     days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     #collects proper indexes in both time and add_time
#     if len(given_t) == 8: 
#         ghour = int(f'{given_t[0]}{given_t[1]}')
#         gminutes = int(f'{given_t[3]}{given_t[4]}')
#         gam_pm = (f'{given_t[6]}{given_t[7]}').lower()
#     else:
#         ghour = int(f'{given_t[0]}')
#         gminutes = int(f'{given_t[2]}{given_t[3]}')
#         gam_pm = (f'{given_t[5]}{given_t[6]}').lower()
#     if len(plus_t) == 6:
#         adhour = int(f'{plus_t[0]}{plus_t[1]}{plus_t[2]}')
#         adminutes = int(f'{plus_t[4]}{plus_t[5]}')
#     elif len(plus_t) == 5:
#         adhour = int(f'{plus_t[0]}{plus_t[1]}')
#         adminutes = int(f'{plus_t[3]}{plus_t[4]}')
#     else:
#         adhour = int(plus_t[0])
#         adminutes = int(f'{plus_t[2]}{plus_t[3]}')
#     fhour = int(f'{(ghour + adhour)}')
#     fminutes = int(f'{(gminutes + adminutes)}')

#     # deal with changing hour based on 59 min and above
#     while fminutes >= 59: 
#         fminutes -= 60
#         fhour += 1
#     if fminutes <= 0:
#         fminutes += 60
#         fhour -= 1
    
#     days_tick = 0
#     halfday = 12
#     #deals with finding days later and days_in_hour1 comes into play with the am/pm
#     days_in_hour1 = (fhour / 24)
#     days_tick = int(-(-days_in_hour1// 1)) 

#     # if fhour > 12 and gam_pm == 'PM':
#     #     if (fhour % 24) >= 1.0:
#     #         days_tick += 1
#     #         print(f'{days_tick}')
#     # if fhour >= 12:
#     #     fhour_div12 = (fhour / 24)
#     #     days_tick += int(fhour_div12)
#     #     print(f'days tick is{days_tick}')

#     #deals with changing am to pm depending on day change at 12am or every time the sum of the hours is ->
#     #-> equal to or greater than 12 hours.
#     loop_count= 0    
#     if fhour < 48 and int(days_in_hour1) <= 1:
#         if days_in_hour1 >= 1.5:
#             days_tick = days_tick
#         else:
#             days_tick = ('next day')
#     while fhour >= halfday:
#         loop_count += 1
#         if gam_pm == 'am':
#             gam_pm = ('pm')
#         else:
#             gam_pm = 'am'
#         fhour -= 12
#         continue
        
#         # if fhour >= halfday:
#         #     continue
#         # else:
#         #     break
#     # if days_in_hour1 <= 0.5 and gam_pm == 'AM':
#     #     gam_pm = ('pm')
#     if fhour == 0:
#         fhour = 12
    

#     # finds which day is given, adds how many days passed and gives that day of the week x days later
#     if day:
#         day = day.strip().title()
#         given_day_pos = int(days_list.index(day))
#         if type(days_tick) is int:
#             x = int(given_day_pos + days_tick) 
#             while x > len(days_list):
#                 given_day_pos = 0
#                 x = int(((given_day_pos + days_tick) // 7) - 2)  
#             day = (days_list[x])
#         if type(days_tick) is str:
#             x = int(given_day_pos + 1)
#             if int(days_in_hour1) < 1 :
#                 x = 0
#             while x >= len(days_list):
#                 given_day_pos = 0
#                 x = int(((given_day_pos + 1) // 7))    
#             day = (days_list[x])
        


#     # elif days_in_hour1 < 1:
#     #     print('here')
#     #     days_tick = ('same day')
#     # print(f'total fhour/24 = {days_tick}')
#     # if fhour < 12:
#     #     gam_pm = gam_pm
#     # elif fhour >= 12:
#     #     if gam_pm == 'AM':
#     #         gam_pm = ('PM')
#     #     elif gam_pm == 'PM':
#     #         gam_pm = ('AM')

#     #hpday = 24
#     # loop = 0
#     # total_hpday_loop = 0
#     # while fhour >= halfday:
#     #     fhour -= 12
#     #     #loop += 1
#     #     # total_hpday_loop += 12
#     #     continue
#     # if fhour == 0:
#     #     fhour = 12
#     # deals with changing AM - PM 
#     # print(f'loop is {loop}')
#     # if (loop % 2) == 0:
#     #     gam_pm = gam_pm
#     # elif (loop % 2) >= 1:####
#     #     print('here')
#     #     if gam_pm == 'AM':
#     #         gam_pm = ('PM')
#     #     elif gam_pm == 'PM':
#     #         gam_pm = ('AM')
#     # if loop == 1: 
#     #     gam_pm = gam_pm
#     #     # if gam_pm == 'AM':
#     #     #     gam_pm = ('AM')
#     #     # elif gam_pm == 'PM':
#     #     #     gam_pm = ('PM')
#     # elif loop == 2:
#     #     gam_pm = gam_pm
#     #     # if gam_pm == 'AM':
#     #     #     gam_pm = ('AM')
#     #     # elif gam_pm == 'PM':
#     #     #     gam_pm = ('PM')
    
#     # # deals with counting how many days later
#     # next_day_flag = False

#     # print(f'total hpday loop = {total_hpday_loop}')
#     # while total_hpday_loop >= 1.3:
#     #     if (total_hpday_loop < 48) and (total_hpday_loop > 24):
#     #         print('in if')
#     #         if gam_pm == 'AM':
#     #             print('in child if of first if')
#     #             total_hpday_loop -= 24 
#     #             days_tick += 1
#     #         else:
#     #             print('in child else of first if')
#     #             days_tick = ('next day')
#     #             next_day_flag = True
#     #             break
#     #     elif total_hpday_loop < halfday:
#     #             print('in elif')
#     #             days_tick = ('next day')
#     #             next_day_flag = True
#     #             break
#     #     # elif total_hpday_loop <= 24:
#     #     #     print('in tick if')
#     #     #     days_tick = ('next day')
#     #     #     next_day_flag = True
#     #     #     break
#     #     else:
#     #         print('in else')
#     #         total_hpday_loop -= 24 
#     #         days_tick += 1

#     # print(f'the day tick is {days_tick}')

#     # if loop == 0 or loop == 1:
#     #     return  printprint(f'The time is {fhour}:{fminutes:02} {gam_pm} ({days_tick})')
#     print(f'days_tick {days_tick}')
#     print(f'days in hour1 {days_in_hour1}')
#     print(f'{day}')
#     print(f'loop count is {loop_count}')
#     if day and 2 > (days_in_hour1) >= 1.5: 
#         return  print(f'{fhour}:{fminutes:02} {gam_pm.upper()}, {day} ({days_tick} days later)')
#     elif day and int(days_in_hour1) == 0:
#         return  print(f'{fhour}:{fminutes:02} {gam_pm.upper()}, {day}')
#     elif day  and int(days_in_hour1) <= 1:
#         return  print(f'{fhour}:{fminutes:02} {gam_pm.upper()}, {day} ({days_tick})')
#     while day == None:
#         if gam_pm == 'am' and loop_count == 1:
#             break
            
#         elif loop_count == 1 and days_in_hour1 >= 0.51:
#             return  print(f'{fhour}:{fminutes:02} {gam_pm.upper()}')
#         else:
#             break
#         # else:
#         #     return  print(f'{fhour}:{fminutes:02} {gam_pm.upper()} ({days_tick})')
#     if days_tick == ('next day') and (days_in_hour1) > 0.5:
#         return  print(f'{fhour}:{fminutes:02} {gam_pm.upper()} ({days_tick})')
#     elif day:
#         return  print(f'{fhour}:{fminutes:02} {gam_pm.upper()}, {day} ({days_tick} days later)')
#     else:
#         return  print(f'{fhour}:{fminutes:02} {gam_pm.upper()} ({days_tick} days later)')



# add_time("9:15 PM", "5:30")
