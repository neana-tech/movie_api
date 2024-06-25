#!/bin/bash

# API endpoint
URL="http://127.0.0.1:5000/movies"

# List of movie titles
titles=(
"Spiderman"
"Batman"
"Ironman"
"Hulk"
"Thor"
"Captain America"
"Black Panther"
"Wonder Woman"
"Aquaman"
"Flash"
"Green Lantern"
"Doctor Strange"
"Ant-Man"
"Wasp"
"Black Widow"
"Hawkeye"
"Scarlet Witch"
"Vision"
"Falcon"
"Winter Soldier"
"Star-Lord"
"Gamora"
"Drax"
"Rocket Raccoon"
)

# Function to make a POST request
post_data() {
title=$1
curl -X POST -H "Content-Type: application/json" -d "{\"title\": \"$title\"}" $URL
}

# Iterate over the list and post data
for title in "${titles[@]}"; do
post_data "$title"
done

echo "Data population completed!"