#!/usr/bin/env python3
"""
Demo script to showcase the Cyber Risk Monitor functionality
Creates sample files of different risk levels for demonstration
"""

import os
import time

def create_demo_files():
    """Create sample files for demonstration"""

    demo_files = {
        # High risk files
        'malware.exe': 'Simulated executable file',
        'script.bat': 'Batch script content',
        'suspicious.dll': 'Dynamic link library',

        # Medium risk files
        'archive.zip': 'Compressed archive',
        'document.pdf': 'PDF document content',
        'spreadsheet.xlsx': 'Excel spreadsheet data',

        # Low risk files
        'readme.txt': 'Project documentation',
        'image.jpg': 'JPEG image data',
        'code.py': 'Python source code',
        'config.json': 'Configuration file',
    }

    print("🔧 Creating demo files for Cyber Risk Monitor...")

    for filename, content in demo_files.items():
        try:
            with open(filename, 'w') as f:
                f.write(content)
            print(f"✅ Created: {filename}")
            time.sleep(0.1)  # Small delay to ensure different timestamps
        except Exception as e:
            print(f"❌ Failed to create {filename}: {e}")

    print("\n🎯 Demo files created! Start the application with:")
    print("   python app.py")
    print("   Then visit: http://localhost:5000")

if __name__ == "__main__":
    create_demo_files()