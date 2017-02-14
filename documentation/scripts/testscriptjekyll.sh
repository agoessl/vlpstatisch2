#!/bin/bash
[[ -f "${TM_SUPPORT_PATH}/lib/bash_init.sh" ]] && . "${TM_SUPPORT_PATH}/lib/bash_init.sh"

cd /Users/admin/Documents/git/vlp/vlpstatisch2/vlpjekyll && jekyll b -d /Applications/MAMP/htdocs/vlpjekyll 
