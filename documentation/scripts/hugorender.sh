#!/bin/bash
PATH=$PATH:~/Documents/git/vlp/vlpstatisch/bookshelf:~/Documents/git/vlp/vlpstatisch/bookshelf/themes:/usr/local/bin

#hugo server --theme=hugo_theme_robust --buildDrafts --config="~/Documents/git/vlp/vlpstatisch2/bookshelf/config.toml" 

hugo --theme=hugo_theme_robust --config="~/Documents/git/vlp/vlpstatisch/bookshelf/config2.toml"