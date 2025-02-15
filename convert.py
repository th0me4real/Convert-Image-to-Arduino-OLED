from PIL import Image
import numpy as np

# 載入圖片並轉換為黑白
img = Image.open('1122.jpg').convert('1') #仔入位置請自行置換

img = img.resize((128, 64)) # 縮放圖片至128x64 可依OLED尺寸調整

# 轉換圖片為numpy array
img_array = np.array(img)

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
