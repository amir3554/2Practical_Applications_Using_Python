def get_text(filename):
    import docx
    The_file =  docx.Document(filename)
    paragraphs = []
    for para in The_file.paragraphs:
        paragraphs.append(para.text)
    return '\n'.join(paragraphs)

