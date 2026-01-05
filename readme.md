Responsive Image Encryption Tool

A modern Python GUI application that allows users to encrypt and decrypt images using XOR and pixel shuffling. Built with CustomTkinter and Pillow, this tool is fully responsive, handles large images, and provides a real-time preview.

Features

Encrypt images with a user-defined key (0–255)

Decrypt images using the same key

XOR + Pixel shuffling algorithm for secure, reversible encryption

Threaded processing for responsive GUI, even with large images

Real-time image preview using CTkImage

CustomTkinter modern UI with rounded buttons and frames

Supports PNG, JPG, JPEG formats


Installation

Clone the repository:

git clone https://github.com/yourusername/image-encryption-tool.git
cd image-encryption-tool


Install required packages:

python -m pip install customtkinter pillow

Usage

Run the application:

python image_encryption_tool.py


Load an image using the "Load Image" button.

Enter an encryption key (0–255).

Click Encrypt Image or Decrypt Image.

Preview will appear, and you can save the processed image to your computer.

Note: Use the same key for encryption and decryption to recover the original image.

How It Works

The image is converted into RGB pixels.

Each pixel is XORed with the user-provided key.

Pixel positions are shuffled based on the key.

The encrypted image is saved and previewed.

Decryption reverses the shuffling and XOR operation using the same key.

Supported Image Formats

PNG

JPG / JPEG

Dependencies

Python 3.x

CustomTkinter

Pillow

Future Improvements

Drag & drop image support

Progress bar for large images

Dark/light mode toggle

Copy/save preview functionality

License

This project is licensed under the MIT License – see the LICENSE
 file for details.
