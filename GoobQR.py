import qrcode
import argparse
import sys
from pyfiglet import Figlet
from termcolor import colored

def create_qr_code(url, output_file=None):
    """Generate a QR code from a URL and optionally save it to a file."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    if output_file:
        img.save(output_file)
        print(f"QR code saved to {output_file}")
    else:
        img.show()
        print("QR code displayed")

def main():
    figlet = Figlet(font='slant')
    large_text = figlet.renderText('Brought to you by:')
    print(colored(large_text, 'green'))

    ascii_art = """
   █████████                    █████      █████████                   
  ███░░░░░███                  ░░███      ███░░░░░███                  
 ███     ░░░   ██████   ██████  ░███████ ░███    ░░░   ██████   ██████ 
░███          ███░░███ ███░░███ ░███░░███░░█████████  ███░░███ ███░░███
░███    █████░███ ░███░███ ░███ ░███ ░███ ░░░░░░░░███░███████ ░███ ░░░ 
░░███  ░░███ ░███ ░███░███ ░███ ░███ ░███ ███    ░███░███░░░  ░███  ███
 ░░█████████ ░░██████ ░░██████  ████████ ░░█████████ ░░██████ ░░██████ 
  ░░░░░░░░░   ░░░░░░   ░░░░░░  ░░░░░░░░   ░░░░░░░░░   ░░░░░░   ░░░░░░  
    



Shoutout to my Goobs on X(Twitter) @Mad_PicSnaps @Psy_ware @hornruna_
    """
    print(colored(ascii_art, 'green'))
    
    parser = argparse.ArgumentParser(
        description="Enter a URL to generate a QR code! :DDD",
        epilog="HOW TO USE:\n"
               "  python3 GoobQR.py https://youtube.com/RICKROLLEDDDD -o myqrcode.png\n"
               
    )
    parser.add_argument("url", help="URL to encode in the QR code")
    parser.add_argument("-o", "--output", help="Output file to save the QR code (e.g., qr.png)")
    
    args = parser.parse_args()
    
    try:
        create_qr_code(args.url, args.output)
    except Exception as e:
        print(f"Error generating QR code: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()