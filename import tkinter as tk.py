import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
from customtkinter import CTkImage
import random
import threading

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def start_encryption():
    thread = threading.Thread(target=encrypt_image)
    thread.start()

def start_decryption():
    thread = threading.Thread(target=decrypt_image)
    thread.start()

def encrypt_image():
    process_image(encrypt=True)

def decrypt_image():
    process_image(encrypt=False)

def process_image(encrypt=True):
    global img_path, display_img
    if not img_path:
        messagebox.showerror("Error", "Please select an image first.")
        return

    try:
        key = int(key_entry.get())
        if key < 0 or key > 255:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Key must be a number between 0 and 255.")
        return

    try:
        img = Image.open(img_path).convert("RGB")
        
        max_size = 1024
        img.thumbnail((max_size, max_size))
        width, height = img.size

        pixels = list(img.get_flattened_data())

        
        pixels = [(r ^ key, g ^ key, b ^ key) for (r, g, b) in pixels]

       
        random.seed(key)
        indices = list(range(len(pixels)))
        if encrypt:
            random.shuffle(indices)
        else:
           
            shuffle = list(range(len(pixels)))
            random.shuffle(shuffle)
            reverse_map = [0] * len(shuffle)
            for i, j in enumerate(shuffle):
                reverse_map[j] = i
            indices = reverse_map

        pixels = [pixels[i] for i in indices]

        
        new_img = Image.new("RGB", (width, height))
        new_img.putdata(pixels)

        
        preview_img = new_img.copy()
        preview_img.thumbnail((300, 300))
        display_img = CTkImage(preview_img)
        image_label.configure(image=display_img)

       
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")]
        )
        if save_path:
            new_img.save(save_path)
            messagebox.showinfo("Success", "Image processed successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def load_image():
    global img_path, display_img
    img_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )
    if img_path:
        img = Image.open(img_path)
        img.thumbnail((300, 300))
        display_img = CTkImage(img)
        image_label.configure(image=display_img)



app = ctk.CTk()
app.title("Responsive Image Encryption Tool")
app.geometry("500x550")
app.resizable(False, False)



img_frame = ctk.CTkFrame(app, corner_radius=15)
img_frame.pack(pady=10, padx=20, fill="both", expand=False)

image_label = ctk.CTkLabel(img_frame)
image_label.pack(padx=10, pady=10)


ctk.CTkButton(app, text="Load Image", command=load_image, width=200).pack(pady=10)


ctk.CTkLabel(app, text="Encryption Key (0–255)", font=ctk.CTkFont(size=14)).pack(pady=(20, 5))
key_entry = ctk.CTkEntry(app, width=150)
key_entry.pack(pady=5)


btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=20)

ctk.CTkButton(btn_frame, text="Encrypt Image", width=150, command=start_encryption).grid(row=0, column=0, padx=10)
ctk.CTkButton(btn_frame, text="Decrypt Image", width=150, command=start_decryption).grid(row=0, column=1, padx=10)

app.mainloop()
