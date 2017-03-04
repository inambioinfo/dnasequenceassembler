import copy
import random

class Assembler():
    """
    input: list of strings. each string is a sequences
    output: one string
    """

    def __init__(self,sequences):
        self.bottoms_dict_key = 'bottoms'
        self.indices_dict_key = 'indices'
        self.sequences = sequences
        self.seqs = {}
        for idx, sequence in enumerate(self.sequences):
            self.seqs[idx] = list(sequence)


    def fragment_matcher(self, top_seq, bottom_seq):
        '''
        '''
        top_len = len(top_seq)
        bottom_len = len(bottom_seq)
        min_match_length = (max(top_len, bottom_len) / 2) + 1
        sequences_match = False
        bottom_string = ''.join(bottom_seq[0:min_match_length])
        x = 0
        x_stop = x + min_match_length
        print min_match_length
        while x_stop <= top_len:
            top_string = top_seq[x: x_stop]
            if ''.join(top_string) == bottom_string:
                sequences_match = True
                return x
            x +=1
            x_stop +=1

        return False


    def _find_matching_pairs(self):
        '''
        '''
        map_top_bottom = {}
        map_bottom_top = {}

        num_sequences = len(self.sequences)

        for ID_top in range(0, num_sequences):
            for ID_bottom in range(0, num_sequences):
                if ID_top != ID_bottom:
                    top_seq = self.seqs[ID_top]
                    bottom_seq = self.seqs[ID_bottom]
                    match_index = self.fragment_matcher(top_seq, bottom_seq)
                    if match_index:

                        map_top_bottom[ID_top] = {
                            'ID_bottom_match' : ID_bottom,
                            'match_index' : match_index
                        }

                        map_bottom_top[ID_bottom] = {
                            'ID_top_match' : ID_top
                        }

        print 'TOP_BOTTOM'
        for k,v in map_top_bottom.iteritems():
            print k,v

        print 'BOTTOM_TOP'
        for k,v in map_bottom_top.iteritems():
            print k,v

        return map_top_bottom, map_bottom_top


    def _determine_order(self, map_top_bottom, map_bottom_top):
        '''
        determines the order of the sequences using the matching pairs info

        generates the following variables:
            order
        '''

        order = []

        first_seq_id = random.choice(self.seqs.keys())
        print 'first_seq_id: ', first_seq_id
        if first_seq_id in map_bottom_top:
            order= [ map_bottom_top[first_seq_id]['ID_top_match'], first_seq_id ]
        else:
            order = [first_seq_id, map_top_bottom[first_seq_id]['ID_bottom_match']]

        while len(order) < len(self.seqs): # is this one hacky?
            end = order[-1]
            start = order[0]
            if end in map_top_bottom:
                order.append(map_top_bottom[end]['ID_bottom_match'])
            elif start in map_bottom_top:
                order.insert(0,map_bottom_top[start]['ID_top_match'])

        print 'order', order
        return order


    def assemble(self):
        '''
        assembles the sequence given the info on the pairs and the order
        '''
        map_top_bottom, map_bottom_top = self._find_matching_pairs()
        order = self._determine_order(map_top_bottom, map_bottom_top)

        sequence = self.seqs[order[0]]
        insert_index = 0
        print ''.join(sequence)
        for ID in order[0:-1]:

            ID_bottom_match = map_top_bottom[ID]['ID_bottom_match']
            match_index = map_top_bottom[ID]['match_index']
            insert_index += match_index
            sequence[insert_index:] = self.seqs[ID_bottom_match]
            print '_'*insert_index + ''.join(self.seqs[ID_bottom_match])



        "Resulting assembled sequence"
        print ''.join(sequence)
        return ''.join(sequence)
        #TODO: assumption unique
        #TODO: assumption there will be only one other sequence that will match by more than half the length
        #TODO: do I need to put the sequences into a list?
