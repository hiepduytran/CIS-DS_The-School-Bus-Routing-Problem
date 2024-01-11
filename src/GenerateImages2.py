import Route as r
import matplotlib.pyplot as plt
import time

###! settings size of points

def plotStops(stops):
    plt.scatter(stops[0][0], stops[0][1], marker='o', s = 50, color='red',
                edgecolor='xkcd:dark grey')
    for keyStop, valueStop in list(stops.items())[1:]:
        plt.scatter(valueStop[0], valueStop[1], marker='.', s = 40, color='black')


def plotStudents(students):
    for keyStudent, valueStudent in students.items():
        plt.scatter(valueStudent[0], valueStudent[1], marker='.', s = 40, color='blue')


def plotStudentPotentialAssignments(studentNearStops):
    for key, value in studentNearStops.items():
        studentX, studentY = students[key]
        for i in value:
            stopX, stopY = stops[i]
            plt.plot([studentX, stopX], [studentY, stopY], 'k:', lw=0.2)  # Ve duong manh 'k' co do day la 1.5


# def routeLocalSearch(loop):
#     startTime = time.process_time()
#     minValue = float('+Inf')  # gia tri khoang cach nho nhat tim thay
#     # 2 gia tri tuong ung voi khoang cach nho nhat hien tai!
#     minPathList = None
#     minStudentsDict = None
#     print('Local search: {0} iterations'.format(loop))
#     for i in range(loop):
#         globalPathList, globalStudentsDict = route.routeLocalSearch()
#         if globalPathList == None or globalStudentsDict == None:
#             i = i - 1
#         distance = route.getDistance()
#         if distance < minValue:
#             print('Distance:', distance)
#             minValue = distance
#             minPathList = globalPathList
#             minStudentsDict = globalStudentsDict
#     endTime = time.process_time()
#     print(endTime - startTime)
#     return [minPathList, minStudentsDict]

def routeGRASP(loop):
    startTime = time.process_time()
    minValue = float('inf')  # Giá trị khoảng cách nhỏ nhất tìm thấy
    minPathList = None
    minStudentsDict = None
    print('GRASP: {0} iterations'.format(loop))
    for i in range(loop):
        route.routeGRASP(1)  # Gọi phương thức routeGRASP với 1 lần lặp trong mỗi vòng lặp
        distance = route.getDistance()
        if distance < minValue:
            print('Distance:', distance)
            minValue = distance
            minPathList = route.globalPathList
            minStudentsDict = route.globalStudentsDict
    endTime = time.process_time()
    print(endTime - startTime)
    return [minPathList, minStudentsDict]

if __name__ == '__main__':
    fileName = '../instances/sbr10.txt'
    route = r.Route(fileName)

    stops = route.getStops()
    students = route.getStudents()
    maximumWalk = route.getMaximumWalk()
    capacity = route.getCapacity()
    studentNearStops = route.getStudentNearStops()

    # print('Route local search', end=' ')
    # paths, studentAssignments = routeLocalSearch(10)

    print('GRASP:', end=' ')
    paths, studentAssignments = routeGRASP(100)

    # plotStudents(students)
    # plotStops(stops)
    #
    # plt.savefig('../images/sbr10-stops.jpg', dpi = 250)

    # plotStudentPotentialAssignments(studentNearStops)

    # plt.savefig('../images/sbr10-potential-stops.jpg', dpi = 250)

    # khoi tao lai de xoa cac tuyen duong tiem nang
    plotStudents(students)
    plotStops(stops)

    for key, value in studentAssignments.items():
        studentX, studentY = students[key]
        stopX, stopY = stops[value]
        plt.plot([studentX, stopX], [studentY, stopY], 'red', lw=0.5)

    for path in paths:
        for i in range(len(path) + 1):
            if i == 0:
                stopX, stopY = stops[path[0]]
                plt.plot([stops[0][0], stopX], [stops[0][1], stopY], 'green', lw=2)
            elif i == len(path):
                stopX, stopY = stops[path[i - 1]]
                plt.plot([stops[0][0], stopX], [stops[0][1], stopY], 'green', lw=2)
            elif i < len(path):
                firstX, firstY = stops[path[i]]
                secondX, secondY = stops[path[i - 1]]
                plt.plot([firstX, secondX], [firstY, secondY], 'green', lw=2)

    plt.savefig('../images/sbr10-route-by-GRASP.jpg', dpi = 250)