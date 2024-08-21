import os
from pypdf import PdfReader, PdfWriter

# def merge_pdfs_by_hierarchy(base_dir):
#     # Define the categories and order
#     categories = ["Multiple Choice Questions", "Theory Questions", "Alternative to Practical Questions"]
#     difficulty_order = ["easy.pdf", "medium.pdf", "hard.pdf"]

#     # Traverse the directory structure
#     for root, dirs, files in os.walk(base_dir):

#         if root.count(os.sep) == base_dir.count(os.sep) + 2:
#             # Initialize a dictionary to hold PDFs by category

#             pdf_writer = PdfWriter()

#             if root.count(os.sep) == base_dir.count(os.sep) + 4:
#                 pdf_dict = {category: [] for category in categories}
#                 for file in files:
#                     if file.lower() in difficulty_order:
#                         # Determine the category from the folder name
#                         for category in categories:
#                             if category in subdir_root:
#                                 pdf_path = os.path.join(subdir_root, file)
#                                 pdf_dict[category].append(pdf_path)
#                                 break
                    
#                 for category in categories:
#                     if pdf_dict[category]:
#                         sorted_pdfs = sorted(
#                             pdf_dict[category],
#                             key=lambda f: difficulty_order.index(os.path.basename(f).lower())
#                         )
#                         for pdf_path in sorted_pdfs:
#                             try:
#                                 pdf_reader = PdfReader(pdf_path)
#                                 if len(pdf_reader.pages) > 0:
#                                     for page in pdf_reader.pages:
#                                         pdf_writer.add_page(page)
#                             except Exception as e:
#                                 print(f"Error reading {pdf_path}: {e}")

#             if len(pdf_writer.pages) > 0:
#                 # Create output path for the merged PDF in the Level 2 folder
#                 level_2_folder = os.path.basename(root)
#                 output_pdf_path = os.path.join(root, f"{level_2_folder}_merged.pdf")
                
#                 # Write the merged PDF
#                 try:
#                     with open(output_pdf_path, 'wb') as output_pdf:
#                         pdf_writer.write(output_pdf)
#                     print(f'Merged PDF saved as: {output_pdf_path}')
#                 except Exception as e:
#                     print(f"Error saving merged PDF to {output_pdf_path}: {e}")
#             else:
#                 print(f"No valid PDFs found in {root}")

# Define base directory

def my_pdf_merge(base_dir):

    categories = ["Multiple Choice Questions", "Theory Questions", "Alternative to Practical Questions"]
    difficulty_order = ["easy.pdf", "medium.pdf", "hard.pdf"]

    for root, dir, files in os.walk(base_dir):
        if root.count(os.sep) == base_dir.count(os.sep) + 2:
            pdf_writer = PdfWriter()
            for root2, dir, files2 in os.walk(root):
                if root2.count(os.sep) == base_dir.count(os.sep) + 4:
                    pdf_dict = {category: [] for category in categories}

                    for root3, dir, files3 in os.walk(root2):
                        if root3.count(os.sep) == base_dir.count(os.sep) + 5:
                            for file in files3:
                                if file.lower() in difficulty_order:
                                    # Determine the category from the folder name
                                    for category in categories:
                                        if category in root3:
                                            pdf_path = os.path.join(root3, file)
                                            pdf_dict[category].append(pdf_path)
                                            break
                    
                    for category in categories:
                        if pdf_dict[category]:
                            sorted_pdfs = sorted(
                                pdf_dict[category],
                                key=lambda f: difficulty_order.index(os.path.basename(f).lower())
                            )

                            for pdf_path in sorted_pdfs:
                                try:
                                    pdf_reader = PdfReader(pdf_path)
                                    if len(pdf_reader.pages) > 0:
                                        for page in pdf_reader.pages:
                                            pdf_writer.add_page(page)
                                except Exception as e:
                                    print(f"Error reading {pdf_path}: {e}")

            if len(pdf_writer.pages) > 0:
                # Create output path for the merged PDF in the Level 2 folder
                level_2_folder = os.path.basename(root)
                output_pdf_path = os.path.join(root, f"{level_2_folder}_merged.pdf")
                
                # Write the merged PDF
                try:
                    with open(output_pdf_path, 'wb') as output_pdf:
                        pdf_writer.write(output_pdf)
                    print(f'Merged PDF saved as: {output_pdf_path}')
                except Exception as e:
                    print(f"Error saving merged PDF to {output_pdf_path}: {e}")
            else:
                print(f"No valid PDFs found in {root}")      


base_dir = r'C:\Users\hungk\OneDrive\Documents\Code\Python\Cambridge-PDF-Merger\output_files'  # Use raw string to handle Windows paths
my_pdf_merge(base_dir)
# Run the merging function