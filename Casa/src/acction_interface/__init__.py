# -*- encoding: utf8 -*-

import os
import xml.etree.ElementTree

from .pattern import TPatterns
from .matcher import TMatcher


def load_config_file(file_path):
    if os.path.isfile(file_path):
        xml_file = xml.etree.ElementTree.parse(file_path)
        root = xml_file.getroot()
        patterns = TPatterns()
        for target_elem in root.iter("target"):
            target_value = target_elem.attrib["name"]
            target_positions = set()
            target_literals = {target_elem.attrib["name"]}
            positions = target_elem.find("positions")
            if positions:
                for position in positions.iter("position"):
                    target_positions.add(position.attrib["place"])
            else:
                target_positions.add(None)
            literals = target_elem.find("literals")
            if literals:
                for literal in literals.iter("literal"):
                    target_literals.add(literal.attrib["text"])
            states = target_elem.find("states")
            if states:
                for state_elem in states.iter("state"):
                    state_obj = state_elem.attrib["name"]
                    state_literals = set()
                    literals = state_elem.find("literals")
                    if literals:
                        for literal in literals.iter("literal"):
                            state_literals.add(literal.attrib["text"])
                    else:
                        state_literals.add(state_elem.attrib["name"])
                    patterns.add_match(target_value, state_obj, state_literals, target_literals, target_positions)

            else:
                raise IOError("Invalid file format. Found a target without states")
        return patterns
    else:
        raise IOError("Invalid file path.")


