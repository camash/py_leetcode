cat words.txt | tr -s '[:space:]' '\n'|sort| uniq -c |sort -nr | awk '{print$2,$1}'
