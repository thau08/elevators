# Importa todas as classes necessárias
from Elevator import Elevator
from CentralMonitor import CentralMonitor
from ProblemSimulator import ProblemSimulator

def main():
    """
    Função principal que testa todo o sistema.
    """
    
    print("=== INICIANDO SISTEMA DE ELEVADORES ===")
    
    # Cria a central de monitoramento (Singleton)
    central = CentralMonitor()
    
    # Cria o simulador de problemas
    simulator = ProblemSimulator(central)
    
    # Cria elevadores
    elevator1 = Elevator("A1")
    elevator2 = Elevator("B2")
    elevator3 = Elevator("C3")
    
    # Adiciona elevadores à central
    central.add_elevator(elevator1)
    central.add_elevator(elevator2)
    central.add_elevator(elevator3)
    
    print("\n=== TESTE 1: FUNCIONAMENTO NORMAL ===")
    elevator1.request_elevator(5)
    elevator2.request_elevator(3)
    elevator3.request_elevator(7)
    
    # Mostra relatório
    central.general_report()
    
    print("\n=== TESTE 2: SIMULANDO PROBLEMAS ===")
    # Simula que o elevador A1 ficou emperrado
    simulator.simulate_stuck("A1")
    
    # Tenta usar o elevador emperrado
    print("Tentando usar elevador emperrado:")
    elevator1.request_elevator(8)
    
    print("\n=== TESTE 3: SIMULANDO MANUTENÇÃO ===")
    # Coloca elevador B2 em manutenção
    simulator.simulate_maintenance("B2")
    
    # Tenta usar elevador em manutenção
    print("Tentando usar elevador em manutenção:")
    elevator2.request_elevator(4)
    
    # Mostra relatório atualizado
    central.general_report()
    
    print("\n=== TESTE 4: CONSERTANDO ELEVADORES ===")
    # Conserta os elevadores
    simulator.fix_elevator("A1")
    simulator.fix_elevator("B2")
    
    # Testa se voltaram a funcionar
    print("Testando elevadores consertados:")
    elevator1.request_elevator(10)
    elevator2.request_elevator(6)
    
    print("\n=== TESTE 5: VERIFICANDO SINGLETON ===")
    # Tenta criar outra central
    central2 = CentralMonitor()
    print(f"Central1 é a mesma que Central2? {central is central2}")
    
    # Relatório final
    central.general_report()
    
    print("=== TESTES CONCLUÍDOS ===")


# Executa a função main quando o arquivo é executado diretamente
if __name__ == "__main__":
    main()
