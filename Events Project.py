# oldmonth = ['Jan', 'Feb', 'Mar', 'Apr']
# t = tuple(oldmonth)
# import sqlite3
# conn = sqlite3.connect("events.db")
# cur = conn.cursor()
# cur.execute("DELETE FROM quarter_events WHERE Month = 'Jan'")
# cur.execute("DELETE FROM quarter_events WHERE Month = 'Feb'")
# cur.execute("DELETE FROM quarter_events WHERE Month = 'Mar'")
# cur.execute("DELETE FROM quarter_events WHERE Month = 'Apr'")
#
# # cur.execute("UPDATE quarter_events SET Month = 'August' where Username = 'Sandra'")
# conn.commit()
# conn.close()
# input()
import sqlite3
import pandas as pd
for i in range(6):

      statusforchoice = False
      userchoice1 = ""
      while statusforchoice == False:
            print("Welcome to D'Atrium Event Booking Co-opreation :)")
            print("Here's the current state of our database: ")
            conn = sqlite3.connect("events.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM quarter_events ")
            listofavalabledays = cur.fetchall()
            # import pandas as pd

            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            pd.set_option('display.max_colwidth', None)
            listofavalabledays = pd.DataFrame(listofavalabledays)
            listofavalabledays.columns = ['Event_Name', 'Event_Type', 'Sub-Type', 'Month', 'Day_in_month', 'Hall',
                                          'Time_slot', 'Username', 'UserPhone', 'Event_Status']

            conn.commit()
            conn.close()
            print(listofavalabledays)
            print("\n")
            print("Here's a list of operations we cover:\n(a) Book an Event \t(b) Filter your Event by time slot \t(c) "
                  "Reshedule your Event ")
            userchoice1 = str(input("Select an action menu :) "))
            if userchoice1 == "a" or userchoice1 == 'A':
                  print("Welcome to a booking session with D'Atrium Hall :)")
                  print("You should pick a date not listed here \nNote: The date you should select must be greater than today's date :) ")

                  newBookingEventName = ""
                  while newBookingEventName == "":
                        newBookingEventName = input("Enter your event name: ").strip().title()

                        if newBookingEventName  == "":
                              print("Event name cant be null")

                  NewEventType = ""
                  while NewEventType == "":
                        NewEventType = str(input("Enter the type of event you're booking: ")).strip().title()
                        if NewEventType == "":
                              print("Event type can't be null")
                  newsubType = ""
                  while newsubType == "":
                        newsubType = str(input("Enter the sub-type of your event: ")).strip().title()
                        if newsubType == "":
                              print("Sub-type can't be left null")
                  status = ''

                  while status == '':
                        futuremonth = ['June', 'July', 'August', 'September', 'October', 'November', 'December']
                        newEventmonth = ""
                        while newEventmonth not in futuremonth:
                              newEventmonth = str(input("Enter the month of your event: ")).strip().title()
                              if newEventmonth ==  "":
                                    print("The event month cannot be null")
                              elif newEventmonth not in futuremonth :
                                    print("Month selected is invalid")

                        err = ""
                        newdayInMonth = int()
                        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                   21, 22, 23, 24, 25, 26.27, 28, 29, 30, 31]
                        while newdayInMonth not in numbers:
                              try:
                                    newdayInMonth = newdayInMonth not in  numbers
                                    newdayInMonth = int(input("Enter a day of the month for your event:  "))
                                    if newdayInMonth <= 0:
                                          print("invalid date")

                              except ValueError:
                                    print("Wrong value entered :(")
                                    newdayInMonth = int()
                              except newdayInMonth == int():
                                    print("Date cannot be null")
                              except TypeError:
                                    print("You enter in a wrong data type")
                              except newdayInMonth <= 0:
                                    print("Invalid date")

                              else:
                                    status = ""
                                    while status == "":
                                          conn = sqlite3.connect("events.db")
                                          cur = conn.cursor()
                                          cur.execute(
                                                f"Select * from quarter_events WHERE Month = '{newEventmonth}' AND Day_in_month == '{newdayInMonth}'")
                                          datecheck = cur.fetchall()
                                          conn.commit()
                                          conn.close()
                                          pastMonthlist = ['January', 'February', 'March', 'April', 'May']
                                          futuremonth = ['June', 'July', 'August', 'September', 'October', 'November',
                                                         'December']
                                          days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31,
                                                  'June': 30,
                                                  'July': 31, 'August': 31, 'September': 30, 'October': 31,
                                                  'November': 30,
                                                  'December': 31}
                                          # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                          #            21, 22, 23, 24, 25, 26,27, 28, 29, 30, 31]
                                          if datecheck == [] and newEventmonth not in pastMonthlist and newEventmonth in futuremonth and newdayInMonth <= \
                                                  days[newEventmonth]:

                                                status = 'Pending'

                                                break
                                          elif newdayInMonth > days[newEventmonth] :

                                                print('Please select a valid date: ')
                                                newdayInMonth = int()
                                          else:
                                                print("Date selected has been chosen by another user")
                                                newdayInMonth = int()
                              finally:
                                    pass
                        # print(newdayInMonth)
                        # conn = sqlite3.connect("events.db")
                        # cur = conn.cursor()
                        # cur.execute(
                        #       f"Select * from quarter_events WHERE Month = '{newEventmonth}' AND Day_in_month == '{newdayInMonth}'")
                        # datecheck = cur.fetchall()
                        # conn.commit()
                        # conn.close()
                        # pastMonthlist = ['January', 'February', 'March', 'April', 'May']
                        # futuremonth = ['June', 'July', 'August', 'September', 'October', 'November', 'December']
                        # days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
                        #  'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
                        # numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26.27,28,29,30,31]
                        # if datecheck == [] and newEventmonth not in pastMonthlist and newEventmonth in futuremonth and newdayInMonth <= days[newEventmonth ] :
                        #
                        #      status = 'Pending'
                        #      pass
                        # else:
                        #       print("Date selected has been chosen by another user")
                        #       print('Please select a valid date: ')
                  # print(status)
                  from random import randint

                  bookingHall = randint(0,6)
                  # print(bookingHall)
                  bookingTimeSlot = ''
                  timeformat = ['Morning', 'Afternoon', 'Evening']
                  states = False
                  while bookingTimeSlot not in timeformat:
                        bookingTimeSlot = str(input("Enter a time slot for the event: ")).title().strip()
                        if bookingTimeSlot in timeformat:
                              states = True

                        else:
                              print("Enter a valid time slot like (morning), (afternoon),(evening)")
                  bookingUsername = ""
                  while bookingUsername == "":
                        bookingUsername = str(input("Enter your user name: ")).strip().title()
                        if bookingUsername == "":
                              print("Username cannot be null")
                  bookingUserphone = ""
                  while bookingUserphone == "":
                        bookingUserphone = str(input("Enter your phone number: ")).strip()
                        if bookingUserphone == "":
                              print("Phone number cannot be null")
                  conn = sqlite3.connect("events.db")
                  cur = conn.cursor()
                  cur.execute(f"INSERT INTO quarter_events VALUES ('{newBookingEventName}', '{NewEventType}', '{newsubType}', '{newEventmonth}', '{newdayInMonth}', '{bookingHall}',"
                              f" '{bookingTimeSlot}', '{bookingUsername}', '{bookingUserphone}', '{status}') ")
                  conn.commit()
                  conn.close()
                  print("Congratulations your booking was successful :)")



            elif userchoice1 == "b" or userchoice1  == "B":
                  print("What Event time slot would you like to see:\n (a) Morning\t (b) Afternoon\t (c) Evening")

                  filteroption = ""
                  choicelist = ['a','A','B','b','c','C', 'morning', 'afternoon','evening']
                  while filteroption not in choicelist:
                        filteroption = str(input("Enter a choice: ")).lower().strip()
                        if filteroption == "a" or filteroption == "A" or filteroption == 'morning':
                              conn = sqlite3.connect("events.db")
                              cur = conn.cursor()
                              cur.execute("SELECT * FROM quarter_events WHERE  Time_Slot = 'Morning'")
                              timeslotMorning = cur.fetchall()
                              import pandas as pd
                              pd.set_option('display.max_rows', None)
                              pd.set_option('display.max_columns', None)
                              pd.set_option('display.width', None)
                              pd.set_option('display.max_colwidth', None)
                              daystable = pd.DataFrame(timeslotMorning)
                              daystable.columns = ['Event_Name', 'Event_Type', 'Sub-Type', 'Month', 'Day_in_month', 'Hall',
                                                   'Time_slot', 'Username', 'UserPhone', 'Event_Status']

                              conn.commit()
                              conn.close()

                              if timeslotMorning == [ ]:
                                    print("There no available slot for morning")
                              else:
                                    print(daystable)
                        elif filteroption == "b" or filteroption == "B" or filteroption == 'afternoon':
                              conn = sqlite3.connect("events.db")
                              cur = conn.cursor()
                              cur.execute("SELECT * FROM quarter_events WHERE Time_Slot = 'Afternoon'")
                              timeslotAfternoon = cur.fetchall()
                              import pandas as pd

                              pd.set_option('display.max_rows', None)
                              pd.set_option('display.max_columns', None)
                              pd.set_option('display.width', None)
                              pd.set_option('display.max_colwidth', None)
                              daystable2 = pd.DataFrame(timeslotAfternoon)
                              daystable2.columns = ['Event_Name', 'Event_Type', 'Sub-Type', 'Month', 'Day_in_month', 'Hall',
                                                   'Time_slot', 'Username', 'UserPhone', 'Event_Status']
                              conn.commit()
                              conn.close()

                              if timeslotAfternoon == [ ]:
                                    print("There's no available slot for Afternoon")
                              else:
                                    print(daystable2)
                        elif filteroption == "c" or filteroption == "C" or filteroption == 'evening':
                              conn = sqlite3.connect("events.db")
                              cur = conn.cursor()
                              cur.execute("SELECT * FROM quarter_events WHERE  Time_Slot = 'Evening'")
                              timeslotEvening = cur.fetchall()
                              import pandas as pd

                              pd.set_option('display.max_rows', None)
                              pd.set_option('display.max_columns', None)
                              pd.set_option('display.width', None)
                              pd.set_option('display.max_colwidth', None)
                              daystable3 = pd.DataFrame(timeslotEvening)
                              daystable3.columns = ['Event_Name', 'Event_Type', 'Sub-Type', 'Month', 'Day_in_month', 'Hall',
                                                    'Time_slot', 'Username', 'UserPhone', 'Event_Status']
                              conn.commit()
                              conn.close()
                              if timeslotEvening == [ ]:
                                    print("There's no available slot for Evening")
                              else:
                                    print(daystable3)
                        else:
                              print("invalid option chosen :(")



            elif userchoice1 == "c" or userchoice1 == "C":
                  print("Welcome to the Re-schedule section :) ")
                  conn = sqlite3.connect("events.db")
                  cur = conn.cursor()
                  cur.execute("Select Username From quarter_events WHERE Event_Status = 'Pending'")
                  nameslist1 = [i[0] for i in cur.fetchall()]
                  cur.execute("Select * From quarter_events WHERE Event_Status = 'Pending'")
                  nameslist = cur.fetchall()
                  import pandas as pd

                  pd.set_option('display.max_rows', None)
                  pd.set_option('display.max_columns', None)
                  pd.set_option('display.width', None)
                  pd.set_option('display.max_colwidth', None)
                  nameslist = pd.DataFrame(nameslist)
                  nameslist.columns = ['Event_Name', 'Event_Type', 'Sub-Type', 'Month', 'Day_in_month', 'Hall',
                                                'Time_slot', 'Username', 'UserPhone', 'Event_Status']
                  conn.commit()
                  conn.close()
                  print(nameslist)
                  username = ""
                  while username not in nameslist1:
                        username = str(input("Enter your UserName used to book an event: ")).strip().title()
                        if username in nameslist1:
                              status3 = ""
                              while status3 == "":
                                    conn = sqlite3.connect("events.db")
                                    cur = conn.cursor()
                                    cur.execute(f"Select * from quarter_events where Username = '{username}'")
                                    name = cur.fetchall()
                                    import pandas as pd

                                    pd.set_option('display.max_rows', None)
                                    pd.set_option('display.max_columns', None)
                                    pd.set_option('display.width', None)
                                    pd.set_option('display.max_colwidth', None)
                                    names = pd.DataFrame(name)
                                    names.columns = ['Event_Name', 'Event_Type', 'Sub-Type', 'Month',
                                                         'Day_in_month', 'Hall',
                                                         'Time_slot', 'Username', 'UserPhone', 'Event_Status']
                                    conn.commit()
                                    conn.close()
                                    print(names)
                                    print("Would you like to choose a new date to reschedule your event?")
                                    print("(a) YES or (b) No")
                                    choice = str(input("Select an action menu :)"))
                                    if choice == 'a' or choice =='A':
                                          newMonth = ""
                                          bookedMonths = ['January', 'Febuary', 'March', 'April', 'May']
                                          futuremonth2 = ['June', 'July', 'August', 'September', 'October', 'November',
                                                          'December']
                                          while newMonth not in futuremonth2 :
                                                newMonth = str(input("Select a month you'll like to re-schedule your event: ")).strip().title()
                                                if newMonth == "":
                                                      print("cannot be null")
                                                elif newMonth not in futuremonth2:
                                                      print("invalid month selected ")
                                                elif newMonth in bookedMonths:
                                                      print("Booking process for this month has being closed temporaly")
                                          newdate = int()
                                          numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                     20,
                                                     21, 22, 23, 24, 25, 26.27, 28, 29, 30, 31]
                                          while newdate not in numbers:
                                                try:
                                                      newdate = newdate not in numbers
                                                      newdate = int(
                                                            input("Enter a day of the month for your event:  "))
                                                      if newdate <= 0:
                                                            print("invalid date")

                                                except ValueError:
                                                      print("Wrong value entered :(")
                                                      newdate = int()

                                                except TypeError:
                                                      print("You enter in a wrong data type")
                                                except newdate <= 0:
                                                      print("Invalid date")

                                                else:
                                                      status = ""
                                                      while status == "":
                                                            conn = sqlite3.connect("events.db")
                                                            cur = conn.cursor()
                                                            cur.execute(
                                                                  f"Select * from quarter_events WHERE Month = '{newMonth}' AND Day_in_month == '{newdate}'")
                                                            datecheck = cur.fetchall()
                                                            conn.commit()
                                                            conn.close()
                                                            pastMonthlist = ['January', 'February', 'March', 'April',
                                                                             'May']
                                                            futuremonth = ['June', 'July', 'August', 'September',
                                                                           'October', 'November',
                                                                           'December']
                                                            days = {'January': 31, 'February': 28, 'March': 31,
                                                                    'April': 30, 'May': 31,
                                                                    'June': 30,
                                                                    'July': 31, 'August': 31, 'September': 30,
                                                                    'October': 31,
                                                                    'November': 30,
                                                                    'December': 31}
                                                            # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                                            #            21, 22, 23, 24, 25, 26,27, 28, 29, 30, 31]
                                                            if datecheck == [] and newMonth not in pastMonthlist and newMonth in futuremonth and newdate <= \
                                                                    days[newMonth]:

                                                                  status = 'Pending'

                                                                  break
                                                            elif newdate > days[newMonth]:

                                                                  print('Please select a valid date: ')
                                                                  newdate = int()
                                                            else:
                                                                  print("Date selected has been chosen by another user")
                                                                  newdate = int()
                                                finally:
                                                      pass

                                          print("Would you like to change your time slot? \n(a) Yes (b) No")
                                          choicetime = ""
                                          while choicetime == "":
                                                choicetime = input("Enter your answer: ").strip()
                                                if choicetime == "a" or choicetime == "A":
                                                      time2 = False
                                                      timeslotR = ""
                                                      timeformat2 = ['Morning', 'Afternoon', 'Evening']
                                                      while timeslotR not in timeformat2:
                                                            timeslotR = str(input("Choose a time slot: ")).title().strip()
                                                            if timeslotR == "":
                                                                  print("Time slot cannot be null")
                                                            if timeslotR not in timeformat2:
                                                                  print("Invalid time slot :(")
                                                            else:
                                                                  time2 = True

                                                      import sqlite3

                                                      conn = sqlite3.connect("events.db")
                                                      cur = conn.cursor()
                                                      cur.execute(
                                                            f"UPDATE quarter_events SET Day_in_month = '{newdate}' WHERE Username = '{username}'")
                                                      cur.execute(
                                                            f"UPDATE quarter_events SET Month = '{newMonth}' WHERE Username = '{username}'")
                                                      cur.execute(
                                                            f"UPDATE quarter_events SET Time_slot = '{timeslotR}' WHERE Username = '{username}'")
                                                      conn.commit()
                                                      conn.close()
                                                      print("Information updated successfully")
                                                elif choicetime == "b" or choicetime =="B":

                                                      import sqlite3

                                                      conn = sqlite3.connect("events.db")
                                                      cur = conn.cursor()
                                                      cur.execute(
                                                            f"UPDATE quarter_events SET Day_in_month = '{newdate}' WHERE Username = '{username}'")
                                                      cur.execute(
                                                            f"UPDATE quarter_events SET Month = '{newMonth}' WHERE Username = '{username}'")
                                                      conn.commit()
                                                      conn.close()
                                                      print("Information updated successfully :)")

                                    elif choice == "b" or choice == "B":
                                          time = ""
                                          timeformat2 = ['Morning', 'Afternoon', 'Evening']
                                          while time not in timeformat2:
                                                time = str(input("Enter a new time slot")).strip().title()
                                                if time == "":
                                                      print("Time slot cannot be null")
                                                elif time not in timeformat2:
                                                      print("Enter a valid time slot like (morning), (afternoon),(evening)")

                                          conn = sqlite3.connect("events.db")
                                          cur = conn.cursor()
                                          cur.execute(f"UPDATE quarter_events SET Time_slot = '{time}' WHERE Username = '{username}'")
                                          conn.commit()
                                          conn.close()
                                          print("Information updated successfully :)")
                                          status3 = "Pending"
                                    else:
                                          print("Invalid request")
                                          choicetime = ""



                              # else:
                              #       print("month selected is unavailable")


                        else:
                              print("Invalid name entered :(")
            else:
                  print("Unknown action selected :( \nPlease choose a valid option")
                  statusforchoice = False


# import sqlite3
# conn = sqlite3.connect("events.db")
# cur = conn.cursor()
# cur.execute("Delete from quarter_events where month = 'Jan'")
# cur.execute("Delete from quarter_events where month = 'Feb'")
# cur.execute("Delete from quarter_events where month = 'Mar'")
# cur.execute("Delete from quarter_events where month = 'Apr'")
# conn.commit()
# conn.close()


# import sqlite3
# conn = sqlite3.connect("events.db")
# cur = conn.cursor()
# cur.execute("Delete from quarter_events where Username = 'gf'")
# conn.commit()
# conn.close()