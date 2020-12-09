# -*- encoding: utf8 -*-

from .target import TTarget


class TPatterns:
    def __init__(self):
        self.patterns = {}

    def add_match(self, element_target, element_state, literal_state, literal_target, literal_position=[None]):
        positions = {}
        for position in literal_position:
            target = TTarget(element_target, element_state, position)
            positions[position] = target

        literals = {}
        for literal in literal_target:
            literals[literal] = positions

        for literal_state_elem in literal_state:
            if literal_state_elem not in self.patterns:
                self.patterns[literal_state_elem] = []
            self.patterns[literal_state_elem].append(literals)

    def get_states(self):
        for state in self.patterns.keys():
            yield state

    def get_valid_target_for_state(self, state):
        for target in range(len(self.patterns[state])):
            yield target

    def get_lexical_for_target(self, state, target_index):
        for target in self.patterns[state][target_index].keys():
            yield target

    def has_locations(self, state, target_index, target):
        return None not in self.patterns[state][target_index][target]

    def get_target(self, state, target_index, target, location=None):
        return self.patterns[state][target_index][target][location]

    def get_locations(self, state, target_index, target):
        for key in self.patterns[state][target_index][target]:
            yield key

