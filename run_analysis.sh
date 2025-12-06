#!/bin/bash

# Script to run the OSINT analysis tool
# Usage: ./run_analysis.sh [URL]
# If no URL is provided, it starts a temporary local server to analyze index.html

URL=$1

if [ -z "$URL" ]; then
    echo "[*] No URL provided. Starting local server to analyze index.html..."
    # Start server on port 8082 in background
    python3 -m http.server 8082 > /dev/null 2>&1 &
    SERVER_PID=$!
    
    # Wait for server to start
    sleep 2
    
    URL="http://localhost:8082/index.html"
    
    echo "[*] Analyzing $URL..."
    python3 analyze_osint.py "$URL"
    
    # Cleanup
    echo "[*] Stopping local server..."
    kill $SERVER_PID
else
    echo "[*] Analyzing $URL..."
    python3 analyze_osint.py "$URL"
fi
