import os
from pypdf import PdfMerger

def merge_pdfs_in_folder(folder_path: str, output_folder_base: str):
    # Get the name of the folder to use as the output PDF name
    folder_name = os.path.basename(folder_path.rstrip("/\\"))
    
    # Create the output folder path mirroring the original structure
    relative_path = os.path.relpath(folder_path, start=parent_directory)
    output_folder_path = os.path.join(output_folder_base, relative_path)
    os.makedirs(output_folder_path, exist_ok=True)

    output_pdf_path = os.path.join(output_folder_path, f"{folder_name}.pdf")
    
    # Initialize the PdfMerger object
    merger = PdfMerger()

    # Define the order of PDFs
    merge_order = ["easy.pdf", "medium.pdf", "hard.pdf"]

    # Loop through the defined order and merge if the file exists
    for pdf_name in merge_order:
        file_path = os.path.join(folder_path, pdf_name)
        if os.path.exists(file_path):
            merger.append(file_path)

    # Write the merged PDF to the output file
    with open(output_pdf_path, 'wb') as output_file:
        merger.write(output_file)

    # Close the merger
    merger.close()

    print(f"Merged PDF created: {output_pdf_path}")

# Specify the parent directory containing all folders and the output directory
parent_directory = "./output_files"
output_directory = os.path.join(parent_directory, "booklets")

# Function to get the folder at the 4th level
def get_4th_level_folders(base_path):
    fourth_level_folders = []
    for root, dirs, _ in os.walk(base_path):
        # Count the level based on the number of directory separators in the path
        if root[len(base_path):].count(os.sep) == 3:  # 3 separators indicate the 4th level
            for dir_name in dirs:
                fourth_level_folders.append(os.path.join(root, dir_name))
    return fourth_level_folders

# Get all 4th level folders
fourth_level_folders = get_4th_level_folders(parent_directory)

# Merge PDFs in each 4th-level folder and save to the mirrored directory structure
for folder in fourth_level_folders:
    merge_pdfs_in_folder(folder, output_directory)
