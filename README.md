# Product Folder Creator

This Python script creates a folder and a text file inside it, based on user input of a product name and a link.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/product-folder-creator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd product-folder-creator
    ```

3. Run the script:

    ```bash
    python create_folder_with_link.py
    ```

4. Follow the prompts to enter the product name and link.

## Code Explanation

This script defines a function `create_folder_with_link_file` that performs the following steps:

1. Takes two parameters: `folder_name` (the name of the folder) and `txt_link` (the link).
2. Receives the folder name and link provided by the user.
3. Determines a directory path pointing to a directory under the user's desktop called "YourCompanyName/Products."
4. Creates a folder with the specified folder name.
5. Creates a text file inside the folder, named according to the folder name with "_link.txt" appended to it.
6. Writes the provided link into the text file.
7. Prints a notification if the process is completed successfully.

However, there seems to be an issue with the code. When creating the folder with `os.makedirs(folder_path)`, if the target directory already exists, the code may raise an error. Specifically, if it attempts to recreate an existing folder, it could raise a `FileExistsError`. To prevent this error, it's better to call the `os.makedirs()` function with the argument `exist_ok=True`.

```python
os.makedirs(folder_path, exist_ok=True)
