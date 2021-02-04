
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
## NOTE: This module was autogenerated. ##
## Contains no user-servicable parts!!! ##
##########################################

import unittest

from inflexion.verb_core import convert_to_past_part

class TestVerbToPastPart(unittest.TestCase):
    # test_args has the format [{
    #    "in":     ..., # (required)
    #    "out":    ..., # (required)
    #    "desc":   ..., # (optional) 
    #    "kwargs": ...  # (optional)
    # }, ...
    # ]
    test_args = [
        {'in': 'abide', 'out': 'abided'},
        {'in': 'abided', 'out': 'abided'},
        {'in': 'abides', 'out': 'abided'},
        {'in': 'abiding', 'out': 'abided'},
        {'in': 'ache', 'out': 'ached'},
        {'in': 'ached', 'out': 'ached'},
        {'in': 'aches', 'out': 'ached'},
        {'in': 'aching', 'out': 'ached'},
        {'in': 'am', 'out': 'been'},
        {'in': 'arc', 'out': 'arced'},
        {'in': 'arced', 'out': 'arced'},
        {'in': 'arcing', 'out': 'arced'},
        {'in': 'arcs', 'out': 'arced'},
        {'in': 'are', 'out': 'been'},
        {'in': 'arise', 'out': 'arisen'},
        {'in': 'arisen', 'out': 'arisen'},
        {'in': 'arises', 'out': 'arisen'},
        {'in': 'arising', 'out': 'arisen'},
        {'in': 'arose', 'out': 'arisen'},
        {'in': 'ask', 'out': 'asked'},
        {'in': 'asked', 'out': 'asked'},
        {'in': 'asking', 'out': 'asked'},
        {'in': 'asks', 'out': 'asked'},
        {'in': 'ate', 'out': 'eaten'},
        {'in': 'avalanche', 'out': 'avalanched'},
        {'in': 'avalanched', 'out': 'avalanched'},
        {'in': 'avalanches', 'out': 'avalanched'},
        {'in': 'avalanching', 'out': 'avalanched'},
        {'in': 'awake', 'out': 'awoken'},
        {'in': 'awakening', 'out': 'awoken'},
        {'in': 'awakes', 'out': 'awoken'},
        {'in': 'awoke', 'out': 'awoken'},
        {'in': 'awoken', 'out': 'awoken'},
        {'in': 'be', 'out': 'been'},
        {'in': 'beat', 'out': 'beaten'},
        {'in': 'beaten', 'out': 'beaten'},
        {'in': 'beating', 'out': 'beaten'},
        {'in': 'beats', 'out': 'beaten'},
        {'in': 'became', 'out': 'become'},
        {'in': 'become', 'out': 'become'},
        {'in': 'becomes', 'out': 'become'},
        {'in': 'becoming', 'out': 'become'},
        {'in': 'been', 'out': 'been'},
        {'in': 'began', 'out': 'begun'},
        {'in': 'beget', 'out': 'begotten'},
        {'in': 'begets', 'out': 'begotten'},
        {'in': 'begetting', 'out': 'begotten'},
        {'in': 'begin', 'out': 'begun'},
        {'in': 'beginning', 'out': 'begun'},
        {'in': 'begins', 'out': 'begun'},
        {'in': 'begot', 'out': 'begotten'},
        {'in': 'begotten', 'out': 'begotten'},
        {'in': 'begun', 'out': 'begun'},
        {'in': 'beheld', 'out': 'beheld'},
        {'in': 'behold', 'out': 'beheld'},
        {'in': 'beholding', 'out': 'beheld'},
        {'in': 'beholds', 'out': 'beheld'},
        {'in': 'being', 'out': 'been'},
        {'in': 'bellyache', 'out': 'bellyached'},
        {'in': 'bellyached', 'out': 'bellyached'},
        {'in': 'bellyaches', 'out': 'bellyached'},
        {'in': 'bellyaching', 'out': 'bellyached'},
        {'in': 'bend', 'out': 'bent'},
        {'in': 'bending', 'out': 'bent'},
        {'in': 'bends', 'out': 'bent'},
        {'in': 'bent', 'out': 'bent'},
        {'in': 'bet', 'out': 'bet'},
        {'in': 'bets', 'out': 'bet'},
        {'in': 'betting', 'out': 'bet'},
        {'in': 'bias', 'out': 'biased'},
        {'in': 'biased', 'out': 'biased'},
        {'in': 'biases', 'out': 'biased'},
        {'in': 'biasing', 'out': 'biased'},
        {'in': 'bit', 'out': 'bitten'},
        {'in': 'bite', 'out': 'bitten'},
        {'in': 'bites', 'out': 'bitten'},
        {'in': 'biting', 'out': 'bitten'},
        {'in': 'bitten', 'out': 'bitten'},
        {'in': 'bled', 'out': 'bled'},
        {'in': 'bleed', 'out': 'bled'},
        {'in': 'bleeding', 'out': 'bled'},
        {'in': 'bleeds', 'out': 'bled'},
        {'in': 'blew', 'out': 'blown'},
        {'in': 'blitz', 'out': 'blitzed'},
        {'in': 'blitzed', 'out': 'blitzed'},
        {'in': 'blitzes', 'out': 'blitzed'},
        {'in': 'blitzing', 'out': 'blitzed'},
        {'in': 'blow', 'out': 'blown'},
        {'in': 'blowing', 'out': 'blown'},
        {'in': 'blown', 'out': 'blown'},
        {'in': 'blows', 'out': 'blown'},
        {'in': 'break', 'out': 'broken'},
        {'in': 'breaking', 'out': 'broken'},
        {'in': 'breaks', 'out': 'broken'},
        {'in': 'bring', 'out': 'brought'},
        {'in': 'bringing', 'out': 'brought'},
        {'in': 'brings', 'out': 'brought'},
        {'in': 'broke', 'out': 'broken'},
        {'in': 'broken', 'out': 'broken'},
        {'in': 'brought', 'out': 'brought'},
        {'in': 'build', 'out': 'built'},
        {'in': 'building', 'out': 'built'},
        {'in': 'builds', 'out': 'built'},
        {'in': 'built', 'out': 'built'},
        {'in': 'burn', 'out': 'burnt'},
        {'in': 'burning', 'out': 'burnt'},
        {'in': 'burns', 'out': 'burnt'},
        {'in': 'burnt', 'out': 'burnt'},
        {'in': 'burst', 'out': 'burst'},
        {'in': 'bursting', 'out': 'burst'},
        {'in': 'bursts', 'out': 'burst'},
        {'in': 'bus', 'out': 'bused'},
        {'in': 'bused', 'out': 'bused'},
        {'in': 'buses', 'out': 'bused'},
        {'in': 'busing', 'out': 'bused'},
        {'in': 'bust', 'out': 'bust'},
        {'in': 'busting', 'out': 'bust'},
        {'in': 'busts', 'out': 'bust'},
        {'in': 'cache', 'out': 'cached'},
        {'in': 'cached', 'out': 'cached'},
        {'in': 'caches', 'out': 'cached'},
        {'in': 'caching', 'out': 'cached'},
        {'in': 'caddie', 'out': 'caddied'},
        {'in': 'caddied', 'out': 'caddied'},
        {'in': 'caddies', 'out': 'caddied'},
        {'in': 'caddying', 'out': 'caddied'},
        {'in': 'came', 'out': 'come'},
        {'in': 'canvas', 'out': 'canvased'},
        {'in': 'canvased', 'out': 'canvased'},
        {'in': 'canvases', 'out': 'canvased'},
        {'in': 'canvasing', 'out': 'canvased'},
        {'in': 'catch', 'out': 'caught'},
        {'in': 'catches', 'out': 'caught'},
        {'in': 'catching', 'out': 'caught'},
        {'in': 'caucus', 'out': 'caucused'},
        {'in': 'caucused', 'out': 'caucused'},
        {'in': 'caucuses', 'out': 'caucused'},
        {'in': 'caucusing', 'out': 'caucused'},
        {'in': 'caught', 'out': 'caught'},
        {'in': 'change', 'out': 'changed'},
        {'in': 'changed', 'out': 'changed'},
        {'in': 'changes', 'out': 'changed'},
        {'in': 'changing', 'out': 'changed'},
        {'in': 'choose', 'out': 'chosen'},
        {'in': 'chooses', 'out': 'chosen'},
        {'in': 'choosing', 'out': 'chosen'},
        {'in': 'chorus', 'out': 'chorused'},
        {'in': 'chorused', 'out': 'chorused'},
        {'in': 'choruses', 'out': 'chorused'},
        {'in': 'chorusing', 'out': 'chorused'},
        {'in': 'chose', 'out': 'chosen'},
        {'in': 'chosen', 'out': 'chosen'},
        {'in': 'clap', 'out': 'clapped'},
        {'in': 'clapped', 'out': 'clapped'},
        {'in': 'clapping', 'out': 'clapped'},
        {'in': 'claps', 'out': 'clapped'},
        {'in': 'cling', 'out': 'clung'},
        {'in': 'clinging', 'out': 'clung'},
        {'in': 'clings', 'out': 'clung'},
        {'in': 'clung', 'out': 'clung'},
        {'in': 'come', 'out': 'come'},
        {'in': 'comes', 'out': 'come'},
        {'in': 'coming', 'out': 'come'},
        {'in': 'continue', 'out': 'continued'},
        {'in': 'continued', 'out': 'continued'},
        {'in': 'continues', 'out': 'continued'},
        {'in': 'continuing', 'out': 'continued'},
        {'in': 'cost', 'out': 'cost'},
        {'in': 'costing', 'out': 'cost'},
        {'in': 'costs', 'out': 'cost'},
        {'in': 'creche', 'out': 'creched'},
        {'in': 'creched', 'out': 'creched'},
        {'in': 'creches', 'out': 'creched'},
        {'in': 'creching', 'out': 'creched'},
        {'in': 'creep', 'out': 'crept'},
        {'in': 'creeping', 'out': 'crept'},
        {'in': 'creeps', 'out': 'crept'},
        {'in': 'crept', 'out': 'crept'},
        {'in': 'dare', 'out': 'dared'},
        {'in': 'dared', 'out': 'dared'},
        {'in': 'dares', 'out': 'dared'},
        {'in': 'daring', 'out': 'dared'},
        {'in': 'deal', 'out': 'dealt'},
        {'in': 'dealing', 'out': 'dealt'},
        {'in': 'deals', 'out': 'dealt'},
        {'in': 'dealt', 'out': 'dealt'},
        {'in': 'did', 'out': 'done'},
        {'in': 'die', 'out': 'died'},
        {'in': 'died', 'out': 'died'},
        {'in': 'dies', 'out': 'died'},
        {'in': 'dig', 'out': 'dug'},
        {'in': 'digging', 'out': 'dug'},
        {'in': 'digs', 'out': 'dug'},
        {'in': 'dis', 'out': 'dissed'},
        {'in': 'dissed', 'out': 'dissed'},
        {'in': 'disses', 'out': 'dissed'},
        {'in': 'dissing', 'out': 'dissed'},
        {'in': 'dive', 'out': 'dived'},
        {'in': 'dived', 'out': 'dived'},
        {'in': 'dives', 'out': 'dived'},
        {'in': 'diving', 'out': 'dived'},
        {'in': 'do', 'out': 'done'},
        {'in': 'does', 'out': 'done'},
        {'in': 'doing', 'out': 'done'},
        {'in': 'done', 'out': 'done'},
        {'in': 'douche', 'out': 'douched'},
        {'in': 'douched', 'out': 'douched'},
        {'in': 'douches', 'out': 'douched'},
        {'in': 'douching', 'out': 'douched'},
        {'in': 'drag', 'out': 'dragged'},
        {'in': 'dragged', 'out': 'dragged'},
        {'in': 'dragging', 'out': 'dragged'},
        {'in': 'drags', 'out': 'dragged'},
        {'in': 'drank', 'out': 'drunk'},
        {'in': 'dream', 'out': 'dreamed'},
        {'in': 'dreamed', 'out': 'dreamed'},
        {'in': 'dreaming', 'out': 'dreamed'},
        {'in': 'dreams', 'out': 'dreamed'},
        {'in': 'drink', 'out': 'drunk'},
        {'in': 'drinking', 'out': 'drunk'},
        {'in': 'drinks', 'out': 'drunk'},
        {'in': 'drive', 'out': 'driven'},
        {'in': 'driven', 'out': 'driven'},
        {'in': 'drives', 'out': 'driven'},
        {'in': 'driving', 'out': 'driven'},
        {'in': 'drove', 'out': 'driven'},
        {'in': 'drunk', 'out': 'drunk'},
        {'in': 'dug', 'out': 'dug'},
        {'in': 'dwell', 'out': 'dwelt'},
        {'in': 'dwelling', 'out': 'dwelt'},
        {'in': 'dwells', 'out': 'dwelt'},
        {'in': 'dwelt', 'out': 'dwelt'},
        {'in': 'dying', 'out': 'died'},
        {'in': 'eat', 'out': 'eaten'},
        {'in': 'eaten', 'out': 'eaten'},
        {'in': 'eating', 'out': 'eaten'},
        {'in': 'eats', 'out': 'eaten'},
        {'in': 'expect', 'out': 'expected'},
        {'in': 'expected', 'out': 'expected'},
        {'in': 'expecting', 'out': 'expected'},
        {'in': 'expects', 'out': 'expected'},
        {'in': 'fall', 'out': 'fallen'},
        {'in': 'fallen', 'out': 'fallen'},
        {'in': 'falling', 'out': 'fallen'},
        {'in': 'falls', 'out': 'fallen'},
        {'in': 'feel', 'out': 'felt'},
        {'in': 'feeling', 'out': 'felt'},
        {'in': 'feels', 'out': 'felt'},
        {'in': 'fell', 'out': 'fallen'},
        {'in': 'felt', 'out': 'felt'},
        {'in': 'fight', 'out': 'fought'},
        {'in': 'fighting', 'out': 'fought'},
        {'in': 'fights', 'out': 'fought'},
        {'in': 'find', 'out': 'found'},
        {'in': 'finding', 'out': 'found'},
        {'in': 'finds', 'out': 'found'},
        {'in': 'fled', 'out': 'fled'},
        {'in': 'flee', 'out': 'fled'},
        {'in': 'fleeing', 'out': 'fled'},
        {'in': 'flees', 'out': 'fled'},
        {'in': 'flew', 'out': 'flown'},
        {'in': 'flies', 'out': 'flown'},
        {'in': 'fling', 'out': 'flung'},
        {'in': 'flinging', 'out': 'flung'},
        {'in': 'flings', 'out': 'flung'},
        {'in': 'flown', 'out': 'flown'},
        {'in': 'flung', 'out': 'flung'},
        {'in': 'fly', 'out': 'flown'},
        {'in': 'flying', 'out': 'flown'},
        {'in': 'focus', 'out': 'focused'},
        {'in': 'focused', 'out': 'focused'},
        {'in': 'focuses', 'out': 'focused'},
        {'in': 'focusing', 'out': 'focused'},
        {'in': 'follow', 'out': 'followed'},
        {'in': 'followed', 'out': 'followed'},
        {'in': 'following', 'out': 'followed'},
        {'in': 'follows', 'out': 'followed'},
        {'in': 'forbade', 'out': 'forbidden'},
        {'in': 'forbid', 'out': 'forbidden'},
        {'in': 'forbidden', 'out': 'forbidden'},
        {'in': 'forbidding', 'out': 'forbidden'},
        {'in': 'forbids', 'out': 'forbidden'},
        {'in': 'foresaw', 'out': 'foreseen'},
        {'in': 'foresee', 'out': 'foreseen'},
        {'in': 'foreseeing', 'out': 'foreseen'},
        {'in': 'foreseen', 'out': 'foreseen'},
        {'in': 'foresees', 'out': 'foreseen'},
        {'in': 'foretell', 'out': 'foretold'},
        {'in': 'foretelling', 'out': 'foretold'},
        {'in': 'foretells', 'out': 'foretold'},
        {'in': 'foretold', 'out': 'foretold'},
        {'in': 'forgave', 'out': 'forgiven'},
        {'in': 'forget', 'out': 'forgotten'},
        {'in': 'forgets', 'out': 'forgotten'},
        {'in': 'forgetting', 'out': 'forgotten'},
        {'in': 'forgive', 'out': 'forgiven'},
        {'in': 'forgiven', 'out': 'forgiven'},
        {'in': 'forgives', 'out': 'forgiven'},
        {'in': 'forgiving', 'out': 'forgiven'},
        {'in': 'forgot', 'out': 'forgotten'},
        {'in': 'forgotten', 'out': 'forgotten'},
        {'in': 'forsake', 'out': 'forsaken'},
        {'in': 'forsaken', 'out': 'forsaken'},
        {'in': 'forsakes', 'out': 'forsaken'},
        {'in': 'forsaking', 'out': 'forsaken'},
        {'in': 'forsook', 'out': 'forsaken'},
        {'in': 'fought', 'out': 'fought'},
        {'in': 'found', 'out': 'found'},
        {'in': 'gas', 'out': 'gassed'},
        {'in': 'gases', 'out': 'gassed'},
        {'in': 'gassed', 'out': 'gassed'},
        {'in': 'gassing', 'out': 'gassed'},
        {'in': 'gave', 'out': 'given'},
        {'in': 'get', 'out': 'gotten'},
        {'in': 'gets', 'out': 'gotten'},
        {'in': 'getting', 'out': 'gotten'},
        {'in': 'gild', 'out': 'gilded'},
        {'in': 'gilded', 'out': 'gilded'},
        {'in': 'gilding', 'out': 'gilded'},
        {'in': 'gilds', 'out': 'gilded'},
        {'in': 'give', 'out': 'given'},
        {'in': 'given', 'out': 'given'},
        {'in': 'gives', 'out': 'given'},
        {'in': 'giving', 'out': 'given'},
        {'in': 'go', 'out': 'gone'},
        {'in': 'goes', 'out': 'gone'},
        {'in': 'going', 'out': 'gone'},
        {'in': 'gone', 'out': 'gone'},
        {'in': 'got', 'out': 'gotten'},
        {'in': 'gotten', 'out': 'gotten'},
        {'in': 'grind', 'out': 'ground'},
        {'in': 'grinding', 'out': 'ground'},
        {'in': 'grinds', 'out': 'ground'},
        {'in': 'ground', 'out': 'ground'},
        {'in': 'had', 'out': 'had'},
        {'in': 'happen', 'out': 'happened'},
        {'in': 'happened', 'out': 'happened'},
        {'in': 'happening', 'out': 'happened'},
        {'in': 'happens', 'out': 'happened'},
        {'in': 'has', 'out': 'had'},
        {'in': 'have', 'out': 'had'},
        {'in': 'having', 'out': 'had'},
        {'in': 'held', 'out': 'held'},
        {'in': 'help', 'out': 'helped'},
        {'in': 'helped', 'out': 'helped'},
        {'in': 'helping', 'out': 'helped'},
        {'in': 'helps', 'out': 'helped'},
        {'in': 'hew', 'out': 'hewn'},
        {'in': 'hewed', 'out': 'hewn'},
        {'in': 'hewing', 'out': 'hewn'},
        {'in': 'hewn', 'out': 'hewn'},
        {'in': 'hews', 'out': 'hewn'},
        {'in': 'hie', 'out': 'hied'},
        {'in': 'hied', 'out': 'hied'},
        {'in': 'hies', 'out': 'hied'},
        {'in': 'hit', 'out': 'hit'},
        {'in': 'hits', 'out': 'hit'},
        {'in': 'hitting', 'out': 'hit'},
        {'in': 'hocus', 'out': 'hocused'},
        {'in': 'hocused', 'out': 'hocused'},
        {'in': 'hocuses', 'out': 'hocused'},
        {'in': 'hocusing', 'out': 'hocused'},
        {'in': 'hold', 'out': 'held'},
        {'in': 'holding', 'out': 'held'},
        {'in': 'holds', 'out': 'held'},
        {'in': 'hurt', 'out': 'hurt'},
        {'in': 'hurting', 'out': 'hurt'},
        {'in': 'hurts', 'out': 'hurt'},
        {'in': 'hying', 'out': 'hied'},
        {'in': 'inlaid', 'out': 'inlaid'},
        {'in': 'inlay', 'out': 'inlaid'},
        {'in': 'inlaying', 'out': 'inlaid'},
        {'in': 'inlays', 'out': 'inlaid'},
        {'in': 'insist', 'out': 'insisted'},
        {'in': 'insisted', 'out': 'insisted'},
        {'in': 'insisting', 'out': 'insisted'},
        {'in': 'insists', 'out': 'insisted'},
        {'in': 'interlaid', 'out': 'interlaid'},
        {'in': 'interlay', 'out': 'interlaid'},
        {'in': 'interlaying', 'out': 'interlaid'},
        {'in': 'interlays', 'out': 'interlaid'},
        {'in': 'iris', 'out': 'irised'},
        {'in': 'irised', 'out': 'irised'},
        {'in': 'irises', 'out': 'irised'},
        {'in': 'irising', 'out': 'irised'},
        {'in': 'is', 'out': 'been'},
        {'in': 'keep', 'out': 'kept'},
        {'in': 'keeping', 'out': 'kept'},
        {'in': 'keeps', 'out': 'kept'},
        {'in': 'kept', 'out': 'kept'},
        {'in': 'kill', 'out': 'killed'},
        {'in': 'killed', 'out': 'killed'},
        {'in': 'killing', 'out': 'killed'},
        {'in': 'kills', 'out': 'killed'},
        {'in': 'kneel', 'out': 'knelt'},
        {'in': 'kneeling', 'out': 'knelt'},
        {'in': 'kneels', 'out': 'knelt'},
        {'in': 'knelt', 'out': 'knelt'},
        {'in': 'knew', 'out': 'known'},
        {'in': 'knit', 'out': 'knitted'},
        {'in': 'knits', 'out': 'knitted'},
        {'in': 'knitted', 'out': 'knitted'},
        {'in': 'knitting', 'out': 'knitted'},
        {'in': 'know', 'out': 'known'},
        {'in': 'knowing', 'out': 'known'},
        {'in': 'known', 'out': 'known'},
        {'in': 'knows', 'out': 'known'},
        {'in': 'laid', 'out': 'laid'},
        {'in': 'lain', 'out': 'lain'},
        {'in': 'lay', 'out': 'laid'},
        {'in': 'laying', 'out': 'laid'},
        {'in': 'lays', 'out': 'laid'},
        {'in': 'lead', 'out': 'led'},
        {'in': 'leading', 'out': 'led'},
        {'in': 'leads', 'out': 'led'},
        {'in': 'lean', 'out': 'leaned'},
        {'in': 'leaned', 'out': 'leaned'},
        {'in': 'leaning', 'out': 'leaned'},
        {'in': 'leans', 'out': 'leaned'},
        {'in': 'leap', 'out': 'leapt'},
        {'in': 'leaping', 'out': 'leapt'},
        {'in': 'leaps', 'out': 'leapt'},
        {'in': 'leapt', 'out': 'leapt'},
        {'in': 'learn', 'out': 'learned'},
        {'in': 'learned', 'out': 'learned'},
        {'in': 'learning', 'out': 'learned'},
        {'in': 'learns', 'out': 'learned'},
        {'in': 'leave', 'out': 'left'},
        {'in': 'leaves', 'out': 'left'},
        {'in': 'leaving', 'out': 'left'},
        {'in': 'led', 'out': 'led'},
        {'in': 'left', 'out': 'left'},
        {'in': 'let', 'out': 'let'},
        {'in': 'lets', 'out': 'let'},
        {'in': 'letting', 'out': 'let'},
        {'in': 'lie', 'out': 'lain'},
        {'in': 'lies', 'out': 'lain'},
        {'in': 'like', 'out': 'liked'},
        {'in': 'liked', 'out': 'liked'},
        {'in': 'likes', 'out': 'liked'},
        {'in': 'liking', 'out': 'liked'},
        {'in': 'live', 'out': 'lived'},
        {'in': 'lived', 'out': 'lived'},
        {'in': 'lives', 'out': 'lived'},
        {'in': 'living', 'out': 'lived'},
        {'in': 'look', 'out': 'looked'},
        {'in': 'looked', 'out': 'looked'},
        {'in': 'looking', 'out': 'looked'},
        {'in': 'looks', 'out': 'looked'},
        {'in': 'lose', 'out': 'lost'},
        {'in': 'loses', 'out': 'lost'},
        {'in': 'losing', 'out': 'lost'},
        {'in': 'lost', 'out': 'lost'},
        {'in': 'love', 'out': 'loved'},
        {'in': 'loved', 'out': 'loved'},
        {'in': 'loves', 'out': 'loved'},
        {'in': 'loving', 'out': 'loved'},
        {'in': 'lying', 'out': 'lain'},
        {'in': 'mean', 'out': 'meant'},
        {'in': 'meaning', 'out': 'meant'},
        {'in': 'means', 'out': 'meant'},
        {'in': 'meant', 'out': 'meant'},
        {'in': 'meet', 'out': 'met'},
        {'in': 'meeting', 'out': 'met'},
        {'in': 'meets', 'out': 'met'},
        {'in': 'menu', 'out': 'menued'},
        {'in': 'menued', 'out': 'menued'},
        {'in': 'menuing', 'out': 'menued'},
        {'in': 'menus', 'out': 'menued'},
        {'in': 'met', 'out': 'met'},
        {'in': 'mislead', 'out': 'misled'},
        {'in': 'misleading', 'out': 'misled'},
        {'in': 'misleads', 'out': 'misled'},
        {'in': 'misled', 'out': 'misled'},
        {'in': 'mistake', 'out': 'mistaken'},
        {'in': 'mistaken', 'out': 'mistaken'},
        {'in': 'mistakes', 'out': 'mistaken'},
        {'in': 'mistaking', 'out': 'mistaken'},
        {'in': 'mistook', 'out': 'mistaken'},
        {'in': 'misunderstand', 'out': 'misunderstood'},
        {'in': 'misunderstanding', 'out': 'misunderstood'},
        {'in': 'misunderstands', 'out': 'misunderstood'},
        {'in': 'misunderstood', 'out': 'misunderstood'},
        {'in': 'move', 'out': 'moved'},
        {'in': 'moved', 'out': 'moved'},
        {'in': 'moves', 'out': 'moved'},
        {'in': 'moving', 'out': 'moved'},
        {'in': 'need', 'out': 'needed'},
        {'in': 'needed', 'out': 'needed'},
        {'in': 'needing', 'out': 'needed'},
        {'in': 'needs', 'out': 'needed'},
        {'in': 'niche', 'out': 'niched'},
        {'in': 'niched', 'out': 'niched'},
        {'in': 'nicheing', 'out': 'niched'},
        {'in': 'niches', 'out': 'niched'},
        {'in': 'outvie', 'out': 'outvied'},
        {'in': 'outvied', 'out': 'outvied'},
        {'in': 'outvies', 'out': 'outvied'},
        {'in': 'outvying', 'out': 'outvied'},
        {'in': 'overdraw', 'out': 'overdrawn'},
        {'in': 'overdrawing', 'out': 'overdrawn'},
        {'in': 'overdrawn', 'out': 'overdrawn'},
        {'in': 'overdraws', 'out': 'overdrawn'},
        {'in': 'overdrew', 'out': 'overdrawn'},
        {'in': 'overhear', 'out': 'overheard'},
        {'in': 'overheard', 'out': 'overheard'},
        {'in': 'overhearing', 'out': 'overheard'},
        {'in': 'overhears', 'out': 'overheard'},
        {'in': 'overtake', 'out': 'overtaken'},
        {'in': 'overtaken', 'out': 'overtaken'},
        {'in': 'overtakes', 'out': 'overtaken'},
        {'in': 'overtaking', 'out': 'overtaken'},
        {'in': 'overtook', 'out': 'overtaken'},
        {'in': 'preset', 'out': 'preset'},
        {'in': 'presets', 'out': 'preset'},
        {'in': 'presetting', 'out': 'preset'},
        {'in': 'prove', 'out': 'proven'},
        {'in': 'proved', 'out': 'proven'},
        {'in': 'proven', 'out': 'proven'},
        {'in': 'proves', 'out': 'proven'},
        {'in': 'provide', 'out': 'provided'},
        {'in': 'provided', 'out': 'provided'},
        {'in': 'provides', 'out': 'provided'},
        {'in': 'providing', 'out': 'provided'},
        {'in': 'proving', 'out': 'proven'},
        {'in': 'psyche', 'out': 'psyched'},
        {'in': 'psyched', 'out': 'psyched'},
        {'in': 'psyches', 'out': 'psyched'},
        {'in': 'psyching', 'out': 'psyched'},
        {'in': 'put', 'out': 'put'},
        {'in': 'puts', 'out': 'put'},
        {'in': 'putting', 'out': 'put'},
        {'in': 'quit', 'out': 'quit'},
        {'in': 'quits', 'out': 'quit'},
        {'in': 'quitting', 'out': 'quit'},
        {'in': 'quiz', 'out': 'quizzed'},
        {'in': 'quizzed', 'out': 'quizzed'},
        {'in': 'quizzes', 'out': 'quizzed'},
        {'in': 'quizzing', 'out': 'quizzed'},
        {'in': 'rang', 'out': 'rung'},
        {'in': 'reach', 'out': 'reached'},
        {'in': 'reached', 'out': 'reached'},
        {'in': 'reaches', 'out': 'reached'},
        {'in': 'reaching', 'out': 'reached'},
        {'in': 'remain', 'out': 'remained'},
        {'in': 'remained', 'out': 'remained'},
        {'in': 'remaining', 'out': 'remained'},
        {'in': 'remains', 'out': 'remained'},
        {'in': 'remember', 'out': 'remembered'},
        {'in': 'remembered', 'out': 'remembered'},
        {'in': 'remembering', 'out': 'remembered'},
        {'in': 'remembers', 'out': 'remembered'},
        {'in': 'rend', 'out': 'rent'},
        {'in': 'rending', 'out': 'rent'},
        {'in': 'rends', 'out': 'rent'},
        {'in': 'rent', 'out': 'rent'},
        {'in': 'rented', 'out': 'rented'},
        {'in': 'renting', 'out': 'rented'},
        {'in': 'rents', 'out': 'rented'},
        {'in': 'rid', 'out': 'rid'},
        {'in': 'ridding', 'out': 'rid'},
        {'in': 'rids', 'out': 'rid'},
        {'in': 'ring', 'out': 'rung'},
        {'in': 'ringing', 'out': 'rung'},
        {'in': 'rings', 'out': 'rung'},
        {'in': 'rise', 'out': 'risen'},
        {'in': 'risen', 'out': 'risen'},
        {'in': 'rises', 'out': 'risen'},
        {'in': 'rising', 'out': 'risen'},
        {'in': 'rive', 'out': 'riven'},
        {'in': 'rived', 'out': 'riven'},
        {'in': 'riven', 'out': 'riven'},
        {'in': 'rives', 'out': 'riven'},
        {'in': 'riving', 'out': 'riven'},
        {'in': 'rose', 'out': 'risen'},
        {'in': 'rung', 'out': 'rung'},
        {'in': 'sang', 'out': 'sung'},
        {'in': 'sank', 'out': 'sunk'},
        {'in': 'sat', 'out': 'sat'},
        {'in': 'saw', 'out': 'sawn'},
        {'in': 'sawed', 'out': 'sawn'},
        {'in': 'sawing', 'out': 'sawn'},
        {'in': 'sawn', 'out': 'sawn'},
        {'in': 'saws', 'out': 'sawn'},
        {'in': 'seek', 'out': 'sought'},
        {'in': 'seeking', 'out': 'sought'},
        {'in': 'seeks', 'out': 'sought'},
        {'in': 'seem', 'out': 'seemed'},
        {'in': 'seemed', 'out': 'seemed'},
        {'in': 'seeming', 'out': 'seemed'},
        {'in': 'seems', 'out': 'seemed'},
        {'in': 'shake', 'out': 'shaken'},
        {'in': 'shaken', 'out': 'shaken'},
        {'in': 'shakes', 'out': 'shaken'},
        {'in': 'shaking', 'out': 'shaken'},
        {'in': 'shat', 'out': 'shitted'},
        {'in': 'shave', 'out': 'shaved'},
        {'in': 'shaved', 'out': 'shaved'},
        {'in': 'shaves', 'out': 'shaved'},
        {'in': 'shaving', 'out': 'shaved'},
        {'in': 'shed', 'out': 'shed'},
        {'in': 'shedding', 'out': 'shed'},
        {'in': 'sheds', 'out': 'shed'},
        {'in': 'shit', 'out': 'shitted'},
        {'in': 'shits', 'out': 'shitted'},
        {'in': 'shitted', 'out': 'shitted'},
        {'in': 'shitting', 'out': 'shitted'},
        {'in': 'shod', 'out': 'shod'},
        {'in': 'shoe', 'out': 'shod'},
        {'in': 'shoeing', 'out': 'shod'},
        {'in': 'shoes', 'out': 'shod'},
        {'in': 'shook', 'out': 'shaken'},
        {'in': 'show', 'out': 'shown'},
        {'in': 'showed', 'out': 'shown'},
        {'in': 'showing', 'out': 'shown'},
        {'in': 'shown', 'out': 'shown'},
        {'in': 'shows', 'out': 'shown'},
        {'in': 'shrank', 'out': 'shrunk'},
        {'in': 'shrink', 'out': 'shrunk'},
        {'in': 'shrinking', 'out': 'shrunk'},
        {'in': 'shrinks', 'out': 'shrunk'},
        {'in': 'shrunk', 'out': 'shrunk'},
        {'in': 'sing', 'out': 'sung'},
        {'in': 'singing', 'out': 'sung'},
        {'in': 'sings', 'out': 'sung'},
        {'in': 'sink', 'out': 'sunk'},
        {'in': 'sinking', 'out': 'sunk'},
        {'in': 'sinks', 'out': 'sunk'},
        {'in': 'sit', 'out': 'sat'},
        {'in': 'sits', 'out': 'sat'},
        {'in': 'sitting', 'out': 'sat'},
        {'in': 'ski', 'out': 'skied'},
        {'in': 'skied', 'out': 'skied'},
        {'in': 'skiing', 'out': 'skied'},
        {'in': 'skis', 'out': 'skied'},
        {'in': 'slain', 'out': 'slain'},
        {'in': 'slay', 'out': 'slain'},
        {'in': 'slaying', 'out': 'slain'},
        {'in': 'slays', 'out': 'slain'},
        {'in': 'slew', 'out': 'slain'},
        {'in': 'slid', 'out': 'slid'},
        {'in': 'slide', 'out': 'slid'},
        {'in': 'slides', 'out': 'slid'},
        {'in': 'sliding', 'out': 'slid'},
        {'in': 'slink', 'out': 'slunk'},
        {'in': 'slinking', 'out': 'slunk'},
        {'in': 'slinks', 'out': 'slunk'},
        {'in': 'slit', 'out': 'slit'},
        {'in': 'slits', 'out': 'slit'},
        {'in': 'slitting', 'out': 'slit'},
        {'in': 'slunk', 'out': 'slunk'},
        {'in': 'smell', 'out': 'smelled'},
        {'in': 'smelled', 'out': 'smelled'},
        {'in': 'smelling', 'out': 'smelled'},
        {'in': 'smells', 'out': 'smelled'},
        {'in': 'smite', 'out': 'smitten'},
        {'in': 'smites', 'out': 'smitten'},
        {'in': 'smiting', 'out': 'smitten'},
        {'in': 'smitten', 'out': 'smitten'},
        {'in': 'smote', 'out': 'smitten'},
        {'in': 'sneak', 'out': 'sneaked'},
        {'in': 'sneaked', 'out': 'sneaked'},
        {'in': 'sneaking', 'out': 'sneaked'},
        {'in': 'sneaks', 'out': 'sneaked'},
        {'in': 'sought', 'out': 'sought'},
        {'in': 'sow', 'out': 'sown'},
        {'in': 'sowed', 'out': 'sown'},
        {'in': 'sowing', 'out': 'sown'},
        {'in': 'sown', 'out': 'sown'},
        {'in': 'sows', 'out': 'sown'},
        {'in': 'spat', 'out': 'spat'},
        {'in': 'speak', 'out': 'spoken'},
        {'in': 'speaking', 'out': 'spoken'},
        {'in': 'speaks', 'out': 'spoken'},
        {'in': 'sped', 'out': 'sped'},
        {'in': 'speed', 'out': 'sped'},
        {'in': 'speeding', 'out': 'sped'},
        {'in': 'speeds', 'out': 'sped'},
        {'in': 'spend', 'out': 'spent'},
        {'in': 'spending', 'out': 'spent'},
        {'in': 'spends', 'out': 'spent'},
        {'in': 'spent', 'out': 'spent'},
        {'in': 'spit', 'out': 'spat'},
        {'in': 'spits', 'out': 'spat'},
        {'in': 'spitting', 'out': 'spat'},
        {'in': 'spoil', 'out': 'spoiled'},
        {'in': 'spoiled', 'out': 'spoiled'},
        {'in': 'spoiling', 'out': 'spoiled'},
        {'in': 'spoils', 'out': 'spoiled'},
        {'in': 'spoilt', 'out': 'spoiled'},
        {'in': 'spoke', 'out': 'spoken'},
        {'in': 'spoken', 'out': 'spoken'},
        {'in': 'sprang', 'out': 'sprung'},
        {'in': 'spring', 'out': 'sprung'},
        {'in': 'springing', 'out': 'sprung'},
        {'in': 'springs', 'out': 'sprung'},
        {'in': 'sprung', 'out': 'sprung'},
        {'in': 'stand', 'out': 'stood'},
        {'in': 'standing', 'out': 'stood'},
        {'in': 'stands', 'out': 'stood'},
        {'in': 'stank', 'out': 'stunk'},
        {'in': 'stave', 'out': 'staved'},
        {'in': 'staved', 'out': 'staved'},
        {'in': 'staves', 'out': 'staved'},
        {'in': 'staving', 'out': 'staved'},
        {'in': 'stay', 'out': 'stayed'},
        {'in': 'stayed', 'out': 'stayed'},
        {'in': 'staying', 'out': 'stayed'},
        {'in': 'stays', 'out': 'stayed'},
        {'in': 'steal', 'out': 'stolen'},
        {'in': 'stealing', 'out': 'stolen'},
        {'in': 'steals', 'out': 'stolen'},
        {'in': 'sting', 'out': 'stung'},
        {'in': 'stinging', 'out': 'stung'},
        {'in': 'stings', 'out': 'stung'},
        {'in': 'stink', 'out': 'stunk'},
        {'in': 'stinking', 'out': 'stunk'},
        {'in': 'stinks', 'out': 'stunk'},
        {'in': 'stole', 'out': 'stolen'},
        {'in': 'stolen', 'out': 'stolen'},
        {'in': 'stood', 'out': 'stood'},
        {'in': 'stop', 'out': 'stopped'},
        {'in': 'stopped', 'out': 'stopped'},
        {'in': 'stopping', 'out': 'stopped'},
        {'in': 'stops', 'out': 'stopped'},
        {'in': 'strew', 'out': 'strewn'},
        {'in': 'strewed', 'out': 'strewn'},
        {'in': 'strewing', 'out': 'strewn'},
        {'in': 'strewn', 'out': 'strewn'},
        {'in': 'strews', 'out': 'strewn'},
        {'in': 'stride', 'out': 'strode'},
        {'in': 'strides', 'out': 'strode'},
        {'in': 'striding', 'out': 'strode'},
        {'in': 'strip', 'out': 'stripped'},
        {'in': 'stripped', 'out': 'stripped'},
        {'in': 'stripping', 'out': 'stripped'},
        {'in': 'strips', 'out': 'stripped'},
        {'in': 'strive', 'out': 'strived'},
        {'in': 'strived', 'out': 'strived'},
        {'in': 'strives', 'out': 'strived'},
        {'in': 'striving', 'out': 'strived'},
        {'in': 'strode', 'out': 'strode'},
        {'in': 'strove', 'out': 'strived'},
        {'in': 'stung', 'out': 'stung'},
        {'in': 'stunk', 'out': 'stunk'},
        {'in': 'sublet', 'out': 'sublet'},
        {'in': 'sublets', 'out': 'sublet'},
        {'in': 'subletting', 'out': 'sublet'},
        {'in': 'sunburn', 'out': 'sunburned'},
        {'in': 'sunburned', 'out': 'sunburned'},
        {'in': 'sunburning', 'out': 'sunburned'},
        {'in': 'sunburns', 'out': 'sunburned'},
        {'in': 'sung', 'out': 'sung'},
        {'in': 'sunk', 'out': 'sunk'},
        {'in': 'swam', 'out': 'swum'},
        {'in': 'swear', 'out': 'sworn'},
        {'in': 'swearing', 'out': 'sworn'},
        {'in': 'swears', 'out': 'sworn'},
        {'in': 'sweat', 'out': 'sweated'},
        {'in': 'sweated', 'out': 'sweated'},
        {'in': 'sweating', 'out': 'sweated'},
        {'in': 'sweats', 'out': 'sweated'},
        {'in': 'sweep', 'out': 'swept'},
        {'in': 'sweeping', 'out': 'swept'},
        {'in': 'sweeps', 'out': 'swept'},
        {'in': 'swell', 'out': 'swollen'},
        {'in': 'swelled', 'out': 'swollen'},
        {'in': 'swelling', 'out': 'swollen'},
        {'in': 'swells', 'out': 'swollen'},
        {'in': 'swept', 'out': 'swept'},
        {'in': 'swim', 'out': 'swum'},
        {'in': 'swimming', 'out': 'swum'},
        {'in': 'swims', 'out': 'swum'},
        {'in': 'swing', 'out': 'swung'},
        {'in': 'swinging', 'out': 'swung'},
        {'in': 'swings', 'out': 'swung'},
        {'in': 'swollen', 'out': 'swollen'},
        {'in': 'swore', 'out': 'sworn'},
        {'in': 'sworn', 'out': 'sworn'},
        {'in': 'swum', 'out': 'swum'},
        {'in': 'swung', 'out': 'swung'},
        {'in': 'talk', 'out': 'talked'},
        {'in': 'talked', 'out': 'talked'},
        {'in': 'talking', 'out': 'talked'},
        {'in': 'talks', 'out': 'talked'},
        {'in': 'tear', 'out': 'torn'},
        {'in': 'tearing', 'out': 'torn'},
        {'in': 'tears', 'out': 'torn'},
        {'in': 'thrive', 'out': 'thrived'},
        {'in': 'thrived', 'out': 'thrived'},
        {'in': 'thrives', 'out': 'thrived'},
        {'in': 'thriving', 'out': 'thrived'},
        {'in': 'thrust', 'out': 'thrust'},
        {'in': 'thrusting', 'out': 'thrust'},
        {'in': 'thrusts', 'out': 'thrust'},
        {'in': 'tore', 'out': 'torn'},
        {'in': 'torn', 'out': 'torn'},
        {'in': 'tread', 'out': 'trodden'},
        {'in': 'treading', 'out': 'trodden'},
        {'in': 'treads', 'out': 'trodden'},
        {'in': 'trod', 'out': 'trodden'},
        {'in': 'trodden', 'out': 'trodden'},
        {'in': 'undergo', 'out': 'undergone'},
        {'in': 'undergoes', 'out': 'undergone'},
        {'in': 'undergoing', 'out': 'undergone'},
        {'in': 'undergone', 'out': 'undergone'},
        {'in': 'underlain', 'out': 'underlain'},
        {'in': 'underlay', 'out': 'underlain'},
        {'in': 'underlie', 'out': 'underlain'},
        {'in': 'underlies', 'out': 'underlain'},
        {'in': 'underlying', 'out': 'underlain'},
        {'in': 'understand', 'out': 'understood'},
        {'in': 'understanding', 'out': 'understood'},
        {'in': 'understands', 'out': 'understood'},
        {'in': 'understood', 'out': 'understood'},
        {'in': 'undertake', 'out': 'undertaken'},
        {'in': 'undertaken', 'out': 'undertaken'},
        {'in': 'undertakes', 'out': 'undertaken'},
        {'in': 'undertaking', 'out': 'undertaken'},
        {'in': 'undertook', 'out': 'undertaken'},
        {'in': 'underwent', 'out': 'undergone'},
        {'in': 'upset', 'out': 'upset'},
        {'in': 'upsets', 'out': 'upset'},
        {'in': 'upsetting', 'out': 'upset'},
        {'in': 'vex', 'out': 'vexed'},
        {'in': 'vexed', 'out': 'vexed'},
        {'in': 'vexes', 'out': 'vexed'},
        {'in': 'vexing', 'out': 'vexed'},
        {'in': 'vie', 'out': 'vied'},
        {'in': 'vied', 'out': 'vied'},
        {'in': 'vies', 'out': 'vied'},
        {'in': 'vying', 'out': 'vied'},
        {'in': 'wait', 'out': 'waited'},
        {'in': 'waited', 'out': 'waited'},
        {'in': 'waiting', 'out': 'waited'},
        {'in': 'waits', 'out': 'waited'},
        {'in': 'wake', 'out': 'woken'},
        {'in': 'wakes', 'out': 'woken'},
        {'in': 'waking', 'out': 'woken'},
        {'in': 'walk', 'out': 'walked'},
        {'in': 'walked', 'out': 'walked'},
        {'in': 'walking', 'out': 'walked'},
        {'in': 'walks', 'out': 'walked'},
        {'in': 'want', 'out': 'wanted'},
        {'in': 'wanted', 'out': 'wanted'},
        {'in': 'wanting', 'out': 'wanted'},
        {'in': 'wants', 'out': 'wanted'},
        {'in': 'was', 'out': 'been'},
        {'in': 'watch', 'out': 'watched'},
        {'in': 'watched', 'out': 'watched'},
        {'in': 'watches', 'out': 'watched'},
        {'in': 'watching', 'out': 'watched'},
        {'in': 'wear', 'out': 'worn'},
        {'in': 'wearing', 'out': 'worn'},
        {'in': 'wears', 'out': 'worn'},
        {'in': 'weep', 'out': 'wept'},
        {'in': 'weeping', 'out': 'wept'},
        {'in': 'weeps', 'out': 'wept'},
        {'in': 'wend', 'out': 'wended'},
        {'in': 'wended', 'out': 'wended'},
        {'in': 'wending', 'out': 'wended'},
        {'in': 'wends', 'out': 'wended'},
        {'in': 'went', 'out': 'gone'},
        {'in': 'wept', 'out': 'wept'},
        {'in': 'were', 'out': 'been'},
        {'in': 'win', 'out': 'won'},
        {'in': 'winning', 'out': 'won'},
        {'in': 'wins', 'out': 'won'},
        {'in': 'wis', 'out': 'wised'},
        {'in': 'wised', 'out': 'wised'},
        {'in': 'wises', 'out': 'wised'},
        {'in': 'wising', 'out': 'wised'},
        {'in': 'withdraw', 'out': 'withdrawn'},
        {'in': 'withdrawing', 'out': 'withdrawn'},
        {'in': 'withdrawn', 'out': 'withdrawn'},
        {'in': 'withdraws', 'out': 'withdrawn'},
        {'in': 'withdrew', 'out': 'withdrawn'},
        {'in': 'withheld', 'out': 'withheld'},
        {'in': 'withhold', 'out': 'withheld'},
        {'in': 'withholding', 'out': 'withheld'},
        {'in': 'withholds', 'out': 'withheld'},
        {'in': 'withstand', 'out': 'withstood'},
        {'in': 'withstanding', 'out': 'withstood'},
        {'in': 'withstands', 'out': 'withstood'},
        {'in': 'withstood', 'out': 'withstood'},
        {'in': 'woke', 'out': 'woken'},
        {'in': 'woken', 'out': 'woken'},
        {'in': 'won', 'out': 'won'},
        {'in': 'wore', 'out': 'worn'},
        {'in': 'worn', 'out': 'worn'},
        {'in': 'wring', 'out': 'wrung'},
        {'in': 'wringing', 'out': 'wrung'},
        {'in': 'wrings', 'out': 'wrung'},
        {'in': 'wrung', 'out': 'wrung'},
    ]

    def test_convert_to_past_part(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"convert_to_past_part({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": dict()
                }}
                self.assertEqual(convert_to_past_part(test_case["in"], **test_case["kwargs"]), test_case["out"], test_case["desc"])

if __name__ == "__main__":
    unittest.main()
