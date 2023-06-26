

class ClientePossuiConsultasException(Exception):
    def __init__(self):
        super().__init__('Cliente possui consultas cadastradas')
