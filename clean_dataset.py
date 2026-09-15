import os

# Apne dataset ke train ya valid folder ka path yahan theek se dein
labels_dir = 'C:/Users/AMMAR YASIR/Desktop/new_datasetaerial1/test/labels'
images_dir = 'C:/Users/AMMAR YASIR/Desktop/new_datasetaerial1/test/images'

# Upar di gayi list ke mutabiq inki IDs yeh banti hain:
# 0: awning-tricycle, 1: bicycle, 2: bus, 3: car, 4: ignored_regions, 
# 5: motor, 6: others, 7: pedestrian, 8: people, 9: tricycle, 10: truck, 11: van

# Hum sirf Bus (2), Car (3), aur Truck (10) ko rakhna chahte hain.
# Agar aap Van (11) ko Car (3) mein convert karna chahte hain, toh usay neeche remapping mein handle karenge.
allowed_class_ids = [2, 3, 10, 11]  # 11 ko filhal include kar rahe hain taake usay Car mein badal sakein

target_car_id = 3   # Car ki ID
van_id = 11         # Van ki ID jisay Car banana hai

removed_files_count = 0
processed_files_count = 0

for filename in os.listdir(labels_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(labels_dir, filename)
        processed_files_count += 1
        
        with open(file_path, 'r') as f:
            lines = f.readlines()
            
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts:
                class_id = int(parts[0])
                
                # 1. Agar Van (11) hai toh usay Car (3) mein badal do (Remapping)
                if class_id == van_id:
                    parts[0] = str(target_car_id)
                    new_lines.append(" ".join(parts) + "\n")
                
                # 2. Agar Bus, Car, ya Truck hai toh wese hi rakh lo
                elif class_id in allowed_class_ids:
                    new_lines.append(" ".join(parts) + "\n")
                    
        # Agar filtering ke baad koi bhi object nahi bacha, toh file aur image delete kar do
        if len(new_lines) > 0:
            with open(file_path, 'w') as f:
                f.writelines(new_lines)
        else:
            os.remove(file_path)
            removed_files_count += 1
            
            # Corresponding image file ko delete karne ke liye
            base_name = os.path.splitext(filename)[0]
            for ext in ['.jpg', '.jpeg', '.png']:
                img_path = os.path.join(images_dir, base_name + ext)
                if os.path.exists(img_path):
                    os.remove(img_path)
                    break

print(f"Total files checked: {processed_files_count}")
print(f"Empty/Unwanted files & images removed: {removed_files_count}")
print("Dataset successfully cleaned, filtered, and vans remapped to cars!")