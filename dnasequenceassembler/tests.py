import unittest
from mock import MagicMock

sequences = [
    'ATTAGACCTG',
    'CCTGCCGGAA',
    'AGACCTGCCGG',
    'GCCGGAATAC'
]

identifiers = [
    '>Frag_56',
    '>Frag_57',
    '>Frag_58',
    '>Frag_59'
]

map_top_bottom = {0: {'match_index': 3, 'ID_bottom_match': 2}, 1: {'match_index': 3, 'ID_bottom_match': 3}, 2: {'match_index': 3, 'ID_bottom_match': 1}}
map_bottom_top = {1: {'ID_top_match': 2}, 2: {'ID_top_match': 0}, 3: {'ID_top_match': 1}}
order = [0, 2, 1, 3]
assembled_seq = 'ATTAGACCTGCCGGAATAC'

class TestAssembler(unittest.TestCase):

    def test_fragment_matcher(self):
        from assembler import Assembler
        assbl = Assembler(sequences, identifiers)
        assbl._fragment_matcher(['a','b','c'], ['b','c','d'])
        assert assbl._fragment_matcher(['a','b','c'], ['b','c','d'])

    def test_find_matching_fragment_pairs(self):
        from assembler import Assembler
        assbl = Assembler(sequences, identifiers)
        c, d = assbl._find_matching_fragment_pairs()
        self.assertEqual(c, map_top_bottom)
        self.assertEqual(d, map_bottom_top)

    def test_determine_order(self):
        from assembler import Assembler
        assbl = Assembler(sequences, identifiers)
        c = map_top_bottom
        d = map_bottom_top
        o = assbl._determine_order(c,d)
        self.assertEqual(o, order)

    def test_assemble(self):
        from assembler import Assembler
        assbl = Assembler(sequences, identifiers)
        assbl._find_matching_pairs = MagicMock(return_value=(map_top_bottom, map_bottom_top))
        assbl._determine_order = MagicMock(return_value=order)
        self.assertEqual(assbl.assemble(), assembled_seq)


class TestFastaParser(unittest.TestCase):

    def test_fasta_parser(self):
        from fastaparser import FastaParser
        fap = FastaParser('dnasequenceassembler/data/sample_input.txt')
        seqs, ids = fap.parse()
        self.assertEqual(seqs, sequences)
