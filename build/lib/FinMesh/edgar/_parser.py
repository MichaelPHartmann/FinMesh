def strip_file_to_text(filein):
    begin_tag = '<'
    end_tag = '>'
    state = False
    filename = filein.replace('.txt','text_only.txt')
    with open(filein, 'r') as f, open(filename, 'a') as nf:
        lines = f.readlines()
        for line in lines:
            line_to_write = ''
            for a in line:
                if a == begin_tag:
                    state = False
                    pass
                if a == end_tag:
                    state = True
                    pass
                elif state = True:
                    line_to_write += a
            nf.write(line_to_write)
