import os
import random
import tkinter as tk
from PIL import Image, ImageTk, ImageOps # Import ImageOps

# --- Configuration (rest remains the same) ---
IMAGE_FOLDER = "./rdmimages"
NUM_TOTAL_IMAGES_TO_SELECT = 16
IMAGES_PER_SLIDE = 3
SLIDE_INTERVAL_MS = 3000
TARGET_IMAGE_SIZE = (500, 400)

# --- Image Loading and Selection (rest remains the same) ---
def get_random_image_paths(folder_path, num_images_to_select):
    """
    Gets a list of random image paths from a specified folder.
    """
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')
    all_images = []
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(image_extensions):
                full_path = os.path.join(folder_path, filename)
                all_images.append(full_path)
    else:
        print(f"Error: Image folder '{folder_path}' not found.")
        return []

    if len(all_images) <= num_images_to_select:
        return all_images
    else:
        return random.sample(all_images, num_images_to_select)

class ImageMontageApp:
    def __init__(self, master):
        self.master = master
        master.title("Random Image Montage")
        master.geometry("1000x500")
        master.configure(bg="#ADD8E6")

        self.all_selected_image_paths = get_random_image_paths(IMAGE_FOLDER, NUM_TOTAL_IMAGES_TO_SELECT)

        if not self.all_selected_image_paths:
            print("No images found or selected for the montage. Please check the 'rdmimage' folder.")
            master.destroy()
            return

        self.current_group_start_index = 0
        self.tk_image_references = []

        self.image_display_frame = tk.Frame(master, bg="#D3D3D3", bd=5, relief="ridge")
        self.image_display_frame.pack(padx=20, pady=20, expand=True, fill="both")

        self.image_labels = []
        for _ in range(IMAGES_PER_SLIDE):
            label = tk.Label(self.image_display_frame, bg="#D3D3D3")
            label.pack(side="left", expand=True, fill="both", padx=5, pady=5)
            self.image_labels.append(label)

        self.display_current_slide()
        self.schedule_next_slide()

    def display_current_slide(self):
        self.tk_image_references = []

        for i in range(IMAGES_PER_SLIDE):
            image_index_in_list = (self.current_group_start_index + i) % len(self.all_selected_image_paths)
            img_path = self.all_selected_image_paths[image_index_in_list]
            
            try:
                original_img = Image.open(img_path)
                
                # --- NEW LINE ADDED HERE ---
                # Apply EXIF orientation if present
                original_img = ImageOps.exif_transpose(original_img)
                # --- END NEW LINE ---
                
                # Resize while maintaining aspect ratio
                img_width, img_height = original_img.size
                
                ratio = max(TARGET_IMAGE_SIZE[0] / img_width, TARGET_IMAGE_SIZE[1] / img_height)
                new_width = int(img_width * ratio)
                new_height = int(img_height * ratio)

                resized_img = original_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                tk_img = ImageTk.PhotoImage(resized_img)
                
                self.image_labels[i].config(image=tk_img)
                self.image_labels[i].image = tk_img
                self.tk_image_references.append(tk_img)

            except Exception as e:
                print(f"Error loading or processing image '{img_path}': {e}")
                self.image_labels[i].config(image='')
                self.image_labels[i].image = None

        self.current_group_start_index = (self.current_group_start_index + IMAGES_PER_SLIDE) % len(self.all_selected_image_paths)

    def schedule_next_slide(self):
        self.master.after(SLIDE_INTERVAL_MS, self.display_current_slide)
        self.master.after(SLIDE_INTERVAL_MS, self.schedule_next_slide)


def run_image_montage():
    root = tk.Tk()
    app = ImageMontageApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_image_montage()