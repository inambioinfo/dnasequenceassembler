import unittest
from mock import MagicMock

sequences = [
    'ATTAGACCTG',
    'CCTGCCGGAA',
    'AGACCTGCCGG',
    'GCCGGAATAC'
]

top_ranges_dict = {0: (3, 8), 1: (3, 8), 2: (3, 8)}
bottom_ranges_dict = {1: (0, 5), 2: (0, 5), 3: (0, 5)}
top_seq_dict = {0: {'match_bottom': 2},
                1: {'match_bottom': 3},
                2: {'match_bottom': 1}}
bottom_seq_dict = {1: {'match_top': 2},
                   2: {'match_top': 0},
                   3: {'match_top': 1}}
order = [0, 2, 1, 3]
assembled_seq = 'ATTAGACCTGCCGGAATAC'

class TestAssembler(unittest.TestCase):

    def test_find_matching_pairs(self):
        from assembler import Assembler
        assbl = Assembler(sequences)
        a, b, c, d = assbl._find_matching_pairs()
        self.assertEqual(c, top_ranges_dict)
        self.assertEqual(d, bottom_ranges_dict)
        self.assertEqual(a, top_seq_dict)
        self.assertEqual(b, bottom_seq_dict)


    def test_determine_order(self):
        from assembler import Assembler
        assbl = Assembler(sequences)
        c = top_ranges_dict
        d = bottom_ranges_dict
        a = top_seq_dict
        b = bottom_seq_dict
        o = assbl._determine_order(a,b,c,d)
        self.assertEqual(o, order)

    def test_assemble(self):
        from assembler import Assembler
        assbl = Assembler(sequences)
        assbl._find_matching_pairs = MagicMock(return_value=(top_seq_dict, bottom_seq_dict, top_ranges_dict, bottom_ranges_dict))
        assbl._determine_order = MagicMock(return_value=order)
        self.assertEqual(assbl.assemble(), assembled_seq)


class TestFastaParser(unittest.TestCase):

    def test_fasta_parser(self):
        from fastaparser import FASTAparser
        fap = FASTAparser('dnasequenceassembler/data/sample_input.txt')
        seqs = fap.parse()
        self.assertEqual(seqs, sequences)
