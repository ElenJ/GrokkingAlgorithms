def findSmallest(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    #print(smallest)
    return(smallest_index)

def SelectionSort(list):
    newArray = []
    for i in range(len(list)):
        smallest_index = findSmallest(list)
        newArray.append(list.pop(smallest_index))
    return(newArray)


def _main():
    mylist = [7,1,6,3,9,5,7,2]
    print('Hello, lerner!')
    print(findSmallest(mylist))
    print(SelectionSort(mylist))
    print("done")

if __name__ == "__main__":
    _main()