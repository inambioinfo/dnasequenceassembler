import unittest

sequences = [
    'ATTAGACCTG',
    'CCTGCCGGAA'
]

top_ranges_dict = {0: (3, 8), 1: (3, 8), 2: (3, 8)}
bottom_ranges_dict = {1: (0, 5), 2: (0, 5), 3: (0, 5)}
top_seq_dict = {0: {'match_bottom': 2},
                1: {'match_bottom': 3},
                2: {'match_bottom': 1}}
bottom_seq_dict = {1: {'match_top': 2},
                   2: {'match_top': 0},
                   3: {'match_top': 1}}


class TestAssembler(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_matches(self):
        from assembler import Assembler
        a = Assembler(sequences)

        a.find_matches()
        self.assertEqual(a.top_ranges_dict()[0], (3,8))
