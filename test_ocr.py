from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
# ocr = PaddleOCR(use_angle_cls=True, lang="ch", page_num=2)

# det_model_dir 检测模型，用于确定文本方位
# rec_model_dir 识别模型，用于识别文本内容
# cls_model_dir  文本方向分类模型，支持0和180度文本
# use_angle_cls
ocr = PaddleOCR(det_model_dir='./det_model', rec_model_dir='./rec_model',
                cls_model_dir='./cls_model', use_angle_cls=True)
img_path = './2.png'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# 显示结果
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')