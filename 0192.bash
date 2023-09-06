cat words.txt | tr " " "\n" | grep -v "^$" | sort | uniq --count | sort --numeric-sort --reverse | awk '{print $2, $1 }'
