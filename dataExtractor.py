import requests
from bs4 import BeautifulSoup


# Data Extractor è creato per rendere automatiche le operazioni di estrazione dati 
# da cataloghi web. Le sue funzioni sono molto limitate ma renderà meno macchinose
# le operazioni con Beautiful Soup. Basterà inserire l'url del catalogo, un prefisso
# ed un range ed estrarrà le pagine desiderate. Utilizzando il find_all() di BeautifulSoup
# sarà in grado di estrarre i dati desiderati restituendoli in una lista.

class DataExtractor:

    def __init__(self, url: str, subfix: str, pages: int) -> None:
        

        self.url = url
        self.subf= subfix
        self.max_range= pages
        self.pages= []
        self.pages_extractor()
        
        
    def pages_extractor(self) -> bool:

        for x in range(1, self.max_range + 1):
            
            incr_url = f"{self.url}{'' if x == 1 else self.subf + str(x)}"
            req = requests.get(incr_url)
            
            if "200" not in str(req):
                print("One or More Requests Not Accepted. Interrupting operation")
                self.pages = []
                
                return False
            
            else:
                self.pages.append(req)
        
        print("All requests accepted")
        return True

    def data_ext(self, type: str, classes: list):
        
        strings = []
        for req in self.pages:
            
            bf_obj = BeautifulSoup(req.text, "html.parser").find_all(type, class_= classes)
            
            for x in bf_obj:
                
                strings.append(x.text.strip())
        if strings:
            return strings

        print("Operation Failed")

        return False  

    

melluso_url = "https://www.melluso.com/it/melluso-donna/nuova-collezione.html"
melluso_subfix = '?p='
lumberjack_url = "https://www.lumberjack.com/it/campaign/woman?category=shoes"
lumberjack_subfix = "&page="

melluso_data= DataExtractor(melluso_url, melluso_subfix, 25)
melluso_models = melluso_data.data_ext("a",["product-item-link"])
melluso_prices = melluso_data.data_ext("span", ["price"])

lumberjack_data = DataExtractor(lumberjack_url, lumberjack_subfix, 7)
lumberjack_models = lumberjack_data.data_ext("div",["product__name"])
lumberjack_prices = [float(x[:-4].replace(",",".")) for x in lumberjack_data.data_ext("span", ["product__prices-sale"])]


print(lumberjack_prices)

# L'operazione di scraping può essere molto lenta. Con to_txt, inserendo come stringa il nome che vorremo
# dare al file, verranno prodotti dei file txt con tutti i dati estratti

def to_txt(filename: str, file: list):

     with open(f"{filename}.txt", "w") as file1:
         for item in file:
             
            file1.write(str(item) + "\n")

to_txt("melluso_models", melluso_models)
to_txt("melluso_prices", melluso_prices)
to_txt("lumberjack_models", lumberjack_models)
to_txt("lumberjack_prices", lumberjack_prices)