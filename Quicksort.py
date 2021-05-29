def Quicksort(array):
    #BAse case
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return Quicksort(less) + [pivot] + Quicksort(greater)


def _main():
    myarray = [3,2,7,4,9,5,1]
    print("Hi")
    print(Quicksort(myarray))
    print("Done")

if __name__=="__main__":
    _main()