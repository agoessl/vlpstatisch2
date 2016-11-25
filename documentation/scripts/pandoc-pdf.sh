#!/bin/bash
PATH=$PATH:/Library/TeX/texbin:/usr/texbin:/usr/local/bin

pandoc -o $HOME/Documents/git/vlp/vlpstatisch2/documentation/docu.pdf $HOME/Documents/git/vlp/vlpstatisch2/documentation/docu.md --latex-engine=pdflatex -V geometry:margin=1in -V lang=de