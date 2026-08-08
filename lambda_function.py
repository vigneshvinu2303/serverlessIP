from PIL import Image

def lambda_handler(event, context):

    image = Image.new("RGB", (300, 300), "blue")

    print("Pillow is working!")

    return {
        "statusCode": 200,
        "body": "Pillow successfully loaded"
    }