class Pessoa:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        return f"{self.nome} - Cargo: {self.cargo}"


class Servidor(Pessoa):
    def __init__(self, nome, cargo, ativo):
        super().__init__(nome, cargo)
        self.ativo = ativo

    def __str__(self):
        status = 'Ativo' if self.ativo else 'Inativo'
        return super().__str__() + f" - {status}"


class PortalTransparencia:
    def __init__(self):
        self.servidores = []

    def adicionar_servidor(self, nome, cargo, ativo):
        servidor = Servidor(nome, cargo, ativo)
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

# Exemplo de uso:
# Criar instância do portal de transparência
portal = PortalTransparencia()

# Adicionar mais exemplos fictícios de servidores
portal.adicionar_servidor("João", "Analista de TI", True)
portal.adicionar_servidor("Maria", "Programador", False)
portal.adicionar_servidor("Carlos", "Engenheiro", True)
portal.adicionar_servidor("Juliana", "Administrador", False)
portal.adicionar_servidor("Fernando", "Contador", True)
portal.adicionar_servidor("Larissa", "Designer", False)
portal.adicionar_servidor("Ricardo", "Analista Financeiro", True)
portal.adicionar_servidor("Isabel", "Gerente de Projetos", False)

# Listar todos os servidores
portal.listar_servidores()

# Listar servidores ativos
portal.listar_servidores(ativos=True)

# Listar servidores inativos
portal.listar_servidores(ativos=False)