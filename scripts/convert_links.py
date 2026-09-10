# -*- coding: utf-8 -*-
"""将站点卡片从 onclick=window.open 统一为真实 <a href> 链接。"""
import re

path = 'cn/index.html'
s = open(path, encoding='utf-8').read()

# 匹配整个卡片块：外层 div(带 onclick) + 内容 + 3 个连续闭合 </div>
card_re = re.compile(
    r'(<div class="xe-widget xe-conversations box2 label-info" onclick="window\.open\(\'([^\']*)\', \'_blank\'\)" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="[^"]*">)'
    r'(.*?)'
    r'(</div>\s*</div>\s*</div>)',
    re.S
)

count = 0

def repl(m):
    global count
    open_tag, url, content, close = m.group(1), m.group(2), m.group(3), m.group(4)
    count += 1

    # 1) 外层 div -> a，去掉 onclick，加 href/target/rel
    new_open = open_tag.replace(
        "onclick=\"window.open('%s', '_blank')\"" % url,
        'href="%s" target="_blank" rel="noopener"' % url
    ).replace('<div class="xe-widget', '<a class="xe-widget')

    # 2) 内层两个 <a> -> <span>（避免嵌套锚点）
    content = content.replace('<a class="xe-user-img">', '<span class="xe-user-img">')
    content = content.replace('<a href="#" class="xe-user-name overflowClip_1">',
                              '<span class="xe-user-name overflowClip_1">')
    # 内容中仅剩的 </a> 都是这两个内层锚点的闭合
    content = content.replace('</a>', '</span>')

    # 3) 卡片闭合：最后一个 </div> -> </a>
    idx = close.rfind('</div>')
    new_close = close[:idx] + '</a>' + close[idx + len('</div>'):]

    return new_open + content + new_close

new_s, n = card_re.subn(repl, s)
print('替换卡片数:', n)

# 校验：不应再残留 onclick=window.open
leftover = re.findall(r"onclick=\"window\.open", new_s)
print('残留 onclick window.open:', len(leftover))

# 校验：不应再有嵌套 <a>（<a ...> 内包含 <a）
nested = re.findall(r'<a[^>]*>[^<]*<a', new_s)
print('疑似嵌套 <a>:', len(nested))

open(path, 'w', encoding='utf-8').write(new_s)
print('写入完成')
