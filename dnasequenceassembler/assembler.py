
class Assembler():
    """
    input: list of strings. each string is a sequences
    output: one string
    """
    MATCHING_TOP_KEY = 'match_top'
    MATCHING_BOTTOM_KEY = 'match_bottom'

    def __init__(self,sequences):
        self.sequences = sequences
        self.seqs = {}
        for idx, sequence in enumerate(self.sequences):
            self.seqs[idx] = list(sequence)


    def _find_matching_pairs(self):
        '''
        finds pairs of sequences that overlap with each other

        creates the following variables:
            top_seq_dict
            bottom_seq_dict
            top_ranges_dict
            bottom_ranges_dict
        '''
        top_seq_dict = {}
        bottom_seq_dict = {}
        top_ranges_dict = {}
        bottom_ranges_dict = {}

        num_sequences = len(self.sequences)
        match_id = 0

        for top_index in range(0, num_sequences):
            # print 'top_index', top_index
            for bottom_index in range(0, num_sequences):
                if top_index != bottom_index:
                    top_seq = self.seqs[top_index]
                    bottom_seq = self.seqs[bottom_index]
                    top_len = len(top_seq)
                    bottom_len = len(bottom_seq)
                    self.min_match_length = (max(top_len, bottom_len) / 2) + 1

                    x = 0
                    x_stop = x + self.min_match_length
                    while x_stop <= top_len:
                        top_string = top_seq[x: x_stop]
                        # print 'TOP'
                        # print ''.join(top_string)

                        y = 0
                        y_stop = y + self.min_match_length
                        while y_stop <= bottom_len:
                            bottom_string = bottom_seq[y: y_stop]
                            # print ''.join(bottom_string)

                            if ''.join(top_string) == ''.join(bottom_string):
                                # print '[x: x_stop]', x, x_stop
                                # print '[y: y_stop]', y, y_stop
                                top_seq_dict[top_index] = {
                                    Assembler.MATCHING_BOTTOM_KEY: bottom_index
                                }

                                bottom_seq_dict[bottom_index] = {
                                    Assembler.MATCHING_TOP_KEY: top_index
                                }

                                top_ranges_dict[top_index] = (x, x_stop)
                                bottom_ranges_dict[bottom_index] = (y, y_stop)
                                #TODO: account for almost identical sequences
                                #TODO: FIGURE OUT WHEN TO BREAK

                            y +=1
                            y_stop +=1

                        x+=1
                        x_stop +=1


        return top_seq_dict, bottom_seq_dict, top_ranges_dict, bottom_ranges_dict


    def _determine_order(self, top_seq_dict, bottom_seq_dict, top_ranges_dict, bottom_ranges_dict):
        '''
        determines the order of the sequences using the matching pairs info

        generates the following variables:
            order

        '''

        # print 'top_seq_dict', top_seq_dict
        # print "bottom_seq_dict", bottom_seq_dict
        # print "top_ranges_dict", top_ranges_dict
        # print "bottom_ranges_dict", bottom_ranges_dict
        #start with one pair
        first_seq_id = 0
        if first_seq_id in bottom_seq_dict:
            first_match = bottom_seq_dict[first_seq_id]
            order= [first_match[Assembler.MATCHING_TOP_KEY], first_seq_id]
        elif first_seq_id in top_seq_dict:
            first_match = top_seq_dict[first_seq_id]
            order = [first_seq_id, first_match[Assembler.MATCHING_BOTTOM_KEY]]

        while len(order) != len(self.sequences):
            end = order[-1]
            start = order[0]
            if end in top_seq_dict:
                order.append(top_seq_dict[end][Assembler.MATCHING_BOTTOM_KEY])
            elif start in bottom_seq_dict:
                order.insert(0,bottom_seq_dict[start][Assembler.MATCHING_TOP_KEY])

        print 'order', order
        return order

    def assemble(self):
        '''
        assembles the sequence given the info on the pairs and the order
        '''
        top_seq_dict, bottom_seq_dict, top_ranges_dict, bottom_ranges_dict = \
            self._find_matching_pairs()
        order = self._determine_order(top_seq_dict, bottom_seq_dict, top_ranges_dict, bottom_ranges_dict)

        start_seq_index = order[0]

        range_first_seq = top_ranges_dict[start_seq_index]
        stop = range_first_seq[1]
        self.sequence = self.seqs[start_seq_index][0:stop]
        # import ipdb; ipdb.set_trace()

        for seq_id in order[1:]:
            start = bottom_ranges_dict[seq_id][1]

            if seq_id == order[-1]:
                segment_to_add = self.seqs[seq_id][start:]
            else:
                end = top_ranges_dict[seq_id][1]
                segment_to_add = self.seqs[seq_id][start:end]

            for b in segment_to_add:
                self.sequence.append(b)

        "Resulting assembled sequence"
        print ''.join(self.sequence)
        return ''.join(self.sequence)
