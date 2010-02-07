# A LIFT to CSV Converter for the Holo Language

This project provides a tool that converts [LIFT](http://www.wesay.org/wiki/LIFT) (Lexicon Interchange FormaT) to simplified CSV. LIFT is the format used by WeSay, a dictionary collaboration tool project initiated by [SIL International](http://sil.org/) and its partners. A typical database in LIFT contains comprehensive information on the lexicon of a language, such as part of speech, meaning, and other phonetic, morphological, and semantic information. The converter presented here extracts the information we need from a LIFT file to build, for example, an input method.

One reason we choose to use WeSay is because it comes with collaboration features as of its version 0.7. The collaboration feature leverages the [Mercurial (Hg)](http://mercurial.selenic.com/) source control management tool, which enables material collection and editing in a distributed manner.

## How to Use It

1.  git clone this project:

        git clone git://github.com/lukhnos/lift-convert.git
        
2.  Get a copy of the nan-tw language source at either:

    *   http://public.languagedepot.org/projects/show/nan-tw (you'll need to request for its access from the administrator, Pektiong Tan), or
    *   http://github.com/lukhnos/langsource-nan-tw (a github mirror currently maintained by me; this repository is pushed directly from the Hg source above using the [Hg-Git plugin](http://hg-git.github.com/))
    
3.  Run the script:

        ./nan-tw-TL-LIFT2CSV.py nan.lift > nan.csv
        
## Notes on the Conversion Process

*   The script currently performs a simple, naive XML extraction from the `<lexical-unit>` tags contained in each word node.
*   All syllables in the language source are of the "composed" form, such as bîn-á-tsài ("tomorrow"). For input method and other information retrieval purposes, this is not really usable. So the script converts them back into the so-called "database query form", such as bin5-a2-tsai3. We make the assumption that only standard vowel symbols, especially composed Unicode forms like "Ô͘", are consistently used throughout the LIFT database.

## Copyright and Licensing

Copyright (c) 2010 Lukhnos D. Liu.

What follows is the standard, very liberal [MIT License](http://en.wikipedia.org/wiki/MIT_License):

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Contact

If you run into any problem, please contact me at: lukhnos at lukhnos dot dog.

## Improving the Code

It's github. Just fork it.
