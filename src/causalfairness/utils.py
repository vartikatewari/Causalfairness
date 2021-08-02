def load_data(path_1,path_2):
    """Open the folder for cartoon dataset and combine them into one dataset with added column flenames which stores
    the corresponding png filename
    :param path_1: File path to the cartoon dataset directory
    :param path_2: File path to save the cobined csv file
    :returns: saves the combined file to the given path_2"""

    import os
    import glob
    import pandas as pd

    os.chdir(path_1)
    #os.chdir("Documents/GitHub/causalfairness/cartoonset10k/")
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

    # combine all files in the list
    combined_csv = pd.DataFrame()
    for f in all_filenames:
        df = pd.read_csv(f)
        df = df.T
        df = df.reset_index()
        df = df.drop([0,2])
        df['filename'] = f
        df = df.reset_index()
        combined_csv = combined_csv.append(df,ignore_index=True)

    # export to csv
    combined_csv = combined_csv.drop(columns=['level_0'])
    combined_csv.columns = ['eye_angle','eye_lashes','eye_lid','chin_length','eyebrow_weight','eyebrow_shape','eyebrow_thickness','face_shape','facial_hair','hair','eye_color','face_color','hair_color','glasses','glasses_color','eye_slant','eyebrow_width','eye_eyebrow_distance','filename']
    combined_csv.to_csv(path_2+"combined_csv.csv", index=False, encoding='utf-8-sig')
    return

def columntobinary(path_1,path_2):
    """Open the combined data file and make a filtered binary datafile
    :param path_1: File path to the combined file
    :param path_2: File path to save binary file
    :returns: saves the binary file to path_2"""
    import pandas as pd
    df = pd.read_csv(path_1)
    df["facial_hair"].replace({14: 0}, inplace=True)
    df["glasses"].replace({11: 0}, inplace=True)
    df.to_csv(path_2+"filtered_data_binary_new.csv", index=False, encoding='utf-8-sig')

    print(df)
    return