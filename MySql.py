import mysql.connector as sqltor
from datetime import date

def get_data(roll, user, password):
    data = exc("select Roll, Name, " + today + " from attendence where roll=" + str(roll), user=user, password=password)
    return data

def addnewdate(user, password):
    global today
    c = exc("select * from attendence", get="colm", user=user, password=password)
    if c[-1] == today:
        pass
    else:
        query = str("Alter table attendence add " + today + " varchar(20)")
        print(query)
        exc(query, get="date", user=user, password=password)

def exc(query_, user, password, database="school", get="n"):
    x = query_
    mycon = sqltor.connect(user=user, host="localhost", passwd=password, database=database,
                           autocommit=True)  # Using autocommit for updating else it was'nt working
    query = str(x)
    cursor = mycon.cursor()
    cursor.execute(query)
    if get == "date":
        data = None
    elif get == "update" or get == 'exeonly':
        data = None
        print("query excuted", today)
    else:
        data = cursor.fetchall()
        print(data)
        print(query_)

    if get == "colm":
        data = [column[0] for column in cursor.description]
    mycon.close()
    return data

# ==========================================================================
today = str(date.today())
today = list(today)
d = ""
for a in range(len(today)):
    if today[a] == "-":
        today[a] = "_"
for a in range(len(today)):
    d = d + today[a]
today = d
# ==========================================================================

