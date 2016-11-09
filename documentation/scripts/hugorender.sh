#!/bin/bash
PATH=$PATH:~/Documents/git/vlp/vlpstatisch2/bookshelf:~/Documents/git/vlp/vlpstatisch2/bookshelf/themes:/usr/local/bin

#hugo server --theme=hugo_theme_robust --buildDrafts --config="~/Documents/git/vlp/vlpstatisch2/bookshelf/config.toml" 

hugo --theme=hugo_theme_robust --config="~/Documents/git/vlp/vlpstatisch2/bookshelf/config2.toml"