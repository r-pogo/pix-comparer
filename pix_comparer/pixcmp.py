from PIL import Image, ImageChops


def compare_images(img1_path, img2_path, save_path):
    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")

    diff = ImageChops.difference(img1, img2)
    diff_pixels = sum(1 for px in diff.getdata() if px != (0,0,0))

    # RGB 255,0,0 czerwony kolor
    highlight = Image.new("RGB", img1.size)
    p1, p2, ph = img1.load(), img2.load(), highlight.load()
    for y in range(img1.height):
        for x in range(img1.width):
            ph[x, y] = (255, 0, 0) if p1[x, y] != p2[x, y] else p1[x, y]
    highlight.save(save_path)

    print(f"Found {diff_pixels} differing pixels.")

img1 = "C:/Users/raf88/Desktop/pix-comparer/temp_img/img1.JPG"
img2 = "C:/Users/raf88/Desktop/pix-comparer/temp_img/img2.JPG"
save = "C:/Users/raf88/Desktop/pix-comparer/temp_img"
compare_images(img1, img2, save)






