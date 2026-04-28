import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image):
    results = reader.readtext(image)
    return " ".join([res[1] for res in results])