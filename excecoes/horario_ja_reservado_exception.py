

class HorarioJaReservado(Exception):
    def __init__(self):
        super().__init__('O horario já foi reservado')
