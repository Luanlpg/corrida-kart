import re

list_logs = [a.rstrip() for a in open("log.txt")]
# removo a primeira linha
list_logs.remove(list_logs[0])

def create_pilot_obj():
    """
    Método que cria objeto piloto.
    """
    # inicio dicionário piloto
    pilot = {}
    # para cada item da lista de logs
    for i in list_logs:
        # eu substituo caractérs estratégicos
        i = i.replace('   ', '\t').replace(' – ', '\t\t')
        # e os recorto, criando uma pequena lista
        x = re.split(r'\t\t+', i)
        # uso seus elementos para criar o dict pilot
        pilot[x[2]] = {
                    'cod': x[1],
                    'nome': x[2],
                    'voltas': {}
                    }
    # novamente para cada item da lista de logs
    for i in list_logs:
        # eu substituo caractérs estratégicos
        i = i.replace('   ', '\t').replace(' – ', '\t\t')
        # e os recorto, criando uma pequena lista
        x = re.split(r'\t\t+', i)
        # uso seus elementos para popular o dict voltas, dentro do dict pilot
        pilot[x[2]]['voltas'][x[3]] = {
                    'hora': x[0],
                    'tempo': x[4].strip(),
                    'vel_media': x[5].replace(',', '.')
                    }
    return pilot
