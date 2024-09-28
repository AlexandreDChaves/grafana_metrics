from influxdb import InfluxDBClient
import psutil

# Configurações do InfluxDB 1.x
host = "localhost"
port = 8086
username = "metrics_user"
password = "senha"
database = "system_metrics"

# Conectar ao InfluxDB
client = InfluxDBClient(host=host, port=port, username=username, password=password, database=database)

#Coletar métricas
cpu_percent = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')
net_io = psutil.net_io_counters()

# Dados InfluxDB
data = [
    {
        "measurement": "cpu_metrics",
        "tags": {
            "host": "server01"
            
        },
        "fields": {
            "cpu_percent": cpu_percent
        }
    },
    {
        "measurement": "memory_metrics",
        "tags": {
            "host": "server01"
        },
        "fields": {
            "total_memory": memory.total,
            "used_memory": memory.used,
            "free_memory": memory.free,
            "memory_percent": memory.percent
        }
    },
    {
        "measurement": "disk_metrics",
        "tags": {
            "host": "server01"
        },
        "fields": {
            "total_disk": disk.total,
            "used_dusk": disk.used,
            "free_disk": disk.free,
            "disk_percent": disk.percent
        }
    },
    {
        "measurement": "network_metrics",
        "tags": {
            "host": "server01"
        },
        "fields": {
            "bytes_sent": net_io.bytes_sent,
            "bytes_recv": net_io.bytes_recv,
            "packets_sent": net_io.packets_recv,
            "packets_recv": net_io.packets_recv
        }
    }
]

# Escrever os dados no influxdb
client.write_points(data)

# Fechar a conexão
client.close()