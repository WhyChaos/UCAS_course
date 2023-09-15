from bs4 import BeautifulSoup
import chat

def parse(html, is_test, sep):

    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'lxml')

    # 找到表格元素
    table = soup.find('table', class_='table')

    # 找到表头（thead）和表体（tbody）
    thead = table.find('thead')
    tbody = table.find('tbody')

    # 提取表头中的列名
    columns = [th.text.strip() for th in thead.find_all('th')]

    # 提取表格数据
    data = []
    for row in tbody.find_all('tr'):
        row_data = [td.text.strip() for td in row.find_all('td')]
        data.append(row_data)

    # 打印列名和数据
    print(columns)
    print(data)
    if not is_test:
        message = ''
        for row in data:
            if int(row[7])!=0 and int(row[8]) >= int(row[7]):
                print(f'关注的{row[4]}({row[3]}),当前{row[8]}/{row[7]},无剩余容量')
                message += f'关注的{row[4]}({row[3]}),当前{row[8]}/{row[7]},无剩余容量'
                # chat.send(f'关注的{row[4]}({row[3]}),当前{row[8]}/{row[7]},无剩余容量')
            else:
                print(f'*关注的{row[4]}({row[3]}),当前{row[8]}/{row[7]},有剩余容量，请注意抢课！！！！！！！！')
                # chat.send(f'关注的{row[4]}({row[3]}),当前{row[8]}/{row[7]},有剩余容量，请注意抢课！！！！！！！！')
                message += f'*关注的{row[4]}({row[3]}),当前{row[8]}/{row[7]},有剩余容量，请注意抢课！！！！！！！！'
        return message
    if len(data) == 1:
        if sep:
            sep.courseCode = data[0][3]
            sep.courseName = data[0][4]
        return '成功'
    elif len(data) == 0:
        return '不存在该门课，添加失败'
    else:
        return '存在多门课，添加失败'
    


def is_login(html):
    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'html.parser')
    buttons = soup.find_all('button')
    for button in buttons:
        if '跳转' in button.get_text():
            return True
    return False