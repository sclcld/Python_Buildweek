from dataExtractor import DataExtractor, to_txt


lumberjack_shops_strings= [
                            "Negozi Lumberjack a Bari e provincia",
                            "Negozi Lumberjack a Brescia e provincia",
                            "Negozi Lumberjack a Bolzano e provincia",
                            "Negozi Lumberjack a Cuneo e provincia",
                            "Negozi Lumberjack a Firenze e provincia",
                            "Negozi Lumberjack a Milano e provincia",
                            "Negozi Lumberjack a Roma e provincia",
                            "Negozi Lumberjack a Venezia e provincia"
                        ]

melluso_shops_strings = [
                            "Negozi Melluso a Salerno e provincia",
                            "Negozi Melluso a Caserta e provincia",
                            "Negozi Melluso a Napoli e provincia",
                            "Negozi Melluso a Bologna e provincia",
                            "Negozi Melluso a Latina e provincia",
                            "Negozi Melluso a Roma e provincia",
                            "Negozi Melluso a Pavia e provincia",
                            "Negozi Melluso a Milano e provincia",
                            "Negozi Melluso a Lodi e provincia",
                            "Negozi Melluso a Lecco e provincia",
                            "Negozi Melluso a Torino e provincia",
                            "Negozi Melluso a Messina e provincia",
                            "Negozi Melluso a Vicenza e provincia"
]       

shops_url= "https://www.ciaoshops.com/"

melluso_url = "https://www.melluso.com/it/melluso-donna/nuova-collezione.html"
melluso_subfix = '?p='
lumberjack_url = "https://www.lumberjack.com/it/campaign/woman?category=shoes"
lumberjack_subfix = "&page="

melluso_data= DataExtractor(melluso_url, melluso_subfix, 25, True)
melluso_models = melluso_data.data_ext("a",["product-item-link"])
melluso_prices = melluso_data.data_ext("span", ["price"])

lumberjack_data = DataExtractor(lumberjack_url, lumberjack_subfix, 7, True)
lumberjack_models = lumberjack_data.data_ext("div",["product__name"])
lumberjack_prices = lumberjack_data.data_ext("span", ["product__prices-sale"])


melluso_shops_data = DataExtractor(shops_url, "-", 0, False, melluso_shops_strings)
melluso_shops= set(melluso_shops_data.data_ext("a"))
lumberjack_shops_data = DataExtractor(shops_url, "-", 0, False, lumberjack_shops_strings)
lumberjack_shops= set(lumberjack_shops_data.data_ext("a"))

to_txt("melluso_models", melluso_models)
to_txt("melluso_prices", melluso_prices)
to_txt("lumberjack_models", lumberjack_models)
to_txt("lumberjack_prices", lumberjack_prices)
to_txt("melluso_shops", melluso_shops)
to_txt("lumberjack_shops", lumberjack_shops)



print(lumberjack_shops)