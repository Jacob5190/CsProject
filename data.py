import linecache
import time


def getList():
    file = open("save.txt", "r")
    datas = linecache.getlines("save.txt")
    file.close()
    return datas


def writeFile(string):
    file = open("save.txt", "w")
    file.writelines(string)
    file.close()


class data:
    def __init__(self, index, name, days, id):
        self.index = index
        self.name = name
        self.days = days
        self.id = id

    def getData(self):
        data = str(self.index) + "-" + self.name + "-" + str(self.days) + "-" + str(getDate()) + "-" + str(self.id) + "\n"
        return data


def getDate():
    date = int(time.time())
    return date


def writeData():
    datas = getList()
    name = input("name:")
    days = int(input("days:"))
    id = input("ID:")
    file = open("save.txt", "r")
    index = len(linecache.getlines("save.txt"))
    data_1 = data(index + 1, name, days, id)
    string = data_1.getData()
    datas.append(string)
    writeFile(datas)
    file.close()


def search(index):
    flag = False
    datas = getList()
    for i in range(0, len(datas)):
        ind = (datas[i].split("-"))[0]
        if int(ind) == index:
            flag = True
            return datas[i]
    if not flag:
        return None


def delete(index):
    datas = getList()
    for i in range(0, len(datas)):
        ind = (datas[i].split("-"))[0]
        if int(ind) == index:
            datas.pop(i)
            break
    writeFile(datas)


def chkExpire(date, days):
    datas = getList()
    expire = []
    currentDate = getDate()
    time = days * 86400
    for i in range(len(datas)):
        date = int(datas[i].split("-")[3])
        days = int(datas[i].split("-")[2])
        if date + time <= currentDate:
            expire.append(datas[i].split("-")[0])
    return expire


def chkID(id):
    flag = False
    datas = getList()
    for i in range(len(datas)):
        currentID = int(datas[i].split("-")[4])
        id = int(id)
        if currentID == id:
            flag = True
            break
    return flag
