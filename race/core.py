from separador import create_pilot_obj
from pprint import pprint
from datetime import datetime, timedelta

class FastAndFurious():

    def __init__(self):
        # cria objeto pilot utilizando o arquivo log.txt
        self.pilot = create_pilot_obj()

    def race_time(self, pilot_name):
        """
        Método que recebe piloto como parâmetro e retorna numero de voltas,
        tempo total da prova e melhor tempo.
        """
        # inicio varáveis, do tipo date time
        top_time = datetime.strptime('59:59.999', '%M:%S.%f')
        time = datetime.strptime('0:00.000', '%M:%S.%f')
        num_voltas = 0
        # pego as informações de voltas de um piloto especifico, do obj pilot
        voltas = self.pilot[pilot_name]['voltas']
        # para cada volta dada pelo piloto
        for i in voltas.values():
            # pego a informação do tempo da volta
            volta = i['tempo'].split(':')
            # e adiciono em time
            time += timedelta(minutes=int(volta[0]), seconds=float(volta[1]))
            # somo 1 em numero de voltas
            num_voltas += 1
            # caso esta volta tenha sido a mais rapida
            if datetime.strptime(i['tempo'], '%M:%S.%f') < top_time:
                # tranformo em top_time
                top_time = datetime.strptime(i['tempo'], '%M:%S.%f')

        return num_voltas, str(time).split(' ')[1], str(top_time).split(' ')[1]


    def race_posix(self):
        """
        Método que cria ranking de chega e de melhor volta.
        """
        # inicio as variáveis que utilizarei como retorno
        classificacao = []
        top_times = []
        # para cada item no dict pilot
        for i in self.pilot.items():
            # eu chamo o método race_time, para adiquirir suas métricas
            num_voltas, time, top_time = self.race_time(i[1]['nome'])
            # e as adiciono nas listas de retorno
            classificacao.append((i[1]['nome'], num_voltas, time))
            top_times.append((i[1]['nome'], top_time))
        # as ordeno em uma sequencia que, ordene primeiro o time dps o numero
        # de voltas, co caso da lista de top times apenas as ordeno pelo time
        classificacao.sort(key=lambda x: x[1])
        classificacao.sort(key=lambda x: x[2])
        top_times.sort(key=lambda x: x[1])

        return classificacao, top_times

    def average_speed(self):
        """
        Método que faz o calculo de velocidade média de cda piloto.
        """
        # inicio a variável que utilizarei como retorno
        medias = []
        # para cada item no dict pilot
        for i in self.pilot.items():
            num_voltas = 0
            vel = 0
            voltas = i[1]['voltas']
            # para cada volta dada pelo piloto
            for y in voltas.values():
                vel += float(y['vel_media'])
                num_voltas += 1
            medias.append((i[1]['nome'], vel/num_voltas))
        return medias

    def difference(self):
        """
        Método que calcula diferença de tempo parao 1° colocado.
        """
        # inicio a variável que utilizarei como retorno
        diff = []
        # chamo race_posix para adquirir classificação e tempo
        classificacao = self.race_posix()[0]
        first = classificacao[0]
        first_time = first[2].split(':')
        # para cada tempo no ranking atribuo uma diferença do primeiro lugar
        for i in classificacao:
            # caso seja o msm
            if i == first:
                # coloco uma string nula
                diff.append((first[0], '--:--:--.------'))
            # caso contrario
            else:
                # tranformo a info de tempo em datetime
                mais = datetime.strptime(i[2], '%H:%M:%S.%f')
                # subtraio o melhor tempo, tranformo em str
                mais = str(mais - timedelta(minutes=int(first_time[1]), seconds=float(first_time[2])))
                # e adiciono uma tupla na lista diff
                if i[1] < 4:
                    mais = ' -CORRIDA-INCOMPLETA-'
                diff.append((i[0], '+'+mais.split(' ')[1]))

        return diff
