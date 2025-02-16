import os
from pathlib import Path

# Define paths
log_dir = Path("data/logs")
output_file = Path("data/logs-recent.txt")

# Get list of .log files, sorted by modification time (newest first)
log_files = sorted(log_dir.glob("*.log"), key=os.path.getmtime, reverse=True)[:10]

# Extract first lines from the 10 most recent log files
first_lines = []
for log_file in log_files:
    with open(log_file, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()
        if first_line:
            first_lines.append(first_line)

# Write to logs-recent.txt
output_file.parent.mkdir(parents=True, exist_ok=True)  # Ensure /data exists
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(first_lines))

print("Extracted first lines from 10 most recent log files.")
