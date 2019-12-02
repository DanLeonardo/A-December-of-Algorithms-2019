def csv_to_html(file_str):
    tag_stack = []
    try:
        with open(file_str, 'r') as file:
            tag_stack.append('<table>')

            # Read header
            header_values = format_csv_line(file.readline())
            header_tags = read_csv_header(header_values)
            tag_stack.append(header_tags)

            # Read lines
            for line in file.readlines():
                line_values = format_csv_line(line)
                line_tags = read_csv_line(line_values)
                tag_stack.append(line_tags)

            tag_stack.append('</table>')
    except Exception as e:
        print(type(e).__name__)

    return tag_stack

def read_csv_header(header_values):
    header_tags = '<tr>'
    for value in header_values:
        header_tags += '<th>'
        header_tags += value
        header_tags += '</th>'
    header_tags += '</tr>'

    return header_tags

def read_csv_line(line_values):
    line_tags = '<tr>'
    for value in line_values:
        line_tags += '<td>'
        line_tags += value
        line_tags += '</td>'
    line_tags += '</tr>'

    return line_tags

def format_csv_line(line):
    values = line.split(',')

    for i, value in enumerate(values):
        value = value.strip()
        value = value.strip('\"')
        values[i] = value

    return values

def write_tags_to_file(file_str, tag_stack):
    indent_offset = 0
    # Tags which will increase the indent AFTER they are written
    indent_tags = ['<html>', '<head>', '<body>', '<table>']
    # Tags which will decrease the indent BEFORE they are written
    unindent_tags = ['</html>', '</head>', '</body>', '</table>']

    try:
        with open(file_str, 'w') as file:
            for tag in tag_stack:
                # Control unindents
                if tag in unindent_tags:
                    indent_offset -= 1

                # Write indents
                for i in range(0, indent_offset):
                    file.write('\t')

                # Write tags
                file.write(tag)
                file.write('\n')

                # Control indents
                if tag in indent_tags:
                    indent_offset += 1
    except:
        print('Caught exception')

if __name__ == '__main__':
    data_table = csv_to_html('../src/res/csv_to_html_res.csv')
    tag_stack = []

    tag_stack.append('<!DOCTYPE html>')
    tag_stack.append('<html>')

    # Optional CSS
    css_tags = ['<head>', '<link rel="stylesheet" href="./style.css">', '</head>']
    tag_stack.extend(css_tags)

    tag_stack.append('<body>')
    tag_stack.extend(data_table)
    tag_stack.append('</body>')
    tag_stack.append('</html>')

    write_tags_to_file('./tags.html', tag_stack)
