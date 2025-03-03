import datetime
import json
import os

class Sistema:
    def __init__(self):
        self.faltas = []
        self.alunos = ["Yasmim L B Dias", "Maria Eduarda Bertuzzi"]
        self.arquivo_faltas = "faltas.json"
        self.carregar_faltas()  # Carrega as faltas do arquivo ao iniciar

    def salvar_faltas(self):
        """Salva a lista de faltas no arquivo JSON."""
        with open(self.arquivo_faltas, "w", encoding="utf-8") as f:
            json.dump(self.faltas, f, indent=4, ensure_ascii=False)

    def carregar_faltas(self):
        """Carrega as faltas do arquivo JSON se ele existir."""
        if os.path.exists(self.arquivo_faltas):
            with open(self.arquivo_faltas, "r", encoding="utf-8") as f:
                self.faltas = json.load(f)

    def registrar_falta(self, auditoria):
        print("Selecione o aluno:")
        for i, aluno in enumerate(self.alunos, start=1):
            print(f"{i}. {aluno}")

        while True:
            try:
                escolha = int(input("Digite o número do aluno: "))
                if 1 <= escolha <= len(self.alunos):
                    nome = self.alunos[escolha - 1]
                    break
                else:
                    print("Opção inválida, tente novamente.")
            except ValueError:
                print("Digite um número válido.")

        justificativa = input("Justificativa da falta: ").strip()
        while len(justificativa) < 5:
            print("Justificativa muito curta, forneça mais detalhes.")
            justificativa = input("Justificativa da falta: ").strip()

        data = str(datetime.date.today())

        self.faltas.append({'nome': nome, 'data': data, 'justificativa': justificativa})
        self.salvar_faltas()  # Salva no arquivo após registrar

        auditoria.registrar_auditoria(nome, 'registrou falta', data)
        print(f"Falta registrada para {nome} no dia {data} com a justificativa: {justificativa}")
        input("Pressione Enter para voltar ao menu.")

    def listar_faltas(self):
        """Exibe a lista de faltas registradas."""
        if not self.faltas:
            print("Não há faltas registradas!")
        else:
            for falta in self.faltas:
                print(f"Aluno: {falta['nome']}, Data: {falta['data']}, Justificativa: {falta['justificativa']}")
        input("Pressione Enter para voltar ao menu.")

    def obter_faltas(self):
        """Retorna a lista de faltas para ser usada em relatórios."""
        return self.faltas
