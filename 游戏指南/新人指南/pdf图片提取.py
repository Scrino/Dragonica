# 提取 当前目录下 PDF 中的图片
import fitz  # PyMuPDF

def extract_images_from_pdf(pdf_path, output_folder="extracted_images"):
    import os
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        
        for img_index, img_info in enumerate(image_list):
            xref = img_info[0]
            base_image = doc.extract_image(xref)
            image_data = base_image["image"]
            
            # 保存图片（PNG 或 JPG）
            img_ext = "png"  # 或 "jpg"
            img_path = os.path.join(output_folder, f"page{page_num + 1}_img{img_index + 1}.{img_ext}")
            with open(img_path, "wb") as img_file:
                img_file.write(image_data)
    
    print(f"✅ 图片已提取到 {output_folder}/ 目录！")

import glob
pdf_files = glob.glob("*.pdf")  # 当前目录所有 PDF
for pdf in pdf_files:
    extract_images_from_pdf(pdf)

# 脚本执行命令 python extract_pdf_images.py