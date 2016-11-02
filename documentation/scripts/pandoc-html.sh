#!/bin/bash
PATH=$PATH:/usr/texbin:/usr/local/bin

pandoc -s -o ~/Documents/git/vlp/vlpstatisch2/documentation/docu.html ~/Documents/git/vlp/vlpstatisch2/documentation/docu.md --to=html5