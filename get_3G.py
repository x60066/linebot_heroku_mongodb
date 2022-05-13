
import pygsheets
#存取token
gc = pygsheets.authorize(service_file='Google python.json')
#excel網址
sht = gc.open_by_url(
'https://docs.google.com/spreadsheets/d/1sWBdjt98vF_Bo5Tvs_Iji7jdJSnkrt7uDYy_VQs2vqo/edit#gid=1669047201'
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
        self.ran_4Id=''
        
        wks_list_3G=sht[0]
        
        #模式0搜尋 台名
        if ip == 0:
            #取得表1中的col4
            ran_name_list_3g=list(wks_list_3G.get_col(4))

        #模式1搜尋 台號
        elif ip == 1:
            ran_name_list_3g=list(wks_list_3G.get_col(3))
            
            
        try:
            self.ran_search_index=ran_name_list_3g.index(key_search)
            self.ran_search_index+=1
            self.ran_id=sht[0].cell((self.ran_search_index,3)).value
            self.SiteName=sht[0].cell((self.ran_search_index,4)).value
            self.wCoSite=sht[0].cell((self.ran_search_index,11)).value
            self.RFModule=sht[0].cell((self.ran_search_index,33)).value
            self.BTSIP=sht[0].cell((self.ran_search_index,36)).value
            self.ran_4Id=sht[0].cell((self.ran_search_index,17)).value
        except:
            self.ran_search_index=-1

        
                



