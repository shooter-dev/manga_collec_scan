import psutil
import time

def get_cpu_percentage():
    while True:
        # Obtenir le pourcentage d'utilisation du CPU
        cpu_percent = psutil.cpu_percent(interval=1)  # interval=1 signifie que l'on mesure l'usage du CPU toutes les 1 seconde
        print(f"CPU Usage: {cpu_percent}%")
        time.sleep(1)

if __name__ == "__main__":
    get_cpu_percentage()
