       self.lista_medicamentos.clear()
        for medicamento in self.medicamentos:
            if medicamento.esta_perto_vencimento():
                dias_restantes = (medicamento.data_validade - datetime.now().date()).days
                self.lista_medicamentos.addItem(f"{medicamento.nome} - Vence em {dias_restantes} dias")