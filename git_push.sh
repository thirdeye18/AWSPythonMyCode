#!/bin/bash

if [ -z $1 ]
then
	echo "No comment provided for commit"
else
	git add *
	git commit -m "$1"
	git push origin main
fi

