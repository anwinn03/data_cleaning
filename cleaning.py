import json
import pandas as pd
import re
import glob

# Making a dataframe for localities
localities = pd.read_csv('localities.csv')
lf = pd.DataFrame(localities)

folder_path = r'RAW\\'  # Double backslash at the end to ensure proper path formation

# Using glob to match all .json files in a folder
rawList = glob.glob(folder_path + '*.json')

# Opening the JSON file
error_files = []

for files in rawList:
    output = []  

    with open(files, 'r') as f:
        read_data = json.load(f)

    for i, d in enumerate(read_data):
        try:
            row = [
                d['fips'],
                d['data']['data']['careers'][0]['title'],
                d['data']['data']['careers'][0]['occupationId'],
                d['data']['data']['careers'][0]['currentEmployment'],
                d['data']['data']['jobs'][0]['timeSeries'][0]['postings'],
                d['data']['data']['careers'][0]['annualEarnings'][2]['earnings']
            ]
            output.append(row)
        except:
            continue

    if output:
        df = pd.DataFrame(output, columns=["fips", "Job Title", "OEC", "Currently Employed", "Job Postings", "Earnings"])
        df = pd.merge(df, localities, on="fips")

        # getting names
        ocode = files.split('_')[1]
        job_title = df['Job Title'][0] if not df.empty else "No_Job_Title"

        # cleaning 
        cleaned_job_title = job_title.replace(" ", "_").replace("/", "_").replace(",", "")
        cleaned_job_title = (cleaned_job_title[:50] + '..') if len(cleaned_job_title) > 50 else cleaned_job_title

        # Standard file naming
        filename = f'{ocode}.{cleaned_job_title}.csv'

        # Exporting csv files
        df.to_csv(filename, index=False)
        print(f"{files} processed and saved to {filename}")

    else:
        print(f"No data processed for {files}")
        error_files.append(files)

print(error_files)