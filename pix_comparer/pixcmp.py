from PIL import Image, ImageChops


def resize_to_match(img1, img2):
    size = (max(img1.width, img2.width), max(img1.height, img2.height))
    return img1.resize(size), img2.resize(size)


def compare_images(img1_path, img2_path, save_path, side_path):
    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")

    if img1.size != img2.size:
        img1, img2 = resize_to_match(img1, img2)

    # RGB 255,0,0 czerwony kolor
    highlight = Image.new("RGB", img1.size)
    p1, p2, ph = img1.load(), img2.load(), highlight.load()
    for y in range(img1.height):
        for x in range(img1.width):
            ph[x, y] = (255, 0, 0) if p1[x, y] != p2[x, y] else p1[x, y]
    highlight.save(save_path)

    # Side-by-side image
    combined = Image.new("RGB", (img1.width * 3, img1.height))
    combined.paste(img1, (0, 0))
    combined.paste(img2, (img1.width, 0))
    combined.paste(highlight, (img1.width * 2, 0))
    combined.save(side_path)



img1 = "C:/Users/raf88/Desktop/pix-comparer/temp_img/img1.JPG"
img2 = "C:/Users/raf88/Desktop/pix-comparer/temp_img/img2.JPG"
save = "C:/Users/raf88/Desktop/pix-comparer/temp_img/diff.JPG"
side = "C:/Users/raf88/Desktop/pix-comparer/temp_img/diff2.JPG"
compare_images(img1, img2, save, side)






