## -*- coding: utf-8 -*-
## (C) 2016 Muthiah Annamalai,
from __future__ import print_function
from webspell import app
import json
import sys
from pprint import pprint
import re

from flask import request, render_template, redirect, url_for
from tamilinayavaani import SpellChecker, SpellCheckerResult

@app.route('/')
@app.route('/index')
def index():
    return redirect('/static/tinymce/index.html')

#/spell?word=%E0%AE%B5%E0%AE%B0%E0%AF%81%E0%AE%95&lang=ta
@app.route('/spell',methods=['GET','POST'])
def spell():
    if request.method == "GET":
        return render_template("spell.html",solution=False)

    if request.method != "POST":
        return "<B>404! பிழை அறிக்கை</B>"

    if u'word' in request.form:
        word = request.form['word']
        if not word:
            return "சொல் உள்ளீடு செய்க!"
        lang="TA"
        if "lang" in request.form:
            lang = request.form["lang"]

        try:
            ok, suggs = SpellChecker.REST_interface(word)
            #pprint(suggs)
        except Exception as ioe:
            ok = True

        if ok:
            HTML = "<B style='color:green;'>சரியான் சொல் '{0}'!</B>".format(word)
        else:
            HTML = "<B style='color:red;'>பிழையான சொல் '{0}'</B><br />".format(word)
            if len(suggs) > 0:
                data_suggs = u"<br/>\n".join([u"<option>%d %s</option>"%(itr+1,s_word) for itr,s_word in enumerate(suggs)])
                HTML += "<p>மாற்றங்கள்: <div><select>"+data_suggs+"\n</select></div></p>"

        return render_template("spell.html",solution=True,HTML=HTML,word=word)
    return redirect(url_for('spell'))

@app.route('/spellchecker',methods=['GET','POST'])
def spellchecker():
    if request.method == 'POST':
        #print(request.form.keys(),file=sys.stderr)
        #print(request.form['lang'],file=sys.stderr)
        lang = request.form['lang']
        text = request.form['text']
        if lang != "ta_IN":
            return json.dumps({'error':'Language '+lang+' is not supported; only takes Tamil (code ta_IN))'})
        lang = "TA"
        result_dict = {'words':{}}

        wordlist = list(filter(len,re.split('\s+',text)))
        Lmax = len(wordlist)-1
        for itr,word in enumerate( wordlist ):
            if word.find("<") >= 0: #HTML Tags, skip
                continue
            #print("checking word %d"%itr,file=sys.stderr)
            try:
                next_word = wordlist[itr+1] if itr != Lmax else None
                ok,suggs = SpellChecker.REST_interface(word,next_word)
            except Exception as ioe:
                ok = True

            if not ok:
                word = SpellChecker.scrub_ws(word)
                result_dict['words'][word] = list(suggs)
        return json.dumps(result_dict)
    return "RPC interface for TinyMCE Spell Checker!"
