#!/bin/bash
connections=$(ss | grep "tcp.*ssh" | wc -l)
if [[ $connections > 0 ]]
then
    echo "Hey it looks like Abhishek is connected"
else
    poweroff
fi
