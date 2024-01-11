import time
import datetime
import Route as r

def routeLocalSearch(loop, outputFile):
    startTime = time.process_time()
    minValue = float('+Inf')  # gia tri khoang cach nho nhat tim thay
    # 2 gia tri tuong ung voi khoang cach nho nhat hien tai!
    minPathList = None
    minStudentsDict = None
    print('Local search: {0} iterations'.format(loop), file=outputFile)
    for i in range(loop):
        globalPathList, globalStudentsDict = route.routeLocalSearch()
        if globalPathList == None or globalStudentsDict == None:
            i = i - 1
        distance = route.getDistance()
        if distance < minValue:
            print('Distance:', distance, file=outputFile)
            minValue = distance
            minPathList = globalPathList
            minStudentsDict = globalStudentsDict
            # print([minPathList, minStudentsDict], file=outputFile)
            print("--------------------", file=outputFile)
            outputFile.flush()  # dam bao du lieu duoc ghi vao tep ngay lap tuc
    endTime = time.process_time()
    print("Process Time: {}s".format(endTime - startTime), file=outputFile)
    outputFile.flush()
    return [minPathList, minStudentsDict]

def routeGRASP(loop, outputFile):
    startTime = time.process_time()
    minValue = float('+Inf')  # gia tri khoang cach nho nhat tim thay
    # 2 gia tri tuong ung voi khoang cach nho nhat hien tai!
    minPathList = None
    minStudentsDict = None
    print('GRASP: {0} iterations'.format(loop), file=outputFile)
    for i in range(loop):
        globalPathList, globalStudentsDict = route.routeGRASP(1)
        if globalPathList == None or globalStudentsDict == None:
            i = i - 1
        distance = route.getDistance()
        if distance < minValue:
            print('Distance:', distance, file=outputFile)
            minValue = distance
            minPathList = globalPathList
            minStudentsDict = globalStudentsDict
            # print([minPathList, minStudentsDict], file=outputFile)
            print("--------------------", file=outputFile)
            outputFile.flush()  # dam bao du lieu duoc ghi vao tep ngay lap tuc
    endTime = time.process_time()
    print("Process Time: {}s".format(endTime - startTime), file=outputFile)
    outputFile.flush()
    return [minPathList, minStudentsDict]

if __name__ == '__main__':
    loop = 100
    fn = 'sbr10.txt'
    fileName = '../instances/' + fn
    outputFile = open('../results/res-' + fn, 'a')
    route = r.Route(fileName)

    print('Route local search', end=' ', file=outputFile)
    print(datetime.datetime.now(), file=outputFile)
    routeLocalSearch(loop, outputFile)
    print("====================", file=outputFile)

    print('GRASP', end=' ', file=outputFile)
    print(datetime.datetime.now(), file=outputFile)
    routeGRASP(loop, outputFile)
    print("====================", file=outputFile)
    outputFile.close()
