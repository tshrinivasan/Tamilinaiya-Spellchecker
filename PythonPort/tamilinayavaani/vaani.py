#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .from_Csharp import gpathil11
from tamil.utf8 import get_words
import codecs
from collections import namedtuple

SpellCheckerResult = namedtuple('SpellCheckerResult',['Flag', 'Solspan', 'Userword', 'Suggestions'])

class SpellChecker:
    def __init__(self,filename):
        with codecs.open(filename,'r','utf-8') as fp:
            self.words = get_words(fp.read())
        self.results = [] #object of type Result

    def run(self):
        for idx,result in enumerate(gpathil11(self.words)):
            user_word = self.words[idx]
            suggestions = []
            is_correct = False
            if result[0] == 0:
                if result[1] == 'correct':
                    is_correct = True
                elif result[1] == 'wrong':
                    suggestions = []
            else:
                suggestions = [result[1]]

            self.results.append(SpellCheckerResult(is_correct,None,user_word,suggestions) )
        return self.results
