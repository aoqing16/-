def 更新文件 (链接,图片路径,标题):
    with open(r"C:\Users\ZhuanZ1\Desktop\新建 文本文档.txt", 'r', encoding='utf-8') as a:
        b = a.read()
        d = f'''
        <a href="{链接}" class="video-card">
            <div class="image-container">
                <img src="{图片路径}">
                <div class="stats-overlay">
                </div>
            </div>
            <div class="video-title">{标题}</div>
        </a>      
                        '''

        c = b.replace('唯一标识符', d + '\n唯一标识符')
    if 链接 in b:
        print('该视频已存在')
    else:
        with open(r"C:\Users\ZhuanZ1\Desktop\新建 文本文档.txt", 'w', encoding='utf-8') as a:
            a.write(c)