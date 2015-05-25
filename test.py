#!/usr/bin/env python
# -*- coding: utf-8 -*-
from goslateTranslator import *

assert(getAllLanguages()=={u'gu': u'Gujarati', u'zh-TW': u'Chinese (Traditional)', u'ga': u'Irish', u'gl': u'Galician', u'la': u'Latin', u'lo': u'Lao', u'tr': u'Turkish', u'lv': u'Latvian', u'lt': u'Lithuanian', u'th': u'Thai', u'tg': u'Tajik', u'te': u'Telugu', u'ta': u'Tamil', u'yi': u'Yiddish', u'ceb': u'Cebuano', u'yo': u'Yoruba', u'de': u'German', u'da': u'Danish', u'el': u'Greek', u'eo': u'Esperanto', u'en': u'English', u'zh': u'Chinese', u'eu': u'Basque', u'et': u'Estonian', u'es': u'Spanish', u'ru': u'Russian', u'zh-CN': u'Chinese (Simplified)', u'ro': u'Romanian', u'be': u'Belarusian', u'bg': u'Bulgarian', u'ms': u'Malay', u'bn': u'Bengali', u'jw': u'Javanese', u'bs': u'Bosnian', u'ja': u'Japanese', u'ca': u'Catalan', u'cy': u'Welsh', u'cs': u'Czech', u'pt': u'Portuguese', u'tl': u'Filipino', u'pa': u'Punjabi', u'vi': u'Vietnamese', u'pl': u'Polish', u'hy': u'Armenian', u'hr': u'Croatian', u'ht': u'Haitian Creole', u'hu': u'Hungarian', u'hmn': u'Hmong', u'hi': u'Hindi', u'ha': u'Hausa', u'mg': u'Malagasy', u'uz': u'Uzbek', u'ml': u'Malayalam', u'mn': u'Mongolian', u'mi': u'Maori', u'mk': u'Macedonian', u'ur': u'Urdu', u'mt': u'Maltese', u'uk': u'Ukrainian', u'mr': u'Marathi', u'my': u'Myanmar (Burmese)', u'af': u'Afrikaans', u'sw': u'Swahili', u'is': u'Icelandic', u'it': u'Italian', u'iw': u'Hebrew', u'kn': u'Kannada', u'ar': u'Arabic', u'km': u'Khmer', u'zu': u'Zulu', u'az': u'Azerbaijani', u'id': u'Indonesian', u'ig': u'Igbo', u'nl': u'Dutch', u'no': u'Norwegian', u'ne': u'Nepali', u'ny': u'Chichewa', u'fr': u'French', u'fa': u'Persian', u'fi': u'Finnish', u'ka': u'Georgian', u'kk': u'Kazakh', u'sr': u'Serbian', u'sq': u'Albanian', u'ko': u'Korean', u'sv': u'Swedish', u'su': u'Sundanese', u'st': u'Sesotho', u'sk': u'Slovak', u'si': u'Sinhala', u'so': u'Somali', u'sl': u'Slovenian'})

assert(translate("Hello world",'hi') == u'हैलो वर्ल्ड')
assert(translate("Hello world",'Hindi') == u'हैलो वर्ल्ड')
assert(translate("Hello world",'Chinese') == u'你好世界')
try:
    translate("Hello world",'sdifkjsdf')
except Exception:
    assert True
    
print "All the tests are done. The functions are working correctly."


