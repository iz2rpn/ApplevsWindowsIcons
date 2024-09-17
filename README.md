# Apple vs Windows Icons

"**Apple vs Windows Icons**" è un gioco arcade sviluppato in Python utilizzando il framework Pygame. Il giocatore controlla un'astronave a forma di icona Apple, mentre combatte contro un gruppo di nemici rappresentati dalle icone Windows. Il giocatore deve eliminare tutti i nemici prima che raggiungano il fondo dello schermo o prima che l'astronave venga colpita dai proiettili nemici.

## Funzionalità

- **Controllo dell'astronave**: Muovi l'astronave a sinistra e a destra con le frecce direzionali e spara proiettili con la barra spaziatrice.
- **Nemici**: I nemici sono icone casuali prese da una cartella di immagini, disposte in righe e colonne. Si muovono lateralmente e scendono ogni volta che raggiungono il bordo dello schermo.
- **Proiettili**: Sia l'astronave Apple che i nemici possono sparare proiettili. Evita i proiettili nemici e cerca di eliminarli prima che ti colpiscano!
- **Punteggio**: Guadagna punti ogni volta che elimini un nemico.
- **Menu principale**: Un semplice menu che permette di avviare il gioco premendo "INVIO".
- **Grafica personalizzata**: Il gioco utilizza icone grafiche personalizzate per il giocatore, i nemici e i proiettili.
  
## Requisiti di Sistema

- **Python 3.x**
- **Pygame** (installabile tramite `pip`)

## Installazione

1. **Clona il repository:**
   ```bash
   git clone https://github.com/tuo-username/apple-vs-windows-icons.git
   cd apple-vs-windows-icons
   ```

2. **Crea un ambiente virtuale (opzionale ma consigliato):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Su Windows usa: venv\Scripts\activate
   ```

2. **Aggiungi le icone: Inserisci le icone nella cartella img/. Dovresti avere almeno:**
   - apple.png per l'astronave del giocatore
   - mouse_pointer.png per i proiettili
   - Varie icone .png per i nemici

## Esecuzione del Gioco

**Una volta installate tutte le dipendenze, esegui il gioco con:**
   ```bash
   python main.py
   ```

## Controlli di Gioco
- Freccia Sinistra: Muovi l'astronave a sinistra
- Freccia Destra: Muovi l'astronave a destra
- Barra Spaziatrice: Spara un proiettile
- Tasto INVIO: Avvia il gioco dal menu principale
 -Miglioramenti Futuri

## TODO
- Implementare un sistema di power-up
- Introdurre effetti sonori e musica di sottofondo
- Creare un sistema di classifica per i punteggi più alti
- Aggiungere più tipi di nemici con comportamenti diversi

## Licenza
* Questo progetto è distribuito sotto la licenza MIT. Vedi il file LICENSE per i dettagli.
