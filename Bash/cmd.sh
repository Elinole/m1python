read $1 $2
if [[ $1 && $2 =~ ^[+-]?[0-9]+$ ]]; then
        echo La somme de ces deux arguments est de $(($1+$2))
else
        echo Les arguments doivent être de type integer
fi