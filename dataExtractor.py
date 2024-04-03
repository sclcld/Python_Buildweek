import requests
from bs4 import BeautifulSoup
from typing import Union


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
        print(type, classes)
        strings = []
        for req in self.pages:
            
            bf_obj = BeautifulSoup(req.text, "html.parser").find_all(type, class_= classes)
            
            for x in bf_obj:
                
                strings.append(x.text.strip())
        if strings:
            return strings

        print("Operation Failed")

        return False  



"spf-product-card__price money"
melluso_url = "https://www.melluso.com/it/melluso-donna/nuova-collezione.html"
melluso_subfix = '?p='
lumberjack_url = "https://www.lumberjack.com/it/campaign/woman?category=shoes"
lumberjack_subfix = "&page="


#melluso_data= DataExtractor(melluso_url, melluso_subfix, 3)
#melluso_models = melluso_data.data_ext("a",["product-item-link"])
#melluso_prices = melluso_data.data_ext("span", ["price"])
#melluso_sizes = sorted(list(set(melluso_data.data_ext("div", "text"))))
lumberjack_data = DataExtractor(lumberjack_url, lumberjack_subfix, 2)
lumberjack_models = lumberjack_data.data_ext("div",["product__name"])
lumberjack_prices = [float("33"+x[:-4].replace(",",".")) for x in lumberjack_data.data_ext("span", ["product__prices-sale"])]

print(lumberjack_prices)
    

    

#     request = requests.get(f"https://www.zalando.it/scarpe-bambini/{'' if x == 1 else '&p='+ str(x)})")
#     soup_obj= BeautifulSoup(request.text, "html.parser")
    
#     brnds = soup_obj.find_all("h3", class_= "FtrEr_ lystZ1 FxZV-M HlZ_Tf ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2")
#     for br in brnds:

#         brands.append(br.text)
    
#     descs= soup_obj.find_all("h3", class_="sDq_FX lystZ1 FxZV-M HlZ_Tf ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2")
#     for desc in descs:
        
#         descriptions.append(desc.text)
                                          
#     prcs = soup_obj.find_all(["h3", "span"],  class_= ["sDq_FX lystZ1 FxZV-M HlZ_Tf",
#                                                       "sDq_FX lystZ1 dgII7d Km7l2y"]
                                                      
#                             )
    
#     for price in prcs:
        
#         if price.text not in  "da Scopri ":
#             prices.append(price.text)

# print(len(brands))
# print(len(descriptions))
# print(len(prices))


# with open("b_brands.txt", "w") as file1:

#     for x in brands:

#         file1.write(x + "\n")

# with open("b_descriptions.txt", "w") as file2:

#     for x in descriptions:

#         file2.write(x + "\n")

# with open("b_prices.txt", "w") as file3:

#     for x in prices:

#         file3.write(x + "\n")        

