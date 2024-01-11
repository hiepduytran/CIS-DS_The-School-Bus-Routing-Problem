import time
import matplotlib.pyplot as plt
import Route as r

def routeLocalSearch(loop):
    startTime = time.process_time()
    minValue = float('+Inf')  # Gia tri khoang cach nho nhat tim thay
    minPathList = None
    minStudentsDict = None
    print('Local search: {0} iterations'.format(loop))
    for i in range(loop):
        globalPathList, globalStudentsDict = route.routeLocalSearch()
        if globalPathList == None or globalStudentsDict == None:
            i = i - 1
        distance = route.getDistance()
        if distance < minValue:
            print('Distance:', distance)
            minValue = distance
            minPathList = globalPathList
            minStudentsDict = globalStudentsDict
    endTime = time.process_time()
    print(endTime - startTime)
    return [minPathList, minStudentsDict]

def routeGRASP(loop):
    startTime = time.process_time()
    minValue = float('inf')  # Giá trị khoảng cách nhỏ nhất tìm thấy
    minPathList = None
    minStudentsDict = None
    print('GRASP: {0} iterations'.format(loop))
    for i in range(loop):
        route.routeGRASP(1)  
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
    loop = 20
    fn = 'sbr10.txt'
    fileName = '../instances/' + fn
    route = r.Route(fileName)

    # print('Route local search: ')
    # routeLocalSearch(loop)
    #
    # print('Route GRASP: ')
    # routeGRASP(loop)

    local_search_times = []
    local_search_distances = []  # Store distances for local search
    for _ in range(loop):
        start_time_local_search = time.process_time()
        minPathList_local_search, minStudentsDict_local_search = routeLocalSearch(100)
        end_time_local_search = time.process_time()
        execution_time_local_search = end_time_local_search - start_time_local_search
        local_search_times.append(execution_time_local_search)
        distance_local_search = route.getDistance()
        local_search_distances.append(distance_local_search)

    grasp_times = []
    grasp_distances = []  # Store distances for GRASP
    for _ in range(loop):
        start_time_grasp = time.process_time()
        minPathList_grasp, minStudentsDict_grasp = routeGRASP(100)
        end_time_grasp = time.process_time()
        execution_time_grasp = end_time_grasp - start_time_grasp
        grasp_times.append(execution_time_grasp)
        distance_grasp = route.getDistance()
        grasp_distances.append(distance_grasp)

    # Plot execution times
    x = range(1, loop + 1)
    plt.subplot(2, 1, 1)
    plt.plot(x, local_search_times, label='Route Local Search')
    plt.plot(x, grasp_times, label='Route GRASP')
    plt.xlabel('Run')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time Chart')
    plt.legend()

    # Plot distances
    plt.subplot(2, 1, 2)
    plt.plot(x, local_search_distances, label='Route Local Search')
    plt.plot(x, grasp_distances, label='Route GRASP')
    plt.xlabel('Run')
    plt.ylabel('Distance')
    plt.title('Distance Chart')
    plt.legend()

    plt.tight_layout()
    plt.show()


