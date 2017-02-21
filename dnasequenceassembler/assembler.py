import pprint
class Assembler():
    """
    input: list of strings. each string is a sequences
    output: one string
    """
    MATCHING_TOP_KEY = 'match_top'
    MATCHING_BOTTOM_KEY = 'match_bottom'

    def __init__(self,sequences):
        self.sequences = sequences
        self.top_seq_dict = {}
        self.bottom_seq_dict = {}
        self.top_ranges_dict = {}
        self.bottom_ranges_dict = {}

    def top_ranges_dict(self):
        return self.top_ranges_dict

    def find_matches(self):
        '''
        must keep track of each sequence
              CCTGCCGGAA
        0123456789012345678
        ATTAGACCTG

           0123456789
           AGACCTGCCGG

              0123456789
              CCTGCCGGAA

                 0123456789
                 GCCGGAATAC
        ATTAGACCTGCCGGAATAC
        ATTAGACCTGCCGGAATAC
        '''
        self.seqs = {}

        for idx, sequence in enumerate(self.sequences):
            self.seqs[idx] = list(sequence)

        num_sequences = len(self.sequences)
        match_id = 0

        for top_index in range(0, num_sequences):
            match = False
            for bottom_index in range(0, num_sequences):
                if top_index != bottom_index and not match:
                    # print "matching %s VS %s" % (str(top_index), str(bottom_index))
                    top_seq = self.seqs[top_index]
                    bottom_seq = self.seqs[bottom_index]
                    top_len = len(top_seq)
                    bottom_len = len(bottom_seq)
                    self.min_match_length = max(top_len, bottom_len) / 2

                    # matches = [("0":[3,8],"2":[0,3]), ...]
                    for top_base in range(0, top_len - self.min_match_length):
                        top_base_index = top_base
                        bottom_base_index = 0

                        for bottom_base in range(0, self.min_match_length):
                            if top_seq[top_base_index] == bottom_seq[bottom_base_index]:
                                top_base_index += 1
                                bottom_base_index += 1
                                if bottom_base == (self.min_match_length - 1):
                                    match = True

                                    self.top_seq_dict[top_index] = {
                                        Assembler.MATCHING_BOTTOM_KEY: bottom_index
                                    }

                                    self.bottom_seq_dict[bottom_index] = {
                                        Assembler.MATCHING_TOP_KEY: top_index
                                    }

                                    self.top_ranges_dict[top_index] = (top_base, top_base_index)
                                    self.bottom_ranges_dict[bottom_index] = (0, bottom_base_index)
                                    match_id += 1

                            else:
                                break
        pp = pprint.PrettyPrinter()
        pp.pprint(self.top_ranges_dict)
        pp.pprint(self.bottom_ranges_dict)
        pp = pprint.PrettyPrinter(width=4)
        pp.pprint(self.top_seq_dict)
        pp.pprint(self.bottom_seq_dict)

        self.total_matches = match_id

    def assemble(self):

        self.find_matches()

        #start with one
        first_seq_id = 0

        if first_seq_id in self.bottom_seq_dict:
            first_match = self.bottom_seq_dict[first_seq_id]
            self.order = [first_match[Assembler.MATCHING_TOP_KEY], first_seq_id]
        elif first_seq_id in self.top_seq_dict:
            first_match = self.top_seq_dict[first_seq_id]
            self.order = [first_seq_id, first_match[Assembler.MATCHING_BOTTOM_KEY]]

        while len(self.order) != len(self.sequences):
            end = self.order[-1]
            start = self.order[0]
            if end in self.top_seq_dict:
                self.order.append(self.top_seq_dict[end][Assembler.MATCHING_BOTTOM_KEY])
            elif start in self.bottom_seq_dict:
                self.order.insert(0,self.bottom_seq_dict[start][Assembler.MATCHING_TOP_KEY])

        print self.order
        self.figure_out_sequence()

    def figure_out_sequence(self):
        start_seq_index = 0

        range_first_seq = self.top_ranges_dict[start_seq_index]
        stop = range_first_seq[1]
        self.sequence = self.seqs[start_seq_index][0:stop]

        for seq_id in self.order[1:]:
            start = self.bottom_ranges_dict[seq_id][1]

            if seq_id == self.order[-1]:
                segment_to_add = self.seqs[seq_id][start:]
            else:
                end = self.top_ranges_dict[seq_id][1]
                segment_to_add = self.seqs[seq_id][start:end]

            for b in segment_to_add:
                self.sequence.append(b)

        print "Assembled Response"
        print ''.join(self.sequence)
