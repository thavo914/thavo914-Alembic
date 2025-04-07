import os
import sys
import stat
from datetime import datetime

def check_file_permissions(file_path):
    """Check permissions of a file and return detailed information"""
    try:
        if os.path.exists(file_path):
            file_stat = os.stat(file_path)
            permissions = stat.filemode(file_stat.st_mode)
            
            # Get owner and group info (this might fail in some containers)
            try:
                import pwd, grp
                owner = pwd.getpwuid(file_stat.st_uid).pw_name
                group = grp.getgrgid(file_stat.st_gid).gr_name
            except (ImportError, KeyError):
                owner = str(file_stat.st_uid)
                group = str(file_stat.st_gid)
            
            return {
                "exists": True,
                "permissions": permissions,
                "owner": owner,
                "group": group,
                "size": file_stat.st_size,
                "last_modified": datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            }
        else:
            return {"exists": False, "error": "File does not exist"}
    except Exception as e:
        return {"exists": "error", "error": str(e)}

def check_env_file():
    """Check if .env file exists and is readable"""
    # List of paths to check
    paths_to_check = [
        '/opt/spark/config/.env',
        '/opt/bitnami/spark/config/.env',
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', '.env'),
        os.path.join(os.getcwd(), 'config', '.env')
    ]
    
    print(f"Script running as user: {os.getuid()} / {os.getgid()}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Script location: {__file__}")
    print(f"Python path: {sys.path}")
    
    for path in paths_to_check:
        print(f"\nChecking path: {path}")
        result = check_file_permissions(path)
        
        if result["exists"] == True:
            print(f"✓ File exists: {path}")
            print(f"  Permissions: {result['permissions']}")
            print(f"  Owner: {result['owner']}")
            print(f"  Group: {result['group']}")
            print(f"  Size: {result['size']} bytes")
            print(f"  Last modified: {result['last_modified']}")
            
            # Try to read the file
            try:
                with open(path, 'r') as f:
                    lines = f.readlines()
                    print(f"  Successfully read {len(lines)} lines from file")
                    print("  First few lines (with sensitive data masked):")
                    for i, line in enumerate(lines[:5]):
                        # Mask passwords and sensitive data
                        if "PASSWORD" in line or "password" in line:
                            parts = line.split('=', 1)
                            if len(parts) > 1:
                                masked_line = f"{parts[0]}=********\n"
                                print(f"    {masked_line.strip()}")
                        else:
                            print(f"    {line.strip()}")
            except Exception as e:
                print(f"  ✗ Error reading file: {e}")
        elif result["exists"] == False:
            print(f"✗ File does not exist: {path}")
        else:
            print(f"✗ Error checking file: {result['error']}")
    
    # Check directory permissions
    for dir_path in set([os.path.dirname(p) for p in paths_to_check]):
        if os.path.exists(dir_path):
            print(f"\nChecking directory: {dir_path}")
            dir_result = check_file_permissions(dir_path)
            print(f"  Permissions: {dir_result['permissions']}")
            print(f"  Owner: {dir_result['owner']}")
            print(f"  Group: {dir_result['group']}")
            
            try:
                print("  Directory contents:")
                for item in os.listdir(dir_path):
                    item_path = os.path.join(dir_path, item)
                    item_stat = os.stat(item_path)
                    item_perm = stat.filemode(item_stat.st_mode)
                    print(f"    {item_perm} {item}")
            except Exception as e:
                print(f"  ✗ Error listing directory: {e}")
        else:
            print(f"\n✗ Directory does not exist: {dir_path}")

if __name__ == "__main__":
    check_env_file()