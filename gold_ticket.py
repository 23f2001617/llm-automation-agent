import sqlite3
import os

# Define database and output file paths
db_path = os.path.join("data", "ticket-sales.db")
output_file = os.path.join("data", "ticket-sales-gold.txt")

try:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query to calculate total sales for "Gold" tickets
    cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'")
    total_sales = cursor.fetchone()[0]

    # Ensure total_sales is a valid number
    total_sales = total_sales if total_sales is not None else 0

    # Write result to output file
    with open(output_file, "w") as file:
        file.write(str(total_sales))

    print(f"Total sales for 'Gold' tickets: {total_sales}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close database connection
    if conn:
        conn.close()
