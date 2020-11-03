#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .from_Csharp import gpathil11
from tamil.utf8 import get_words
import re
import codecs
from collections import namedtuple

SpellCheckerResult = namedtuple('SpellCheckerResult',['Flag', 'Solspan', 'Userword', 'Suggestions'])
_ws = re.compile('\\s+')
class SpellChecker:
    def __init__(self,filename):
        with codecs.open(filename,'r','utf-8') as fp:
            self.words = get_words(fp.read())
        self.results = [] #object of type Result

    @staticmethod
    def REST_interface(user_word,next_word=None):
        words = [user_word]
        if next_word:
            words.extend([' ',next_word])
        result = gpathil11(words)
        is_correct,suggestions=SpellChecker.post_proc_result(result[0])
        return is_correct,suggestions

    @staticmethod
    def scrub_ws(word):
        return re.sub(_ws,'',word)

    @staticmethod
    def post_proc_result(result):
        suggestions = []
        is_correct = False
        if result[0] == 0:
            if result[1] == 'correct':
                is_correct = True
            elif result[1] == 'wrong':
                suggestions = []
        else:
            suggestions = [result[1]]
        return is_correct,suggestions

    def run(self):
        for idx,result in enumerate(gpathil11(self.words)):
            user_word = self.words[idx]
            is_correct,suggestions=SpellChecker.post_proc_result(result)

            self.results.append(SpellCheckerResult(is_correct,None,user_word,suggestions) )
        return self.results
