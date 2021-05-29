def Item_Count(array):
    if array == []:
        return(0)
    else:
        return(1+Item_Count(array[1:]))

def _main():
    myarray = [1,2,3] # item count = 3
    print("Starting...")
    print(Item_Count(myarray))
    print("Finished...")

if __name__ == "__main__":
    _main()