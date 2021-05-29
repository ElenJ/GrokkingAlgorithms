def Sum_recursive(array):
    #formulate base case
    if array == []:
        return(0)
    else:
        return(array[0]+Sum_recursive(array[1:]))



def _main():
    myarray = [1,3,6] #sum=10
    print("Start program")
    print(Sum_recursive(myarray))
    print("End program")

if __name__ == "__main__":
    _main()