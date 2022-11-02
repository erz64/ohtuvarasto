import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_laitetaan_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(11)

        self.assertEqual(self.varasto.saldo, 10)
    
    def test_otetaan_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(10)

        self.assertEqual(self.varasto.saldo, 0)
    
    def test_laitetaan_varaston_tilavuudeksi_negatiivinen_luku(self):
        varasto2 = Varasto(-3)

        self.assertEqual(varasto2.tilavuus, 0)
    
    def test_otetaan_varastosta_negatiivinen_maara(self):
        entinen_saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-3)

        self.assertEqual(self.varasto.saldo, entinen_saldo)
    
    def test_lisataan_varastoon_negatiivinen_maara(self):
        entinen_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-3)

        self.assertEqual(self.varasto.saldo, entinen_saldo)

    def test_asetetaan_varaston_alku_saldoksi_negatiivinen_luku(self):
        varasto3 = Varasto(10, -3)

        self.assertEqual(varasto3.saldo, 0)

    def test_tulostetaan_varaston_tiedot(self):
        self.assertEqual('saldo = 0, vielä tilaa 10', str(self.varasto))
    
    pass