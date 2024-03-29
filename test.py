import unittest
import main
from main import GenerateD
from main import Euler
from main import CoprimeTest
from main import Encrypt, Decrypt
from main import Encode, Decode
from main import keygen
from main import MillerRabin
from main import Creat_electronic_signature, Verif_electronic_signature
from main import ReadingPrivate, RecordingPrivate, RecordingPublic, ReadingPublic

class UnitTest(unittest.TestCase):

    main.n, main.e, main.D = keygen()

    def test_encrypt(self):
        self.assertEqual(Decrypt(Encrypt('Привет')), 'Привет')
        self.assertEqual(Decrypt(Encrypt('Russia is great country')), 'Russia is great country')
        self.assertEqual(Decrypt(Encrypt('2,71828182845904532..,./%')), '2,71828182845904532..,./%')
        self.assertEqual(Decrypt(Encrypt('пи=3,1415==---')), 'пи=3,1415==---')
        self.assertEqual(Decrypt(Encrypt('異體字')), '異體字')

    def test_D(self):
        self.assertEqual(GenerateD(215, 56), 96)
        self.assertEqual(GenerateD(1111, 16), 625)

    def test_code(self):
        self.assertEqual(Decode(Encode('Qwerty')), 'Qwerty')
        self.assertEqual(Decode(Encode('HSE_MIEM')), 'HSE_MIEM')
        self.assertEqual(Decode(Encode('TESstss1234_++')), 'TESstss1234_++')

    def test_file(self):
        RecordingPrivate(100, 500, 'test_private1')
        self.assertEqual(ReadingPrivate('test_private1'), (100, 500))

        RecordingPrivate(37192871947984794179984, 2631782627848746183746378, 'test_private2')
        self.assertEqual(ReadingPrivate('test_private2'), (37192871947984794179984, 2631782627848746183746378))

        RecordingPublic(1002556256, 5005674333, 'test_public1')
        self.assertEqual(ReadingPublic('test_public1'), (1002556256, 5005674333))

        RecordingPublic(56789876545678909876543456789, 456789098765434567890987654, 'test_public2')
        self.assertEqual(ReadingPublic('test_public2'), (56789876545678909876543456789, 456789098765434567890987654))

    def test_MilerRabin(self):
        self.assertEqual(MillerRabin(17, 5), True)
        self.assertEqual(MillerRabin(2000000, 5), False)
        self.assertEqual(MillerRabin(991447, 5), True)
        self.assertEqual(MillerRabin(512731763812328916, 5), False)
        self.assertEqual(MillerRabin(2989937, 5), True)
        self.assertEqual(MillerRabin(255667864302, 5), False)

    def test_Coprime(self):
        self.assertEqual(CoprimeTest(105, 8), True)
        self.assertEqual(CoprimeTest(2988143, 122346), True)
        self.assertEqual(CoprimeTest(10008, 1066), False)
        self.assertEqual(CoprimeTest(36276516732, 114550), False)

    def test_signature(self):
        self.assertEqual(Verif_electronic_signature(Creat_electronic_signature('ArgentinaJamaika5:0'),'ArgentinaJamaika5:0'), "Verification successful!")
        self.assertEqual(Verif_electronic_signature(Creat_electronic_signature('251w61dsdnkbdbsd'), '12345'),'Signature is not valid')
        self.assertEqual(Verif_electronic_signature(Creat_electronic_signature('異體字'), '異體字'),"Verification successful!")
        self.assertEqual(Verif_electronic_signature(Creat_electronic_signature('لَمَّا زرتُ الصين'), 'لَمَّا زرتُ الصين'),'Verification successful!')


    def test_Euler(self):
        self.assertEqual(Euler(1001, 250), 249000)
        self.assertEqual(Euler(1111, 7789), 8644680)
        self.assertEqual(Euler(3529, 3571), 12594960)
        self.assertEqual(Euler(1451, 1229), 1780600)



