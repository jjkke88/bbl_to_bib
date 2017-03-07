
#coding=utf-8
import re
title_reg = re.compile('\{(\S*)\}')
emph_reg = re.compile('\\emph\{(.*)\}')
file = open('text.txt');
source = file.readlines()
file.close()
print source

ref = []
content = []
for index in xrange(len(source)):
    if index%2 == 0:
        ref.append(source[index])
    else:
        content.append(source[index])
print len(ref)
print len(content)
print ref
print content

def get_emph_index(content_list):
    for index in xrange(len(content_list)):
        result = emph_reg.findall(content_list[index])
        if len(result) > 0:
            return True, index, result[0]
    return False, 0, ''
def combine_string(content, start_index, end_index):
    str = ''
    for index in xrange(start_index, end_index, 1):
        str += content[index]
    return str
article = []
for index in xrange(len(ref)):
    title_undeal = ref[index]
    result = title_reg.findall(title_undeal)
    if len(result) > 0:
        ref_title = result[0]
        current_content = content[index].split(',')
        flag, emph_index, journal = get_emph_index(current_content)
        if flag:
            title = current_content[emph_index - 1]
            author = combine_string(current_content, 0, emph_index - 1)
            year = current_content[len(current_content)-1].strip('\n')
            volume = combine_string(current_content, emph_index +1, len(current_content)-1)
            article.append(dict(ref=ref_title, title=title, author=author, year=year, volume=volume, journal=journal))
print len(article)
print article

def get_write_content(dict_content):
    str_format = "@article{%s,\n author={%s},\n title={%s},\n journal={%s},\n volume={%s},\n year={%s}\n}\n"
    return str_format%(dict_content["ref"], dict_content["author"], dict_content["title"], dict_content["journal"], dict_content["volume"], dict_content["year"])
file = open('queto.bib', 'w')
for dict_content in article:
    str = get_write_content(dict_content)
    file.write(str)
file.close()