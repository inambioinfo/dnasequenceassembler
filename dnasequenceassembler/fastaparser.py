
class FASTAparser():
    """
    input: text file with dna sequences in FASTA format_filename
    output: a list of strings. each string being a sequence
    """

    def __init__(self, fasta_file):
        self.fasta_file =fasta_file

    def parse(self):
        # TODO assume sequences are multiple lines
        # TODO check that there are no more than 50 sequences
        # TODO make sure sequences don't exceed 1000 characters
        with open(self.fasta_file) as file:
            content = file.readlines()

        sequences = []
        for line in content:
            if not line.startswith('>') and ("A" in line or "T" in line or "C" in line or "G" in line):
                sequences.append(line.strip())

        return sequences
