from pathlib import Path
from constants import EXTANSIONS, FOLDERS
from normalize import normalize


def pre_normalize(file_name, point: bool):
    if point:
        return normalize(file_name)


def folder_selection(file: Path, result: dict):
    file_name = file.name
    file_extension = file.suffix[1:]
    file_type = EXTANSIONS.get(file_extension, "other")
    if result.get(file_type):
        result[file_type].append(file_name)
    else:
        result[file_type] = [file_name]
    return result


def check_folder(folder, deleted_folders: list, unknown_folders: list):
    is_empty = any(folder.iterdir())
    if is_empty:
        unknown_folders.append(folder.name)
        return unknown_folders
    else:
        if folder.name not in FOLDERS:
            deleted_folders.append(folder.name)
            folder.rmdir()
            return deleted_folders


def sorter(path: Path, point):
    result = {}
    deleted_folders = []
    unknown_folders = []
    for item in path.iterdir():
        if item.is_file():
            new_path = path / (pre_normalize(item.name, point))
            (path / item).replace(new_path)
            result = folder_selection(new_path, result)
        elif item.is_dir():
            check_folder(item, deleted_folders, unknown_folders)

    return result, deleted_folders, unknown_folders


def file_parser(*args):
    try:
        folder_for_scan = Path(args[0])
        sorted_file_dict, deleted_folders, unknown_folders = sorter(folder_for_scan, args[1])
    except FileNotFoundError:
        return f"Not able to find '{args[0]}' folder. Please enter a correct folder name."
    except IndexError:
        return "Please enter a folder name."
    except IsADirectoryError:
        return "Unknown file."
    for file_types, files in sorted_file_dict.items():
        for file in files:
            if not (folder_for_scan / file_types).exists():
                (folder_for_scan / file_types).mkdir()
                Path(folder_for_scan / file).rename((folder_for_scan / file_types / file))
            else:
                Path(folder_for_scan / file).rename((folder_for_scan / file_types / file))
    out_text = ""
    if sorted_file_dict:
        out_text += "Sorting is complete\n" + "-" * 20 + "\n" + "Created folders:\n"
        for folder, files in sorted_file_dict.items():
            out_text += f"     {folder}\n"
        out_text += f"Unknown folders: {[i for i in unknown_folders]}\n"
        out_text += f"Deleted folders : {[i for i in deleted_folders]}"
    else:
        out_text += "There is nothing to sort in the current directory"
    return out_text




