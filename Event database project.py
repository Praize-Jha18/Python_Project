import csv

import pandas as pd
import sqlite3
conn = sqlite3.connect("events.db")
cur = conn.cursor()

# cur.execute("Insert into quarter_events values ('Riding the wave','Book Launch', 'Private', 'January', 30, 2,'Evening','Martha','090345710972','Cancelled')")
# cur.execute("INSERT INTO quarter_events values ('Fighting Cancer together','Fund Raiser  Corporate', 'March' ,26 ,5 , 'Afternoon', 'Mildred', '08124468080', 'Complete')")
# cur.execute("INSERT INTO quarter_events values ('Biotech and its hazards ','Conference','Sponsored' ,'Janaury', 17 ,1,'Afternoon', 'Nathaniel', '07034541010','Complete')")
# cur.execute("INSERT INTO quarter_events values ('A New Dawn','Book Launch','Private','Febuary' ,10 ,3 ,'Morning', 'Danica', '08076789012','Cancelled')")
# cur.execute("INSERT INTO quarter_events values ('Tribute to KSA','Social Event/Gala Nite', 'Private','March',12, 6 ,'Evening','Kayode' '09148004505', 'Complete')")
# cur.execute("INSERT INTO quarter_events values ('Youths and Social Media', 'Social/Networking' ,'Sponsored','April' ,16, 6, 'Morning', 'Paul', '09023450505','Cancelled')")
# cur.execute("INSERT INTO quarter_events values ( 'Celebrating Daddy' ,'Birthday' ,'Private', 'April',20  ,4 ,'Evening', 'Nelson' ,'07058035657', 'Complete')")
# print("Information inserted successfully :)")

futuremonth = ['June', 'July', 'August', 'September', 'October', 'November', 'December']
futuremonthtuple = tuple(futuremonth)
cur.execute("Select * from quarter_events where Month in {}".format(futuremonthtuple))
csdata = cur.fetchall()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

column_names = ['Event_Name', 'Event_Type', 'Sub-Type', 'Month',
'Day_in_month', 'Hall','Time_slot', 'Username', 'UserPhone', 'Event_Status']

date = pd.DataFrame(csdata)

csvcol = open('CurrentEvents2.csv', 'w', newline='')
writer = csv.writer(csvcol)
writer.writerow(column_names)
writer.writerows(csdata)

conn.commit()
conn.close()
print(csdata)


