import requests
from bs4 import BeautifulSoup

# Data Extractor è creato per facilitare le operazioni di estrazione dati 
# da alcuni cataloghi web. Le sue funzioni sono molto limitate ma renderà meno macchinose
# le operazioni con Beautiful Soup. Basterà inserire l'url del catalogo, un suffisso
# ed un range ed estrarrà le pagine desiderate. Utilizzando il find_all() di BeautifulSoup
# sarà in grado di estrarre i dati desiderati restituendoli in una lista.

class DataExtractor:

    def __init__(self, url: str, separator: str, pages: int, numeric = True, strings = None) -> None:

        self.url = url
        self.separator= separator
        self.max_range= pages
        
        if numeric:
            self.pages= self.pages_extractor()
        else:
            self.pages= self.non_incr_extractor(strings)    
        
    def pages_extractor(self) -> list:

        pages = []
        
        for x in range(1, self.max_range + 1):
            
            incr_url = f"{self.url}{'' if x == 1 else self.separator + str(x)}"
            req = requests.get(incr_url)
            
            if "200" not in str(req):
                print("One or More Requests Not Accepted. Interrupting operation")

                return False
            
            else:
                pages.append(req)
        
        print("All requests accepted")
        return pages
    
    def non_incr_extractor(self, strings) -> list:

        print(" e mo che faccio??")
        pages = []
        
        for string in strings:

            url = f"{self.url}{string.lower().replace(' ',self.separator)}"
            req = requests.get(url)
            
            if "200" not in str(req):
                print("One or More Requests Not Accepted. Interrupting operation")

                return False
            
            else:
                
                pages.append(req)
        
        print("All requests accepted")
        
        return pages

    
    def data_ext(self, type: str, classes = None) -> list:
        
        strings = []

        for req in self.pages:
            
            if classes:
                
                bf_obj = BeautifulSoup(req.text, "html.parser").find_all(type, class_= classes)
                
                for x in bf_obj:
                
                    strings.append(x.text.strip())
            
            else:

                bf_obj = BeautifulSoup(req.text, "html.parser").find_all(type)

                for x in bf_obj:
                    
                    strings.append(x.text.strip())
                        
        
        if strings:
            return strings

        print("Operation Failed")

        return False  
    

def to_txt(filename: str, file: list):

        with open(f"{filename}_raw.txt", "w") as file1:
            
            for item in file:

                file1.write(str(item) + "\n")


