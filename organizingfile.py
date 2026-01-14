import os

# Change this to the folder you want to organize
TARGET_FOLDER = r"path/to/your/folder"  
dry_run = True  # set False to actually move files

def organize_by_extension(folder, dry_run=True):
    # 1. list everything in folder
    for name in os.listdir(folder):
        full_path = os.path.join(folder, name)
        
        # 2. skip directories (we only want files)
        if os.path.isdir(full_path):
            continue
        
        # 3. split name into base and extension
        base, ext = os.path.splitext(name)
        if not ext:
            ext_folder = "no_extension"
            
        else:
            ext_folder = ext.lstrip(".").lower()  # e.g., ".PDF" -> "pdf"
            
        target_dir = os.path.join(folder, ext_folder)
        target_path = os.path.join(target_dir, name)
        
        # 4. show (or perform) the action
        print(f"{full_path} -> {target_path}")
        if dry_run:
            continue
        
        # 5. ensure target directory exists
        os.makedirs(target_dir, exist_ok=True)
        
         # 6. if a file with same name exists in target, rename to avoid overwrite
        counter = 1
        final_target = target_path
        while os.path.exists(final_target):
            final_target = os.path.join(target_dir, f"{base} ({counter}){ext}")
            counter += 1
            
        # 7. move using rename (works if same filesystem)
        os.rename(full_path, final_target)
        
# Run:
organize_by_extension(TARGET_FOLDER, dry_run=dry_run)