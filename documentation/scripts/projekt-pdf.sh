#!/bin/bash
PATH=$PATH:/Library/TeX/texbin:/usr/texbin:/usr/local/bin

pandoc -o ~/Documents/git/vlp/vlpstatisch2/documentation/projektbeschreibung.pdf ~/Documents/git/vlp/vlpstatisch2/documentation/projektbeschreibung.md --latex-engine=pdflatex -V geometry:margin=1in -V lang=de