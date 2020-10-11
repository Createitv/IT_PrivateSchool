def getPoker():
    item = ['红心', '草花', '黑桃', '方块']
    number = ['A', 2, 3, 4, 5, 6, 7, 8,'#', 9, 10, 'j', 'q', 'k']
    # for i in item:
    #     for j in number:
    all_list = list(zip(number, item))
    print(all_list)
getPoker()