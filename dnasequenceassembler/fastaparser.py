MAX_SEQUENCE_LENGTH = 1000
MAX_SEQUENCES = 50
WARNING_SEQUENCE_LENTH_EXCEEDED = "WARNING: This DNA assembly library may not work well with sequences over 1000 bases"
WARNING_MAX_SEQUENCES_EXCEEDED = "WARNING: This DNA assembly library may not work well with over 50 sequences"


class FASTAparser():
    """
    input: text file with dna sequences in FASTA format_filename
    output: a list of strings. each string being a sequence
    """

    def __init__(self, fasta_file):
        self.fasta_file =fasta_file

    def parse(self):

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
                    if len(''.join(sequence)) > MAX_SEQUENCE_LENGTH:
                        print WARNING_SEQUENCE_LENTH_EXCEEDED
                sequence = []
            elif ("A" in line or "T" in line or "C" in line or "G" in line):
                sequence.append(line.strip())
        sequences.append(''.join(sequence))
        if len(''.join(sequence)) > MAX_SEQUENCE_LENGTH:
            print WARNING_SEQUENCE_LENTH_EXCEEDED

        if len(sequences) > MAX_SEQUENCES:
            print WARNING_MAX_SEQUENCES_EXCEEDED

        return sequences
