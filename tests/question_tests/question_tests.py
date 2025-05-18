#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
#from src.question_a.question_a import test_config
from src.question_b import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_most_likely_ancestor_consensus(self):

        dna_string1 = "GATGCATGCAATGC"
        dna_string2 = "ATAT"

        position1, position2, position3 = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        result = [1, 4, 10]

        self.assertEqual(position1, position2, position3 = result)

        

