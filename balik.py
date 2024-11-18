import pyautogui
import time
import os

# Define the areas (coordinates)
fish_area = {"left": 680, "top": 285, "width": 222, "height": 103}
all_area = {"left": 0, "top": 0, "width": 1540, "height": 867}
text_area = {"left": 445, "top": 650, "width": 650, "height": 150}
envanter_area = {"left": 1172, "top": 25, "width": 350, "height": 750}
balik_kontrol = {"left": 630, "top": 322, "width": 330, "height": 230}

# Define the folder where images are stored (use raw string format)
image_folder = r'C:\Users\furka\OneDrive\Masaüstü\balik'

# Function to locate an image within an area
def find_image(image_path, region):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    return pyautogui.locateOnScreen(image_path, region=(region["left"], region["top"], region["width"], region["height"]))

# List of images to search for
balik_listesi = [
    'sazan.png', 'nehirbaligi.png', 'balik.png', 'solucan.png',
    'cesaretinpelerin.png', 'buyukbalik.png', 'otsazani.png', 'buyukbalig.png', 'ringa.png',
    'gumusanahtar.png', 'lucyyuzugu.png', 'levrek.png', 'kirmiziboya.png', 'altinanahtar.png',
    'sacboyasitemizleyici.png', 'hamsi.png', 'kahverengiboya.png', 'yuzuk.png'
]

# Main loop
while True:
    try:
        # Step 1: Right click on 'solucan.png' in envanter_area and press space
        solucan_path = os.path.join(image_folder, 'solucan.png')
        if find_image(solucan_path, envanter_area):
            balik_path = os.path.join(image_folder, 'balik.png')
            pyautogui.rightClick(find_image(balik_path, envanter_area))
            pyautogui.press('space')

        # Step 2: If 'balik.png' is found in fish_area, wait 1 second and press space
        if find_image(balik_path, fish_area):
            time.sleep(1)
            pyautogui.press('space')

        # Step 3: Check for 'birhedefsec.png' in balik_kontrol_area
        birhedefsec_path = os.path.join(image_folder, 'birhedefsec.png')
        if find_image(birhedefsec_path, balik_kontrol):
            # Check for each image in the list and click if found
            for balik in balik_listesi:
                location = find_image(os.path.join(image_folder, balik), balik_kontrol)
                if location:
                    pyautogui.click(location)
                    break
        else:
            # Step 4: If 'kaybettin.png' is found in text_area, repeat from step 1
            kaybettin_path = os.path.join(image_folder, 'kaybettin.png')
            if find_image(kaybettin_path, text_area):
                yem_path = os.path.join(image_folder, 'yem.png')
                if find_image(yem_path, envanter_area):
                    pyautogui.rightClick(find_image(yem_path, envanter_area))
                    pyautogui.press('space')

    except FileNotFoundError as e:
        print(e)
    except OSError as e:
        print(f"OS error: {e}")
    time.sleep(1)  # Short pause to prevent excessive CPU usage
