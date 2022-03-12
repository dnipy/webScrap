import requests
from bs4 import BeautifulSoup
import json
import time


urlll = 'https://www.chibekhoonam.net/shop/?orderby=date&flt_pa_paye_tahsili[]=107&flt_pa_paye_tahsili[]=108&flt_pa_paye_tahsili[]=109&flt_pa_paye_tahsili[]=104&flt_pa_paye_tahsili[]=105&flt_pa_paye_tahsili[]=106&flt_pa_paye_tahsili[]=53&flt_pa_paye_tahsili[]=54&flt_pa_paye_tahsili[]=55'


header = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36As:'
}




ProductsLink=[]

for x in range(2,150):# (2,150) + urlll #
    urll2 = f'https://www.chibekhoonam.net/shop/page/{x}/?orderby=date&flt_pa_paye_tahsili[0]=107&flt_pa_paye_tahsili[1]=108&flt_pa_paye_tahsili[2]=109&flt_pa_paye_tahsili[3]=104&flt_pa_paye_tahsili[4]=105&flt_pa_paye_tahsili[5]=106&flt_pa_paye_tahsili[6]=53&flt_pa_paye_tahsili[7]=54&flt_pa_paye_tahsili[8]=55'
    req = requests.get(urll2,header)
    baseContent=BeautifulSoup(req.content,'lxml')

    ProductsList= baseContent.findAll('article',class_='standcat')
    

    for item in ProductsList:
        for link in item.findAll('a',href=True,class_='wrapall'):
            ProductsLink.append(link['href'])

    print(x)        


listJson = json.dumps(ProductsLink)


jsonFile = open(f'.json','w')
jsonFile.write(listJson)
jsonFile.close()



bookList = []
num = 0
for link in ProductsLink:
    num+=1
    print(num)
# test_link = """https://www.chibekhoonam.net/product/%d8%ac%d8%a7%d9%85%d8%b9-%d9%81%db%8c%d8%b2%db%8c%da%a9-%d9%be%d8%a7%db%8c%d9%87-%d8%af%d9%87%d9%85-%d9%88-%db%8c%d8%a7%d8%b2%d8%af%d9%87%d9%85-%d8%b1%db%8c%d8%a7%d8%b6%db%8c-%d8%a7%d9%84%da%af%d9%88/"""
    req2 = requests.get(link,header)
    mainPart = BeautifulSoup(req2.content,'lxml')

    try :
        name = mainPart.find('h1',class_='book-title').text.strip()
    except:
        pass  
    ###################################################################################
    try :
        authurs = mainPart.find('div',class_='product-all-authors').text.strip()
    except:
        authurs='' 
    ###################################################################################
    try :
        imageLinkx=mainPart.find('img',class_="attachment-280x414 size-280x414 wp-post-image" )
        imageLink = imageLinkx['src']
    except:
        imageLink=''
    ###################################################################################
    try :
        price = mainPart.find("span",class_="oldprice oldprice-onsale").text.strip()
    except:
        price=''    
    ###################################################################################
    try :
        yearOfPrintX=mainPart.find("div",class_="pa_sale_chap_part").text.strip()
        yearOfPrint = yearOfPrintX[9::]
    except:
        yearOfPrint=''
    ###################################################################################
    try :
        publicationsX=mainPart.find("div",class_='pa_sale_chap_part').text.strip()
        publications = publicationsX[8:13]
    except:
        publications=''
    ###################################################################################
    try :
        pagesCountX = mainPart.find("div",class_="pa_tedad_safhe_part").text.strip()
        pagesCount = pagesCountX[11::]
    except:
        pagesCount=''


    Book ={
        "Image" : imageLink,
        "Name" : name,
        "Authurs" : authurs,
        "YearOfPrint" : yearOfPrint,
        "Price" : price,
        "Publications" : publications,
        "PagesCount" : pagesCount
    }

    bookList.append(Book)

FileName=str(time.ctime()[0:3])+'-'+str(time.ctime()[11:13])+'_'+str(time.ctime()[14:16])+'_'+str(time.ctime()[17:19])


jsonStr = json.dumps(bookList)


jsonFile = open(f'BookList-{FileName}.json','w')
jsonFile.write(jsonStr)
jsonFile.close()
