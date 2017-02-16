
class Aligner():
    """
    input: list of strings. each string is a sequences
    output: one string
    """

    def __init__(self,sequences):
        self.sequences = sequences

    def align(self):
        seqs = {}
        for idx, sequence in enumerate(self.sequences):
            sequence_dict = {}
            for i, base in enumerate(list(sequence)):
                sequence_dict[i] = base
            seqs[idx] = sequence_dict
        print seqs

        #match 2 sequences
        X = seqs[0]
        for Y in seqs:
            if not seq == seq[0]:
                len_X = len(X)
                len_Y = len(Y)
                min_match_length = max(len_X, len_Y) / 2
        #match
                # now we have two sequences
                # pick the larger one to match the smaller one to.
                # match until it matches for more than half the length of
                # the larger sequence
                X_X



        #save
