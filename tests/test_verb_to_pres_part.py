
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

from verb_output import convert_to_pres_part

class TestVerbToPresPart(unittest.TestCase):
    # test_args has the format [{
    #    "in":     ..., # (required)
    #    "out":    ..., # (required)
    #    "desc":   ..., # (optional) 
    #    "kwargs": ...  # (optional)
    # }, ...
    # ]
    test_args = [
        {'in': 'abide', 'out': 'abiding'},
        {'in': 'abided', 'out': 'abiding'},
        {'in': 'abides', 'out': 'abiding'},
        {'in': 'abiding', 'out': 'abiding'},
        {'in': 'ache', 'out': 'aching'},
        {'in': 'ached', 'out': 'aching'},
        {'in': 'aches', 'out': 'aching'},
        {'in': 'aching', 'out': 'aching'},
        {'in': 'am', 'out': 'being'},
        {'in': 'are', 'out': 'being'},
        {'in': 'arise', 'out': 'arising'},
        {'in': 'arisen', 'out': 'arising'},
        {'in': 'arises', 'out': 'arising'},
        {'in': 'arising', 'out': 'arising'},
        {'in': 'arose', 'out': 'arising'},
        {'in': 'ask', 'out': 'asking'},
        {'in': 'asked', 'out': 'asking'},
        {'in': 'asking', 'out': 'asking'},
        {'in': 'asks', 'out': 'asking'},
        {'in': 'ate', 'out': 'eating'},
        {'in': 'avalanche', 'out': 'avalanching'},
        {'in': 'avalanched', 'out': 'avalanching'},
        {'in': 'avalanches', 'out': 'avalanching'},
        {'in': 'avalanching', 'out': 'avalanching'},
        {'in': 'awake', 'out': 'awakening'},
        {'in': 'awakening', 'out': 'awakening'},
        {'in': 'awakes', 'out': 'awakening'},
        {'in': 'awoke', 'out': 'awakening'},
        {'in': 'awoken', 'out': 'awakening'},
        {'in': 'beat', 'out': 'beating'},
        {'in': 'beaten', 'out': 'beating'},
        {'in': 'beating', 'out': 'beating'},
        {'in': 'beats', 'out': 'beating'},
        {'in': 'became', 'out': 'becoming'},
        {'in': 'become', 'out': 'becoming'},
        {'in': 'becomes', 'out': 'becoming'},
        {'in': 'becoming', 'out': 'becoming'},
        {'in': 'been', 'out': 'being'},
        {'in': 'began', 'out': 'beginning'},
        {'in': 'beget', 'out': 'begetting'},
        {'in': 'begets', 'out': 'begetting'},
        {'in': 'begetting', 'out': 'begetting'},
        {'in': 'begin', 'out': 'beginning'},
        {'in': 'beginning', 'out': 'beginning'},
        {'in': 'begins', 'out': 'beginning'},
        {'in': 'begot', 'out': 'begetting'},
        {'in': 'begotten', 'out': 'begetting'},
        {'in': 'begun', 'out': 'beginning'},
        {'in': 'beheld', 'out': 'beholding'},
        {'in': 'behold', 'out': 'beholding'},
        {'in': 'beholding', 'out': 'beholding'},
        {'in': 'beholds', 'out': 'beholding'},
        {'in': 'being', 'out': 'being'},
        {'in': 'bellyache', 'out': 'bellyaching'},
        {'in': 'bellyached', 'out': 'bellyaching'},
        {'in': 'bellyaches', 'out': 'bellyaching'},
        {'in': 'bellyaching', 'out': 'bellyaching'},
        {'in': 'bend', 'out': 'bending'},
        {'in': 'bending', 'out': 'bending'},
        {'in': 'bends', 'out': 'bending'},
        {'in': 'bent', 'out': 'bending'},
        {'in': 'bet', 'out': 'betting'},
        {'in': 'bets', 'out': 'betting'},
        {'in': 'betting', 'out': 'betting'},
        {'in': 'bind', 'out': 'binding'},
        {'in': 'binding', 'out': 'binding'},
        {'in': 'binds', 'out': 'binding'},
        {'in': 'bit', 'out': 'biting'},
        {'in': 'bite', 'out': 'biting'},
        {'in': 'bites', 'out': 'biting'},
        {'in': 'biting', 'out': 'biting'},
        {'in': 'bitten', 'out': 'biting'},
        {'in': 'bled', 'out': 'bleeding'},
        {'in': 'bleed', 'out': 'bleeding'},
        {'in': 'bleeding', 'out': 'bleeding'},
        {'in': 'bleeds', 'out': 'bleeding'},
        {'in': 'blew', 'out': 'blowing'},
        {'in': 'blitz', 'out': 'blitzing'},
        {'in': 'blitzed', 'out': 'blitzing'},
        {'in': 'blitzes', 'out': 'blitzing'},
        {'in': 'blitzing', 'out': 'blitzing'},
        {'in': 'blow', 'out': 'blowing'},
        {'in': 'blowing', 'out': 'blowing'},
        {'in': 'blown', 'out': 'blowing'},
        {'in': 'blows', 'out': 'blowing'},
        {'in': 'bound', 'out': 'binding'},
        {'in': 'break', 'out': 'breaking'},
        {'in': 'breaking', 'out': 'breaking'},
        {'in': 'breaks', 'out': 'breaking'},
        {'in': 'bred', 'out': 'breeding'},
        {'in': 'breed', 'out': 'breeding'},
        {'in': 'breeding', 'out': 'breeding'},
        {'in': 'breeds', 'out': 'breeding'},
        {'in': 'bring', 'out': 'bringing'},
        {'in': 'bringing', 'out': 'bringing'},
        {'in': 'brings', 'out': 'bringing'},
        {'in': 'broke', 'out': 'breaking'},
        {'in': 'broken', 'out': 'breaking'},
        {'in': 'brought', 'out': 'bringing'},
        {'in': 'build', 'out': 'building'},
        {'in': 'building', 'out': 'building'},
        {'in': 'builds', 'out': 'building'},
        {'in': 'built', 'out': 'building'},
        {'in': 'burn', 'out': 'burning'},
        {'in': 'burning', 'out': 'burning'},
        {'in': 'burns', 'out': 'burning'},
        {'in': 'burnt', 'out': 'burning'},
        {'in': 'burst', 'out': 'bursting'},
        {'in': 'bursting', 'out': 'bursting'},
        {'in': 'bursts', 'out': 'bursting'},
        {'in': 'bust', 'out': 'busting'},
        {'in': 'busting', 'out': 'busting'},
        {'in': 'busts', 'out': 'busting'},
        {'in': 'cache', 'out': 'caching'},
        {'in': 'cached', 'out': 'caching'},
        {'in': 'caches', 'out': 'caching'},
        {'in': 'caching', 'out': 'caching'},
        {'in': 'came', 'out': 'coming'},
        {'in': 'catch', 'out': 'catching'},
        {'in': 'catches', 'out': 'catching'},
        {'in': 'catching', 'out': 'catching'},
        {'in': 'caught', 'out': 'catching'},
        {'in': 'change', 'out': 'changing'},
        {'in': 'changed', 'out': 'changing'},
        {'in': 'changes', 'out': 'changing'},
        {'in': 'changing', 'out': 'changing'},
        {'in': 'choose', 'out': 'choosing'},
        {'in': 'chooses', 'out': 'choosing'},
        {'in': 'choosing', 'out': 'choosing'},
        {'in': 'chose', 'out': 'choosing'},
        {'in': 'chosen', 'out': 'choosing'},
        {'in': 'clap', 'out': 'clapping'},
        {'in': 'clapped', 'out': 'clapping'},
        {'in': 'clapping', 'out': 'clapping'},
        {'in': 'claps', 'out': 'clapping'},
        {'in': 'cling', 'out': 'clinging'},
        {'in': 'clinging', 'out': 'clinging'},
        {'in': 'clings', 'out': 'clinging'},
        {'in': 'clung', 'out': 'clinging'},
        {'in': 'come', 'out': 'coming'},
        {'in': 'comes', 'out': 'coming'},
        {'in': 'coming', 'out': 'coming'},
        {'in': 'continue', 'out': 'continuing'},
        {'in': 'continued', 'out': 'continuing'},
        {'in': 'continues', 'out': 'continuing'},
        {'in': 'continuing', 'out': 'continuing'},
        {'in': 'cost', 'out': 'costing'},
        {'in': 'costing', 'out': 'costing'},
        {'in': 'costs', 'out': 'costing'},
        {'in': 'creche', 'out': 'creching'},
        {'in': 'creched', 'out': 'creching'},
        {'in': 'creches', 'out': 'creching'},
        {'in': 'creching', 'out': 'creching'},
        {'in': 'creep', 'out': 'creeping'},
        {'in': 'creeping', 'out': 'creeping'},
        {'in': 'creeps', 'out': 'creeping'},
        {'in': 'crept', 'out': 'creeping'},
        {'in': 'dare', 'out': 'daring'},
        {'in': 'dared', 'out': 'daring'},
        {'in': 'dares', 'out': 'daring'},
        {'in': 'daring', 'out': 'daring'},
        {'in': 'deal', 'out': 'dealing'},
        {'in': 'dealing', 'out': 'dealing'},
        {'in': 'deals', 'out': 'dealing'},
        {'in': 'dealt', 'out': 'dealing'},
        {'in': 'die', 'out': 'dying'},
        {'in': 'died', 'out': 'dying'},
        {'in': 'dies', 'out': 'dying'},
        {'in': 'dig', 'out': 'digging'},
        {'in': 'digging', 'out': 'digging'},
        {'in': 'digs', 'out': 'digging'},
        {'in': 'dive', 'out': 'diving'},
        {'in': 'dived', 'out': 'diving'},
        {'in': 'dives', 'out': 'diving'},
        {'in': 'diving', 'out': 'diving'},
        {'in': 'douche', 'out': 'douching'},
        {'in': 'douched', 'out': 'douching'},
        {'in': 'douches', 'out': 'douching'},
        {'in': 'douching', 'out': 'douching'},
        {'in': 'drag', 'out': 'dragging'},
        {'in': 'dragged', 'out': 'dragging'},
        {'in': 'dragging', 'out': 'dragging'},
        {'in': 'drags', 'out': 'dragging'},
        {'in': 'drank', 'out': 'drinking'},
        {'in': 'dream', 'out': 'dreaming'},
        {'in': 'dreamed', 'out': 'dreaming'},
        {'in': 'dreaming', 'out': 'dreaming'},
        {'in': 'dreams', 'out': 'dreaming'},
        {'in': 'drink', 'out': 'drinking'},
        {'in': 'drinking', 'out': 'drinking'},
        {'in': 'drinks', 'out': 'drinking'},
        {'in': 'drive', 'out': 'driving'},
        {'in': 'driven', 'out': 'driving'},
        {'in': 'drives', 'out': 'driving'},
        {'in': 'driving', 'out': 'driving'},
        {'in': 'drove', 'out': 'driving'},
        {'in': 'drunk', 'out': 'drinking'},
        {'in': 'dug', 'out': 'digging'},
        {'in': 'dwell', 'out': 'dwelling'},
        {'in': 'dwelling', 'out': 'dwelling'},
        {'in': 'dwells', 'out': 'dwelling'},
        {'in': 'dwelt', 'out': 'dwelling'},
        {'in': 'dying', 'out': 'dying'},
        {'in': 'eat', 'out': 'eating'},
        {'in': 'eaten', 'out': 'eating'},
        {'in': 'eating', 'out': 'eating'},
        {'in': 'eats', 'out': 'eating'},
        {'in': 'expect', 'out': 'expecting'},
        {'in': 'expected', 'out': 'expecting'},
        {'in': 'expecting', 'out': 'expecting'},
        {'in': 'expects', 'out': 'expecting'},
        {'in': 'fall', 'out': 'falling'},
        {'in': 'fallen', 'out': 'falling'},
        {'in': 'falling', 'out': 'falling'},
        {'in': 'falls', 'out': 'falling'},
        {'in': 'feel', 'out': 'feeling'},
        {'in': 'feeling', 'out': 'feeling'},
        {'in': 'feels', 'out': 'feeling'},
        {'in': 'fell', 'out': 'falling'},
        {'in': 'felt', 'out': 'feeling'},
        {'in': 'fight', 'out': 'fighting'},
        {'in': 'fighting', 'out': 'fighting'},
        {'in': 'fights', 'out': 'fighting'},
        {'in': 'find', 'out': 'finding'},
        {'in': 'finding', 'out': 'finding'},
        {'in': 'finds', 'out': 'finding'},
        {'in': 'fled', 'out': 'fleeing'},
        {'in': 'flee', 'out': 'fleeing'},
        {'in': 'fleeing', 'out': 'fleeing'},
        {'in': 'flees', 'out': 'fleeing'},
        {'in': 'flew', 'out': 'flying'},
        {'in': 'flies', 'out': 'flying'},
        {'in': 'fling', 'out': 'flinging'},
        {'in': 'flinging', 'out': 'flinging'},
        {'in': 'flings', 'out': 'flinging'},
        {'in': 'flown', 'out': 'flying'},
        {'in': 'flung', 'out': 'flinging'},
        {'in': 'fly', 'out': 'flying'},
        {'in': 'flying', 'out': 'flying'},
        {'in': 'follow', 'out': 'following'},
        {'in': 'followed', 'out': 'following'},
        {'in': 'following', 'out': 'following'},
        {'in': 'follows', 'out': 'following'},
        {'in': 'forbade', 'out': 'forbidding'},
        {'in': 'forbid', 'out': 'forbidding'},
        {'in': 'forbidden', 'out': 'forbidding'},
        {'in': 'forbidding', 'out': 'forbidding'},
        {'in': 'forbids', 'out': 'forbidding'},
        {'in': 'foresaw', 'out': 'foreseeing'},
        {'in': 'foresee', 'out': 'foreseeing'},
        {'in': 'foreseeing', 'out': 'foreseeing'},
        {'in': 'foreseen', 'out': 'foreseeing'},
        {'in': 'foresees', 'out': 'foreseeing'},
        {'in': 'foretell', 'out': 'foretelling'},
        {'in': 'foretelling', 'out': 'foretelling'},
        {'in': 'foretells', 'out': 'foretelling'},
        {'in': 'foretold', 'out': 'foretelling'},
        {'in': 'forgave', 'out': 'forgiving'},
        {'in': 'forget', 'out': 'forgetting'},
        {'in': 'forgets', 'out': 'forgetting'},
        {'in': 'forgetting', 'out': 'forgetting'},
        {'in': 'forgive', 'out': 'forgiving'},
        {'in': 'forgiven', 'out': 'forgiving'},
        {'in': 'forgives', 'out': 'forgiving'},
        {'in': 'forgiving', 'out': 'forgiving'},
        {'in': 'forgot', 'out': 'forgetting'},
        {'in': 'forgotten', 'out': 'forgetting'},
        {'in': 'forsake', 'out': 'forsaking'},
        {'in': 'forsaken', 'out': 'forsaking'},
        {'in': 'forsakes', 'out': 'forsaking'},
        {'in': 'forsaking', 'out': 'forsaking'},
        {'in': 'forsook', 'out': 'forsaking'},
        {'in': 'fought', 'out': 'fighting'},
        {'in': 'found', 'out': 'finding'},
        {'in': 'gave', 'out': 'giving'},
        {'in': 'get', 'out': 'getting'},
        {'in': 'gets', 'out': 'getting'},
        {'in': 'getting', 'out': 'getting'},
        {'in': 'gild', 'out': 'gilding'},
        {'in': 'gilded', 'out': 'gilding'},
        {'in': 'gilding', 'out': 'gilding'},
        {'in': 'gilds', 'out': 'gilding'},
        {'in': 'give', 'out': 'giving'},
        {'in': 'given', 'out': 'giving'},
        {'in': 'gives', 'out': 'giving'},
        {'in': 'giving', 'out': 'giving'},
        {'in': 'go', 'out': 'going'},
        {'in': 'goes', 'out': 'going'},
        {'in': 'going', 'out': 'going'},
        {'in': 'gone', 'out': 'going'},
        {'in': 'got', 'out': 'getting'},
        {'in': 'gotten', 'out': 'getting'},
        {'in': 'grind', 'out': 'grinding'},
        {'in': 'grinding', 'out': 'grinding'},
        {'in': 'grinds', 'out': 'grinding'},
        {'in': 'ground', 'out': 'grinding'},
        {'in': 'had', 'out': 'having'},
        {'in': 'happen', 'out': 'happening'},
        {'in': 'happened', 'out': 'happening'},
        {'in': 'happening', 'out': 'happening'},
        {'in': 'happens', 'out': 'happening'},
        {'in': 'has', 'out': 'having'},
        {'in': 'have', 'out': 'having'},
        {'in': 'having', 'out': 'having'},
        {'in': 'held', 'out': 'holding'},
        {'in': 'help', 'out': 'helping'},
        {'in': 'helped', 'out': 'helping'},
        {'in': 'helping', 'out': 'helping'},
        {'in': 'helps', 'out': 'helping'},
        {'in': 'hew', 'out': 'hewing'},
        {'in': 'hewed', 'out': 'hewing'},
        {'in': 'hewing', 'out': 'hewing'},
        {'in': 'hewn', 'out': 'hewing'},
        {'in': 'hews', 'out': 'hewing'},
        {'in': 'hit', 'out': 'hitting'},
        {'in': 'hits', 'out': 'hitting'},
        {'in': 'hitting', 'out': 'hitting'},
        {'in': 'hold', 'out': 'holding'},
        {'in': 'holding', 'out': 'holding'},
        {'in': 'holds', 'out': 'holding'},
        {'in': 'hurt', 'out': 'hurting'},
        {'in': 'hurting', 'out': 'hurting'},
        {'in': 'hurts', 'out': 'hurting'},
        {'in': 'inlaid', 'out': 'inlaying'},
        {'in': 'inlay', 'out': 'inlaying'},
        {'in': 'inlaying', 'out': 'inlaying'},
        {'in': 'inlays', 'out': 'inlaying'},
        {'in': 'insist', 'out': 'insisting'},
        {'in': 'insisted', 'out': 'insisting'},
        {'in': 'insisting', 'out': 'insisting'},
        {'in': 'insists', 'out': 'insisting'},
        {'in': 'interlaid', 'out': 'interlaying'},
        {'in': 'interlay', 'out': 'interlaying'},
        {'in': 'interlaying', 'out': 'interlaying'},
        {'in': 'interlays', 'out': 'interlaying'},
        {'in': 'iris', 'out': 'irising'},
        {'in': 'irised', 'out': 'irising'},
        {'in': 'irises', 'out': 'irising'},
        {'in': 'irising', 'out': 'irising'},
        {'in': 'is', 'out': 'being'},
        {'in': 'keep', 'out': 'keeping'},
        {'in': 'keeping', 'out': 'keeping'},
        {'in': 'keeps', 'out': 'keeping'},
        {'in': 'kept', 'out': 'keeping'},
        {'in': 'kill', 'out': 'killing'},
        {'in': 'killed', 'out': 'killing'},
        {'in': 'killing', 'out': 'killing'},
        {'in': 'kills', 'out': 'killing'},
        {'in': 'kneel', 'out': 'kneeling'},
        {'in': 'kneeling', 'out': 'kneeling'},
        {'in': 'kneels', 'out': 'kneeling'},
        {'in': 'knelt', 'out': 'kneeling'},
        {'in': 'knew', 'out': 'knowing'},
        {'in': 'knit', 'out': 'knitting'},
        {'in': 'knits', 'out': 'knitting'},
        {'in': 'knitted', 'out': 'knitting'},
        {'in': 'knitting', 'out': 'knitting'},
        {'in': 'know', 'out': 'knowing'},
        {'in': 'knowing', 'out': 'knowing'},
        {'in': 'known', 'out': 'knowing'},
        {'in': 'knows', 'out': 'knowing'},
        {'in': 'laid', 'out': 'laying'},
        {'in': 'lain', 'out': 'lying'},
        {'in': 'lay', 'out': 'lying'},
        {'in': 'laying', 'out': 'laying'},
        {'in': 'lays', 'out': 'laying'},
        {'in': 'lead', 'out': 'leading'},
        {'in': 'leading', 'out': 'leading'},
        {'in': 'leads', 'out': 'leading'},
        {'in': 'lean', 'out': 'leaning'},
        {'in': 'leaned', 'out': 'leaning'},
        {'in': 'leaning', 'out': 'leaning'},
        {'in': 'leans', 'out': 'leaning'},
        {'in': 'leap', 'out': 'leaping'},
        {'in': 'leaping', 'out': 'leaping'},
        {'in': 'leaps', 'out': 'leaping'},
        {'in': 'leapt', 'out': 'leaping'},
        {'in': 'learn', 'out': 'learning'},
        {'in': 'learned', 'out': 'learning'},
        {'in': 'learning', 'out': 'learning'},
        {'in': 'learns', 'out': 'learning'},
        {'in': 'leave', 'out': 'leaving'},
        {'in': 'leaves', 'out': 'leaving'},
        {'in': 'leaving', 'out': 'leaving'},
        {'in': 'led', 'out': 'leading'},
        {'in': 'left', 'out': 'leaving'},
        {'in': 'lie', 'out': 'lying'},
        {'in': 'lies', 'out': 'lying'},
        {'in': 'like', 'out': 'liking'},
        {'in': 'liked', 'out': 'liking'},
        {'in': 'likes', 'out': 'liking'},
        {'in': 'liking', 'out': 'liking'},
        {'in': 'live', 'out': 'living'},
        {'in': 'lived', 'out': 'living'},
        {'in': 'lives', 'out': 'living'},
        {'in': 'living', 'out': 'living'},
        {'in': 'look', 'out': 'looking'},
        {'in': 'looked', 'out': 'looking'},
        {'in': 'looking', 'out': 'looking'},
        {'in': 'looks', 'out': 'looking'},
        {'in': 'lose', 'out': 'losing'},
        {'in': 'loses', 'out': 'losing'},
        {'in': 'losing', 'out': 'losing'},
        {'in': 'lost', 'out': 'losing'},
        {'in': 'love', 'out': 'loving'},
        {'in': 'loved', 'out': 'loving'},
        {'in': 'loves', 'out': 'loving'},
        {'in': 'loving', 'out': 'loving'},
        {'in': 'lying', 'out': 'lying'},
        {'in': 'mean', 'out': 'meaning'},
        {'in': 'meaning', 'out': 'meaning'},
        {'in': 'means', 'out': 'meaning'},
        {'in': 'meant', 'out': 'meaning'},
        {'in': 'meet', 'out': 'meeting'},
        {'in': 'meeting', 'out': 'meeting'},
        {'in': 'meets', 'out': 'meeting'},
        {'in': 'menu', 'out': 'menuing'},
        {'in': 'menued', 'out': 'menuing'},
        {'in': 'menuing', 'out': 'menuing'},
        {'in': 'menus', 'out': 'menuing'},
        {'in': 'met', 'out': 'meeting'},
        {'in': 'mislead', 'out': 'misleading'},
        {'in': 'misleading', 'out': 'misleading'},
        {'in': 'misleads', 'out': 'misleading'},
        {'in': 'misled', 'out': 'misleading'},
        {'in': 'mistake', 'out': 'mistaking'},
        {'in': 'mistaken', 'out': 'mistaking'},
        {'in': 'mistakes', 'out': 'mistaking'},
        {'in': 'mistaking', 'out': 'mistaking'},
        {'in': 'mistook', 'out': 'mistaking'},
        {'in': 'misunderstand', 'out': 'misunderstanding'},
        {'in': 'misunderstanding', 'out': 'misunderstanding'},
        {'in': 'misunderstands', 'out': 'misunderstanding'},
        {'in': 'misunderstood', 'out': 'misunderstanding'},
        {'in': 'move', 'out': 'moving'},
        {'in': 'moved', 'out': 'moving'},
        {'in': 'moves', 'out': 'moving'},
        {'in': 'moving', 'out': 'moving'},
        {'in': 'need', 'out': 'needing'},
        {'in': 'needed', 'out': 'needing'},
        {'in': 'needing', 'out': 'needing'},
        {'in': 'needs', 'out': 'needing'},
        {'in': 'niche', 'out': 'nicheing'},
        {'in': 'niched', 'out': 'nicheing'},
        {'in': 'nicheing', 'out': 'nicheing'},
        {'in': 'niches', 'out': 'nicheing'},
        {'in': 'overdraw', 'out': 'overdrawing'},
        {'in': 'overdrawing', 'out': 'overdrawing'},
        {'in': 'overdrawn', 'out': 'overdrawing'},
        {'in': 'overdraws', 'out': 'overdrawing'},
        {'in': 'overdrew', 'out': 'overdrawing'},
        {'in': 'overhear', 'out': 'overhearing'},
        {'in': 'overheard', 'out': 'overhearing'},
        {'in': 'overhearing', 'out': 'overhearing'},
        {'in': 'overhears', 'out': 'overhearing'},
        {'in': 'overtake', 'out': 'overtaking'},
        {'in': 'overtaken', 'out': 'overtaking'},
        {'in': 'overtakes', 'out': 'overtaking'},
        {'in': 'overtaking', 'out': 'overtaking'},
        {'in': 'overtook', 'out': 'overtaking'},
        {'in': 'preset', 'out': 'presetting'},
        {'in': 'presets', 'out': 'presetting'},
        {'in': 'presetting', 'out': 'presetting'},
        {'in': 'prove', 'out': 'proving'},
        {'in': 'proved', 'out': 'proving'},
        {'in': 'proven', 'out': 'proving'},
        {'in': 'proves', 'out': 'proving'},
        {'in': 'provide', 'out': 'providing'},
        {'in': 'provided', 'out': 'providing'},
        {'in': 'provides', 'out': 'providing'},
        {'in': 'providing', 'out': 'providing'},
        {'in': 'proving', 'out': 'proving'},
        {'in': 'psyche', 'out': 'psyching'},
        {'in': 'psyched', 'out': 'psyching'},
        {'in': 'psyches', 'out': 'psyching'},
        {'in': 'psyching', 'out': 'psyching'},
        {'in': 'put', 'out': 'putting'},
        {'in': 'puts', 'out': 'putting'},
        {'in': 'putting', 'out': 'putting'},
        {'in': 'quit', 'out': 'quitting'},
        {'in': 'quits', 'out': 'quitting'},
        {'in': 'quitting', 'out': 'quitting'},
        {'in': 'quiz', 'out': 'quizzing'},
        {'in': 'quizzed', 'out': 'quizzing'},
        {'in': 'quizzes', 'out': 'quizzing'},
        {'in': 'quizzing', 'out': 'quizzing'},
        {'in': 'ran', 'out': 'running'},
        {'in': 'rang', 'out': 'ringing'},
        {'in': 'reach', 'out': 'reaching'},
        {'in': 'reached', 'out': 'reaching'},
        {'in': 'reaches', 'out': 'reaching'},
        {'in': 'reaching', 'out': 'reaching'},
        {'in': 'remain', 'out': 'remaining'},
        {'in': 'remained', 'out': 'remaining'},
        {'in': 'remaining', 'out': 'remaining'},
        {'in': 'remains', 'out': 'remaining'},
        {'in': 'remember', 'out': 'remembering'},
        {'in': 'remembered', 'out': 'remembering'},
        {'in': 'remembering', 'out': 'remembering'},
        {'in': 'remembers', 'out': 'remembering'},
        {'in': 'rend', 'out': 'rending'},
        {'in': 'rending', 'out': 'rending'},
        {'in': 'rends', 'out': 'rending'},
        {'in': 'rent', 'out': 'rending'},
        {'in': 'rid', 'out': 'ridding'},
        {'in': 'ridden', 'out': 'riding'},
        {'in': 'ridding', 'out': 'ridding'},
        {'in': 'ride', 'out': 'riding'},
        {'in': 'rides', 'out': 'riding'},
        {'in': 'riding', 'out': 'riding'},
        {'in': 'rids', 'out': 'ridding'},
        {'in': 'ring', 'out': 'ringing'},
        {'in': 'ringing', 'out': 'ringing'},
        {'in': 'rings', 'out': 'ringing'},
        {'in': 'rise', 'out': 'rising'},
        {'in': 'risen', 'out': 'rising'},
        {'in': 'rises', 'out': 'rising'},
        {'in': 'rising', 'out': 'rising'},
        {'in': 'rive', 'out': 'riving'},
        {'in': 'rived', 'out': 'riving'},
        {'in': 'riven', 'out': 'riving'},
        {'in': 'rives', 'out': 'riving'},
        {'in': 'riving', 'out': 'riving'},
        {'in': 'rode', 'out': 'riding'},
        {'in': 'rose', 'out': 'rising'},
        {'in': 'run', 'out': 'running'},
        {'in': 'rung', 'out': 'ringing'},
        {'in': 'running', 'out': 'running'},
        {'in': 'runs', 'out': 'running'},
        {'in': 'sang', 'out': 'singing'},
        {'in': 'sank', 'out': 'sinking'},
        {'in': 'sat', 'out': 'sitting'},
        {'in': 'saw', 'out': 'sawing'},
        {'in': 'sawed', 'out': 'sawing'},
        {'in': 'sawing', 'out': 'sawing'},
        {'in': 'sawn', 'out': 'sawing'},
        {'in': 'saws', 'out': 'sawing'},
        {'in': 'seek', 'out': 'seeking'},
        {'in': 'seeking', 'out': 'seeking'},
        {'in': 'seeks', 'out': 'seeking'},
        {'in': 'seem', 'out': 'seeming'},
        {'in': 'seemed', 'out': 'seeming'},
        {'in': 'seeming', 'out': 'seeming'},
        {'in': 'seems', 'out': 'seeming'},
        {'in': 'shake', 'out': 'shaking'},
        {'in': 'shaken', 'out': 'shaking'},
        {'in': 'shakes', 'out': 'shaking'},
        {'in': 'shaking', 'out': 'shaking'},
        {'in': 'shat', 'out': 'shitting'},
        {'in': 'shave', 'out': 'shaving'},
        {'in': 'shaved', 'out': 'shaving'},
        {'in': 'shaves', 'out': 'shaving'},
        {'in': 'shaving', 'out': 'shaving'},
        {'in': 'shed', 'out': 'shedding'},
        {'in': 'shedding', 'out': 'shedding'},
        {'in': 'sheds', 'out': 'shedding'},
        {'in': 'shit', 'out': 'shitting'},
        {'in': 'shits', 'out': 'shitting'},
        {'in': 'shitted', 'out': 'shitting'},
        {'in': 'shitting', 'out': 'shitting'},
        {'in': 'shod', 'out': 'shoeing'},
        {'in': 'shoe', 'out': 'shoeing'},
        {'in': 'shoeing', 'out': 'shoeing'},
        {'in': 'shoes', 'out': 'shoeing'},
        {'in': 'shook', 'out': 'shaking'},
        {'in': 'show', 'out': 'showing'},
        {'in': 'showed', 'out': 'showing'},
        {'in': 'showing', 'out': 'showing'},
        {'in': 'shown', 'out': 'showing'},
        {'in': 'shows', 'out': 'showing'},
        {'in': 'shrank', 'out': 'shrinking'},
        {'in': 'shrink', 'out': 'shrinking'},
        {'in': 'shrinking', 'out': 'shrinking'},
        {'in': 'shrinks', 'out': 'shrinking'},
        {'in': 'shrunk', 'out': 'shrinking'},
        {'in': 'sing', 'out': 'singing'},
        {'in': 'singing', 'out': 'singing'},
        {'in': 'sings', 'out': 'singing'},
        {'in': 'sink', 'out': 'sinking'},
        {'in': 'sinking', 'out': 'sinking'},
        {'in': 'sinks', 'out': 'sinking'},
        {'in': 'sit', 'out': 'sitting'},
        {'in': 'sits', 'out': 'sitting'},
        {'in': 'sitting', 'out': 'sitting'},
        {'in': 'ski', 'out': 'skiing'},
        {'in': 'skied', 'out': 'skiing'},
        {'in': 'skiing', 'out': 'skiing'},
        {'in': 'skis', 'out': 'skiing'},
        {'in': 'slain', 'out': 'slaying'},
        {'in': 'slay', 'out': 'slaying'},
        {'in': 'slaying', 'out': 'slaying'},
        {'in': 'slays', 'out': 'slaying'},
        {'in': 'slew', 'out': 'slaying'},
        {'in': 'slid', 'out': 'sliding'},
        {'in': 'slide', 'out': 'sliding'},
        {'in': 'slides', 'out': 'sliding'},
        {'in': 'sliding', 'out': 'sliding'},
        {'in': 'slink', 'out': 'slinking'},
        {'in': 'slinking', 'out': 'slinking'},
        {'in': 'slinks', 'out': 'slinking'},
        {'in': 'slit', 'out': 'slitting'},
        {'in': 'slits', 'out': 'slitting'},
        {'in': 'slitting', 'out': 'slitting'},
        {'in': 'slunk', 'out': 'slinking'},
        {'in': 'smell', 'out': 'smelling'},
        {'in': 'smelled', 'out': 'smelling'},
        {'in': 'smelling', 'out': 'smelling'},
        {'in': 'smells', 'out': 'smelling'},
        {'in': 'smite', 'out': 'smiting'},
        {'in': 'smites', 'out': 'smiting'},
        {'in': 'smiting', 'out': 'smiting'},
        {'in': 'smitten', 'out': 'smiting'},
        {'in': 'smote', 'out': 'smiting'},
        {'in': 'sneak', 'out': 'sneaking'},
        {'in': 'sneaked', 'out': 'sneaking'},
        {'in': 'sneaking', 'out': 'sneaking'},
        {'in': 'sneaks', 'out': 'sneaking'},
        {'in': 'sought', 'out': 'seeking'},
        {'in': 'sow', 'out': 'sowing'},
        {'in': 'sowed', 'out': 'sowing'},
        {'in': 'sowing', 'out': 'sowing'},
        {'in': 'sown', 'out': 'sowing'},
        {'in': 'sows', 'out': 'sowing'},
        {'in': 'spat', 'out': 'spitting'},
        {'in': 'speak', 'out': 'speaking'},
        {'in': 'speaking', 'out': 'speaking'},
        {'in': 'speaks', 'out': 'speaking'},
        {'in': 'sped', 'out': 'speeding'},
        {'in': 'speed', 'out': 'speeding'},
        {'in': 'speeding', 'out': 'speeding'},
        {'in': 'speeds', 'out': 'speeding'},
        {'in': 'spend', 'out': 'spending'},
        {'in': 'spending', 'out': 'spending'},
        {'in': 'spends', 'out': 'spending'},
        {'in': 'spent', 'out': 'spending'},
        {'in': 'spit', 'out': 'spitting'},
        {'in': 'spits', 'out': 'spitting'},
        {'in': 'spitting', 'out': 'spitting'},
        {'in': 'spoil', 'out': 'spoiling'},
        {'in': 'spoiled', 'out': 'spoiling'},
        {'in': 'spoiling', 'out': 'spoiling'},
        {'in': 'spoils', 'out': 'spoiling'},
        {'in': 'spoilt', 'out': 'spoiling'},
        {'in': 'spoke', 'out': 'speaking'},
        {'in': 'spoken', 'out': 'speaking'},
        {'in': 'sprang', 'out': 'springing'},
        {'in': 'spring', 'out': 'springing'},
        {'in': 'springing', 'out': 'springing'},
        {'in': 'springs', 'out': 'springing'},
        {'in': 'sprung', 'out': 'springing'},
        {'in': 'stand', 'out': 'standing'},
        {'in': 'standing', 'out': 'standing'},
        {'in': 'stands', 'out': 'standing'},
        {'in': 'stank', 'out': 'stinking'},
        {'in': 'stave', 'out': 'staving'},
        {'in': 'staved', 'out': 'staving'},
        {'in': 'staves', 'out': 'staving'},
        {'in': 'staving', 'out': 'staving'},
        {'in': 'stay', 'out': 'staying'},
        {'in': 'stayed', 'out': 'staying'},
        {'in': 'staying', 'out': 'staying'},
        {'in': 'stays', 'out': 'staying'},
        {'in': 'steal', 'out': 'stealing'},
        {'in': 'stealing', 'out': 'stealing'},
        {'in': 'steals', 'out': 'stealing'},
        {'in': 'sting', 'out': 'stinging'},
        {'in': 'stinging', 'out': 'stinging'},
        {'in': 'stings', 'out': 'stinging'},
        {'in': 'stink', 'out': 'stinking'},
        {'in': 'stinking', 'out': 'stinking'},
        {'in': 'stinks', 'out': 'stinking'},
        {'in': 'stole', 'out': 'stealing'},
        {'in': 'stolen', 'out': 'stealing'},
        {'in': 'stood', 'out': 'standing'},
        {'in': 'stop', 'out': 'stopping'},
        {'in': 'stopped', 'out': 'stopping'},
        {'in': 'stopping', 'out': 'stopping'},
        {'in': 'stops', 'out': 'stopping'},
        {'in': 'strew', 'out': 'strewing'},
        {'in': 'strewed', 'out': 'strewing'},
        {'in': 'strewing', 'out': 'strewing'},
        {'in': 'strewn', 'out': 'strewing'},
        {'in': 'strews', 'out': 'strewing'},
        {'in': 'stride', 'out': 'striding'},
        {'in': 'strides', 'out': 'striding'},
        {'in': 'striding', 'out': 'striding'},
        {'in': 'strip', 'out': 'stripping'},
        {'in': 'stripped', 'out': 'stripping'},
        {'in': 'stripping', 'out': 'stripping'},
        {'in': 'strips', 'out': 'stripping'},
        {'in': 'strive', 'out': 'striving'},
        {'in': 'strived', 'out': 'striving'},
        {'in': 'strives', 'out': 'striving'},
        {'in': 'striving', 'out': 'striving'},
        {'in': 'strode', 'out': 'striding'},
        {'in': 'strove', 'out': 'striving'},
        {'in': 'stung', 'out': 'stinging'},
        {'in': 'stunk', 'out': 'stinking'},
        {'in': 'sublet', 'out': 'subletting'},
        {'in': 'sublets', 'out': 'subletting'},
        {'in': 'subletting', 'out': 'subletting'},
        {'in': 'sunburn', 'out': 'sunburning'},
        {'in': 'sunburned', 'out': 'sunburning'},
        {'in': 'sunburning', 'out': 'sunburning'},
        {'in': 'sunburns', 'out': 'sunburning'},
        {'in': 'sung', 'out': 'singing'},
        {'in': 'sunk', 'out': 'sinking'},
        {'in': 'swam', 'out': 'swimming'},
        {'in': 'swear', 'out': 'swearing'},
        {'in': 'swearing', 'out': 'swearing'},
        {'in': 'swears', 'out': 'swearing'},
        {'in': 'sweat', 'out': 'sweating'},
        {'in': 'sweated', 'out': 'sweating'},
        {'in': 'sweating', 'out': 'sweating'},
        {'in': 'sweats', 'out': 'sweating'},
        {'in': 'sweep', 'out': 'sweeping'},
        {'in': 'sweeping', 'out': 'sweeping'},
        {'in': 'sweeps', 'out': 'sweeping'},
        {'in': 'swell', 'out': 'swelling'},
        {'in': 'swelled', 'out': 'swelling'},
        {'in': 'swelling', 'out': 'swelling'},
        {'in': 'swells', 'out': 'swelling'},
        {'in': 'swept', 'out': 'sweeping'},
        {'in': 'swim', 'out': 'swimming'},
        {'in': 'swimming', 'out': 'swimming'},
        {'in': 'swims', 'out': 'swimming'},
        {'in': 'swing', 'out': 'swinging'},
        {'in': 'swinging', 'out': 'swinging'},
        {'in': 'swings', 'out': 'swinging'},
        {'in': 'swollen', 'out': 'swelling'},
        {'in': 'swore', 'out': 'swearing'},
        {'in': 'sworn', 'out': 'swearing'},
        {'in': 'swum', 'out': 'swimming'},
        {'in': 'swung', 'out': 'swinging'},
        {'in': 'talk', 'out': 'talking'},
        {'in': 'talked', 'out': 'talking'},
        {'in': 'talking', 'out': 'talking'},
        {'in': 'talks', 'out': 'talking'},
        {'in': 'tear', 'out': 'tearing'},
        {'in': 'tearing', 'out': 'tearing'},
        {'in': 'tears', 'out': 'tearing'},
        {'in': 'thrive', 'out': 'thriving'},
        {'in': 'thrived', 'out': 'thriving'},
        {'in': 'thrives', 'out': 'thriving'},
        {'in': 'thriving', 'out': 'thriving'},
        {'in': 'thrust', 'out': 'thrusting'},
        {'in': 'thrusting', 'out': 'thrusting'},
        {'in': 'thrusts', 'out': 'thrusting'},
        {'in': 'tore', 'out': 'tearing'},
        {'in': 'torn', 'out': 'tearing'},
        {'in': 'tread', 'out': 'treading'},
        {'in': 'treading', 'out': 'treading'},
        {'in': 'treads', 'out': 'treading'},
        {'in': 'trod', 'out': 'treading'},
        {'in': 'trodden', 'out': 'treading'},
        {'in': 'undergo', 'out': 'undergoing'},
        {'in': 'undergoes', 'out': 'undergoing'},
        {'in': 'undergoing', 'out': 'undergoing'},
        {'in': 'undergone', 'out': 'undergoing'},
        {'in': 'understand', 'out': 'understanding'},
        {'in': 'understanding', 'out': 'understanding'},
        {'in': 'understands', 'out': 'understanding'},
        {'in': 'understood', 'out': 'understanding'},
        {'in': 'undertake', 'out': 'undertaking'},
        {'in': 'undertaken', 'out': 'undertaking'},
        {'in': 'undertakes', 'out': 'undertaking'},
        {'in': 'undertaking', 'out': 'undertaking'},
        {'in': 'undertook', 'out': 'undertaking'},
        {'in': 'underwent', 'out': 'undergoing'},
        {'in': 'upset', 'out': 'upsetting'},
        {'in': 'upsets', 'out': 'upsetting'},
        {'in': 'upsetting', 'out': 'upsetting'},
        {'in': 'vex', 'out': 'vexing'},
        {'in': 'vexed', 'out': 'vexing'},
        {'in': 'vexes', 'out': 'vexing'},
        {'in': 'vexing', 'out': 'vexing'},
        {'in': 'wait', 'out': 'waiting'},
        {'in': 'waited', 'out': 'waiting'},
        {'in': 'waiting', 'out': 'waiting'},
        {'in': 'waits', 'out': 'waiting'},
        {'in': 'wake', 'out': 'waking'},
        {'in': 'wakes', 'out': 'waking'},
        {'in': 'waking', 'out': 'waking'},
        {'in': 'walk', 'out': 'walking'},
        {'in': 'walked', 'out': 'walking'},
        {'in': 'walking', 'out': 'walking'},
        {'in': 'walks', 'out': 'walking'},
        {'in': 'want', 'out': 'wanting'},
        {'in': 'wanted', 'out': 'wanting'},
        {'in': 'wanting', 'out': 'wanting'},
        {'in': 'wants', 'out': 'wanting'},
        {'in': 'was', 'out': 'being'},
        {'in': 'watch', 'out': 'watching'},
        {'in': 'watched', 'out': 'watching'},
        {'in': 'watches', 'out': 'watching'},
        {'in': 'watching', 'out': 'watching'},
        {'in': 'wear', 'out': 'wearing'},
        {'in': 'wearing', 'out': 'wearing'},
        {'in': 'wears', 'out': 'wearing'},
        {'in': 'weep', 'out': 'weeping'},
        {'in': 'weeping', 'out': 'weeping'},
        {'in': 'weeps', 'out': 'weeping'},
        {'in': 'wend', 'out': 'wending'},
        {'in': 'wended', 'out': 'wending'},
        {'in': 'wending', 'out': 'wending'},
        {'in': 'wends', 'out': 'wending'},
        {'in': 'went', 'out': 'going'},
        {'in': 'wept', 'out': 'weeping'},
        {'in': 'were', 'out': 'being'},
        {'in': 'win', 'out': 'winning'},
        {'in': 'winning', 'out': 'winning'},
        {'in': 'wins', 'out': 'winning'},
        {'in': 'withdraw', 'out': 'withdrawing'},
        {'in': 'withdrawing', 'out': 'withdrawing'},
        {'in': 'withdrawn', 'out': 'withdrawing'},
        {'in': 'withdraws', 'out': 'withdrawing'},
        {'in': 'withdrew', 'out': 'withdrawing'},
        {'in': 'withheld', 'out': 'withholding'},
        {'in': 'withhold', 'out': 'withholding'},
        {'in': 'withholding', 'out': 'withholding'},
        {'in': 'withholds', 'out': 'withholding'},
        {'in': 'withstand', 'out': 'withstanding'},
        {'in': 'withstanding', 'out': 'withstanding'},
        {'in': 'withstands', 'out': 'withstanding'},
        {'in': 'withstood', 'out': 'withstanding'},
        {'in': 'woke', 'out': 'waking'},
        {'in': 'woken', 'out': 'waking'},
        {'in': 'won', 'out': 'winning'},
        {'in': 'wore', 'out': 'wearing'},
        {'in': 'worn', 'out': 'wearing'},
        {'in': 'wring', 'out': 'wringing'},
        {'in': 'wringing', 'out': 'wringing'},
        {'in': 'wrings', 'out': 'wringing'},
        {'in': 'wrung', 'out': 'wringing'},
    ]

    def test_convert_to_pres_part(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"convert_to_pres_part({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": dict()
                }}
                self.assertEqual(convert_to_pres_part(test_case["in"], **test_case["kwargs"]), test_case["out"], test_case["desc"])

if __name__ == "__main__":
    unittest.main()
