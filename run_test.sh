#!/bin/bash
for j in {1..10};do
    echo " loop " $j
    # sudo tc qdisc replace dev enp1s0f0 root netem loss 0.05% latency 0ms
    python sender.py --algo="GD" --runtime=200 --identifier="transfer1"
    sleep 2
    # sudo tc qdisc replace dev enp1s0f0 root netem loss 0.03% latency 0ms
    python sender.py --algo="GD_FAST" --runtime=200
    sleep 2
    # sudo tc qdisc replace dev enp1s0f0 root netem loss 0.01% latency 0ms
    python sender.py --algo="BO" --runtime=200
done
echo "Done"
