import os
import json
from fpdf import FPDF

class Relatorio:
    def __init__(self, sistema):
        self.sistema = sistema  # Passa o sistema para acessar as faltas
        self.caminho_relatorio = os.path.join(os.path.expanduser("~"), "Downloads", "Relatorios_Faltas")

    def gerar_relatorio(self):
        """Gera um relatório em PDF das faltas registradas."""
        self.sistema.carregar_faltas()  # Carrega as faltas do JSON antes de gerar o relatório

        if not self.sistema.faltas:  # Verifica se há faltas registradas
            print("Não há faltas registradas! O relatório não pode ser gerado.")
            input("Pressione Enter para voltar ao menu.")
            return

        os.makedirs(self.caminho_relatorio, exist_ok=True)
        caminho_pdf = os.path.join(self.caminho_relatorio, "relatorio_faltas.pdf")

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, "Relatório de Faltas", ln=True, align="C")
        pdf.ln(10)

        pdf.set_font("Arial", size=12)
        for falta in self.sistema.faltas:
            pdf.cell(0, 10, f"Aluno: {falta['nome']}", ln=True)
            pdf.cell(0, 10, f"Data: {falta['data']}", ln=True)
            pdf.cell(0, 10, f"Justificativa: {falta['justificativa']}", ln=True)
            pdf.ln(5)

        pdf.output(caminho_pdf)
        print(f"Relatório gerado com sucesso e salvo em: {caminho_pdf}")

        os.startfile(caminho_pdf)  # Abre o arquivo PDF automaticamente
        input("Pressione Enter para voltar ao menu.")
