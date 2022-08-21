from PIL import Image, ImageOps
ASCII_CHARACTER = ["@","#","S","%","?","*","+",";",":",",","."] #character used for the ascii art ordered by how much white the caracter is ('@' is the whitest, '.' is the least white)

def scale_image(old_img, new_width=150):    #scale the image so that the ascii art will be fully wisible on screen
    w,h  = old_img.size #get old width and height
    ratio = h/w / 1.65
    new_img = old_img.resize((new_width,int(new_width*ratio)))  #resize the image preserving as much as possible the height-width ratio
    return new_img

def main(new_width=150):
    print("Insert the image path")
    try:
        image_path = input()
        myimage = Image.open(image_path)    #open image
    except Exception as e:
        print("Error opening image")

    gray_image = ImageOps.grayscale(myimage)    #convert image to grayscale

    scaled_image = scale_image(gray_image,new_width=new_width)  #scale image

    pixels = scaled_image.getdata() #get every pixel from scaled image

    art = "".join([ASCII_CHARACTER[pixel//25] for pixel in pixels]) #convert each pixel to a character in the ASCII_CHARACTER list based on how much white the pixel is

    ascii_art = "\n".join(art[i:(i+new_width)] for i in range (0,len(art),new_width)) #insert \n character for better rappresentation

    with open("ascii-art.txt","w") as o:    #save ascii art
        o.write(ascii_art)

if __name__ == "__main__":
    main()
