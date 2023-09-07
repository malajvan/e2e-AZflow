import pandas as pd
import os
def xlsx_to_csv(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".xlsx"):
                input_path = os.path.join(root, file)
                output_file = os.path.splitext(file)[0] + ".csv"
                output_path = os.path.join(output_folder, output_file)

                # Read XLSX and write as CSV
                df = pd.read_excel(input_path)
                df.to_csv(output_path, index=False)
                print(f"Converted {input_path} to {output_path}")

input_folder = './archive'  # Replace with the path to your folder containing XLSX files
output_folder = './archive_csv'  # Replace with the path where you want to save the CSV files

xlsx_to_csv(input_folder, output_folder)
