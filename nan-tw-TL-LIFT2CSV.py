#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import xml.parsers.expat

# This script converts nan.lift to the CSV format

whitespace_re = re.compile("\s+")

decompose_lookup = { "á":"a2", "à":"a3", "â":"a5", "ǎ":"a6", "ā":"a7", "a̍":"a8", "a̋":"a9", "ă":"a9", "é":"e2", "è":"e3", "ê":"e5", "ě":"e6", "ē":"e7", "e̍":"e8", "e̋":"e9", "ĕ":"e9", "í":"i2", "ì":"i3", "î":"i5", "ǐ":"i6", "ī":"i7", "i̍":"i8", "i̋":"i9", "ĭ":"i9", "ḿ":"m2", "m̀":"m3", "m̂":"m5", "m̌":"m6", "m̄":"m7", "m̍":"m8", "m̋":"m9", "m̆":"m9", "ń":"n2", "ǹ":"n3", "n̂":"n5", "ň":"n6", "n̄":"n7", "n̍":"n8", "n̋":"n9", "n̆":"n9", "ó":"o2", "ò":"o3", "ô":"o5", "ǒ":"o6", "ō":"o7", "o̍":"o8", "ő":"o9", "ŏ":"o9", "o͘":"oo", "ó͘":"oo2", "ò͘":"oo3", "ô͘":"oo5", "ǒ͘":"oo6", "ō͘":"oo7", "o̍͘":"oo8", "ő͘":"oo9", "ŏ͘":"oo9", "ú":"u2", "ù":"u3", "û":"u5", "ǔ":"u6", "ū":"u7", "u̍":"u8", "ű":"u9", "ŭ":"u9", "Á":"A2", "À":"A3", "Â":"A5", "Ǎ":"A6", "Ā":"A7", "A̍":"A8", "A̋":"A9", "Ă":"A9", "É":"E2", "È":"E3", "Ê":"E5", "Ě":"E6", "Ē":"E7", "E̍":"E8", "E̋":"E9", "Ĕ":"E9", "Í":"I2", "Ì":"I3", "Î":"I5", "Ǐ":"I6", "Ī":"I7", "I̍":"I8", "I̋":"I9", "Ĭ":"I9", "Ḿ":"M2", "M̀":"M3", "M̂":"M5", "M̌":"M6", "M̄":"M7", "M̍":"M8", "M̋":"M9", "M̆":"M9", "Ń":"N2", "Ǹ":"N3", "N̂":"N5", "Ň":"N6", "N̄":"N7", "N̍":"N8", "N̋":"N9", "N̆":"N9", "Ó":"O2", "Ò":"O3", "Ô":"O5", "Ǒ":"O6", "Ō":"O7", "O̍":"O8", "Ő":"O9", "Ŏ":"O9", "O͘":"Oo", "Ó͘":"Oo2", "Ò͘":"Oo3", "Ô͘":"Oo5", "Ǒ͘":"Oo6", "Ō͘":"Oo7", "O̍͘":"Oo8", "Ő͘":"Oo9", "Ŏ͘":"Oo9", "Ú":"U2", "Ù":"U3", "Û":"U5", "Ǔ":"U6", "Ū":"U7", "U̍":"U8", "Ű":"U9", "Ŭ":"U9" }
exp = "Ŭ|Ű|U̍|Ū|Ǔ|Û|Ù|Ú|Ŏ͘|Ő͘|O̍͘|Ō͘|Ǒ͘|Ô͘|Ò͘|Ó͘|O͘|Ŏ|Ő|O̍|Ō|Ǒ|Ô|Ò|Ó|N̆|N̋|N̍|N̄|Ň|N̂|Ǹ|Ń|M̆|M̋|M̍|M̄|M̌|M̂|M̀|Ḿ|Ĭ|I̋|I̍|Ī|Ǐ|Î|Ì|Í|Ĕ|E̋|E̍|Ē|Ě|Ê|È|É|Ă|A̋|A̍|Ā|Ǎ|Â|À|Á|ŭ|ű|u̍|ū|ǔ|û|ù|ú|ŏ͘|ő͘|o̍͘|ō͘|ǒ͘|ô͘|ò͘|ó͘|o͘|ŏ|ő|o̍|ō|ǒ|ô|ò|ó|n̆|n̋|n̍|n̄|ň|n̂|ǹ|ń|m̆|m̋|m̍|m̄|m̌|m̂|m̀|ḿ|ĭ|i̋|i̍|ī|ǐ|î|ì|í|ĕ|e̋|e̍|ē|ě|ê|è|é|ă|a̋|a̍|ā|ǎ|â|à|á"
match_composed_re = re.compile(exp)

tone_re = re.compile("[0-9]")

# called by decompose_syllable; we replace a matched, composed vowel to the database query form, such as à -> a3
def tone_replacement(match_obj):
    k = match_obj.group(0)
    v = decompose_lookup[k]
    if v:
        return v
    else:
        return k


# take a composed syllable, such as tsái, and covert it to tsai2 (the database query form)
def decompose_syllable(s):
    nn_replaced = s.replace("ⁿ", "nn")
    converted = match_composed_re.sub(tone_replacement, nn_replaced)
    
    # the coverted string might take a form like "tsa2i", so we need to take out the tone number and append it to the back
    tone = ""    
    m = tone_re.search(converted)
    if m:
        tone = m.group(0)
        converted = tone_re.sub("", converted)
    
    return converted + tone

# process the key, such as bîn-á-tsài to bin5-a2-tsai3
def process_key(key):
    keys = key.split("-")
    new_keys = [decompose_syllable(x) for x in keys]
    return "-".join(new_keys)

# sanitize the kanji part
def process_value(value):
    return value.replace("*", "")


# the main loop
if len(sys.argv) < 2:
    print("usage: lift-read.py <file>")
    sys.exit(1)

lift_path = sys.argv[1]
lift_file = open(lift_path, 'r')

current_tag = ""
text_data = ""
start_form = False

dedup_table = {}

# 3 handler functions
def start_element(name, attrs):
    global current_tag
    global text_data
    global start_form
    
    current_tag = name
    
    if name == 'text' and start_form:
        text_data = ""
    elif name == 'lexical-unit':
        start_form = True
    
def end_element(name):
    global text_data
    global start_form
    global dedup_table

    if name == 'text' and start_form:
        start_form = False
        line = text_data.encode('utf-8').strip()
        sanitized_line = whitespace_re.sub(" ", line)
        kv = sanitized_line.split(" ")

        if len(kv) > 1:        
            k = process_key(kv[0])
            v = process_value(kv[1])
            
            combined_kv = "%s%s" % (k, v)
            if dedup_table.has_key(combined_kv):
                sys.stderr.write("duplicated: %s %s\n" % (k, v))
            else:
                dedup_table[combined_kv] = True
                print("%s,%s,1" % (k, v))
        else:
            sys.stderr.write("ignored: %s\n" % line)

    elif name == 'lexical-unit':
        start_form = False

def char_data(data):
    global text_data
    global current_tag
    global start_form

    if current_tag == "text" and start_form:
        text_data = text_data + data
        
p = xml.parsers.expat.ParserCreate()
p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data
p.ParseFile(lift_file)
lift_file.close()
