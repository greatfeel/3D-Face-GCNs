import argparse
from PIL import Image
import numpy as np

def highlight_ratio(path, threshold=200):
    """Compute the proportion of pixels brighter than threshold."""
    img = Image.open(path).convert('L')
    arr = np.array(img)
    ratio = np.mean(arr > threshold)
    return ratio

def main():
    parser = argparse.ArgumentParser(description="Compare highlight pixel ratios of two images.")
    parser.add_argument('image1', help='Path to first image')
    parser.add_argument('image2', help='Path to second image')
    parser.add_argument('--threshold', type=int, default=200,
                        help='Brightness threshold (0-255) to consider a pixel highlighted')
    args = parser.parse_args()

    r1 = highlight_ratio(args.image1, args.threshold)
    r2 = highlight_ratio(args.image2, args.threshold)

    print(f"{args.image1} highlight ratio: {r1:.4f}")
    print(f"{args.image2} highlight ratio: {r2:.4f}")
    if r2 != 0:
        print(f"Ratio (image1 / image2): {r1 / r2:.4f}")
    print(f"Difference (image1 - image2): {r1 - r2:.4f}")

if __name__ == '__main__':
    main()
