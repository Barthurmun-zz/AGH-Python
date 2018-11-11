#!/bin/bash

echo "Welcome to calculator!"

function description {
	
	echo "You need to add operator and 2 arguments to run the script !"
	echo "Possible operators:"
	echo "  a add
		b subb
		c mlt
		d div "

}


if [ $# != 3 ];
then
	description
	exit 1
fi

if [[ "$1" = "a" ]]
then
	wynik=`expr $2 + $3`
	echo $wynik
	exit 0
elif [[ "$1" = "b" ]]
then
	wynik=`expr $2 - $3`
	echo $wynik
	exit 0

elif [[ "$1" = "c" ]]
then
	wynik=`expr $2 \* $3`
	echo $wynik
	exit 0

elif [[ "$1" = "d" ]]
then
	wynik=`expr $2 / $3`
	echo $wynik
	exit 0
else
	description
	exit 1
fi
