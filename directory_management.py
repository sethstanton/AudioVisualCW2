import os

# Path to the 'recordings' folder
recordings_path = 'C:/Users/Setha/OneDrive/Documents/GitHub/AudioVisualCW2/recordings'

# Iterate over each name in the recordings directory
for name in os.listdir(recordings_path):
    name_path = os.path.join(recordings_path, name)

    # Check if it's a directory (a name folder)
    if os.path.isdir(name_path):
        # Create 50 sample folders within each name folder
        for sample_num in range(1, 51):
            sample_folder_path = os.path.join(name_path, f'sample_{sample_num}')
            os.makedirs(sample_folder_path, exist_ok=True)

            # Move respective files to the sample folder
            for file in os.listdir(name_path):
                # Check if the file belongs to this sample
                if f'{name}_{sample_num}' in file:
                    original_file_path = os.path.join(name_path, file)
                    new_file_path = os.path.join(sample_folder_path, file)
                    os.rename(original_file_path, new_file_path)
