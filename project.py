import argparse
import os
import shutil
import sys

CATEGORY_MAP = {
    "Images": {"jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg", "webp"},
    "Documents": {"pdf", "doc", "docx", "txt", "odt", "rtf", "xls", "xlsx", "ppt", "pptx", "md"},
    "Videos": {"mp4", "mkv", "mov", "avi", "wmv", "flv", "webm"},
    "Audio": {"mp3", "wav", "flac", "aac", "ogg", "m4a"},
    "Archives": {"zip", "rar", "7z", "tar", "gz", "bz2"},
    "Code": {"py", "js", "ts", "java", "c", "cpp", "cs", "html", "css", "json", "xml", "sh"},
}

DEFAULT_CATEGORY = "Others"


def get_downloads_folder() -> str:
    """Return the current user's Downloads path."""
    home = os.path.expanduser("~")
    downloads = os.path.join(home, "Downloads")
    if os.path.isdir(downloads):
        return downloads

    # Windows fallback using USERPROFILE
    user_profile = os.environ.get("USERPROFILE")
    if user_profile:
        downloads = os.path.join(user_profile, "Downloads")
        if os.path.isdir(downloads):
            return downloads

    raise FileNotFoundError("Could not locate the Downloads folder.")


def categorize_file(filename: str) -> str:
    """Choose the category folder for a file based on extension."""
    ext = os.path.splitext(filename)[1].lstrip(".").lower()
    for category, extensions in CATEGORY_MAP.items():
        if ext in extensions:
            return category
    return DEFAULT_CATEGORY


def ensure_folder(path: str) -> None:
    """Create the target folder if it does not exist."""
    os.makedirs(path, exist_ok=True)


def move_file(src_path: str, dest_folder: str) -> None:
    """Move a file into the destination folder."""
    ensure_folder(dest_folder)
    dest_path = os.path.join(dest_folder, os.path.basename(src_path))
    if os.path.abspath(src_path) == os.path.abspath(dest_path):
        return
    shutil.move(src_path, dest_path)


def organize_downloads(downloads_folder: str, dry_run: bool = False) -> None:
    """Scan the Downloads folder and move files into categorized subfolders."""
    if not os.path.isdir(downloads_folder):
        raise NotADirectoryError(f"The folder does not exist: {downloads_folder}")

    for entry in os.listdir(downloads_folder):
        src_path = os.path.join(downloads_folder, entry)
        if os.path.isdir(src_path):
            continue

        category = categorize_file(entry)
        dest_folder = os.path.join(downloads_folder, category)
        if dry_run:
            print(f"Would move: {entry} -> {category}/")
        else:
            move_file(src_path, dest_folder)
            print(f"Moved: {entry} -> {category}/")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Organize the Downloads folder into category subfolders based on file extensions."
    )
    parser.add_argument(
        "--path",
        help="Path to the Downloads folder. Defaults to the current user's Downloads.",
        default=None,
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be moved without changing any files.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    target_folder = args.path or get_downloads_folder()

    try:
        organize_downloads(target_folder, dry_run=args.dry_run)
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)
