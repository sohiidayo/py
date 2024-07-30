from PIL import Image  
  
def create_rgba_image(r_image=None, g_image=None, b_image=None, a_image=None):  
    # 定义默认灰度值  
    default_gray_value = 0  
  
    # 如果图像为None或数字，则创建一个全为指定灰度值的图像  
    def create_or_set_image(image, size, gray_value):  
        if image is None:  
            gray_value = default_gray_value if gray_value is None else gray_value  
            image = Image.new('L', size, gray_value)  
        elif isinstance(image, int):  
            image = Image.new('L', size, image)  
        return image  
  
    # 检查并获取第一个非None图像的大小  
    sizes = [(r_image, 'R'), (g_image, 'G'), (b_image, 'B'), (a_image, 'A')]  
    for img, channel in sizes:  
        if img is not None and not isinstance(img, int):  
            size = img.size  
            break  
    else:  
        raise ValueError("All input images are None or integers without a specified size.")  
  
    # 创建或设置每个通道的图像  
    r_img = create_or_set_image(r_image, size, None)  
    g_img = create_or_set_image(g_image, size, None)  
    b_img = create_or_set_image(b_image, size, None)  
    a_img = create_or_set_image(a_image, size, 255)  # 默认情况下，Alpha通道设为不透明  
  
    # 创建一个新的RGBA图像  
    rgba_img = Image.new('RGBA', size)  
  
    # 将每个通道的数据复制到RGBA图像的相应通道  
    rgba_img.putdata(list(zip(r_img.getdata(), g_img.getdata(), b_img.getdata(), a_img.getdata())))  
  
    return rgba_img  
  
# 示例用法  
# 假设有4个图像文件或None/数字  
# r_img = Image.open('r_channel.png')  
# g_img = Image.open('g_channel.png')  
# b_img = Image.open('b_channel.png')  
# a_img = Image.open('a_channel.png')  
  
# 使用None和数字作为示例  
r_img = None  # 所有R通道像素为0  
g_img = 128    # 所有G通道像素为128  
b_img = Image.open('b_channel.png')  # 假设有这样一个文件  
a_img = 255    # 所有A通道像素为255（不透明）  
  
result_img = create_rgba_image(r_img, g_img, b_img, a_img)  
result_img.show()  # 显示结果图像  
# 也可以保存结果图像  
# result_img.save('result.png')