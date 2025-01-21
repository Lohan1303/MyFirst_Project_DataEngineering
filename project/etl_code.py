import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

################### EXTRACT METHODS ###################
def extract_from_csv(file_to_process):
    return pd.read_csv(file_to_process)

def extract_from_json(file_to_process):
    return pd.read_json(file_to_process, lines=True)

def extract_from_xml(file_to_process):
    df = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        
        df = pd.concat([df, pd.DataFrame([{"name": name, "height": height, "weight": weight}])], ignore_index=True)
    
    return df

def extract():
    extracted_data = pd.DataFrame(columns=["name", "height", "weight"])
    
    for csv_file in glob.glob(r"source\*.csv"):
        extracted_data = pd.concat([extracted_data, extract_from_csv(csv_file)], ignore_index=True)
    
    for json_file in glob.glob(r"source\*.json"):
        extracted_data = pd.concat([extracted_data, extract_from_json(json_file)], ignore_index=True)
    
    for xml_file in glob.glob(r"source\*.xml"):
        extracted_data = pd.concat([extracted_data, extract_from_xml(xml_file)], ignore_index=True)
        
    return extracted_data

################### TRANSFORM METHODS ###################
def transform(data):
    
    # Convert inches to meters and round off to two decimals
    # 1 inch is 0.0254 meters
    
    data['height'] = round(data['height'] * 0.0254, 2)
    
    # Convert pounds to kilograms and round off to two decimals
    # 1 pound is 0.45359237 kilograms
    
    data['weight'] = round(data['weight'] * 0.45359237, 2)
    
    return data

################### LOADING METHODS ###################
def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file, index=False)

################### LOGGING METHODS ###################
def log_progress(message, log_file):
    timestamp_format = '%Y-%b-%d-%H:%M:%S'  # Corrected format
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    
    with open(log_file, "a") as f:
        f.write(f"{timestamp}, {message}\n")

############# Testing ETL operations and log progress ############# 
log_file = r"C:\Users\Lohan\Desktop\Cursos\IBM_Data_Engineering\project\log_file.txt"
target_file = r"C:\Users\Lohan\Desktop\Cursos\IBM_Data_Engineering\project\target\transformed_data.csv"

# Log the initialization of the ETL process
log_progress("ETL Job Started", log_file)

# Log the beginning of the Extraction process
log_progress("Extract phase Started", log_file)
extracted_data = extract()
log_progress("Extract phase Ended", log_file)

# Log the beginning of the Transformation process
log_progress("Transform phase Started", log_file)
transformed_data = transform(extracted_data)
log_progress("Transform phase Ended", log_file)

# Log the beginning of the Loading process
log_progress("Load phase Started", log_file)
load_data(target_file, transformed_data)
log_progress("Load phase Ended", log_file)

# Log the completion of the ETL process
log_progress("ETL Job Ended", log_file)
