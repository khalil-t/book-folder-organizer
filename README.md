# 📂 Book Folder Grouper

This Python script organizes a large collection of book folders by grouping them into sets of 50. It's especially useful for managing datasets with hundreds or thousands of foldered items by making navigation and batch processing more manageable.

## 🚀 Features

- Automatically detects and sorts book folders by number.
- Groups folders into directories containing 50 books each.
- Maintains original folder names.
- Displays progress for each group created.
- Moves folders instead of copying (to save disk space and improve performance).

## 📁 Example Directory Structure


## 🧰 Requirements

- Python 3.x
- Standard Library only (`os`, `shutil`)

## ⚙️ Configuration

### 1. Set your dataset path

Edit this line in the script:

```python
dataset_dir = "your path"

