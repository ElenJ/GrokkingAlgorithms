def FindMax(array):
    #base case:
    if len(array) == 2:
        return(array[0] if array[0]>array[1] else array[1])
    sub_max = FindMax(array[1:])
    return(array[0] if array[0]>sub_max else sub_max)

def _main():
    myarray = [1,4,10,6,8] #max = 8
    print("Starting...")
    print(FindMax(myarray))
    print("Finishing")

if __name__ == "__main__":
    _main()