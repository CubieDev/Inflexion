
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

from verb_output import is_pres_part

class TestVerbIsPresPart(unittest.TestCase):
    # test_args has the format [{
    #    "in":     ..., # (required)
    #    "out":    ..., # (required)
    #    "desc":   ..., # (optional) 
    #    "kwargs": ...  # (optional)
    # }, ...
    # ]
    test_args = [
        {'in': 'abiding', 'out': True},
        {'in': 'aching', 'out': True},
        {'in': 'arising', 'out': True},
        {'in': 'asking', 'out': True},
        {'in': 'avalanching', 'out': True},
        {'in': 'awakening', 'out': True},
        {'in': 'beating', 'out': True},
        {'in': 'becoming', 'out': True},
        {'in': 'begetting', 'out': True},
        {'in': 'beginning', 'out': True},
        {'in': 'beholding', 'out': True},
        {'in': 'being', 'out': True},
        {'in': 'bellyaching', 'out': True},
        {'in': 'bending', 'out': True},
        {'in': 'betting', 'out': True},
        {'in': 'binding', 'out': True},
        {'in': 'biting', 'out': True},
        {'in': 'bleeding', 'out': True},
        {'in': 'blitzing', 'out': True},
        {'in': 'blowing', 'out': True},
        {'in': 'breaking', 'out': True},
        {'in': 'breeding', 'out': True},
        {'in': 'bringing', 'out': True},
        {'in': 'building', 'out': True},
        {'in': 'burning', 'out': True},
        {'in': 'bursting', 'out': True},
        {'in': 'busting', 'out': True},
        {'in': 'caching', 'out': True},
        {'in': 'catching', 'out': True},
        {'in': 'changing', 'out': True},
        {'in': 'choosing', 'out': True},
        {'in': 'clapping', 'out': True},
        {'in': 'clinging', 'out': True},
        {'in': 'coming', 'out': True},
        {'in': 'continuing', 'out': True},
        {'in': 'costing', 'out': True},
        {'in': 'creching', 'out': True},
        {'in': 'creeping', 'out': True},
        {'in': 'daring', 'out': True},
        {'in': 'dealing', 'out': True},
        {'in': 'digging', 'out': True},
        {'in': 'diving', 'out': True},
        {'in': 'douching', 'out': True},
        {'in': 'dragging', 'out': True},
        {'in': 'dreaming', 'out': True},
        {'in': 'drinking', 'out': True},
        {'in': 'driving', 'out': True},
        {'in': 'dwelling', 'out': True},
        {'in': 'dying', 'out': True},
        {'in': 'eating', 'out': True},
        {'in': 'expecting', 'out': True},
        {'in': 'falling', 'out': True},
        {'in': 'feeling', 'out': True},
        {'in': 'fighting', 'out': True},
        {'in': 'finding', 'out': True},
        {'in': 'fleeing', 'out': True},
        {'in': 'flinging', 'out': True},
        {'in': 'flying', 'out': True},
        {'in': 'following', 'out': True},
        {'in': 'forbidding', 'out': True},
        {'in': 'foreseeing', 'out': True},
        {'in': 'foretelling', 'out': True},
        {'in': 'forgetting', 'out': True},
        {'in': 'forgiving', 'out': True},
        {'in': 'forsaking', 'out': True},
        {'in': 'getting', 'out': True},
        {'in': 'gilding', 'out': True},
        {'in': 'giving', 'out': True},
        {'in': 'going', 'out': True},
        {'in': 'grinding', 'out': True},
        {'in': 'happening', 'out': True},
        {'in': 'having', 'out': True},
        {'in': 'helping', 'out': True},
        {'in': 'hewing', 'out': True},
        {'in': 'hitting', 'out': True},
        {'in': 'holding', 'out': True},
        {'in': 'hurting', 'out': True},
        {'in': 'inlaying', 'out': True},
        {'in': 'insisting', 'out': True},
        {'in': 'interlaying', 'out': True},
        {'in': 'irising', 'out': True},
        {'in': 'keeping', 'out': True},
        {'in': 'killing', 'out': True},
        {'in': 'kneeling', 'out': True},
        {'in': 'knitting', 'out': True},
        {'in': 'knowing', 'out': True},
        {'in': 'laying', 'out': True},
        {'in': 'leading', 'out': True},
        {'in': 'leaning', 'out': True},
        {'in': 'leaping', 'out': True},
        {'in': 'learning', 'out': True},
        {'in': 'leaving', 'out': True},
        {'in': 'liking', 'out': True},
        {'in': 'living', 'out': True},
        {'in': 'looking', 'out': True},
        {'in': 'losing', 'out': True},
        {'in': 'loving', 'out': True},
        {'in': 'lying', 'out': True},
        {'in': 'meaning', 'out': True},
        {'in': 'meeting', 'out': True},
        {'in': 'menuing', 'out': True},
        {'in': 'misleading', 'out': True},
        {'in': 'mistaking', 'out': True},
        {'in': 'misunderstanding', 'out': True},
        {'in': 'moving', 'out': True},
        {'in': 'needing', 'out': True},
        {'in': 'nicheing', 'out': True},
        {'in': 'overdrawing', 'out': True},
        {'in': 'overhearing', 'out': True},
        {'in': 'overtaking', 'out': True},
        {'in': 'presetting', 'out': True},
        {'in': 'providing', 'out': True},
        {'in': 'proving', 'out': True},
        {'in': 'psyching', 'out': True},
        {'in': 'putting', 'out': True},
        {'in': 'quitting', 'out': True},
        {'in': 'quizzing', 'out': True},
        {'in': 'reaching', 'out': True},
        {'in': 'remaining', 'out': True},
        {'in': 'remembering', 'out': True},
        {'in': 'rending', 'out': True},
        {'in': 'ridding', 'out': True},
        {'in': 'riding', 'out': True},
        {'in': 'ringing', 'out': True},
        {'in': 'rising', 'out': True},
        {'in': 'riving', 'out': True},
        {'in': 'running', 'out': True},
        {'in': 'sawing', 'out': True},
        {'in': 'seeking', 'out': True},
        {'in': 'seeming', 'out': True},
        {'in': 'shaking', 'out': True},
        {'in': 'shaving', 'out': True},
        {'in': 'shedding', 'out': True},
        {'in': 'shitting', 'out': True},
        {'in': 'shoeing', 'out': True},
        {'in': 'showing', 'out': True},
        {'in': 'shrinking', 'out': True},
        {'in': 'singing', 'out': True},
        {'in': 'sinking', 'out': True},
        {'in': 'sitting', 'out': True},
        {'in': 'skiing', 'out': True},
        {'in': 'slaying', 'out': True},
        {'in': 'sliding', 'out': True},
        {'in': 'slinking', 'out': True},
        {'in': 'slitting', 'out': True},
        {'in': 'smelling', 'out': True},
        {'in': 'smiting', 'out': True},
        {'in': 'sneaking', 'out': True},
        {'in': 'sowing', 'out': True},
        {'in': 'speaking', 'out': True},
        {'in': 'speeding', 'out': True},
        {'in': 'spending', 'out': True},
        {'in': 'spitting', 'out': True},
        {'in': 'spoiling', 'out': True},
        {'in': 'springing', 'out': True},
        {'in': 'standing', 'out': True},
        {'in': 'staving', 'out': True},
        {'in': 'staying', 'out': True},
        {'in': 'stealing', 'out': True},
        {'in': 'stinging', 'out': True},
        {'in': 'stinking', 'out': True},
        {'in': 'stopping', 'out': True},
        {'in': 'strewing', 'out': True},
        {'in': 'striding', 'out': True},
        {'in': 'stripping', 'out': True},
        {'in': 'striving', 'out': True},
        {'in': 'subletting', 'out': True},
        {'in': 'sunburning', 'out': True},
        {'in': 'swearing', 'out': True},
        {'in': 'sweating', 'out': True},
        {'in': 'sweeping', 'out': True},
        {'in': 'swelling', 'out': True},
        {'in': 'swimming', 'out': True},
        {'in': 'swinging', 'out': True},
        {'in': 'talking', 'out': True},
        {'in': 'tearing', 'out': True},
        {'in': 'thriving', 'out': True},
        {'in': 'thrusting', 'out': True},
        {'in': 'treading', 'out': True},
        {'in': 'undergoing', 'out': True},
        {'in': 'understanding', 'out': True},
        {'in': 'undertaking', 'out': True},
        {'in': 'upsetting', 'out': True},
        {'in': 'vexing', 'out': True},
        {'in': 'waiting', 'out': True},
        {'in': 'waking', 'out': True},
        {'in': 'walking', 'out': True},
        {'in': 'wanting', 'out': True},
        {'in': 'watching', 'out': True},
        {'in': 'wearing', 'out': True},
        {'in': 'weeping', 'out': True},
        {'in': 'wending', 'out': True},
        {'in': 'winning', 'out': True},
        {'in': 'withdrawing', 'out': True},
        {'in': 'withholding', 'out': True},
        {'in': 'withstanding', 'out': True},
        {'in': 'wringing', 'out': True},
    ]

    def test_is_pres_part(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"is_pres_part({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": dict()
                }}
                self.assertEqual(is_pres_part(test_case["in"], **test_case["kwargs"]), test_case["out"], test_case["desc"])

if __name__ == "__main__":
    unittest.main()