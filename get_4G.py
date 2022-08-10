import difflib
import pygsheets

#地址轉換
from geopy.geocoders import Nominatim

import xlrd
import pandas

#存取token
gc = pygsheets.authorize(service_file='Google python.json')
#excel網址
sht = gc.open_by_url(
'https://docs.google.com/spreadsheets/d/1WlBoMCOuSe1n026LIsJcBJrFn2FrTVtVaEWBGERziwM/edit#gid=1865579787'
)

class RAN:
    
    #定義+搜尋模式 self,搜尋字,搜尋模式0=中文 1=數字
    def __init__(self,key_search,ip) :
        self.key_search=key_search 

        self.ran_search_index=-1
        self.ran_id=''
        self.SiteName=''
        self.wCoSite=''
        self.RFModule=''
        self.BTSIP=''
        self.GPSE=''
        self.GPSS=''
        self.ran_PCI=''
        self.ran_5Id=''    
        self.XRAN='' 
        self.TRS='' 
        
        wks_list=sht[0]
        trs_list=sht[1]
        
        geolocation = Nominatim(user_agent="geotest")


        
        #模式0搜尋 台名
        if ip == 0:
            #取得表1中的col4
            ran_name_list_3g=list(wks_list.get_col(2))

        #模式1搜尋 台號
        elif ip == 1:
            ran_name_list_3g=list(wks_list.get_col(1))
            trs_list_check=list(trs_list.get_col(1))
            
            
            
        try:
            self.ran_search_index=ran_name_list_3g.index(key_search)
            self.ran_search_index+=1
            #id A
            self.ran_id=sht[0].cell((self.ran_search_index,1)).value
            #lnBtsIdLL_NameChs L
            self.SiteName=sht[0].cell((self.ran_search_index,12)).value
            #Co-Site M
            self.wCoSite=sht[0].cell((self.ran_search_index,13)).value
            #RF_Module AG
            self.RFModule=sht[0].cell((self.ran_search_index,33)).value
            #IP address AK
            self.BTSIP=sht[0].cell((self.ran_search_index,37)).value
            #insecPCI W
            self.ran_PCI=sht[0].cell((self.ran_search_index,23)).value
            #nrBtsId Q
            self.ran_5Id=sht[0].cell((self.ran_search_index,17)).value  
                      
            location = geolocation.reverse("24.423 120.86642")
            print(location.address)
            
            #LON
            self.GPSS=sht[0].cell((self.ran_search_index,52)).value  +' ' +sht[0].cell((self.ran_search_index,53)).value   
            location1=geolocation.reverse(str(self.GPSS))
            
            str1=(str(location1.address)).split(',')
            k1 = int(len(str1))-4
            s1=''
            while k1 >= 0:
                s1+=str1[k1]
                k1 -= 1     
                
            self.GPSS=self.GPSS+'\n'+s1
            
            #LAT
            self.GPSE=  sht[0].cell((self.ran_search_index,54)).value  +' ' +sht[0].cell((self.ran_search_index,55)).value   
            location2=geolocation.reverse(str(self.GPSE))
            
            str2=(str(location2.address)).split(',')
            k2 = int(len(str2))-4
            s2=''
            while k2 >= 0:
                s2+=str2[k2]
                k2 -= 1           
            
            self.GPSE=self.GPSE+'\n'+s2       
            #RANtype AU
            self.XRAN=sht[0].cell((self.ran_search_index,47)).value
            
            
            print("Columns1")
            df = pandas.read_excel('linebot_heroku_mongodb/20220805_LTE_CoBTS_CHT.xlsx')
            print("Columns2")
            print(df.columns)


            
        except:
            self.ran_search_index=-1
        
        # try:    
        #     res = difflib.get_close_matches(key_search+'L0',trs_list_check,10,cutoff=0.85)
        #     print (res)
            
        #     for trs_search in res:
        #         a=trs_list_check.index(trs_search)+1
        #         self.TRS+=sht[1].cell((a,1)).value+' '+sht[1].cell((a,9)).value +'\n'
        # except:
        #     self.TRS=''
        

        
                



