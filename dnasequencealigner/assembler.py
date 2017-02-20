
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
        ATTAGACCTG
           AGACCTGCCG
              CCTGCCGGAA
                 GCCGGAATAC
        ATTAGACCTGCCGGAATAC
        '''
        seqs = {}

        for idx, sequence in enumerate(self.sequences):
            seqs[idx] = list(sequence)
        print seqs

        num_sequences = len(seqs)
        matches = []
        for index_a in range(0,num_sequences):
            match = False
            for index_b in range(0,num_sequences):
                if index_a != index_b and not match:
                    # print "matching %s VS %s" % (str(index_a), str(index_b))
                    x = seqs[index_a]
                    y = seqs[index_b]
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
                                    matches.append(
                                        (
                                            (index_a, (base, x_index)),
                                            (index_b, (0, y_index))
                                        )

                                    )

                            else:
                                break
        return matches

    def assemble(self):

        matches = self.find_matches()
        for index, match in enumerate(matches):
            print "%s_match" % str(index)
            for d in match:
                print d

        # start with the first one

        first_match = matches[0]
        print "first_match", first_match
        second = first_match[1][0]
        print "second", second

        order = [match[0], match[1]]
        #look through all the seconds to find the one that matches

        for match in matches[1:]:
            potential_match = match[0][1]
            print "potential_match", potential_match
            print "hello", second, potential_match
            if second == potential_match:
                order.append(match[1])
                break
        print order
        #when do we stop: when we have as many matches in the order as we have  segments
