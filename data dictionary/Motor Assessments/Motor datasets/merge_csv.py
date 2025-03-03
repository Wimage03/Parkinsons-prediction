import pandas as pd
import os

def merge_csv_files(file_list, output_file):
    """Merges CSV files and maintains column order."""

    if not file_list:  # Check if the file list is empty
        raise ValueError("File list is empty. Please provide at least one CSV file.")

    # Read the first file to initialize the merged DataFrame
    merged_df = pd.read_csv(file_list[0])

    # Read and merge the remaining files
    for file_path in file_list[1:]:
        df = pd.read_csv(file_path)
        merged_df = pd.merge(merged_df, df, on=['PATNO', 'EVENT_ID'], how='outer', suffixes=('', '_drop'))

        # Drop the duplicate columns that have been renamed with the suffix
        merged_df = merged_df[[col for col in merged_df.columns if not col.endswith('_drop')]]

    # Ensure columns are in the correct order
    fieldnames = list(merged_df.columns)
    merged_df = merged_df[fieldnames]

    # Write the merged data to the output file
    merged_df.to_csv(output_file, index=False)

# Example usage
curr_dir_files = ['MDS-UPDRS_Part_I_24May2024.csv', 'MDS-UPDRS_Part_I_Patient_Questionnaire_24May2024.csv','MDS_UPDRS_Part_II__Patient_Questionnaire_24May2024.csv','MDS-UPDRS_Part_III_24May2024.csv', 'MDS-UPDRS_Part_IV__Motor_Complications_24May2024.csv','Gait_Data___Arm_swing_24May2024.csv', 'Gait_Substudy_Gait_Mobility_Assessment_and_Measurement_24May2024.csv', 'Modified_Schwab___England_Activities_of_Daily_Living_24May2024.csv', 'Neuro_QoL__Lower_Extremity_Function__Mobility__-_Short_Form_24May2024.csv',
'Neuro_QoL__Upper_Extremity_Function_-_Short_Form_24May2024.csv',
'Participant_Motor_Function_Questionnaire_24May2024.csv']

outside_files = ['Benton_Judgement_of_Line_Orientation_24May2024.csv', 'Clock_Drawing_24May2024.csv',
'Clock_Drawing_24May2024.csv',
'Cognitive_Categorization_24May2024.csv',
'Cognitive_Change_24May2024.csv',
'Epworth_Sleepiness_Scale_24May2024.csv',
'Geriatric_Depression_Scale__Short_Version__24May2024.csv',
'Hopkins_Verbal_Learning_Test_-_Revised_24May2024.csv',
'Letter_-_Number_Sequencing_24May2024.csv',
'Lexical_Fluency_24May2024.csv',
'Modified_Boston_Naming_Test_24May2024.csv',
'Modified_Semantic_Fluency_24May2024.csv',
'Montreal_Cognitive_Assessment__MoCA__24May2024.csv',
'Neuro_QoL__Cognition_Function_-_Short_Form_24May2024.csv',
'Neuro_QoL__Communication_-_Short_Form_24May2024.csv',
'QUIP-Current-Short_24May2024.csv',
'REM_Sleep_Behavior_Disorder_Questionnaire_24May2024.csv',
'SCOPA-AUT_24May2024.csv',
'State-Trait_Anxiety_Inventory_24May2024.csv',
'Symbol_Digit_Modalities_Test_24May2024.csv',
'Trail_Making_A_and_B_24May2024.csv',
'University_of_Pennsylvania_Smell_Identification_Test_UPSIT_24May2024.csv']

file_list = curr_dir_files + [
    os.path.join('..', '..', 'Non-Motor Assessments', 'Non-motor_Assessments', f) for f in outside_files
]

output_file = 'merged_files_testing_update.csv'
merge_csv_files(file_list, output_file)