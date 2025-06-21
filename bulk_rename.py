import os
import argparse

def bulk_rename(folder, search, replace, prefix, suffix, dry_run, extension):
    # Klasördeki dosyaları listele
    for filename in os.listdir(folder):
        # Dosya mı kontrolü
        full_path = os.path.join(folder, filename)
        if not os.path.isfile(full_path):
            continue
        
        # Uzantı kontrolü (opsiyonel)
        if extension and not filename.endswith(extension):
            continue
        
        # Yeni isim oluştur
        new_name = filename
        
        if search and replace is not None:
            new_name = new_name.replace(search, replace)
        
        if prefix:
            new_name = prefix + new_name
        
        if suffix:
            # Dosya uzantısını koruyarak ekleme yap
            name_part, ext = os.path.splitext(new_name)
            new_name = name_part + suffix + ext
        
        if new_name == filename:
            # Değişiklik yoksa atla
            continue
        
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        
        if dry_run:
            print(f"[Dry-run] {filename} -> {new_name}")
        else:
            print(f"Renaming: {filename} -> {new_name}")
            os.rename(old_path, new_path)

def main():
    parser = argparse.ArgumentParser(description="Bulk file renamer CLI tool")
    parser.add_argument("folder", help="Target folder with files to rename")
    parser.add_argument("--search", help="Search string in filenames")
    parser.add_argument("--replace", help="Replace string for search")
    parser.add_argument("--prefix", help="Add prefix to filenames")
    parser.add_argument("--suffix", help="Add suffix to filenames (before extension)")
    parser.add_argument("--extension", help="Filter files by extension, e.g. .txt")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be renamed without renaming")
    
    args = parser.parse_args()
    
    if args.search and args.replace is None:
        print("Error: If --search is used, --replace must also be provided")
        return
    
    bulk_rename(
        folder=args.folder,
        search=args.search,
        replace=args.replace,
        prefix=args.prefix,
        suffix=args.suffix,
        dry_run=args.dry_run,
        extension=args.extension
    )

if __name__ == "__main__":
    main()
