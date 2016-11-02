#!/bin/bash
PATH=$PATH:/usr/texbin:/usr/local/bin

pandoc -o ~/Documents/git/vlp/vlpstatisch2/documentation/docu.pdf ~/Documents/git/vlp/vlpstatisch2/documentation/docu.md --latex-engine=pdflatex -V geometry:margin=1in -V lang=german