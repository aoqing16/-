def write_card_to_html(img_path, title, link):
    import re
    # 构建要插入的 HTML 片段
    new_card = f"""
    <a href="{link}" class="video-card">
        <div class="image-container">
            <img src="{img_path}">
            <div class="stats-overlay">
            </div>
        </div>
        <div class="video-title">{title}</div>
    </a>
    """

    # 读取并替换
    with open('/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 将新卡片插入到锚点之前，并保留锚点以便下次继续插入
    new_content = content.replace('<!--唯一标识符-->', f'{new_card}\n<!--唯一标识符-->')

    with open('/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
# write_card_to_html("path/to/pic.jpg", "我是动态写入的标题", "https://xxx.com")