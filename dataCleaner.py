modelli_melluso = ""
prezzi_melluso = ""
shops_melluso = ""
modelli_lumb= ""
prezzi_lumb= ""
shops_lumb= ""

with open("melluso_models_raw.txt", "r") as file:

    modelli_melluso = file.read().splitlines()

with open("melluso_prices_raw.txt", "r") as file:

    prezzi_melluso = file.read().splitlines()

with open("lumberjack_models_raw.txt", "r") as file:

    modelli_lumb = file.read().splitlines()

with open("lumberjack_prices_raw.txt", "r") as file:

    prezzi_lumb_string = file.read().splitlines()

with open("melluso_shops_raw.txt", "r") as file:

    shops_melluso = file.read().splitlines()

with open("lumberjack_shops_raw.txt", "r") as file:

    shops_lumb = file.read().splitlines()


# Lumberjack
# Pattern : THELMA SNEAKERS DONNA
def lumb_cleaner() -> list:

    clean_models = []

    for mod in modelli_lumb:
        #paired = THELMA SNEAKERS
        paired = mod.split()[:-1]
        #*s_type= MODELLO len >= 1
        name, *s_type = paired
        #["Thelma", "Sneakers"]
        clean_models.append([name.capitalize(), " ".join(s_type).capitalize()])
    
    return clean_models


# Melluso
#           0         1     2         3  4        5        6(-1)  7   
# Pattern : Décolleté donna slingback in pelle    nappetta nero   d166w
#           Type                         Material         Color
#  Type = Pattern[0], 
#  Material = Pattern[index "in" + 1], 
#  Color = Pattern[-1]

# in alcune stringhe "in" viene riportato come "il" 

def melluso_cleaner() -> list:

    rows = []

    for string in modelli_melluso:
        
        index = 0
        splitted = string.split()[:-1] 
        
        for i, stop in enumerate(splitted):

            if stop == "il" or stop == "in":

                index = i
        
        model = splitted[0].strip()
        material = splitted[index + 1]
        color = splitted[-1]
        rows.append([model,material, color])
    
    return rows

# I dati relativi agli shops sono stati reperiti tramite analis degli "a" nella pagina. L'assenza
# di classi specifiche nel codice d'origine porta alla necessità di una pulizia molto approfondita.
# Nelle stringhe contenenti gli indirizzi appare il pattern "guarda orari e dettagli". I dati vengono
# filtrati secondo questo criterio. 
# In seguito, tramite iterazione, vengono analizzate le stringhe e "suddivise" tramite slicing a seguito di 
# controlli relativi a casi specifici. Per suddividere le stringhe in "sezioni" viene utilizzato * come 
# segnaposto.

# Pattern: Fissimarket OutletVia de Neri 64FirenzeGuarda Orari e Dettagli
#          NomeShop          Indirizzo     Città
# index NomeShop<index Via
# index città == index ultimo numero

def shops_cleaner(shops):

    shops = [string.lower().removesuffix("guarda orari e dettagli") for string in shops if "orari e " in string.lower()] 
    key_words = ["pompei", "via", "calle", "piazza", "corso", "strada statale"]  
    shops_clean = []
    
    for raw in shops[:]:

        for keyword in key_words:

            if keyword in raw:
                
                raw = raw.replace(keyword,f"*{keyword}").replace("pa*via", " pavia").replace("centro", " centro")
        
        if "strasse" in raw:

            for char in range(raw.index("strasse"), -len(raw), -1):

                if raw[char] == " ":

                    raw = f"{raw[:char]}*{raw[char:].strip()}"
                    break     
        
        for i in range(-1, -len(raw), -1):
            
            if raw[i] == "/" and raw[i + 1].isalpha():

                raw = f"{raw[:i + 2]}*{raw[i + 2:]}"
                
                break
            
            elif raw[i].isdigit() and raw[i + 1].isalpha():

                raw = f"{raw[:i +1]}*{raw[i+1:]}"
        
        shops_clean.append(raw.split("*"))

    return shops_clean    

 

modelli_melluso_clean = melluso_cleaner()
modelli_lumb_clean = lumb_cleaner()
# pattern '89,90\xa0€'
prezzi_melluso_numeric = [float(price[:-2].replace(",", ".")) for price in prezzi_melluso]
# pattern '64,99\xa0EUR'
prezzi_lumb_numeric = [float(price[:-4].replace(",", ".")) for price in prezzi_lumb_string]
shops_melluso_clean = shops_cleaner(shops_melluso)  
shops_lumb_clean = shops_cleaner(shops_lumb)  









def melluso_csv_maker():
    
    with open("melluso.csv", "w") as file:
            
        for index, data in enumerate(zip(modelli_melluso_clean, prezzi_melluso_numeric)):
        
            model, mat, color = data[0]
            price = data[1]

            if index == 0:
            
                file.write("Modello,Materiale,Colore,Prezzo\n")

            file.write(f"{model},{mat},{color},{price}\n")     


def lumberjack_csv_maker():
    
    with open("lumberjack.csv", "w") as file:
        
        for index, data in enumerate(zip(modelli_lumb_clean, prezzi_lumb_string)):

            model_name, model = data[0]
            price = data[-1]
            
            if index == 0 : 
                
                file.write("Nome, Modello, Prezzo\n") 
            
            file.write(f"{model_name},{model},{price}\n")

def shops_csv_maker(name, shops):

    with open(f"{name}.csv", "w") as file:
        
        for index,shop in enumerate(shops):
        
            if index == 0:
                
                file.write("Nome, Indirizzo, Località\n")
            
            file.write(f'{",".join(shop)}\n')


shops_csv_maker("melluso_shops",shops_melluso_clean) 
shops_csv_maker("lumberjack_shops", shops_lumb_clean)