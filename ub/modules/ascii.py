import PIL
from ub.utils import admin_cmd
from ub import CMD_HELP
# ascii characters used to build the output text
import pygments, os, asyncio
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter
from ub.utils import admin_cmd
from ub import bot
from ub import bot as borg
@bot.on(admin_cmd(pattern="ascii ?(.*)", outgoing=True))
# DONOT KANG by @THE_B_LACK_HAT & Sh1vam
async def __(event):
    gltg=event.text
    n=int(gltg[7:])
    path = "jvs"
    await event.delete()
    reply = await event.get_reply_message()
        
    down = await borg.download_media(reply.media, path)


    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    # resize image according to a new width
    def resize_image(image, new_width=n):
        width, height = image.size
        #reference_length = max(width, height)
        #ratio = 512 / reference_length
        ratio = height/width
        new_height = int(new_width * ratio)

        return image.resize((new_width,new_height))

    # convert each pixel to grayscale
    def grayify(image):
        return image.convert("L")
        
    # convert pixels to a string of ascii characters
    def pixels_to_ascii(image):
        pixels = image.getdata()
        return "".join([ASCII_CHARS[pixel//25] for pixel in pixels])    

    def main(new_width=n):
        # attempt to open image from user-input
        d = down
        try:
            image = PIL.Image.open(d)
        except:
            pass

        # convert image to ascii    
        new_image_data = pixels_to_ascii(grayify(resize_image(image)))

        # format
        pixel_count = len(new_image_data)
        ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

        # save result to "ascii_image.txt"
        with open("ascii_image.txt", "w") as f:
            f.write(ascii_image)
        with open("ascii_image.txt", 'r') as s:
            c = s.read()
        pygments.highlight(f"{c}", Python3Lexer(), ImageFormatter(font_name="DejaVu Sans Mono", line_numbers=False), "ascii.png")
        imgs="ascii.png"
        shvm=PIL.Image.open(imgs)
        sh1,vam = image.size
        img=shvm.resize((int(sh1),int(vam)))
        img.save("asci.png", format="PNG", optimize=True)
    main()
   
    await event.client.send_file(event.chat_id, "asci.png", force_document=False, reply_to=event.reply_to_msg_id)
    os.remove('ascii.png')
    os.remove('asci.png')
    os.remove('ascii_image.txt')
    os.remove(down)
    # run program

