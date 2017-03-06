import copy
import random


class Assembler():
    """
    Assembles string (DNA sequence) given smaller substrings (fragments)

    ...

    Attributes
    ----------
    fragments : dictionary
        dictionary of fragments keyed by index.
    fragment_ids : dictionary
        dictionary of fragment_ids keyed by index.
    print_fragment_id_order : bool
        whether or not to print the order of fragments by their identifier

    Methods
    -------
    assemble()
        returns string that represents assembled sequence

    """


    def __init__(self,fragments, fragment_ids, print_fragment_id_order=False):
        self.fragments = {}
        self.fragment_ids = {}
        self.print_fragment_id_order = print_fragment_id_order
        for idx, fragment in enumerate(fragments):
            self.fragments[idx] = list(fragment)
        for idx, idy in enumerate(fragment_ids):
            self.fragment_ids[idx] = idy


    def _fragment_matcher(self, top_fragment, bottom_fragment):
        """ Determines whether two fragments match
        by more than half of their lengths.

        Parameters
        ----------
        top_fragment : list
        bottom_fragment : list

        Returns
        -------
        bool
        """
        top_len = len(top_fragment)
        bottom_len = len(bottom_fragment)
        min_match_length = (max(top_len, bottom_len) / 2) + 1
        match_found = False
        bottom_string = ''.join(bottom_fragment[0:min_match_length])

        x = 0
        x_stop = x + min_match_length
        while x_stop <= top_len:
            top_string = top_fragment[x: x_stop]
            if ''.join(top_string) == bottom_string:
                match_found = True
                return x
            x +=1
            x_stop +=1

        return False


    def _find_matching_fragment_pairs(self):
        """ Compares each fragment to other fragments and finds matching pairs.

        Returns
        -------
        map_top_bottom : dictionary
        map_bottom_top : dictionary
        """
        map_top_bottom = {}
        map_bottom_top = {}

        for ID_top, top_fragment in self.fragments.iteritems():
            for ID_bottom, bottom_fragment in self.fragments.iteritems():
                if ID_top != ID_bottom:
                    match_index = self._fragment_matcher(top_fragment,
                                                        bottom_fragment)

                    if match_index:
                        map_top_bottom[ID_top] = {
                            'ID_bottom_match' : ID_bottom,
                            'match_index' : match_index
                        }

                        map_bottom_top[ID_bottom] = {
                            'ID_top_match' : ID_top
                        }

        return map_top_bottom, map_bottom_top


    def _determine_order(self, map_top_bottom, map_bottom_top):
        """ Determines order of fragments given matching pair info

        Parameters
        ----------
        map_top_bottom : dictionary
        map_bottom_top : dictionary

        Returns
        -------
        order : list
        """

        order = []

        ID = random.choice(self.fragments.keys())
        if ID in map_bottom_top:
            order = [ map_bottom_top[ID]['ID_top_match'], ID ]
        else:
            order = [ ID, map_top_bottom[ID]['ID_bottom_match']]

        while len(order) < len(self.fragments): # is this one hacky?
            end = order[-1]
            start = order[0]
            if end in map_top_bottom:
                order.append(map_top_bottom[end]['ID_bottom_match'])
            elif start in map_bottom_top:
                order.insert(0, map_bottom_top[start]['ID_top_match'])

        return order


    def assemble(self):
        """ Assembles DNA sequence string by using matching fragment pair maps
        and order

        Returns
        -------
        string
        """

        map_top_bottom, map_bottom_top = self._find_matching_fragment_pairs()
        order = self._determine_order(map_top_bottom, map_bottom_top)

        sequence = self.fragments[order[0]]
        insert_index = 0

        for ID in order[:-1]: # last fragment ID is not in map_top_bottom
            ID_bottom_match = map_top_bottom[ID]['ID_bottom_match']
            match_index = map_top_bottom[ID]['match_index']
            insert_index += match_index
            # print '----'
            # print ''.join(sequence[insert_index: insert_index + 5])
            # print ''.join(self.fragments[ID_bottom_match][0:5])
            sequence[insert_index:] = self.fragments[ID_bottom_match]
            # print '_'*insert_index + ''.join(self.fragments[ID_bottom_match])

        if self.print_fragment_id_order:
            for idx in order:
                print self.fragment_ids[idx]

        # Final result
        return ''.join(sequence)
