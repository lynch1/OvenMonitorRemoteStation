#!/bin/bash
python ~/OvenMonitorRemoteStation/makeMeasurement.py
sleep 6
python ~/OvenMonitorRemoteStation/sendMessage.py