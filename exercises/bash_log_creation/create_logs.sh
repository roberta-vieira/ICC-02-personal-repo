#!/bin/bash

current_date=$(date +"%Y-%m-%d %H:%M:%S") 

read -r -p "Please enter your message: " message

echo "[$current_date] User: [$USER] - Log entry: $message" >> user_activity.log