import os
import pandas as pd
from datetime import datetime

def mark_attendance(person_id, name):
    # Path to the Excel file
    file_path = "attendance.xlsx"
    
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Check if the Excel file exists
    if os.path.exists(file_path):
        # Load the existing attendance file
        df = pd.read_excel(file_path)
    else:
        # Create a new DataFrame if the file doesn't exist
        df = pd.DataFrame(columns=["ID", "Name", "Timestamp"])
    
    # Check if the ID has already been marked for the same day
    if not ((df["ID"] == person_id) & (df["Timestamp"].str[:10] == timestamp[:10])).any():
        # Add a new entry to the DataFrame
        new_entry = {"ID": person_id, "Name": name, "Timestamp": timestamp}
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        print(f"Attendance marked for ID: {person_id}, Name: {name}")
    else:
        print(f"Attendance already marked for ID: {person_id}, Name: {name} today.")
    
    # Save the updated DataFrame back to the Excel file
    df.to_excel(file_path, index=False)
