def find_min_value(input_list):
    min_index = 0
    for i in range(1, len(input_list)):
        if input_list[i] < input_list[min_index]:
            min_index = i
    return min_index


if __name__ == "__main__":
    lis1 = [5,6,2,1,8,7,0,1]
    for i in range(0,len(lis1)-1):
        min_index = find_min_value(lis1[i:])
        lis1[i], lis1[min_index+i] = lis1[min_index+i], lis1[i]
    print(lis1)