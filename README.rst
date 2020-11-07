Tamilinaiyam - Pizhaithiruthi (Spellchecker)
============================================

Python Package
==============
Python Port of TamilInaiya spell checker is named 'tamilinayavaani'
and available as Python module form same name. It can be used with a UTF-8 encoded text file as follows,

Installation
------------
.. code-block:: bash

    $ python3 -m pip install --upgrade tamilinayavaani>=0.1

Usage - in-memory
-----------------
.. code-block:: python

    from tamilinaiyavaani import SpellChecker

    flag,suggs=SpellChecker.REST_interface('வாழை','பழம்')

    expected=['வாழைப்', 'பழம்']

    assert not flag

    assert expected[0]==suggs[0]

Usage - file-based
------------------
An file-based use of the library would look like,

.. code-block:: python

    from tamilinaiyavaani import SpellChecker, SpellCheckerResult

    result = SpellChecker(fname).run() #fname is a full filename

    # result is a list of SpellCheckerResult objects.

Source 
======
Tamil Virtual Academy release sources at `link. <http://www.tamilvu.org/ta/content/%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D%E0%AE%95%E0%AF%8D-%E0%AE%95%E0%AE%A3%E0%AE%BF%E0%AE%A9%E0%AE%BF%E0%AE%95%E0%AF%8D-%E0%AE%95%E0%AE%B0%E0%AF%81%E0%AE%B5%E0%AE%BF%E0%AE%95%E0%AE%B3%E0%AF%8D>`__

License
=======
This code is licensed under terms of GNU GPL V2. Check `link <https://commons.wikimedia.org/wiki/File:Tamil-Virtual-Academy-Copyright-Declaration.jpg>`__ for license info.

Credits
=======
- Thanks to Tamil Virtual Academy, Chennai for releasing ths source code of this application. This work is open-source
  publication of Vaani from `link <http://vaani.neechalkaran.com>`__
  You can support the close-source Vaani project, an 8 yr effort
  as of 2020, by donating here  `donate(link) <http://neechalkaran.com/p/donate.html>`__

- Python Port was enabled by Kaniyam Foundation, T. Shrinivasan, @manikk, Ashok Ramachandran, and others.
  You can support Kaniyam Foundation and its mission by donating via instructions
  here, `Kaniyam <http://www.kaniyam.com>`__
  The Python port depends on tamilsandhichecker project `link <https://github.com/nithyadurai87/tamil-sandhi-checker>`__ and the Open-Tamil
  project `link: <https://pypi.org/project/Open-Tamil/>`__

