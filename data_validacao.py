from datetime import datetime,timedelta

class DataBr:

    def __init__(self):
        self._momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = self.meses_do_ano()
        mes_cadastro = self._momento_cadastro.month
        return meses_do_ano[mes_cadastro - 1]

    def meses_do_ano(self):
        return ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho",
                "Agosto","Setembro","Outubro","Setembro","Novembro","Dezembro"]

    def dia_semana(self):
        dia_semana_lista = ["segunda","terça","quarta","quinta","sexta","sabado","domingo"]
        dia_semana = self._momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def format_data(self):
        data_formatada = self._momento_cadastro.strftime("%m/%d/%Y - %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) -self._momento_cadastro
        return tempo_cadastro

