
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
## NOTE: This module was autogenerated. ##
## Contains no user-servicable parts!!! ##
##########################################

# Temporary imports for hack, will be reworked once this becomes a package!!!
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..')) 
# End of hack

import unittest

from verb_output import is_past_part

class TestVerbIsPastPart(unittest.TestCase):
    # test_args has the format [{
    #    "in":     ..., # (required)
    #    "out":    ..., # (required)
    #    "desc":   ..., # (optional) 
    #    "kwargs": ...  # (optional)
    # }, ...
    # ]
    test_args = [
        {'in': 'abided', 'out': True},
        {'in': 'ached', 'out': True},
        {'in': 'arisen', 'out': True},
        {'in': 'asked', 'out': True},
        {'in': 'avalanched', 'out': True},
        {'in': 'awoken', 'out': True},
        {'in': 'beaten', 'out': True},
        {'in': 'become', 'out': True},
        {'in': 'been', 'out': True},
        {'in': 'begotten', 'out': True},
        {'in': 'begun', 'out': True},
        {'in': 'beheld', 'out': True},
        {'in': 'bellyached', 'out': True},
        {'in': 'bent', 'out': True},
        {'in': 'bet', 'out': True},
        {'in': 'bitten', 'out': True},
        {'in': 'bled', 'out': True},
        {'in': 'blitzed', 'out': True},
        {'in': 'blown', 'out': True},
        {'in': 'bound', 'out': True},
        {'in': 'bred', 'out': True},
        {'in': 'broken', 'out': True},
        {'in': 'brought', 'out': True},
        {'in': 'built', 'out': True},
        {'in': 'burnt', 'out': True},
        {'in': 'burst', 'out': True},
        {'in': 'bust', 'out': True},
        {'in': 'cached', 'out': True},
        {'in': 'caught', 'out': True},
        {'in': 'changed', 'out': True},
        {'in': 'chosen', 'out': True},
        {'in': 'clapped', 'out': True},
        {'in': 'clung', 'out': True},
        {'in': 'come', 'out': True},
        {'in': 'continued', 'out': True},
        {'in': 'cost', 'out': True},
        {'in': 'creched', 'out': True},
        {'in': 'crept', 'out': True},
        {'in': 'dared', 'out': True},
        {'in': 'dealt', 'out': True},
        {'in': 'died', 'out': True},
        {'in': 'dived', 'out': True},
        {'in': 'douched', 'out': True},
        {'in': 'dragged', 'out': True},
        {'in': 'dreamed', 'out': True},
        {'in': 'driven', 'out': True},
        {'in': 'drunk', 'out': True},
        {'in': 'dug', 'out': True},
        {'in': 'dwelt', 'out': True},
        {'in': 'eaten', 'out': True},
        {'in': 'expected', 'out': True},
        {'in': 'fallen', 'out': True},
        {'in': 'felt', 'out': True},
        {'in': 'fled', 'out': True},
        {'in': 'flown', 'out': True},
        {'in': 'flung', 'out': True},
        {'in': 'followed', 'out': True},
        {'in': 'forbidden', 'out': True},
        {'in': 'foreseen', 'out': True},
        {'in': 'foretold', 'out': True},
        {'in': 'forgiven', 'out': True},
        {'in': 'forgotten', 'out': True},
        {'in': 'forsaken', 'out': True},
        {'in': 'fought', 'out': True},
        {'in': 'found', 'out': True},
        {'in': 'gilded', 'out': True},
        {'in': 'given', 'out': True},
        {'in': 'gone', 'out': True},
        {'in': 'gotten', 'out': True},
        {'in': 'ground', 'out': True},
        {'in': 'had', 'out': True},
        {'in': 'happened', 'out': True},
        {'in': 'held', 'out': True},
        {'in': 'helped', 'out': True},
        {'in': 'hewn', 'out': True},
        {'in': 'hit', 'out': True},
        {'in': 'hurt', 'out': True},
        {'in': 'inlaid', 'out': True},
        {'in': 'insisted', 'out': True},
        {'in': 'interlaid', 'out': True},
        {'in': 'irised', 'out': True},
        {'in': 'kept', 'out': True},
        {'in': 'killed', 'out': True},
        {'in': 'knelt', 'out': True},
        {'in': 'knitted', 'out': True},
        {'in': 'known', 'out': True},
        {'in': 'laid', 'out': True},
        {'in': 'lain', 'out': True},
        {'in': 'leaned', 'out': True},
        {'in': 'leapt', 'out': True},
        {'in': 'learned', 'out': True},
        {'in': 'led', 'out': True},
        {'in': 'left', 'out': True},
        {'in': 'liked', 'out': True},
        {'in': 'lived', 'out': True},
        {'in': 'looked', 'out': True},
        {'in': 'lost', 'out': True},
        {'in': 'loved', 'out': True},
        {'in': 'meant', 'out': True},
        {'in': 'menued', 'out': True},
        {'in': 'met', 'out': True},
        {'in': 'misled', 'out': True},
        {'in': 'mistaken', 'out': True},
        {'in': 'misunderstood', 'out': True},
        {'in': 'moved', 'out': True},
        {'in': 'needed', 'out': True},
        {'in': 'niched', 'out': True},
        {'in': 'overdrawn', 'out': True},
        {'in': 'overheard', 'out': True},
        {'in': 'overtaken', 'out': True},
        {'in': 'preset', 'out': True},
        {'in': 'proved', 'out': True},
        {'in': 'proven', 'out': True},
        {'in': 'provided', 'out': True},
        {'in': 'psyched', 'out': True},
        {'in': 'put', 'out': True},
        {'in': 'quit', 'out': True},
        {'in': 'quizzed', 'out': True},
        {'in': 'reached', 'out': True},
        {'in': 'remained', 'out': True},
        {'in': 'remembered', 'out': True},
        {'in': 'rent', 'out': True},
        {'in': 'rid', 'out': True},
        {'in': 'ridden', 'out': True},
        {'in': 'risen', 'out': True},
        {'in': 'riven', 'out': True},
        {'in': 'run', 'out': True},
        {'in': 'rung', 'out': True},
        {'in': 'sat', 'out': True},
        {'in': 'sawn', 'out': True},
        {'in': 'seemed', 'out': True},
        {'in': 'shaken', 'out': True},
        {'in': 'shaved', 'out': True},
        {'in': 'shed', 'out': True},
        {'in': 'shitted', 'out': True},
        {'in': 'shod', 'out': True},
        {'in': 'shown', 'out': True},
        {'in': 'shrunk', 'out': True},
        {'in': 'skied', 'out': True},
        {'in': 'slain', 'out': True},
        {'in': 'slid', 'out': True},
        {'in': 'slit', 'out': True},
        {'in': 'slunk', 'out': True},
        {'in': 'smelled', 'out': True},
        {'in': 'smitten', 'out': True},
        {'in': 'sneaked', 'out': True},
        {'in': 'sought', 'out': True},
        {'in': 'sown', 'out': True},
        {'in': 'spat', 'out': True},
        {'in': 'sped', 'out': True},
        {'in': 'spent', 'out': True},
        {'in': 'spoiled', 'out': True},
        {'in': 'spoken', 'out': True},
        {'in': 'sprung', 'out': True},
        {'in': 'staved', 'out': True},
        {'in': 'stayed', 'out': True},
        {'in': 'stolen', 'out': True},
        {'in': 'stood', 'out': True},
        {'in': 'stopped', 'out': True},
        {'in': 'strewn', 'out': True},
        {'in': 'stripped', 'out': True},
        {'in': 'strived', 'out': True},
        {'in': 'strode', 'out': True},
        {'in': 'stung', 'out': True},
        {'in': 'stunk', 'out': True},
        {'in': 'sublet', 'out': True},
        {'in': 'sunburned', 'out': True},
        {'in': 'sung', 'out': True},
        {'in': 'sunk', 'out': True},
        {'in': 'sweated', 'out': True},
        {'in': 'swept', 'out': True},
        {'in': 'swollen', 'out': True},
        {'in': 'sworn', 'out': True},
        {'in': 'swum', 'out': True},
        {'in': 'swung', 'out': True},
        {'in': 'talked', 'out': True},
        {'in': 'thrived', 'out': True},
        {'in': 'thrust', 'out': True},
        {'in': 'torn', 'out': True},
        {'in': 'trodden', 'out': True},
        {'in': 'undergone', 'out': True},
        {'in': 'understood', 'out': True},
        {'in': 'undertaken', 'out': True},
        {'in': 'upset', 'out': True},
        {'in': 'vexed', 'out': True},
        {'in': 'waited', 'out': True},
        {'in': 'walked', 'out': True},
        {'in': 'wanted', 'out': True},
        {'in': 'watched', 'out': True},
        {'in': 'wended', 'out': True},
        {'in': 'wept', 'out': True},
        {'in': 'withdrawn', 'out': True},
        {'in': 'withheld', 'out': True},
        {'in': 'withstood', 'out': True},
        {'in': 'woken', 'out': True},
        {'in': 'won', 'out': True},
        {'in': 'worn', 'out': True},
        {'in': 'wrung', 'out': True},
    ]

    def test_is_past_part(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"is_past_part({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": dict()
                }}
                self.assertEqual(is_past_part(test_case["in"], **test_case["kwargs"]), test_case["out"], test_case["desc"])

if __name__ == "__main__":
    unittest.main()
