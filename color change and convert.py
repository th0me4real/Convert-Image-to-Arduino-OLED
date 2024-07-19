from PIL import Image, ImageOps
import numpy as np
# 載入圖片
img = Image.open('未命名.jpg')

# 反轉圖片顏色
inverted_image = ImageOps.invert(img.convert('RGB'))

# 將反轉後的圖片轉換為黑白並縮放至128x64
inverted_image_bw = inverted_image.convert('1').resize((128, 64))

# 轉換圖片為numpy array
img_array = np.array(inverted_image_bw)

# 生成二進制序列
bitmap = []
for byte in range(0, 1024):  # 128 * 64 / 8 = 1024
    byte_data = 0
    for bit in range(0, 8):
        x = byte % 128
        y = (byte // 128) * 8 + bit
        if img_array[y, x] == 0:  # 黑色像素
            byte_data |= (1 << bit)
    bitmap.append(byte_data)

# 輸出二進制序列
hex_output = []
for i, byte in enumerate(bitmap):
    if i % 16 == 0:
        hex_output.append("\n")
    hex_output.append(f'0x{byte:02X}, ')

# 將生成的16進制序列輸出為字符串
hex_string = ''.join(hex_output)
print(hex_string)
