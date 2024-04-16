#definição de bibliotecas
import psutil

def monitor_database():
    # Lista todos os processos em execução
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Verifica se o nome do processo contém a palavra "database"
            if 'database' in proc.name().lower():
                print(f"Processo: {proc.name()} | PID: {proc.pid}")  # Exibe o nome e o PID do processo relacionado ao banco de dados
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  # Ignora erros de processos inacessíveis ou inexistentes

    # Obtém informações sobre o uso de memória
    mem = psutil.virtual_memory()
    print(f"Uso de Memória Total: {mem.total / (1024 ** 3)} GB")  # Converte e exibe o uso total de memória em GB
    print(f"Uso de Memória Disponível: {mem.available / (1024 ** 3)} GB")  # Converte e exibe a memória disponível em GB

    # Obtém informações sobre o uso de CPU
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)  # Obtém a porcentagem de uso de CPU por núcleo
    print("Uso de CPU por núcleo:")
    for i, percent in enumerate(cpu_percent):
        print(f"Núcleo {i+1}: {percent}%")  # Exibe a porcentagem de uso de CPU de cada núcleo

if __name__ == "__main__":
    monitor_database()  # Chama a função principal para monitorar o banco de dados



# © 2024. Todos os direitos reservados. Este código é propriedade intelectual de Italo Nicacio.
