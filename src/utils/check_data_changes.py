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
    Gets the data file with required subset columns."""
    df = pd.read_csv(filepath, header=None, names=column_names, delimiter=" ")
    return df[locomotion_set]

def get_filenames(data_dir, test_files):
    os.chdir(data_dir)
    train_filenames = []
    test_filenames = []

    for folder in os.listdir():
        if folder not in test_files:
            os.chdir(folder)
            sensor_path = os.path.join(os.getcwd(), f"{folder}_sensors_data.csv")
            train_filenames.append(sensor_path)
            os.chdir("..")
        else:
            os.chdir(folder)
            sensor_path = os.path.join(os.getcwd(), f"{folder}_sensors_data.csv")
            test_filenames.append(sensor_path)
            os.chdir("..")
    return train_filenames, test_filenames

def get_old_filenames(data_dir):
    filenames = os.listdir(data_dir)
    fnames = []
    for filename in filenames:
        if filename.endswith('.dat'):
            fnames.append(os.path.join(data_dir, filename))
    return fnames

def compare_files(new_file, old_file):
    new_df = pd.read_csv(new_file, header=None, names=column_names, delimiter=" ")
    old_df = pd.read_csv(old_file, header=None, names=column_names, delimiter=" ")
    
    if new_df.equals(old_df):
        return True, None
    else:
        diff = new_df.compare(old_df)
        return False, diff

# Load the new and old dataset files
new_filenames, _ = get_filenames(new_dataset_dir, [])
old_filenames = get_old_filenames(old_dataset_dir)

for new_file in new_filenames:
    new_basename = os.path.basename(new_file).replace(".csv", ".dat")
    old_file = next((f for f in old_filenames if os.path.basename(f) == new_basename), None)
    print(old_file)
    if old_file:
        print(f"Comparing {new_file} with {old_file}")
        are_same, diff = compare_files(new_file, old_file)
        if are_same:
            print(f"{new_file} and {old_file} are the same.")
        else:
            print(f"{new_file} and {old_file} are different.")
            print(diff)
    else:
        pass
        #print(f"Corresponding old file for {new_file} not found.")