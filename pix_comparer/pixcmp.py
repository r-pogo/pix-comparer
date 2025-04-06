import argparse

from PIL import Image


def resize_to_match(img1, img2):
    size = (max(img1.width, img2.width), max(img1.height, img2.height))
    return img1.resize(size), img2.resize(size)


def compare_images(img1_path, img2_path, save_path, side_path, tolerance ):
    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")

    if img1.size != img2.size:
        img1, img2 = resize_to_match(img1, img2)

    highlight = Image.new("RGB", img1.size)
    p1, p2, ph = img1.load(), img2.load(), highlight.load()

    for y in range(img1.height):
        for x in range(img1.width):
            r1, g1, b1 = p1[x, y]
            r2, g2, b2 = p2[x, y]
            # Calculate diff for each color channel
            diff_r = abs(r1 - r2)
            diff_g = abs(g1 - g2)
            diff_b = abs(b1 - b2)
            # RGB 255,0,0 czerwony kolor
            if diff_r > tolerance or diff_g > tolerance or diff_b > tolerance:
                ph[x, y] = (255, 0, 0)
            else:
                ph[x, y] = p1[x, y]

    highlight.save(save_path)

    # Side-by-side image
    """
    +--------+--------+-----------+
    | img1   | img2   | highlight |
    +--------+--------+-----------+
    """
    combined = Image.new("RGB", (img1.width * 3, img1.height))
    combined.paste(img1, (0, 0))
    combined.paste(img2, (img1.width, 0))
    combined.paste(highlight, (img1.width * 2, 0))
    combined.save(side_path)


def main():
    parser = argparse.ArgumentParser(
        description="PixComparer: Compare two images pixel by pixel.")
    parser.add_argument("img1", help="path for first image")
    parser.add_argument("img2", help="path for second image")
    parser.add_argument("--diff", default="diff.png", help='Path to save the diff image (optional, defaults to "diff.png")')
    parser.add_argument("--side", default="side_by_side.png", help='Path to save the side-by-side comparison (optional, defaults to "side_by_side.png")')
    parser.add_argument("--tolerance", type=int, default=110,
                        help="Tolerance threshold for pixel differences")

    args = parser.parse_args()
    compare_images(args.img1, args.img2, args.diff, args.side, args.tolerance)


if __name__ == "__main__":
    main()
