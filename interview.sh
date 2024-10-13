#!/bin/bash

instance_number=41
while [ $instance_number -le 60 ]; do
    current_directory=$(pwd)
    python3 main.py > $current_directory/logs/individual-interviews/instance-$instance_number.txt

    instance_number=$((instance_number + 1))
done
