import os
import re

select_search = input('type in 1 to search interface information , or type in 2 to search log:\n')
#輸入1或2抓取不同的資料

log_dir = input('''
please type in the log dir full path:
ex:C:\\Users\\Ein Lin\\Desktop\\log_dir\\2021-12-23
''')
#輸入資料夾

search_keyword = input('''
please type in with statement keyword you want search:
ex: if selected 1 , used CRC or unknown protocol
ex: if selected 2 , used likely vlan mismatch or MACFLAP or anything you want search:
''')
#輸入關鍵字，不分大小寫

os.chdir(log_dir)

for i in os.listdir():
#使用迴圈讀取資料夾內所有檔案
    with open(i,'r') as log_obj:
    #依序開啟檔案
        print(i)
        #列出檔名
        information_data = []
        x = []
        #建立空值以利後續延伸寫入
        if select_search == '1':
            for j in log_obj.readlines():
                j = j.strip().split('\n')
                #等於前的i為自定義變數，等於後的i為讀取資料，strip為取消多餘enter，split為把換行分割並把此資料格式轉為list
                information_data.append(j)
                #使用剛剛空字串用append做延伸寫入(不覆寫)
            for k in range(len(information_data)):
            #使用len把資料顯示成長度
                if search_keyword.lower() in information_data[k][0].lower():
                #因上述把資料格式轉成長度，所以如果直接print(j)會變成數字，然後抓出語句有含關鍵字的字串，此處關鍵字為crc 或 unknown protocol drops
                    if '0' not in information_data[k][0]:
                    #分類出0以外的資料
                        x.append(k)
                        #用空字串append的資料做成index
            for y in x:
            #如上所述，x為list，可以用for的方式讀取
                z = y
                #使用一個變數等於y這個index
                while not (information_data[z][0].startswith('Vlan') or information_data[z][0].startswith('GigabitEthernet')):
                #interface 中有vlan，和giga所以使用while 用往回找的方式找到對應的interface
                    z = z - 1
                print(information_data[z][0])
                #因while not 在抓到關鍵字後會跳出迴圈，所以需在這print關鍵字
            print('\n')
        else:
            for j in log_obj.readlines():
                if bool(re.search(search_keyword,i,re.IGNORECASE)):
                #找尋logg 關鍵字，不分大小寫
                    print(j.strip())
            print('\n')
