# Python Data Analysis Project

Questa repository contiene:

- Il modulo DataExtractor.py
- Il modulo DataCleaner.py
- Due file Csv ottenuti tramite l'operazione di pulizia dati
- Quattro file txt contenenti i dati originari estratti tramite webscraping.

Nel modulo DataExtractor è implementata una classe DataExtractor che servendosi del modulo requests e bs4, acquisisce come attributo una lista di pagine e tramite a sua funzione data_ext() utilizza find_all() di bfs4 su ogni pagina della lista. Dato che il processo di request può richiedere parecchio tempo, con la funzione to_text() genera dei file .txt separando i prezzi dal resto delle informazioni ed evitando di dover ripere il processo ogni volta si voglia accedere 
alle pagine.

Tramite il modulo DataCleaner, dopo un'analisi dei pattern in ogni lista, vengono ottenute le stringhe relative a nome modello, modello dei prodotti Lumberjack e modello, materiale, colore dei prodotti Melluso.
I valori in entrambe le liste contenenti i prezzi vengono convertiti in float. Con le funzioni melluso_csv_maker() e lumberjack_csv_maker() possono essere creati dei csv con i dati estratti.   
Questo modulo può anche essere importato come modulo esterno e i dati raccolti usati come variabili.