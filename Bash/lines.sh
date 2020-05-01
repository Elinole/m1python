for f in *.txt;
do
        echo $f
        echo "Lignes :" && wc -l $f
        echo "Mots :" && wc -w $f
done;