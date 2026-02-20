from PIL import Image, ImageDraw, ImageFont
import os

def create_image():
    width = 1920
    height = 1080
    color = (13, 110, 253) # Bootstrap primary color
    
    img = Image.new('RGB', (width, height), color=color)
    d = ImageDraw.Draw(img)
    
    # Try to load a font, otherwise use default
    try:
        font = ImageFont.truetype("arial.ttf", 100)
    except IOError:
        font = ImageFont.load_default()
        
    text = "Hero Background"
    # Basic centering logic (approximate if font usage is tricky without specific font file)
    text_width = d.textlength(text, font=font)
    x = (width - text_width) / 2
    y = height / 2
    
    d.text((x, y), text, fill=(255, 255, 255), font=font)
    
    output_path = os.path.join("static", "img", "hero-bg.jpg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    create_image()
