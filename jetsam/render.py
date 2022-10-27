
import re

import bbcode as bbc

from ._samoji import samoji as _samoji_list

def bbcode():
    parser = bbc.Parser(url_template='<a rel="nofollow" referrerpolicy="same-origin" href="{href}" target="_blank">{text}</a>')

    def render_email(name, value, args, parent, context):
        text = value
        if 'email' in args:
            target = args['email']
        else:
            target = text
        
        return f'<a href="email:{target}">{text}</a>'
    
    def render_img(name, value, args, parent, context):
        text = value
        if 'img' in args:
            target = args['img']
        else:
            target = text
            text = 'image'
        
        return f'<img src="{target}" alt="{text}"/>'
    
    def render_timg(name, value, args, parent, context):
        text = value
        if 'timg' in args:
            target = args['timg']
        else:
            target = text
            text = 'image'
        
        return f'<img class="timg" src="{target}" alt="{text}"/>'
    
    def render_video(name, value, args, parent, context):
        # this is going to require extra magic, hooray.
        target = value
        if 'type' in args:
            # this will perform magic eventually
            pass

        return f'<video src="{target}"/>'
    
    def render_code(name, value, args, parent, context):
        # TODO - use Pygments for syntax highlighting
        if 'code' in args:
            pass

        return f'<pre><code>{value}</code></pre>'
    
    parser.add_formatter('email', render_email, strip=True, escape_html=True)
    parser.add_formatter('img', render_img, strip=True, escape_html=True, render_embedded=False)
    parser.add_formatter('timg', render_timg, strip=True, escape_html=True)
    parser.add_formatter('video', render_video, strip=True, escape_html=True, render_embedded=False)
    parser.add_simple_formatter('super', '<sup>%(value)</sup>')
    parser.add_simple_formatter('fixed', '<tt>%(value)</sup>')
    parser.add_simple_formatter('spoiler', '<span class="spoiler">%(value)</span>')
    parser.add_simple_formatter('pre', '<pre>%(value)</pre>', escape_html=True, strip=False, transform_newlines=False)
    parser.add_formatter('code', render_code, strip=False, escape_html=True, render_embedded=False)

    return parser

_samoji = re.compile(r'(?::([a-z0-9]+):|(\:[()]))', flags=re.IGNORECASE)
def samoji(text):
    samojis = _samoji.findall(text)

    for s in samoji:
        if s in _samoji_list.keys():
            image = _samoji_list[s]
            s = f':{s}:' if s not in (':(', ':)') else s
            text.replace(s, f'<img src="/emoji/{image}"/>')
    
    return text
