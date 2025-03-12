import os
import shutil

# Define dataset directory
dataset_dir = "your path"

# Check if the provided path exists
if not os.path.isdir(dataset_dir):
    print(f"❌ Error: The path '{dataset_dir}' does not exist.")
    exit()

# Output folder
output_dir = r"E:\output_books"
os.makedirs(output_dir, exist_ok=True)

# Function to extract numerical values for correct sorting
def extract_number(folder_name):
    numbers = ''.join(filter(str.isdigit, folder_name))  # Extract digits
    return int(numbers) if numbers else float('inf')  # Convert to int or move non-numeric last

# Get all book folders and sort them numerically
books = sorted(
    [book for book in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, book))],
    key=extract_number
)

# Group books into sets of 50
for i in range(0, len(books), 50):
    group_number = (i // 50) + 1  # Group index
    group_folder = os.path.join(output_dir, f"Group-{group_number}")  # Naming the big folder
    os.makedirs(group_folder, exist_ok=True)

    for book in books[i:i + 50]:  # Take 50 folders per group
        book_path = os.path.join(dataset_dir, book)
        dest_path = os.path.join(group_folder, book)  # Keep original folder name
        shutil.move(book_path, dest_path)  # Move instead of copying

    print(f"📦 Created {group_folder} containing {len(books[i:i + 50])} book folders.")

print("✅ Books have been regrouped into sets of 50 in correct order!")
