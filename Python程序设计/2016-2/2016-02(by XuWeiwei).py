def get_record(n):
    f1=open(n,"r")
    lst=f1.readlines()
    lst1=[]
    for i in lst:
        lst1.append(i.strip())
    f1.close()
    return lst1

def get_v(vehicle_lst):
    import re
    a=" ".join(vehicle_lst)
    b=re.findall(r"[A-Z]{2}-\d{3}-\d{3}",a)
    vehicle_set=set(b)
    return vehicle_set

def count_v(vehicle_lst, vehicle_set):
    dic={}
    for i in vehicle_set:
        if dic.get(i,0)==0:
            count = 0
            for j in vehicle_lst:
                if j.startswith(i):
                    count+=1
            dic[i]=count
    return dic

def times(lst):
    a=[int(i) for i in lst[0].split(":")]
    b=[int(i) for i in lst[1].split(":")]
    time1=3600*a[0]+60*a[1]+a[2]
    time2=3600*b[0]+60*b[1]+b[2]
    times=time2-time1
    return times

def count_t(vehicle_lst, vehicle_set):
    dic = {}
    for i in vehicle_set:
        if dic.get(i, 0) == 0:
            count = 0
            for j in vehicle_lst:
                if j.startswith(i):
                    import re
                    lst=re.findall(r"\d{2}:\d{2}:\d{2}",j)
                    count+=times(lst)
            dic[i]=count
    return dic

def write_to_file(vehicle_lst, fre_dict, inter_dict, n):
    f1=open(n,"w")
    f1.write("记录条数：{a:d}\n车辆数：{b:d}\n进校次数最多的五辆车（单位：次）:\n".format(a=len(vehicle_lst),b= len(get_v(vehicle_lst))))
    a=sorted(fre_dict.items(),key=lambda e:e[1],reverse=True)
    for i in range(5):
        f1.write(a[i][0]+","+str(a[i][1])+"\n")
    f1.write("累计停留时间最长的五辆车：（单位：秒）:\n")
    b=sorted(inter_dict.items(),key=lambda e:e[1],reverse=True)
    for i in range(5):
        f1.write(b[i][0]+","+str(b[i][1])+"\n")
    f1.close()
if __name__=="__main__":
    vehicle_lst = get_record("data.txt")  # 读文件，获取全部ETC记录，构成列表
    vehicle_set = get_v(vehicle_lst)  # 获取全部不同的ETC编号，构成集合
    fre_dict = count_v(vehicle_lst, vehicle_set)  # 构造车辆进出校园次数的字典
    inter_dict = count_t(vehicle_lst, vehicle_set)  # 构造车辆累计停留时间的字典
    write_to_file(vehicle_lst, fre_dict, inter_dict, "report.txt")  # 输出结果到文件中
