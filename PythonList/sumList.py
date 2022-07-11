class List:
    list = [1,2,3,4,5,6,7,8,9,10]
#Sum List In Python
    def sumList(list):
        total_sum = 0
        for x in list:
            total_sum +=x
        return total_sum

    print(sumList(list))
