[1 week]

- La struttura del progetto è stata definita:
  - src: Dove la parte logica del progetto è definita.
  - scripts: Qui ci sono gli entrypoint
  - configs: Per esempio se vogliamo avere la riproducibilità qui possiamo salvare config che sono riutilizzabili
  - artifacts:
  - data: I dati che vogliamo utilizzare
  - tests
- Ho clonato il progetto NASA Anomaly Detection Dataset SMAP, questo è un dataset che proviene da un paper nei quali si studiano le anomalie.
  C'è un modello alla base quindi si ritrvano i dati di train e test.
- Ho creato il primo script che:
  - Recupera i dati
  - Stampa train shape, test shape e labels shape e l'anomaly ratio
  - Crea il grafico

![alt text](images/diagramma.png "Graph")

- La linea blu sono i valori reali;
- le linee blu grosse è una sequenza binaria che indica dove un punto è anomalo o meno
- la linea rosa una maschera di anomalie

---

Quella che pensavo essere un'anomaly mask in realtà non lo era.
Grafo corretto:
![alt text](images/diagrammaok.png "Graph")
Per l'anomaly mask ho dovuta crearla dato il file labeled anomalies che da un range per ogni file di valori anomali.
La sequenza binaria è stata rimossa e ora ci sono le parti viola che indicano i range anomali che sono segnalati nel fle labeled_anomalies.csv presenti direttamente dal dataset NASA

As I studied in different courses of machine learning studying the dataset is important, the next step is to check for relevant characteristics of the dataset.

Ho aggiunto delle funzioni in explore anomalies per far sì che eseguano correttamente le operazioni in explore anomalies
