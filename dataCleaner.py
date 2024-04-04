modelli_melluso = ""
prezzi_melluso = ""
modelli_lumb= ""
#il file lumberjack prices è già pulito e in formato stringa
prezzi_lumb_string = ""

with open("melluso_models_raw.txt", "r") as file:

    modelli_melluso = file.read().splitlines()

with open("melluso_prices_raw.txt", "r") as file:

    prezzi_melluso = file.read().splitlines()

with open("lumberjack_models_raw.txt", "r") as file:

    modelli_lumb = file.read().splitlines()

with open("lumberjack_prices_raw.txt", "r") as file:

    prezzi_lumb_string = file.read().splitlines()


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
 
modelli_melluso_clean = melluso_cleaner()
modelli_lumb_clean = lumb_cleaner()
# pattern '89,90\xa0€'
prezzi_melluso_numeric = [float(prezzo[:-2].replace(",", ".")) for prezzo in prezzi_melluso]
# pattern '49.99'
prezzi_lumb_numeric = [float(price) for price in prezzi_lumb_string]


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

melluso_csv_maker()
lumberjack_csv_maker()
