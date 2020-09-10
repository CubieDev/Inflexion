
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

from verb_output import convert_to_singular

class TestVerbToSingular(unittest.TestCase):
    # test_args has the format [{
    #    "in":     ..., # (required)
    #    "out":    ..., # (required)
    #    "desc":   ..., # (optional) 
    #    "kwargs": ...  # (optional)
    # }, ...
    # ]
    test_args = [
        {'in': '', 'out': 's'},
        {'in': 'abide', 'out': 'abides'},
        {'in': 'ache', 'out': 'aches'},
        {'in': 'are', 'out': 'am'},
        {'in': 'arise', 'out': 'arises'},
        {'in': 'ask', 'out': 'asks'},
        {'in': 'avalanche', 'out': 'avalanches'},
        {'in': 'awake', 'out': 'awakes'},
        {'in': 'beat', 'out': 'beats'},
        {'in': 'become', 'out': 'becomes'},
        {'in': 'beget', 'out': 'begets'},
        {'in': 'begin', 'out': 'begins'},
        {'in': 'behold', 'out': 'beholds'},
        {'in': 'bellyache', 'out': 'bellyaches'},
        {'in': 'bend', 'out': 'bends'},
        {'in': 'bet', 'out': 'bets'},
        {'in': 'bind', 'out': 'binds'},
        {'in': 'bite', 'out': 'bites'},
        {'in': 'bleed', 'out': 'bleeds'},
        {'in': 'blitz', 'out': 'blitzes'},
        {'in': 'blow', 'out': 'blows'},
        {'in': 'break', 'out': 'breaks'},
        {'in': 'breed', 'out': 'breeds'},
        {'in': 'bring', 'out': 'brings'},
        {'in': 'build', 'out': 'builds'},
        {'in': 'burn', 'out': 'burns'},
        {'in': 'burst', 'out': 'bursts'},
        {'in': 'bust', 'out': 'busts'},
        {'in': 'cache', 'out': 'caches'},
        {'in': 'can', 'out': 'can'},
        {'in': 'catch', 'out': 'catches'},
        {'in': 'change', 'out': 'changes'},
        {'in': 'choose', 'out': 'chooses'},
        {'in': 'clap', 'out': 'claps'},
        {'in': 'cling', 'out': 'clings'},
        {'in': 'come', 'out': 'comes'},
        {'in': 'continue', 'out': 'continues'},
        {'in': 'cost', 'out': 'costs'},
        {'in': 'could', 'out': 'could'},
        {'in': 'creche', 'out': 'creches'},
        {'in': 'creep', 'out': 'creeps'},
        {'in': 'dare', 'out': 'dares'},
        {'in': 'deal', 'out': 'deals'},
        {'in': 'die', 'out': 'dies'},
        {'in': 'dig', 'out': 'digs'},
        {'in': 'dive', 'out': 'dives'},
        {'in': 'douche', 'out': 'douches'},
        {'in': 'drag', 'out': 'drags'},
        {'in': 'dream', 'out': 'dreams'},
        {'in': 'drink', 'out': 'drinks'},
        {'in': 'drive', 'out': 'drives'},
        {'in': 'dwell', 'out': 'dwells'},
        {'in': 'eat', 'out': 'eats'},
        {'in': 'expect', 'out': 'expects'},
        {'in': 'fall', 'out': 'falls'},
        {'in': 'feel', 'out': 'feels'},
        {'in': 'fight', 'out': 'fights'},
        {'in': 'find', 'out': 'finds'},
        {'in': 'flee', 'out': 'flees'},
        {'in': 'fling', 'out': 'flings'},
        {'in': 'fly', 'out': 'flies'},
        {'in': 'follow', 'out': 'follows'},
        {'in': 'forbid', 'out': 'forbids'},
        {'in': 'foresee', 'out': 'foresees'},
        {'in': 'foretell', 'out': 'foretells'},
        {'in': 'forget', 'out': 'forgets'},
        {'in': 'forgive', 'out': 'forgives'},
        {'in': 'forsake', 'out': 'forsakes'},
        {'in': 'get', 'out': 'gets'},
        {'in': 'gild', 'out': 'gilds'},
        {'in': 'give', 'out': 'gives'},
        {'in': 'go', 'out': 'goes'},
        {'in': 'grind', 'out': 'grinds'},
        {'in': 'happen', 'out': 'happens'},
        {'in': 'have', 'out': 'has'},
        {'in': 'help', 'out': 'helps'},
        {'in': 'hew', 'out': 'hews'},
        {'in': 'hit', 'out': 'hits'},
        {'in': 'hold', 'out': 'holds'},
        {'in': 'hurt', 'out': 'hurts'},
        {'in': 'inlay', 'out': 'inlays'},
        {'in': 'insist', 'out': 'insists'},
        {'in': 'interlay', 'out': 'interlays'},
        {'in': 'iris', 'out': 'irises'},
        {'in': 'keep', 'out': 'keeps'},
        {'in': 'kill', 'out': 'kills'},
        {'in': 'kneel', 'out': 'kneels'},
        {'in': 'knit', 'out': 'knits'},
        {'in': 'know', 'out': 'knows'},
        {'in': 'lay', 'out': 'lays'},
        {'in': 'lead', 'out': 'leads'},
        {'in': 'lean', 'out': 'leans'},
        {'in': 'leap', 'out': 'leaps'},
        {'in': 'learn', 'out': 'learns'},
        {'in': 'leave', 'out': 'leaves'},
        {'in': 'lie', 'out': 'lies'},
        {'in': 'like', 'out': 'likes'},
        {'in': 'live', 'out': 'lives'},
        {'in': 'look', 'out': 'looks'},
        {'in': 'lose', 'out': 'loses'},
        {'in': 'love', 'out': 'loves'},
        {'in': 'may', 'out': 'may'},
        {'in': 'mean', 'out': 'means'},
        {'in': 'meet', 'out': 'meets'},
        {'in': 'menu', 'out': 'menus'},
        {'in': 'might', 'out': 'might'},
        {'in': 'mislead', 'out': 'misleads'},
        {'in': 'mistake', 'out': 'mistakes'},
        {'in': 'misunderstand', 'out': 'misunderstands'},
        {'in': 'move', 'out': 'moves'},
        {'in': 'must', 'out': 'must'},
        {'in': 'need', 'out': 'needs'},
        {'in': 'niche', 'out': 'niches'},
        {'in': 'ought', 'out': 'ought'},
        {'in': 'overdraw', 'out': 'overdraws'},
        {'in': 'overhear', 'out': 'overhears'},
        {'in': 'overtake', 'out': 'overtakes'},
        {'in': 'preset', 'out': 'presets'},
        {'in': 'prove', 'out': 'proves'},
        {'in': 'provide', 'out': 'provides'},
        {'in': 'psyche', 'out': 'psyches'},
        {'in': 'put', 'out': 'puts'},
        {'in': 'quit', 'out': 'quits'},
        {'in': 'quiz', 'out': 'quizzes'},
        {'in': 'reach', 'out': 'reaches'},
        {'in': 'remain', 'out': 'remains'},
        {'in': 'remember', 'out': 'remembers'},
        {'in': 'rend', 'out': 'rends'},
        {'in': 'rid', 'out': 'rids'},
        {'in': 'ride', 'out': 'rides'},
        {'in': 'ring', 'out': 'rings'},
        {'in': 'rise', 'out': 'rises'},
        {'in': 'rive', 'out': 'rives'},
        {'in': 'run', 'out': 'runs'},
        {'in': 'saw', 'out': 'saws'},
        {'in': 'seek', 'out': 'seeks'},
        {'in': 'seem', 'out': 'seems'},
        {'in': 'shake', 'out': 'shakes'},
        {'in': 'shall', 'out': 'shall'},
        {'in': 'shave', 'out': 'shaves'},
        {'in': 'shed', 'out': 'sheds'},
        {'in': 'shit', 'out': 'shits'},
        {'in': 'shoe', 'out': 'shoes'},
        {'in': 'should', 'out': 'should'},
        {'in': 'show', 'out': 'shows'},
        {'in': 'shrink', 'out': 'shrinks'},
        {'in': 'sing', 'out': 'sings'},
        {'in': 'sink', 'out': 'sinks'},
        {'in': 'sit', 'out': 'sits'},
        {'in': 'ski', 'out': 'skis'},
        {'in': 'slay', 'out': 'slays'},
        {'in': 'slide', 'out': 'slides'},
        {'in': 'slink', 'out': 'slinks'},
        {'in': 'slit', 'out': 'slits'},
        {'in': 'smell', 'out': 'smells'},
        {'in': 'smite', 'out': 'smites'},
        {'in': 'sneak', 'out': 'sneaks'},
        {'in': 'sow', 'out': 'sows'},
        {'in': 'speak', 'out': 'speaks'},
        {'in': 'speed', 'out': 'speeds'},
        {'in': 'spend', 'out': 'spends'},
        {'in': 'spit', 'out': 'spits'},
        {'in': 'spoil', 'out': 'spoils'},
        {'in': 'spring', 'out': 'springs'},
        {'in': 'stand', 'out': 'stands'},
        {'in': 'stave', 'out': 'staves'},
        {'in': 'stay', 'out': 'stays'},
        {'in': 'steal', 'out': 'steals'},
        {'in': 'sting', 'out': 'stings'},
        {'in': 'stink', 'out': 'stinks'},
        {'in': 'stop', 'out': 'stops'},
        {'in': 'strew', 'out': 'strews'},
        {'in': 'stride', 'out': 'strides'},
        {'in': 'strip', 'out': 'strips'},
        {'in': 'strive', 'out': 'strives'},
        {'in': 'sublet', 'out': 'sublets'},
        {'in': 'sunburn', 'out': 'sunburns'},
        {'in': 'swear', 'out': 'swears'},
        {'in': 'sweat', 'out': 'sweats'},
        {'in': 'sweep', 'out': 'sweeps'},
        {'in': 'swell', 'out': 'swells'},
        {'in': 'swim', 'out': 'swims'},
        {'in': 'swing', 'out': 'swings'},
        {'in': 'talk', 'out': 'talks'},
        {'in': 'tear', 'out': 'tears'},
        {'in': 'thrive', 'out': 'thrives'},
        {'in': 'thrust', 'out': 'thrusts'},
        {'in': 'tread', 'out': 'treads'},
        {'in': 'undergo', 'out': 'undergoes'},
        {'in': 'understand', 'out': 'understands'},
        {'in': 'undertake', 'out': 'undertakes'},
        {'in': 'upset', 'out': 'upsets'},
        {'in': 'vex', 'out': 'vexes'},
        {'in': 'wait', 'out': 'waits'},
        {'in': 'wake', 'out': 'wakes'},
        {'in': 'walk', 'out': 'walks'},
        {'in': 'want', 'out': 'wants'},
        {'in': 'watch', 'out': 'watches'},
        {'in': 'wear', 'out': 'wears'},
        {'in': 'weep', 'out': 'weeps'},
        {'in': 'wend', 'out': 'wends'},
        {'in': 'were', 'out': 'was'},
        {'in': 'will', 'out': 'will'},
        {'in': 'win', 'out': 'wins'},
        {'in': 'withdraw', 'out': 'withdraws'},
        {'in': 'withhold', 'out': 'withholds'},
        {'in': 'withstand', 'out': 'withstands'},
        {'in': 'would', 'out': 'would'},
        {'in': 'wring', 'out': 'wrings'},
    ]

    def test_convert_to_singular(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"convert_to_singular({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": dict()
                }}
                self.assertEqual(convert_to_singular(test_case["in"], **test_case["kwargs"]), test_case["out"], test_case["desc"])

if __name__ == "__main__":
    unittest.main()