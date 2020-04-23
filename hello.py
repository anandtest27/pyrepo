def main(): 
    anand = [10, 20, 30, 40, 50]  # For array
    # x = bytes(anand)    # this is byte data type and it cant be changed 
    # print (type(x))
    # # x[3] = 100
    # anand[3] = 110
    # # print (x)
    # print (anand)
    x = bytearray(anand)  # This is byte array data type. The items inside can be changed
    x[3] = 25
    print (type(x) , " Value on 1st position is: " + str(x[3]))
    print(x)

if __name__ == "__main__":
    main()
