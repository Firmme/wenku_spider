# -*- coding:utf-8 -*-


class HtmlOutput(object):
    """
    将程序爬取的数据写入字典,再遍历输出到文件
    """

    def __init__(self):
        self.datas = {}

    def collect_data(self, data):
        if data is None:
            return
        self.datas = dict(self.datas, **data)  # 合并数据

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf16')  # python str对象默认unicode编码即为utf-16
        fout.write('<html>')
        # 网页编码需要和输出格式一致
        fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')

        fout.write('<body>')
        fout.write('<table>')

        for key, value in self.datas.items():
            fout.write('<tr>')
            fout.write('<td><a href=\'%s\'>%s</a></td>' % (key,key))
            fout.write('<td>%s</td>' % value)  # 如果输出文件乱码则应加上encode='编码格式'
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
