# -*- coding: utf-8 -*-

import unittest
from tamilinayavaani.from_Csharp import gpathil11, checkviku, getsample
from tamilinayavaani import checkword, check_sandhi, SpellChecker, SpellCheckerResult
import os

# spelling correction
# testlist = ['நேயர்கலே', ' ', 'நிகழ்சியைப்', ' ', 'பார்த்தீர்கலா']
# testlist = ['கன்னால்', ' ', 'பார்த்தென்']
# testlist = ['வேண்டுகிறேண்']
# testlist = ['கற்ப்பிக்கிறேன்']
# testlist = ['முன்ணணி']
# testlist = ['சறியாக', ' ', 'கன்டுபிடிக்கும்']

# sandhi
# testlist = ['இந்த', ' ', 'பெட்டியில்']
# testlist = ['கூலி', ' ', 'படை']
# testlist = ['இலக்கண', ' ', 'பிழைகளை']

# sandhi and spelling correction together

# testlist = ['சரிவர', ' ', 'சோதிக்கிரதா']


class TestSpellCheckWords(unittest.TestCase):
    def test_வலைவழிஅணுகுதல்(self):
        #REST_interface test
        words = ['நேயர்கலே', 'நிகழ்சியைப்', 'பார்த்தீர்கலா']
        திருத்திய = [['நேயர்களே'],[],['பார்த்தீர்களா']]
        for idx,word in enumerate(words):
            பட்டியல் = SpellChecker.REST_interface(word)
            self.assertFalse( பட்டியல்[0] )
            self.assertEqual( திருத்திய[idx],  பட்டியல்[1] )
        self.assertEqual(idx,2)
        word_p_ws = '  '+words[0]+'\n'
        self.assertEqual(words[0],SpellChecker.scrub_ws(word_p_ws))

    def test_கோப்பிலிருந்து(self):
        expected=[SpellCheckerResult(Flag=False, Solspan=None, Userword='நேயர்கலே', Suggestions=['நேயர்களே']),
        SpellCheckerResult(Flag=False, Solspan=None, Userword='நிகழ்சியைப்',
        Suggestions=[]), SpellCheckerResult(Flag=False, Solspan=None, Userword='பார்த்தீர்கலா', Suggestions=['பார்த்தீர்களா'])]
        fname = 'demo.txt'
        words = ['நேயர்கலே', 'நிகழ்சியைப்', 'பார்த்தீர்கலா']
        with open(fname,'w') as fp:
            [fp.write(word+'\n') for word in words]
        result = SpellChecker(fname).run()
        os.unlink(fname)
        print(result)
        self.assertEqual(len(result),3)

    def test_sandhi_web_interface(self):
        flag,suggs=SpellChecker.REST_interface('வாழை','பழம்')
        expected=['வாழைப்', 'பழம்']
        self.assertFalse(flag)
        self.assertEqual(expected[0],suggs[0])

    def test_அ(self):
        testlist = ['கூலி', ' ', 'படை']
        expected = [[1, 'கூலிப்'], [0, 'correct'], [0, 'correct']]
        self.assertListEqual(expected, gpathil11(testlist, True, 'exe'))

    def test_ஆ(self):
        testlist = ['பிடிக்க', ' ', 'தடுமாரலாம்']
        expected = [[1, 'பிடிக்கத்'], [0, 'correct'], [1, 'தடுமாறலாம்']]
        self.assertListEqual(expected, gpathil11(testlist, True, 'exe'))

    def test_இ(self):
        testlist = ['பிடிக்க', ' ', 'தடுமாரலாம்']
        expected = [[1, 'பிடிக்கத்'], [0, 'correct'], [1, 'தடுமாறலாம்']]
        self.assertListEqual(expected, gpathil11(testlist, True, 'exe'))

    def test_ஈ(self):
        testlist = ['இறை', 'வனக்கம்']
        expected = [[0, 'correct'], [0, 'wrong']]
        self.assertListEqual( expected, gpathil11(testlist, True, 'exe') )

    def test_சொல்(self):
        self.assertTrue(checkword('வேண்டுகிறேன்', 7))
        expected=[['கிற்ப்பிக்கிறேன்', 'கிற்ப்பிக்கிறேன்'], ['முந்நநி', 'முந்ணணி', 'முண்நணி', 'முண்ணநி']]
        self.assertListEqual(expected[0],getsample("0", 'கற்ப்பிக்கிறேன்', 'கற', 'கிற'))
        self.assertListEqual(expected[1],getsample("0", 'முண்ணணி', 'ண', 'ந'))
        self.assertTrue(checkword('சரியாகக்கண்டுபிடிக்கும்', 0))
        self.assertTrue(checkviku('சரியா', 'க', "", 'ஆ', '15', 0))

    def test_முகப்பு(self):
        self.assertFalse(checkword('நேயர்கலே',0))

if __name__ == u'__main__':
    unittest.main()
