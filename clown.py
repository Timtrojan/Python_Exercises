import pathlib

path = pathlib.Path
file_path = path.cwd() / "my_folder"
file_path.mkdir(exist_ok=True)
new_file_path = file_path / "my_file.txt"
new_file_path.touch()
print("Does file path Exists?-", file_path.exists())
print("name-", file_path.name)
print ("name of folder-", file_path.parent)
