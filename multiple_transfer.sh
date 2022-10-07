#!/bin/bash

python sender.py --algo="GD" --runtime=200 --identifier="transfer1_" &
sleep 50
python /users/jamilm/ICC23-2/sender.py --algo="GD" --runtime=200 --identifier="transfer2_" &
sleep 50
python /users/jamilm/ICC23-3/sender.py --algo="GD" --runtime=200 --identifier="transfer3_" &

sleep 5

python sender.py --algo="GD_FAST" --runtime=200 --identifier="transfer1_" &
sleep 50
python /users/jamilm/ICC23-2/sender.py --algo="GD_FAST" --runtime=200 --identifier="transfer2_" &
sleep 50
python /users/jamilm/ICC23-3/sender.py --algo="GD_FAST" --runtime=200 --identifier="transfer3_" &

sleep 5

python sender.py --algo="BO" --runtime=200 --identifier="transfer1_" &
sleep 50
python /users/jamilm/ICC23-2/sender.py --algo="BO" --runtime=200 --identifier="transfer2_" &
sleep 50
python /users/jamilm/ICC23-3/sender.py --algo="BO" --runtime=200 --identifier="transfer3_" &
