def BinarySearch(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)/2
        guess = list[mid]
        if guess == item:
            return(mid)
        if guess < item:
            low = mid + 1
        else:
            high = mid -1
    return(None)


def _main():
    print("Hello")
    mylist = [0,1,3,4,5,6,7,8,9]
    myitem = 3
    print(BinarySearch(mylist, myitem))

if __name__ == "__main__":
    _main()