from datetime import date

class Pessoa:
    def __init__(self, nome, cpf, data_nascimento, cargo):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.cargo = cargo

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf} - Nascimento: {self.data_nascimento} - Cargo: {self.cargo}"


class Servidor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, cargo, ativo):
        super().__init__(nome, cpf, data_nascimento, cargo)
        self.ativo = ativo

    def __str__(self):
        status = 'Ativo' if self.ativo else 'Inativo'
        return super().__str__() + f" - {status}"


class PortalTransparencia:
    def __init__(self):
        self.servidores = []

    def adicionar_servidor(self, nome, cpf, data_nascimento, cargo, ativo):
        servidor = Servidor(nome, cpf, data_nascimento, cargo, ativo)
        self.servidores.append(servidor)

    def listar_servidores(self, ativos=None):
        if ativos is not None:
            status = 'Ativos' if ativos else 'Inativos'
            print(f"\nServidores {status}:")
            servidores_filtrados = [servidor for servidor in self.servidores if servidor.ativo == ativos]
            if not servidores_filtrados:
                print("Nenhum servidor encontrado.")
            for servidor in servidores_filtrados:
                print(servidor)
        else:
            print("\nTodos os Servidores:")
            for servidor in self.servidores:
                print(servidor)

# Exemplos ficticios do portal de transparência
portal = PortalTransparencia()

portal.adicionar_servidor("João", "123.456.789-09", date(1985, 5, 12), "Analista de TI", True)
portal.adicionar_servidor("Maria", "987.654.321-00", date(1990, 8, 23), "Programador", False)
portal.adicionar_servidor("Carlos", "111.222.333-44", date(1978, 3, 7), "Engenheiro", True)
portal.adicionar_servidor("Juliana", "555.666.777-88", date(1982, 11, 15), "Administrador", False)
portal.adicionar_servidor("Fernando", "333.444.555-66", date(1980, 2, 25), "Contador", True)
portal.adicionar_servidor("Larissa", "999.888.777-66", date(1995, 9, 8), "Designer", False)
portal.adicionar_servidor("Ricardo", "777.888.999-00", date(1987, 6, 14), "Analista Financeiro", True)
portal.adicionar_servidor("Isabel", "111.222.333-44", date(1983, 4, 30), "Gerente de Projetos", False)


# Listar todos os servidores
portal.listar_servidores()

# Listar servidores ativos
portal.listar_servidores(ativos=True)

# Listar servidores inativos
portal.listar_servidores(ativos=False)