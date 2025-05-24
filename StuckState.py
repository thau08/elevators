class StuckState:
    
    def handle_request(self, elevator, floor):

        print(f"O elevador {elevator.name} está emperrado.")
        print(f"Tocando música calma")
        print("Chamando equipe de manutenção")
    
    def state_name(self):
        return "Emperrado"
