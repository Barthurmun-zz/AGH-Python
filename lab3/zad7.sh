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


function add {
	a = 0 
	echo "The result of adding is:"
	a = $(( $1 + $2 ))
	echo $a
}

function sub {
	echo "The result of subtracting is:"
	a = $(( $1 - $2 ))
	echo $a
}

function mlt {
	echo "The result of multiply is:"
	a = $(( $1 * $2 ))
	echo $a
}

function div {
	echo "The result of dividing is:"
	a = $(( $1 / $2 ))
	echo $a
}



if [ $# != 3 ];
then
	description
	exit 1
fi

if [[ "$1" = "a" ]]
then
	add $2 $3
	exit 0
elif [[ "$1" = "b" ]]
then
	sub $2 $3
	exit 0

elif [[ "$1" = "c" ]]
then
	mlt $2 $3
	exit 0

elif [[ "$1" = "d" ]]
then
	div $2 $3
	exit 0
else
	description
	exit 1
fi
