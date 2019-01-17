import unittest
from core import FastAndFurious

class RacingTestCase(unittest.TestCase):

    def setUp(self):
        self.racing = FastAndFurious()

    def test_race_time(self):
        # testa numero de voltas do Felipe Massa
        self.assertEqual(self.racing.race_time('F.MASSA')[0], 4)
        # testa numero de voltas do S.Vettel
        self.assertEqual(self.racing.race_time('S.VETTEL')[0], 3)
        # testa tempo total de prova de Massa
        self.assertEqual(self.racing.race_time('F.MASSA')[1], '00:04:11.578000')
        # testa melhor tempo de Massa
        self.assertEqual(self.racing.race_time('F.MASSA')[2], '00:01:02.769000')

    def test_race_posix(self):
        # testa o nome do quarto colocado: M.WEBBER
        self.assertEqual(self.racing.race_posix()[0][3][0], 'M.WEBBER')
        # testa o nome do quarto colocado: S.VETTEL
        self.assertEqual(self.racing.race_posix()[0][5][0], 'S.VETTEL')
        # testa o tempo da melhor volta
        self.assertEqual(self.racing.race_posix()[1][0][1], '00:01:02.769000')
        # testa o nome do autor da melhor volta: F.MASSA
        self.assertEqual(self.racing.race_posix()[1][0][0], 'F.MASSA')

    def test_average_speed(self):
        # testa a segunda maior media de velocidade
        self.assertEqual(self.racing.average_speed()[1][1], 43.467999999999996)
        # testa a maior media de velocidade
        self.assertEqual(self.racing.average_speed()[0][1], 44.24575)
        # testa a menor media de velocidade
        self.assertEqual(self.racing.average_speed()[5][1], 25.745666666666665)
        # testa o nome do dono da maior media de velocidade
        self.assertEqual(self.racing.average_speed()[0][0], 'F.MASSA')

    def test_difference(self):
        # testa da maior diferença para o primeiro lugar
        self.assertEqual(self.racing.difference()[5][1], '+-CORRIDA-INCOMPLETA-')
        # testa da menor diferença para o primeiro lugar
        self.assertEqual(self.racing.difference()[1][1], '+00:00:03.575000')
        # testa difereça do 1° para 1°
        self.assertEqual(self.racing.difference()[0][1], '--:--:--.------')

if __name__ == '__main__':
    unittest.main()
