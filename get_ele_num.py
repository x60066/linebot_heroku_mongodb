
import pygsheets
#存取token
gc = pygsheets.authorize(service_file='Google python.json')
#excel網址
sht = gc.open_by_url(
'https://docs.google.com/spreadsheets/d/1Y92LLK8D2Gm0fLVGoZ1oHdGvfn8frKcIMap8qGSttio/edit#gid=818526228'
)

class RAN:
    
    #定義
    def __init__(self,key_search) :
        self.key_search=key_search 

        self.ran_search_index=-1
        self.ran_id=''
        
        wks_list=sht[0]
        
        ran_name_list_3g=list(wks_list.get_col(2))
            
            
        try:
            self.ran_search_index=ran_name_list_3g.index(key_search)
            self.ran_search_index+=1
            self.ran_id=sht[0].cell((self.ran_search_index,11)).value + ' ' +sht[0].cell((self.ran_search_index,12)).value

        except:
            self.ran_search_index=-1

        
                



