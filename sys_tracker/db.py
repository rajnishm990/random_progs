import sqlite3 


conn = sqlite3("metrics.db")

c = conn.cursor()

c.execute(
    """ 
CREATE TABLE IF NOT EXISTS metrics(
    timestamp TEXT,
    cpu REAL,
    memory REAL,
    disk REAL
    
    )
    """
)

def store_metrics(data):
    import datetime
    now = datetime.datetime.now().isoformat()
    c.execute("INSERT INTO metrics VALUES (?, ?, ?, ?)", 
              (now, data["cpu"], data["memory"], data["disk"]))
    conn.commit()