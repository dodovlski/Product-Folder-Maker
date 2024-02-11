import os
import pathlib


def create_folder_with_link_file(folder_name, txt_link):
    try:
        # Specify target directory
        desktop_path = pathlib.Path.home() / "Desktop/YourCompanyName/Products"

        # Create folder
        folder_path = desktop_path / folder_name
        os.makedirs(folder_path)

        # Generate text document name
        file_name = f"{folder_name.replace(' ', '')}_link.txt"

        # Create text document and write something in it
        with open(folder_path / file_name, 'w') as file:
            file.write(txt_link)

        print(
            f"File '{folder_name}' created on desktop and created a text document named '{file_name}' ")
    except OSError as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    folder_name = input("Enter the name of the product that will created: ")
    txt_link = input("Enter the link: ")
    create_folder_with_link_file(folder_name, txt_link)
