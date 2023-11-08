class Tag(object):

    def __init__(self, tag, content):
        self.start_tag = '<{}>'.format(tag)
        self.end_tag = '</{}>'.format(tag)
        self.content = content

    def __str__(self):
        return "{0.start_tag}{0.content}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE html', '')
        self.end_tag = ''


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.content = str(self._title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')
        self._body_contents = []

    def add_tag(self, tag, content):
        new_tag = Tag(tag, content)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag_in in self._body_contents:
            self.content += str(tag_in) + "\n"

        super().display(file=file)


class HtmlDoc(object):

    def __init__(self, _doc_type, _head, _body):
        self._doc_type = _doc_type
        self._head = _head
        self._body = _body

    def add_tag(self, tag, content):
        self._body.add_tag(tag, content)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    body = Body()
    body.add_tag('h1', "How are <strong> you ?  </strong>")
    body.add_tag('h2', "The beautiful day")
    body.add_tag('p', "Lorem ipsum ")
    body.add_tag('button', "Click me!")
    doctype = DocType()
    header = Head()
    my_page = HtmlDoc(doctype, header, body)

    with open('web.html', 'w') as html_doc:
        my_page.display(file=html_doc)
