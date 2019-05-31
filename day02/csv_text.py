import csv

with open('老师.csv','w') as f:
    #初始化写入对象
    writer = csv.writer(f)

    #对象的writerow()方法写入数据
    writer.writerow(['七龙珠','神龙'])
    writer.writerow(['赛亚人','悟空'])