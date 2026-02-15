import sqlite3
from datetime import datetime

class CRM:
    # Sistema di gestione clienti professionale per caffè
    def __init__(self, nome_db="clienti_caffe.db"):
        self.conn = sqlite3.connect(nome_db)
        self.cursor = self.conn.cursor()  # Correzione: self.cursor e sqlite3.cursor()
        self._crea_tabelle()

    def _crea_tabelle(self):
        """Crea le tabelle necessarie per il CRM"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clienti (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefono TEXT,
                email TEXT,
                indirizzo TEXT,
                citta TEXT DEFAULT 'Budapest',
                note TEXT,
                data_inserimento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                totale_speso REAL DEFAULT 0.0
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ordini (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER,
                data_ordine TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                importo REAL,
                prodotti TEXT,
                FOREIGN KEY (cliente_id) REFERENCES clienti (id)
            )
        ''')
        self.conn.commit()

    def aggiungi_cliente(self, nome, telefono='', email='', indirizzo='', note=''):
        """Aggiunge un nuovo cliente"""
        self.cursor.execute('''
            INSERT INTO clienti (nome, telefono, email, indirizzo, note)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, telefono, email, indirizzo, note))
        self.conn.commit()
        return self.cursor.lastrowid

    def cerca_clienti(self, cerca=''):
        """Cerca clienti per nome o telefono"""
        self.cursor.execute('''
            SELECT * FROM clienti 
            WHERE nome LIKE ? OR telefono LIKE ? OR email LIKE ?
            ORDER BY data_inserimento DESC
        ''', (f'%{cerca}%', f'%{cerca}%', f'%{cerca}%'))
        return self.cursor.fetchall()

    def cliente_dettagli(self, cliente_id):
        """Dettagli completi di un cliente con ordini"""
        self.cursor.execute('SELECT * FROM clienti WHERE id = ?', (cliente_id,))
        cliente = self.cursor.fetchone()
        
        if cliente:
            self.cursor.execute('''
                SELECT * FROM ordini 
                WHERE cliente_id = ? 
                ORDER BY data_ordine DESC
            ''', (cliente_id,))
            ordini = self.cursor.fetchall()
            return cliente, ordini
        return None, []

    def aggiungi_ordine(self, cliente_id, importo, prodotti):
        """Registra un nuovo ordine"""
        self.cursor.execute('''
            UPDATE clienti SET totale_speso = totale_speso + ?
            WHERE id = ?
        ''', (importo, cliente_id))
        
        self.cursor.execute('''
            INSERT INTO ordini (cliente_id, importo, prodotti)
            VALUES (?, ?, ?)
        ''', (cliente_id, importo, prodotti))
        self.conn.commit()

    def statistiche_clienti(self):
        """Statistiche generali clienti"""
        self.cursor.execute('SELECT COUNT(*) FROM clienti')
        totale_clienti = self.cursor.fetchone()[0]
        
        self.cursor.execute('SELECT SUM(totale_speso) FROM clienti')
        totale_fatturato = self.cursor.fetchone()[0] or 0
        
        self.cursor.execute('''
            SELECT nome, totale_speso FROM clienti 
            ORDER BY totale_speso DESC LIMIT 5
        ''')
        top_clienti = self.cursor.fetchall()
        
        return {
            'totale_clienti': totale_clienti,
            'totale_fatturato': totale_fatturato,
            'top_clienti': top_clienti
        }

    def chiudi(self):
        """Chiude la connessione al database"""
        self.conn.close()
# Inizializza il CRM
crm = CRM()

# Aggiungi un cliente
cliente_id = crm.aggiungi_cliente(
    nome="Mario Rossi", 
    telefono="+36301234567",
    email="mario@esempio.hu",
    note="Cliente abituale, preferisce cappuccino"
)

# Aggiungi un ordine
crm.aggiungi_ordine(cliente_id, 2500, "2x Cappuccino, 1x Croissant")

# Cerca clienti
clienti = crm.cerca_clienti("Mario")
print("Clienti trovati:", clienti)

# Statistiche
stats = crm.statistiche_clienti()
print("Statistiche:", stats)

# Chiudi
crm.chiudi()
