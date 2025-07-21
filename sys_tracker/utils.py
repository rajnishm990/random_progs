import psutil

def get_metrics():
    return {
        "cpu":psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "net": psutil.net_io_counters(pernic=False)._asdict()
    }

def alert_if_high(data):
    if data["cpu"] > 90:
        print('Alert High tempreture ')
    else:
        print("Safe Temp")

if __name__ == "__main__":
    data = get_metrics()
    print(data)
    alert_if_high(data)



    