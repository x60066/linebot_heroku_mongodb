
import pygsheets
#存取token
gc = pygsheets.authorize(service_file='Google python.json')
#excel網址
sht = gc.open_by_url(
'https://docs.google.com/spreadsheets/d/1kC0iU1NGvuF6cPA8uVkTIf3Rj-tltgbVZOd7XP9Cq0A/edit#gid=834260441'
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
        
        wks_list=sht[0]
        
        #模式0搜尋 台名
        if ip == 0:
            #取得表1中的col4
            ran_name_list_3g=list(wks_list.get_col(2))

        #模式1搜尋 台號
        elif ip == 1:
            ran_name_list_3g=list(wks_list.get_col(1))
            
            
        try:
            self.ran_search_index=ran_name_list_3g.index(key_search)
            self.ran_search_index+=1
            self.ran_id=sht[0].cell((self.ran_search_index,1)).value
            self.SiteName=sht[0].cell((self.ran_search_index,14)).value
            self.wCoSite=sht[0].cell((self.ran_search_index,16)).value
            self.RFModule=sht[0].cell((self.ran_search_index,22)).value
            self.BTSIP=sht[0].cell((self.ran_search_index,23)).value
        except:
            self.ran_search_index=-1

        
                



