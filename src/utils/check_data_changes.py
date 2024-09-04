import os
import pandas as pd
import yaml

new_dataset_dir = r"C:\Users\Pranshu\Downloads\Opportunity++\data"
old_dataset_dir = r'C:\Users\Pranshu\Downloads\opportunity\OpportunityUCIDataset\dataset'

def load_variable_names(filename):
    with open(filename, "r") as file:
        names = yaml.safe_load(file)
    return names

column_names = load_variable_names("./src/config/unique_column_names.yaml")
locomotion_set = load_variable_names("./src/config/locomotion_set.yaml")
body_features = yaml.safe_load("./src/config/body_features.yaml")
assert type(locomotion_set) == list, "Yaml not loaded correctly"

def get_file(filepath: str):
    """
    Gets the data file with required subset columns.
    """
    df = pd.read_csv(filepath, header=None, names=column_names, delimiter=" ")
    return df[locomotion_set]

def get_new_filenames(data_dir):
    """
    Get filenames from the new dataset directory.
    """
    new_filenames = []
    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith('_sensors_data.txt'):
                new_filenames.append(os.path.join(root, file))
    return new_filenames

def get_old_filenames(data_dir):
    """
    Get filenames from the old dataset directory.
    """
    old_filenames = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.dat'):
            old_filenames.append(os.path.join(data_dir, filename))
    return old_filenames

def compare_files(new_file, old_file):
    """
    Compare the contents of the new and old files.
    """
    new_df = pd.read_csv(new_file, header=None, names=column_names, delimiter=" ")
    old_df = pd.read_csv(old_file, header=None, names=column_names, delimiter=" ")
    
    if new_df.equals(old_df):
        return True, None
    else:
        diff = new_df.compare(old_df)
        return False, diff

new_filenames = get_new_filenames(new_dataset_dir)
old_filenames = get_old_filenames(old_dataset_dir)

for new_file in new_filenames:
    new_basename = os.path.basename(new_file).replace("_sensors_data.txt", ".dat")
    old_file = None
    for old in old_filenames:
        if os.path.basename(old) == new_basename:
            old_file = old
            break
    
    if old_file:
        print(f"Comparing {new_file} with {old_file}")
        are_same, diff = compare_files(new_file, old_file)
        if are_same:
            print("same\n")
        else:
            print(f"{new_file} and {old_file} are different.\n")
            print(diff)
    else:
        print(f"Corresponding old file for {new_file} not found.")
