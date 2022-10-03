#!/bin/bash
  for j in {1..10};do
      echo " loop " $j
      python sender.py --algo="GD" --runtime=200
      sleep 2
      python sender.py --algo="GD_FAST" --runtime=200
      sleep 2
      python sender.py --algo="BO" --runtime=200
  done
echo "Done"
