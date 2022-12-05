import pathlib

path = pathlib.Path("/cohort/private.img")
cwd_path = path.cwd() / "felix"
# fake_path = path("/cohort/private.img")
# print(cwd_path)
# print("parent-", cwd_path.parent)
# print(list(fake_path.parents))
# print("Anchor-", fake_path.anchor)
# print("name-", fake_path.name)
# print("Suffix-", fake_path.suffix)
print(list(path.parents))
print(path.is_absolute())
cwd_path.mkdir(exist_ok=True)
new_file_path = cwd_path / "private.txt"
new_file_path.touch()
print("Exists?-", cwd_path.exists())


