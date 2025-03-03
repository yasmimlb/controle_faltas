def validar_justificativa(justificativa):
    if len(justificativa) < 5:
        print("Justificativa muito curta. Por favor, forneça uma justificativa mais detalhada.")
        return False
    return True
