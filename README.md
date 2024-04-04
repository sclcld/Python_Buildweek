# Python Data Analysis Project

Questa repository contiene:

- Il modulo DataExtractor.py
- Il modulo DataCleaner.py
- Il modulo Extractions.py
- Due file Csv ottenuti tramite l'operazione di pulizia dati
- I file txt contenenti i dati originari estratti tramite webscraping.

Nel modulo DataExtractor è implementata una classe DataExtractor che servendosi del modulo requests e bs4, acquisisce come attributo una lista di pagine e tramite a sua funzione data_ext() utilizza find_all() di bfs4 su ogni pagina della lista. Dato che il processo di request può richiedere parecchio tempo, con la funzione to_text() genera dei file .txt separando i prezzi dal resto delle informazioni ed evitando di dover ripere il processo ogni volta si voglia accedere 
alle pagine.

Tramite il modulo Extractions, utilizzando DataExtractor e to_txt() vengono generati i file raw da ripulire.

Con il modulo il modulo DataCleaner, dopo un'analisi dei pattern in ogni lista, vengono ottenute le stringhe relative a nome modello, modello dei prodotti Lumberjack e modello, materiale, colore dei prodotti Melluso.
I valori in entrambe le liste contenenti i prezzi vengono convertiti in float.    
Tramite la fuzione shops_cleaner(), analizzando i pattern delle stringhe relativa agli shops e l'inserimento di un segnaposto delimitante le varie sezioni, si ottengono nomeshop, indirizzo, località.
Con le funzioni melluso_csv_maker(), lumberjack_csv_maker(), shops_csv_maker() possono essere creati dei csv con i dati estratti.
Questo modulo può anche essere importato come modulo esterno e i dati raccolti usati come variabili.
