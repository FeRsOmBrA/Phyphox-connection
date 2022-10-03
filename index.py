import pyphox

host = ['192.168.1.4:8080']

for ip in host:
    conn = pyphox.connect(ip)
    conn.export('excel')