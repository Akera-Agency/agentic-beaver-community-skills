#!/bin/bash
# Word counter for cold emails
# Usage: ./word-count.sh email.txt
# Or:    echo "your email text" | ./word-count.sh
# Or:    ./word-count.sh (then paste text, Ctrl+D to finish)

MAX_WORDS=75

# Read from file or stdin
if [ -n "$1" ] && [ -f "$1" ]; then
    text=$(cat "$1")
else
    text=$(cat -)
fi

# Count words
count=$(echo "$text" | wc -w | tr -d ' ')

# Output result
if [ "$count" -le "$MAX_WORDS" ]; then
    echo "✅ $count words (under $MAX_WORDS)"
    exit 0
else
    over=$((count - MAX_WORDS))
    echo "❌ $count words (over by $over)"
    exit 1
fi
