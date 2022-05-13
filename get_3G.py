import pygsheets
key_search=''

gc = pygsheets.authorize(service_file='Google python.json')

sheet_3G = gc.open_by_url(
'https://docs.google.com/spreadsheets/d/1sWBdjt98vF_Bo5Tvs_Iji7jdJSnkrt7uDYy_VQs2vqo/edit#gid=1669047201'
)

#搜尋
def set_key_search(key):    
    global key_search
    key_search=key
    

def get_index_by_name(key_search):
    #取得表1
    wks_list_3G=sheet_3G[0]
    #取得表1中的col4
    ran_name_list_3g=list(wks_list_3G.get_col(4))
    try:
        #搜尋col4相符的
        ran_search_index_3g=ran_name_list_3g.index(key_search)
        ran_search_index_3g+=1
        ran_3g_id=sheet_3G[0].cell((ran_search_index_3g,3)).value
    except:
        ran_search_index_3g=-1



        
