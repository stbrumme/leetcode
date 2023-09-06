cat file.txt | awk '{ nf=NF; for (i=1; i<=nf; i++) t[i]=t[i]" "$i } END { for (i=1; i<=nf; i++) print(t[i]) }' | sed "s/^ //"
