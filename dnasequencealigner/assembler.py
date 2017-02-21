
class Assembler():
    """
    input: list of strings. each string is a sequences
    output: one string
    """

    def __init__(self,sequences):
        self.sequences = sequences

    def find_matches(self):
        '''
        must keep track of each sequence
              CCTGCCGGAA
        0123456789012345678
        ATTAGACCTG

           0123456789
           AGACCTGCCG

              0123456789
              CCTGCCGGAA

                 0123456789
                 GCCGGAATAC
        ATTAGACCTGCCGGAATAC
        '''
        self.seqs = {}

        for idx, sequence in enumerate(self.sequences):
            self.seqs[idx] = list(sequence)

        num_sequences = len(self.sequences)
        match_id = 0
        self.firsts_dict = {}
        self.seconds_dict = {}
        self.firsts_ranges_dict = {}
        self.seconds_ranges_dict = {}
        for index_a in range(0,num_sequences):
            match = False
            for index_b in range(0,num_sequences):
                if index_a != index_b and not match:
                    # print "matching %s VS %s" % (str(index_a), str(index_b))
                    x = self.seqs[index_a]
                    y = self.seqs[index_b]
                    len_x = len(x)
                    len_y = len(y)
                    min_match_length = max(len_x, len_y) / 2
                    x_start = 0
                    y_start = 0

                    # matches = [("0":[3,8],"2":[0,3]), ...]
                    for base in range(0, len_x - min_match_length):
                        x_index = base
                        y_index = 0

                        for i in range(0,min_match_length):
                            if x[x_index] == y[y_index]:
                                x_index += 1
                                y_index += 1
                                if i == (min_match_length - 1):
                                    # print "%s: %s" % (str(index_a), ''.join(x))
                                    # print "%s: %s" % (str(index_b), ''.join(y))
                                    # print "FOUND A MATCH"
                                    # print "%s to %s"  % (base, x_index)
                                    # print x[base:x_index]
                                    # print "0 to %s"  % (y_index)
                                    # print y[0:y_index]
                                    # print
                                    match = True
                                    # firsts_dict:
                                    #     {
                                    #         'sequence_id': {
                                    #             'match_id' : 0,
                                    #             'second': 3
                                    #         }
                                    #
                                    #     }
                                    #
                                    self.firsts_dict[index_a] = {
                                        'match_id': match_id,
                                        'second': index_b
                                    }
                                    # seconds_dict:
                                    #         {
                                    #             'sequence_id': {
                                    #                 'match_id' : 0,
                                    #                 'first': 3
                                    #             }
                                    #         }
                                    #
                                    self.seconds_dict[index_b] = {
                                        'match_id': match_id,
                                        'first': index_a
                                    }
                                    # firsts_ranges_dict:
                                    #         {
                                    #             'sequence_id': (3, 8)
                                    #           }
                                    # seconds_ranges_dict:
                                    #         {
                                    #             'sequence_id': (0, 5)
                                    #           }

                                    self.firsts_ranges_dict[index_a] = (base, x_index)
                                    self.seconds_ranges_dict[index_b] = (0, y_index)
                                    match_id += 1

                            else:
                                break
        self.total_matches = match_id

    def assemble(self):

        self.find_matches()

        #start with one
        first_seq_id = 0

        if first_seq_id in self.seconds_dict:
            first_match = self.seconds_dict[first_seq_id]
            self.order = [first_match['first'], first_seq_id]
        elif first_seq_id in self.firsts_dict:
            first_match = self.firsts_dict[first_seq_id]
            self.order = [first_seq_id, first_match['second']]


        print "Total matches: %s" % str(self.total_matches)
        print "order: ", self.order

        # for k,v in self.firsts_dict.iteritems():
        #     print k, v
        # print
        # for k,v in self.seconds_dict.iteritems():
        #     print k, v
        #first figure out the order of matches then figure out the sequence
        while len(self.order) != len(self.sequences):
            end = self.order[-1]
            start = self.order[0]
            if end in self.firsts_dict:
                self.order.append(self.firsts_dict[end]['second'])
                print "appended at end", self.order
            elif start in self.seconds_dict:
                self.order.insert(0,self.seconds_dict[start]['first'])
                print "appended at beggining", self.order

        print self.order
        self.figure_out_sequence()

    def figure_out_sequence(self):
        start_seq_index = 0

        range_first_seq = self.firsts_ranges_dict[start_seq_index]
        stop = range_first_seq[1]
        self.sequence = self.seqs[start_seq_index][0:stop]

        for seq_id in self.order[1:]:
            start = self.seconds_ranges_dict[seq_id][1]

            if seq_id == self.order[-1]:
                segment_to_add = self.seqs[seq_id][start:]
            else:
                end = self.firsts_ranges_dict[seq_id][1]
                segment_to_add = self.seqs[seq_id][start:end]

            for b in segment_to_add:
                self.sequence.append(b)



        print ''.join(self.sequence)
