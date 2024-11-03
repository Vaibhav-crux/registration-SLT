from pathlib import Path

def check_image_exists():
    # Get the current directory of this script
    current_directory = Path(__file__).resolve().parent

    # Navigate to the 'static/images/upi.png' location relative to the project root
    project_root = current_directory.parents[4]  # Adjust based on your folder structure
    qr_image_path = project_root / 'static' / 'images' / 'upi.png'

    # Check if the image exists
    if not qr_image_path.exists():
        print(f"Image not found at: {qr_image_path}")
        return False
    return True
