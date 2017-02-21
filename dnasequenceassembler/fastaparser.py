
class FASTAparser():
    """
    input: text file with dna sequences in FASTA format_filename
    output: a list of strings. each string being a sequence
    """

    def __init__(self, fasta_file):
        self.fasta_file =fasta_file

    def parse(self):
        # TODO check that there are no more than 50 sequences
        # TODO make sure sequences don't exceed 1000 characters
        with open(self.fasta_file) as file:
            content = file.readlines()

        sequences = []
        sequence_ids = []
        sequence = []
        for line in content:
            if line.startswith('>'):
                sequence_ids.append(line.strip())
                if len(sequence) != 0:
                    sequences.append(''.join(sequence))
                sequence = []
            elif ("A" in line or "T" in line or "C" in line or "G" in line):
                sequence.append(line.strip())
        sequences.append(''.join(sequence))
        # for sequence in sequences:
        #     print len(''.join(sequence))


        # import ipdb; ipdb.set_trace()
        return sequences
