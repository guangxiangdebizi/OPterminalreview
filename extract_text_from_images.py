"""
信息安全图片文字提取脚本
使用EasyOCR从图片中提取文字内容，生成统一的markdown文档
"""

import os

try:
    import easyocr
except ImportError:
    print("正在安装 EasyOCR...")
    os.system("pip install easyocr -i https://pypi.tuna.tsinghua.edu.cn/simple")
    import easyocr

def extract_text_from_images(image_folder, output_file="信息安全_图片提取内容.md"):
    """从图片文件夹中提取文字并生成markdown文档"""
    
    # 初始化OCR
    print("正在初始化OCR引擎(首次使用会下载模型，请耐心等待)...")
    reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
    
    # 获取所有图片文件
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg')])
    print(f"找到 {len(image_files)} 张图片\n")
    
    all_content = []
    all_content.append("# 信息安全 - 图片提取内容\n\n")
    all_content.append(f"*提取时间: 2026-01-03*\n\n")
    all_content.append(f"*共 {len(image_files)} 张图片*\n\n")
    all_content.append("---\n\n")
    
    # 处理每张图片
    for idx, image_file in enumerate(image_files, 1):
        image_path = os.path.join(image_folder, image_file)
        print(f"正在处理 [{idx}/{len(image_files)}]: {image_file}")
        
        try:
            # OCR识别
            result = reader.readtext(image_path, detail=0, paragraph=True)
            
            if result:
                all_content.append(f"## 图片 {idx}: {image_file}\n\n")
                
                # 提取文字内容
                content_text = "\n\n".join(result)
                all_content.append(f"{content_text}\n\n")
                all_content.append("---\n\n")
            else:
                all_content.append(f"## 图片 {idx}: {image_file}\n\n")
                all_content.append("*（未识别到文字）*\n\n")
                all_content.append("---\n\n")
                
        except Exception as e:
            print(f"   ⚠️  处理出错: {str(e)}")
            all_content.append(f"## 图片 {idx}: {image_file}\n\n")
            all_content.append(f"*（处理出错: {str(e)}）*\n\n")
            all_content.append("---\n\n")
    
    # 保存文档
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(all_content)
    
    print(f"\n{'='*60}")
    print(f"✓ 提取完成！")
    print(f"✓ 文件已保存: {output_file}")
    print(f"{'='*60}")
    
    return output_file

def main():
    """主函数"""
    print("="*60)
    print("信息安全图片文字提取工具")
    print("="*60)
    print()
    
    image_folder = "信息安全图片"
    output_file = "信息安全_图片提取内容.md"
    
    if not os.path.exists(image_folder):
        print(f"错误: 找不到图片文件夹 '{image_folder}'")
        return
    
    # 提取文字
    extract_text_from_images(image_folder, output_file)

if __name__ == "__main__":
    main()
