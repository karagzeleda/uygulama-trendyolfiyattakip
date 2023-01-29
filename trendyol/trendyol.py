import requests
from bs4 import BeautifulSoup
from send_email import sendMail
import time


url1="https://www.trendyol.com/mango/yakasi-kurklu-ceket-p-348211491"


def checkPrice(url,paramPrice): 
      headers={
            
             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
      }


      page = requests.get(url, headers=headers)

      htmlPage = BeautifulSoup(page.content,'html.parser')

      productTitle=htmlPage.find("h1", class_="pr-new-br").getText()

      price=htmlPage.find("span", class_="prc-dsc").getText()

      image=htmlPage.find("img", class_="base-product-image")

      convertedPrice = float(price.replace(",",".").replace(" TL",""))

      if(convertedPrice <= paramPrice ):
        
           print("Takip Edilen Ürün İstenilen Fiyattan Aşağı Düştü. Fırsatı Kaçırmayın")
           htmlEmailContent= """\
              <html>
              <head></head>
              <body>
              <h3>{0}</h3>
              <br/>
              {1}
              <br/>
              <p>Takip Edilen Urun Linki:{2}</p>
              </body>
              </html>
              """.format(productTitle, image, url)
      else: 
          print("Takip Edilen Ürün İstenilen Fiyattan Asağı Düşmedi")

def new_func(htmlEmailContent):
    sendMail("edakaraguzel6@gmail.com","Takip Edilen Urun Istenilen Fiyattan Asagi Dustu. Firsati Kacirmayin", htmlEmailContent)



while(True):
      checkPrice(url1,1800)
      time.sleep(3)
