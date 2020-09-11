
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

from verb import convert_to_past

class TestVerbToPast(unittest.TestCase):
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
        {'in': 'am', 'out': 'was'},
        {'in': 'are', 'out': 'were'},
        {'in': 'arise', 'out': 'arose'},
        {'in': 'arisen', 'out': 'arose'},
        {'in': 'arises', 'out': 'arose'},
        {'in': 'arising', 'out': 'arose'},
        {'in': 'ask', 'out': 'asked'},
        {'in': 'asked', 'out': 'asked'},
        {'in': 'asking', 'out': 'asked'},
        {'in': 'asks', 'out': 'asked'},
        {'in': 'avalanche', 'out': 'avalanched'},
        {'in': 'avalanched', 'out': 'avalanched'},
        {'in': 'avalanches', 'out': 'avalanched'},
        {'in': 'avalanching', 'out': 'avalanched'},
        {'in': 'awake', 'out': 'awoke'},
        {'in': 'awakening', 'out': 'awoke'},
        {'in': 'awakes', 'out': 'awoke'},
        {'in': 'awoken', 'out': 'awoke'},
        {'in': 'beat', 'out': 'beat'},
        {'in': 'beaten', 'out': 'beat'},
        {'in': 'beating', 'out': 'beat'},
        {'in': 'beats', 'out': 'beat'},
        {'in': 'become', 'out': 'became'},
        {'in': 'becomes', 'out': 'became'},
        {'in': 'becoming', 'out': 'became'},
        {'in': 'been', 'out': 'was'},
        {'in': 'beget', 'out': 'begot'},
        {'in': 'begets', 'out': 'begot'},
        {'in': 'begetting', 'out': 'begot'},
        {'in': 'begin', 'out': 'began'},
        {'in': 'beginning', 'out': 'began'},
        {'in': 'begins', 'out': 'began'},
        {'in': 'begotten', 'out': 'begot'},
        {'in': 'begun', 'out': 'began'},
        {'in': 'beheld', 'out': 'beheld'},
        {'in': 'behold', 'out': 'beheld'},
        {'in': 'beholding', 'out': 'beheld'},
        {'in': 'beholds', 'out': 'beheld'},
        {'in': 'being', 'out': 'was'},
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
        {'in': 'bind', 'out': 'bound'},
        {'in': 'binding', 'out': 'bound'},
        {'in': 'binds', 'out': 'bound'},
        {'in': 'bite', 'out': 'bit'},
        {'in': 'bites', 'out': 'bit'},
        {'in': 'biting', 'out': 'bit'},
        {'in': 'bitten', 'out': 'bit'},
        {'in': 'bled', 'out': 'bled'},
        {'in': 'bleed', 'out': 'bled'},
        {'in': 'bleeding', 'out': 'bled'},
        {'in': 'bleeds', 'out': 'bled'},
        {'in': 'blitz', 'out': 'blitzed'},
        {'in': 'blitzed', 'out': 'blitzed'},
        {'in': 'blitzes', 'out': 'blitzed'},
        {'in': 'blitzing', 'out': 'blitzed'},
        {'in': 'blow', 'out': 'blew'},
        {'in': 'blowing', 'out': 'blew'},
        {'in': 'blown', 'out': 'blew'},
        {'in': 'blows', 'out': 'blew'},
        {'in': 'bound', 'out': 'bound'},
        {'in': 'break', 'out': 'broke'},
        {'in': 'breaking', 'out': 'broke'},
        {'in': 'breaks', 'out': 'broke'},
        {'in': 'bred', 'out': 'bred'},
        {'in': 'breed', 'out': 'bred'},
        {'in': 'breeding', 'out': 'bred'},
        {'in': 'breeds', 'out': 'bred'},
        {'in': 'bring', 'out': 'brought'},
        {'in': 'bringing', 'out': 'brought'},
        {'in': 'brings', 'out': 'brought'},
        {'in': 'broken', 'out': 'broke'},
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
        {'in': 'bust', 'out': 'bust'},
        {'in': 'busting', 'out': 'bust'},
        {'in': 'busts', 'out': 'bust'},
        {'in': 'cache', 'out': 'cached'},
        {'in': 'cached', 'out': 'cached'},
        {'in': 'caches', 'out': 'cached'},
        {'in': 'caching', 'out': 'cached'},
        {'in': 'can', 'out': 'could'},
        {'in': 'catch', 'out': 'caught'},
        {'in': 'catches', 'out': 'caught'},
        {'in': 'catching', 'out': 'caught'},
        {'in': 'caught', 'out': 'caught'},
        {'in': 'change', 'out': 'changed'},
        {'in': 'changed', 'out': 'changed'},
        {'in': 'changes', 'out': 'changed'},
        {'in': 'changing', 'out': 'changed'},
        {'in': 'choose', 'out': 'chose'},
        {'in': 'chooses', 'out': 'chose'},
        {'in': 'choosing', 'out': 'chose'},
        {'in': 'chosen', 'out': 'chose'},
        {'in': 'clap', 'out': 'clapped'},
        {'in': 'clapped', 'out': 'clapped'},
        {'in': 'clapping', 'out': 'clapped'},
        {'in': 'claps', 'out': 'clapped'},
        {'in': 'cling', 'out': 'clung'},
        {'in': 'clinging', 'out': 'clung'},
        {'in': 'clings', 'out': 'clung'},
        {'in': 'clung', 'out': 'clung'},
        {'in': 'come', 'out': 'came'},
        {'in': 'comes', 'out': 'came'},
        {'in': 'coming', 'out': 'came'},
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
        {'in': 'die', 'out': 'died'},
        {'in': 'died', 'out': 'died'},
        {'in': 'dies', 'out': 'died'},
        {'in': 'dig', 'out': 'dug'},
        {'in': 'digging', 'out': 'dug'},
        {'in': 'digs', 'out': 'dug'},
        {'in': 'dive', 'out': 'dived'},
        {'in': 'dived', 'out': 'dived'},
        {'in': 'dives', 'out': 'dived'},
        {'in': 'diving', 'out': 'dived'},
        {'in': 'douche', 'out': 'douched'},
        {'in': 'douched', 'out': 'douched'},
        {'in': 'douches', 'out': 'douched'},
        {'in': 'douching', 'out': 'douched'},
        {'in': 'drag', 'out': 'dragged'},
        {'in': 'dragged', 'out': 'dragged'},
        {'in': 'dragging', 'out': 'dragged'},
        {'in': 'drags', 'out': 'dragged'},
        {'in': 'dream', 'out': 'dreamed'},
        {'in': 'dreamed', 'out': 'dreamed'},
        {'in': 'dreaming', 'out': 'dreamed'},
        {'in': 'dreams', 'out': 'dreamed'},
        {'in': 'drink', 'out': 'drank'},
        {'in': 'drinking', 'out': 'drank'},
        {'in': 'drinks', 'out': 'drank'},
        {'in': 'drive', 'out': 'drove'},
        {'in': 'driven', 'out': 'drove'},
        {'in': 'drives', 'out': 'drove'},
        {'in': 'driving', 'out': 'drove'},
        {'in': 'drunk', 'out': 'drank'},
        {'in': 'dug', 'out': 'dug'},
        {'in': 'dwell', 'out': 'dwelt'},
        {'in': 'dwelling', 'out': 'dwelt'},
        {'in': 'dwells', 'out': 'dwelt'},
        {'in': 'dwelt', 'out': 'dwelt'},
        {'in': 'dying', 'out': 'died'},
        {'in': 'eat', 'out': 'ate'},
        {'in': 'eaten', 'out': 'ate'},
        {'in': 'eating', 'out': 'ate'},
        {'in': 'eats', 'out': 'ate'},
        {'in': 'expect', 'out': 'expected'},
        {'in': 'expected', 'out': 'expected'},
        {'in': 'expecting', 'out': 'expected'},
        {'in': 'expects', 'out': 'expected'},
        {'in': 'fall', 'out': 'fell'},
        {'in': 'fallen', 'out': 'fell'},
        {'in': 'falling', 'out': 'fell'},
        {'in': 'falls', 'out': 'fell'},
        {'in': 'feel', 'out': 'felt'},
        {'in': 'feeling', 'out': 'felt'},
        {'in': 'feels', 'out': 'felt'},
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
        {'in': 'flies', 'out': 'flew'},
        {'in': 'fling', 'out': 'flung'},
        {'in': 'flinging', 'out': 'flung'},
        {'in': 'flings', 'out': 'flung'},
        {'in': 'flown', 'out': 'flew'},
        {'in': 'flung', 'out': 'flung'},
        {'in': 'fly', 'out': 'flew'},
        {'in': 'flying', 'out': 'flew'},
        {'in': 'follow', 'out': 'followed'},
        {'in': 'followed', 'out': 'followed'},
        {'in': 'following', 'out': 'followed'},
        {'in': 'follows', 'out': 'followed'},
        {'in': 'forbid', 'out': 'forbade'},
        {'in': 'forbidden', 'out': 'forbade'},
        {'in': 'forbidding', 'out': 'forbade'},
        {'in': 'forbids', 'out': 'forbade'},
        {'in': 'foresee', 'out': 'foresaw'},
        {'in': 'foreseeing', 'out': 'foresaw'},
        {'in': 'foreseen', 'out': 'foresaw'},
        {'in': 'foresees', 'out': 'foresaw'},
        {'in': 'foretell', 'out': 'foretold'},
        {'in': 'foretelling', 'out': 'foretold'},
        {'in': 'foretells', 'out': 'foretold'},
        {'in': 'foretold', 'out': 'foretold'},
        {'in': 'forget', 'out': 'forgot'},
        {'in': 'forgets', 'out': 'forgot'},
        {'in': 'forgetting', 'out': 'forgot'},
        {'in': 'forgive', 'out': 'forgave'},
        {'in': 'forgiven', 'out': 'forgave'},
        {'in': 'forgives', 'out': 'forgave'},
        {'in': 'forgiving', 'out': 'forgave'},
        {'in': 'forgotten', 'out': 'forgot'},
        {'in': 'forsake', 'out': 'forsook'},
        {'in': 'forsaken', 'out': 'forsook'},
        {'in': 'forsakes', 'out': 'forsook'},
        {'in': 'forsaking', 'out': 'forsook'},
        {'in': 'fought', 'out': 'fought'},
        {'in': 'found', 'out': 'found'},
        {'in': 'get', 'out': 'got'},
        {'in': 'gets', 'out': 'got'},
        {'in': 'getting', 'out': 'got'},
        {'in': 'gild', 'out': 'gilded'},
        {'in': 'gilded', 'out': 'gilded'},
        {'in': 'gilding', 'out': 'gilded'},
        {'in': 'gilds', 'out': 'gilded'},
        {'in': 'give', 'out': 'gave'},
        {'in': 'given', 'out': 'gave'},
        {'in': 'gives', 'out': 'gave'},
        {'in': 'giving', 'out': 'gave'},
        {'in': 'go', 'out': 'went'},
        {'in': 'goes', 'out': 'went'},
        {'in': 'going', 'out': 'went'},
        {'in': 'gone', 'out': 'went'},
        {'in': 'gotten', 'out': 'got'},
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
        {'in': 'hew', 'out': 'hewed'},
        {'in': 'hewing', 'out': 'hewed'},
        {'in': 'hewn', 'out': 'hewed'},
        {'in': 'hews', 'out': 'hewed'},
        {'in': 'hit', 'out': 'hit'},
        {'in': 'hits', 'out': 'hit'},
        {'in': 'hitting', 'out': 'hit'},
        {'in': 'hold', 'out': 'held'},
        {'in': 'holding', 'out': 'held'},
        {'in': 'holds', 'out': 'held'},
        {'in': 'hurt', 'out': 'hurt'},
        {'in': 'hurting', 'out': 'hurt'},
        {'in': 'hurts', 'out': 'hurt'},
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
        {'in': 'is', 'out': 'was'},
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
        {'in': 'knit', 'out': 'knitted'},
        {'in': 'knits', 'out': 'knitted'},
        {'in': 'knitted', 'out': 'knitted'},
        {'in': 'knitting', 'out': 'knitted'},
        {'in': 'know', 'out': 'knew'},
        {'in': 'knowing', 'out': 'knew'},
        {'in': 'known', 'out': 'knew'},
        {'in': 'knows', 'out': 'knew'},
        {'in': 'laid', 'out': 'laid'},
        {'in': 'lain', 'out': 'lay'},
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
        {'in': 'lie', 'out': 'lay'},
        {'in': 'lies', 'out': 'lay'},
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
        {'in': 'lying', 'out': 'lay'},
        {'in': 'may', 'out': 'might'},
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
        {'in': 'mistake', 'out': 'mistook'},
        {'in': 'mistaken', 'out': 'mistook'},
        {'in': 'mistakes', 'out': 'mistook'},
        {'in': 'mistaking', 'out': 'mistook'},
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
        {'in': 'overdraw', 'out': 'overdrew'},
        {'in': 'overdrawing', 'out': 'overdrew'},
        {'in': 'overdrawn', 'out': 'overdrew'},
        {'in': 'overdraws', 'out': 'overdrew'},
        {'in': 'overhear', 'out': 'overheard'},
        {'in': 'overheard', 'out': 'overheard'},
        {'in': 'overhearing', 'out': 'overheard'},
        {'in': 'overhears', 'out': 'overheard'},
        {'in': 'overtake', 'out': 'overtook'},
        {'in': 'overtaken', 'out': 'overtook'},
        {'in': 'overtakes', 'out': 'overtook'},
        {'in': 'overtaking', 'out': 'overtook'},
        {'in': 'preset', 'out': 'preset'},
        {'in': 'presets', 'out': 'preset'},
        {'in': 'presetting', 'out': 'preset'},
        {'in': 'prove', 'out': 'proved'},
        {'in': 'proved', 'out': 'proved'},
        {'in': 'proven', 'out': 'proved'},
        {'in': 'proves', 'out': 'proved'},
        {'in': 'provide', 'out': 'provided'},
        {'in': 'provided', 'out': 'provided'},
        {'in': 'provides', 'out': 'provided'},
        {'in': 'providing', 'out': 'provided'},
        {'in': 'proving', 'out': 'proved'},
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
        {'in': 'rid', 'out': 'rid'},
        {'in': 'ridden', 'out': 'rode'},
        {'in': 'ridding', 'out': 'rid'},
        {'in': 'ride', 'out': 'rode'},
        {'in': 'rides', 'out': 'rode'},
        {'in': 'riding', 'out': 'rode'},
        {'in': 'rids', 'out': 'rid'},
        {'in': 'ring', 'out': 'rang'},
        {'in': 'ringing', 'out': 'rang'},
        {'in': 'rings', 'out': 'rang'},
        {'in': 'rise', 'out': 'rose'},
        {'in': 'risen', 'out': 'rose'},
        {'in': 'rises', 'out': 'rose'},
        {'in': 'rising', 'out': 'rose'},
        {'in': 'rive', 'out': 'rived'},
        {'in': 'riven', 'out': 'rived'},
        {'in': 'rives', 'out': 'rived'},
        {'in': 'riving', 'out': 'rived'},
        {'in': 'run', 'out': 'ran'},
        {'in': 'rung', 'out': 'rang'},
        {'in': 'running', 'out': 'ran'},
        {'in': 'runs', 'out': 'ran'},
        {'in': 'sat', 'out': 'sat'},
        {'in': 'saw', 'out': 'sawed'},
        {'in': 'sawing', 'out': 'sawed'},
        {'in': 'sawn', 'out': 'sawed'},
        {'in': 'saws', 'out': 'sawed'},
        {'in': 'seek', 'out': 'sought'},
        {'in': 'seeking', 'out': 'sought'},
        {'in': 'seeks', 'out': 'sought'},
        {'in': 'seem', 'out': 'seemed'},
        {'in': 'seemed', 'out': 'seemed'},
        {'in': 'seeming', 'out': 'seemed'},
        {'in': 'seems', 'out': 'seemed'},
        {'in': 'shake', 'out': 'shook'},
        {'in': 'shaken', 'out': 'shook'},
        {'in': 'shakes', 'out': 'shook'},
        {'in': 'shaking', 'out': 'shook'},
        {'in': 'shall', 'out': 'should'},
        {'in': 'shave', 'out': 'shaved'},
        {'in': 'shaved', 'out': 'shaved'},
        {'in': 'shaves', 'out': 'shaved'},
        {'in': 'shaving', 'out': 'shaved'},
        {'in': 'shed', 'out': 'shed'},
        {'in': 'shedding', 'out': 'shed'},
        {'in': 'sheds', 'out': 'shed'},
        {'in': 'shit', 'out': 'shat'},
        {'in': 'shits', 'out': 'shat'},
        {'in': 'shitted', 'out': 'shat'},
        {'in': 'shitting', 'out': 'shat'},
        {'in': 'shod', 'out': 'shod'},
        {'in': 'shoe', 'out': 'shod'},
        {'in': 'shoeing', 'out': 'shod'},
        {'in': 'shoes', 'out': 'shod'},
        {'in': 'show', 'out': 'showed'},
        {'in': 'showing', 'out': 'showed'},
        {'in': 'shown', 'out': 'showed'},
        {'in': 'shows', 'out': 'showed'},
        {'in': 'shrink', 'out': 'shrank'},
        {'in': 'shrinking', 'out': 'shrank'},
        {'in': 'shrinks', 'out': 'shrank'},
        {'in': 'shrunk', 'out': 'shrank'},
        {'in': 'sing', 'out': 'sang'},
        {'in': 'singing', 'out': 'sang'},
        {'in': 'sings', 'out': 'sang'},
        {'in': 'sink', 'out': 'sank'},
        {'in': 'sinking', 'out': 'sank'},
        {'in': 'sinks', 'out': 'sank'},
        {'in': 'sit', 'out': 'sat'},
        {'in': 'sits', 'out': 'sat'},
        {'in': 'sitting', 'out': 'sat'},
        {'in': 'ski', 'out': 'skied'},
        {'in': 'skied', 'out': 'skied'},
        {'in': 'skiing', 'out': 'skied'},
        {'in': 'skis', 'out': 'skied'},
        {'in': 'slain', 'out': 'slew'},
        {'in': 'slay', 'out': 'slew'},
        {'in': 'slaying', 'out': 'slew'},
        {'in': 'slays', 'out': 'slew'},
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
        {'in': 'smite', 'out': 'smote'},
        {'in': 'smites', 'out': 'smote'},
        {'in': 'smiting', 'out': 'smote'},
        {'in': 'smitten', 'out': 'smote'},
        {'in': 'sneak', 'out': 'sneaked'},
        {'in': 'sneaked', 'out': 'sneaked'},
        {'in': 'sneaking', 'out': 'sneaked'},
        {'in': 'sneaks', 'out': 'sneaked'},
        {'in': 'sought', 'out': 'sought'},
        {'in': 'sow', 'out': 'sowed'},
        {'in': 'sowing', 'out': 'sowed'},
        {'in': 'sown', 'out': 'sowed'},
        {'in': 'sows', 'out': 'sowed'},
        {'in': 'spat', 'out': 'spat'},
        {'in': 'speak', 'out': 'spoke'},
        {'in': 'speaking', 'out': 'spoke'},
        {'in': 'speaks', 'out': 'spoke'},
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
        {'in': 'spoil', 'out': 'spoilt'},
        {'in': 'spoiled', 'out': 'spoilt'},
        {'in': 'spoiling', 'out': 'spoilt'},
        {'in': 'spoils', 'out': 'spoilt'},
        {'in': 'spoken', 'out': 'spoke'},
        {'in': 'spring', 'out': 'sprang'},
        {'in': 'springing', 'out': 'sprang'},
        {'in': 'springs', 'out': 'sprang'},
        {'in': 'sprung', 'out': 'sprang'},
        {'in': 'stand', 'out': 'stood'},
        {'in': 'standing', 'out': 'stood'},
        {'in': 'stands', 'out': 'stood'},
        {'in': 'stave', 'out': 'staved'},
        {'in': 'staved', 'out': 'staved'},
        {'in': 'staves', 'out': 'staved'},
        {'in': 'staving', 'out': 'staved'},
        {'in': 'stay', 'out': 'stayed'},
        {'in': 'stayed', 'out': 'stayed'},
        {'in': 'staying', 'out': 'stayed'},
        {'in': 'stays', 'out': 'stayed'},
        {'in': 'steal', 'out': 'stole'},
        {'in': 'stealing', 'out': 'stole'},
        {'in': 'steals', 'out': 'stole'},
        {'in': 'sting', 'out': 'stung'},
        {'in': 'stinging', 'out': 'stung'},
        {'in': 'stings', 'out': 'stung'},
        {'in': 'stink', 'out': 'stank'},
        {'in': 'stinking', 'out': 'stank'},
        {'in': 'stinks', 'out': 'stank'},
        {'in': 'stolen', 'out': 'stole'},
        {'in': 'stood', 'out': 'stood'},
        {'in': 'stop', 'out': 'stopped'},
        {'in': 'stopped', 'out': 'stopped'},
        {'in': 'stopping', 'out': 'stopped'},
        {'in': 'stops', 'out': 'stopped'},
        {'in': 'strew', 'out': 'strewed'},
        {'in': 'strewing', 'out': 'strewed'},
        {'in': 'strewn', 'out': 'strewed'},
        {'in': 'strews', 'out': 'strewed'},
        {'in': 'stride', 'out': 'strode'},
        {'in': 'strides', 'out': 'strode'},
        {'in': 'striding', 'out': 'strode'},
        {'in': 'strip', 'out': 'stripped'},
        {'in': 'stripped', 'out': 'stripped'},
        {'in': 'stripping', 'out': 'stripped'},
        {'in': 'strips', 'out': 'stripped'},
        {'in': 'strive', 'out': 'strove'},
        {'in': 'strived', 'out': 'strove'},
        {'in': 'strives', 'out': 'strove'},
        {'in': 'striving', 'out': 'strove'},
        {'in': 'strode', 'out': 'strode'},
        {'in': 'stung', 'out': 'stung'},
        {'in': 'stunk', 'out': 'stank'},
        {'in': 'sublet', 'out': 'sublet'},
        {'in': 'sublets', 'out': 'sublet'},
        {'in': 'subletting', 'out': 'sublet'},
        {'in': 'sunburn', 'out': 'sunburned'},
        {'in': 'sunburned', 'out': 'sunburned'},
        {'in': 'sunburning', 'out': 'sunburned'},
        {'in': 'sunburns', 'out': 'sunburned'},
        {'in': 'sung', 'out': 'sang'},
        {'in': 'sunk', 'out': 'sank'},
        {'in': 'swear', 'out': 'swore'},
        {'in': 'swearing', 'out': 'swore'},
        {'in': 'swears', 'out': 'swore'},
        {'in': 'sweat', 'out': 'sweat'},
        {'in': 'sweated', 'out': 'sweat'},
        {'in': 'sweating', 'out': 'sweat'},
        {'in': 'sweats', 'out': 'sweat'},
        {'in': 'sweep', 'out': 'swept'},
        {'in': 'sweeping', 'out': 'swept'},
        {'in': 'sweeps', 'out': 'swept'},
        {'in': 'swell', 'out': 'swelled'},
        {'in': 'swelling', 'out': 'swelled'},
        {'in': 'swells', 'out': 'swelled'},
        {'in': 'swept', 'out': 'swept'},
        {'in': 'swim', 'out': 'swam'},
        {'in': 'swimming', 'out': 'swam'},
        {'in': 'swims', 'out': 'swam'},
        {'in': 'swing', 'out': 'swung'},
        {'in': 'swinging', 'out': 'swung'},
        {'in': 'swings', 'out': 'swung'},
        {'in': 'swollen', 'out': 'swelled'},
        {'in': 'sworn', 'out': 'swore'},
        {'in': 'swum', 'out': 'swam'},
        {'in': 'swung', 'out': 'swung'},
        {'in': 'talk', 'out': 'talked'},
        {'in': 'talked', 'out': 'talked'},
        {'in': 'talking', 'out': 'talked'},
        {'in': 'talks', 'out': 'talked'},
        {'in': 'tear', 'out': 'tore'},
        {'in': 'tearing', 'out': 'tore'},
        {'in': 'tears', 'out': 'tore'},
        {'in': 'thrive', 'out': 'thrived'},
        {'in': 'thrived', 'out': 'thrived'},
        {'in': 'thrives', 'out': 'thrived'},
        {'in': 'thriving', 'out': 'thrived'},
        {'in': 'thrust', 'out': 'thrust'},
        {'in': 'thrusting', 'out': 'thrust'},
        {'in': 'thrusts', 'out': 'thrust'},
        {'in': 'torn', 'out': 'tore'},
        {'in': 'tread', 'out': 'trod'},
        {'in': 'treading', 'out': 'trod'},
        {'in': 'treads', 'out': 'trod'},
        {'in': 'trodden', 'out': 'trod'},
        {'in': 'undergo', 'out': 'underwent'},
        {'in': 'undergoes', 'out': 'underwent'},
        {'in': 'undergoing', 'out': 'underwent'},
        {'in': 'undergone', 'out': 'underwent'},
        {'in': 'understand', 'out': 'understood'},
        {'in': 'understanding', 'out': 'understood'},
        {'in': 'understands', 'out': 'understood'},
        {'in': 'understood', 'out': 'understood'},
        {'in': 'undertake', 'out': 'undertook'},
        {'in': 'undertaken', 'out': 'undertook'},
        {'in': 'undertakes', 'out': 'undertook'},
        {'in': 'undertaking', 'out': 'undertook'},
        {'in': 'upset', 'out': 'upset'},
        {'in': 'upsets', 'out': 'upset'},
        {'in': 'upsetting', 'out': 'upset'},
        {'in': 'vex', 'out': 'vexed'},
        {'in': 'vexed', 'out': 'vexed'},
        {'in': 'vexes', 'out': 'vexed'},
        {'in': 'vexing', 'out': 'vexed'},
        {'in': 'wait', 'out': 'waited'},
        {'in': 'waited', 'out': 'waited'},
        {'in': 'waiting', 'out': 'waited'},
        {'in': 'waits', 'out': 'waited'},
        {'in': 'wake', 'out': 'woke'},
        {'in': 'wakes', 'out': 'woke'},
        {'in': 'waking', 'out': 'woke'},
        {'in': 'walk', 'out': 'walked'},
        {'in': 'walked', 'out': 'walked'},
        {'in': 'walking', 'out': 'walked'},
        {'in': 'walks', 'out': 'walked'},
        {'in': 'want', 'out': 'wanted'},
        {'in': 'wanted', 'out': 'wanted'},
        {'in': 'wanting', 'out': 'wanted'},
        {'in': 'wants', 'out': 'wanted'},
        {'in': 'was', 'out': 'was'},
        {'in': 'watch', 'out': 'watched'},
        {'in': 'watched', 'out': 'watched'},
        {'in': 'watches', 'out': 'watched'},
        {'in': 'watching', 'out': 'watched'},
        {'in': 'wear', 'out': 'wore'},
        {'in': 'wearing', 'out': 'wore'},
        {'in': 'wears', 'out': 'wore'},
        {'in': 'weep', 'out': 'wept'},
        {'in': 'weeping', 'out': 'wept'},
        {'in': 'weeps', 'out': 'wept'},
        {'in': 'wend', 'out': 'wended'},
        {'in': 'wended', 'out': 'wended'},
        {'in': 'wending', 'out': 'wended'},
        {'in': 'wends', 'out': 'wended'},
        {'in': 'wept', 'out': 'wept'},
        {'in': 'were', 'out': 'were'},
        {'in': 'will', 'out': 'would'},
        {'in': 'win', 'out': 'won'},
        {'in': 'winning', 'out': 'won'},
        {'in': 'wins', 'out': 'won'},
        {'in': 'withdraw', 'out': 'withdrew'},
        {'in': 'withdrawing', 'out': 'withdrew'},
        {'in': 'withdrawn', 'out': 'withdrew'},
        {'in': 'withdraws', 'out': 'withdrew'},
        {'in': 'withheld', 'out': 'withheld'},
        {'in': 'withhold', 'out': 'withheld'},
        {'in': 'withholding', 'out': 'withheld'},
        {'in': 'withholds', 'out': 'withheld'},
        {'in': 'withstand', 'out': 'withstood'},
        {'in': 'withstanding', 'out': 'withstood'},
        {'in': 'withstands', 'out': 'withstood'},
        {'in': 'withstood', 'out': 'withstood'},
        {'in': 'woken', 'out': 'woke'},
        {'in': 'won', 'out': 'won'},
        {'in': 'worn', 'out': 'wore'},
        {'in': 'wring', 'out': 'wrung'},
        {'in': 'wringing', 'out': 'wrung'},
        {'in': 'wrings', 'out': 'wrung'},
        {'in': 'wrung', 'out': 'wrung'},
    ]

    def test_convert_to_past(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {**test_case, **{
                    "desc": f"convert_to_past({repr(test_case['in'])}) => {repr(test_case['out'])}",
                    "kwargs": dict()
                }}
                self.assertEqual(convert_to_past(test_case["in"], **test_case["kwargs"]), test_case["out"], test_case["desc"])

if __name__ == "__main__":
    unittest.main()
