# -*- encoding: UTF-8 -*-


class TMatcher:
    def __init__(self, patterns):
        self.patterns = patterns

    @classmethod
    def __distance(cls, str1, str2):
        d = dict()
        for i in range(len(str1) + 1):
            d[i] = dict()
            d[i][0] = i
        for i in range(len(str2) + 1):
            d[0][i] = i
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                d[i][j] = min(d[i][j - 1] + 1, d[i - 1][j] + 1, d[i - 1][j - 1] + (not str1[i - 1] == str2[j - 1]))
        return d[len(str1)][len(str2)]

    def process(self, candidate):
        candidate = candidate.lower()
        tokens = candidate.split()
        index = 0
        for state in self.patterns.get_states():
            match, target_position = self.__match(tokens, state.split(), index)
            if match:
                for target_index in self.patterns.get_valid_target_for_state(state):
                    for target in self.patterns.get_lexical_for_target(state, target_index):
                        match, position_index = self.__match(tokens, target.split(), target_position)
                        if match:
                            location = self.patterns.has_locations(state, target_index, target)
                            if location:
                                if position_index < len(tokens):
                                    for location in self.patterns.get_locations(state, target_index, target):
                                        match, loc_index = self.__match(tokens, location.split(), position_index)
                                        if match:
                                            return self.patterns.get_target(state, target_index, target, location)
                                return None
                            else:
                                return self.patterns.get_target(state, target_index, target)
        return None

    def __match(self, tokens, target, start):
        ltokens = len(tokens) - 1
        for tt in target:
            while True:
                dd = TMatcher.__distance(tokens[start], tt)
                if dd > len(tt)/2:
                    if len(tokens[start]) <= 3 and start < ltokens:
                        start += 1
                        continue
                    return False, None
                else:
                    break
            start += 1
        return True, start
