echo "Entrez un nombre (non flottant)"
read number
if [[ $number =~ ^[+-]?[0-9]+$ ]]; then
        echo Votre nombre comporte "${#number}" chiffres.
else
        echo "Ce n'est pas un nombre."
fi