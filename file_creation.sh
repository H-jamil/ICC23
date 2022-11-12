#! /bin/bash

NUM=${1:-4}   ## default to 10 files
SIZE=${2:-1000000000} ## default to 666 bytes
n=0
while [ $n -lt $NUM ]
do
  printf "%0${SIZE}d" 0 > "FILE$n"
  n=$(( $n + 1 ))
done
