# CODSOFT AI INTERNSHIP
# TASK 3: IMAGE CAPTIONING
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

print("=" * 50)
print("        CODSOFT AI INTERNSHIP")
print("           IMAGE CAPTIONING")
print("=" * 50)

# Load the pre-trained image captioning model
print("Loading AI model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("Model loaded successfully!")

# Enter image path
image_path = input("Enter image path: ")

try:
    image = Image.open(image_path).convert("RGB")

    print("\nImage loaded successfully!")
    print("Generating caption...")

    # Process image
    inputs = processor(image, return_tensors="pt")

    # Generate caption
    output = model.generate(**inputs, max_new_tokens=30)

    # Convert output to text
    caption = processor.decode(output[0], skip_special_tokens=True)

    print("\n" + "=" * 50)
    print("GENERATED CAPTION")
    print("=" * 50)
    print(caption)
    print("=" * 50)

except FileNotFoundError:
    print("Error: Image file not found.")

except Exception as e:
    print("Error:", e)