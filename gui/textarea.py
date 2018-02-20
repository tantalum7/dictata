
from PyQt5 import QtWidgets, QtGui, QtCore
from bs4 import BeautifulSoup


class TextArea:

    BOLD_WEIGHT = QtGui.QFont.Bold
    NORMAL_WEIGHT = QtGui.QFont.Normal
    HEADING_SIZE = 14
    HEADING_WEIGHT = BOLD_WEIGHT
    HEADING_UNDERLINE = True
    NORMAL_SIZE = 12
    NORMAL_UNDERLINE = False

    def __init__(self, qTextEdit):
        self._qtextedit = qTextEdit
        self._html_edit = False
        self.init_formats()


    def init_formats(self):
        pass

    def load_html(self, html):
        self.html = html
        self.soup = BeautifulSoup(self.html, "html.parser")

    def toggle_selection_tag(self, tag):
        start, end = self._cursor_block_coords()
        pass

    def _cursor(self):
        return self._qtextedit.textCursor()

    def _cursor_soup(self):
        return self.soup.find_all("p")[self._cursor().block().blockNumber()]

    def _cursor_block_coords(self):
        end = self._cursor().positionInBlock()
        start = end - (self._cursor().position() - self._cursor().anchor())
        return start, end

    def _trim_selection(self):
        text_selection = self._qtextedit.textCursor().selectedText()
        start = self._qtextedit.textCursor().anchor()
        start += len(text_selection) - len(text_selection.lstrip())
        self._qtextedit.textCursor().setPosition(start)

    def toggle_selected_bold(self):
        self.real_html = self._qtextedit.document().toHtml()
        self.soup = BeautifulSoup(self.real_html, "html.parser")
        blk = self._cursor().block().blockNumber()
        a = self.soup.body.find_all("p")[blk]
        pos = self._cursor().positionInBlock()
        start, end = self._cursor_block_coords()

        original_string = a.string
        a.string = original_string[0:start]
        new_span = self.soup.new_tag("b")
        new_span.string = original_string[start:end]
        a.append(new_span)
        a.append(original_string[end:])
        print(self.soup.prettify())
        self._qtextedit.document().setHtml(str(self.soup))

        pass



    def old_toggle_selected_bold(self):
        text_format = self._qtextedit.textCursor().blockCharFormat()
        text_format.setFontWeight(self.BOLD_WEIGHT if self._qtextedit.fontWeight() < self.BOLD_WEIGHT
                                                   else self.NORMAL_WEIGHT)
        self._qtextedit.textCursor().mergeCharFormat(text_format)

    def toggle_selected_underline(self):
        text_format = self._qtextedit.textCursor().blockCharFormat()
        text_format.setFontUnderline(not self._qtextedit.fontUnderline())
        self._qtextedit.textCursor().mergeCharFormat(text_format)

    def toggle_selected_italics(self):
        text_format = self._qtextedit.textCursor().blockCharFormat()
        text_format.setFontItalic(not self._qtextedit.fontItalic())
        self._qtextedit.textCursor().mergeCharFormat(text_format)

    def toggle_selected_strikethrough(self):
        text_format = self._qtextedit.currentCharFormat()
        text_format.setFontStrikeOut(not text_format.fontStrikeOut())
        self._qtextedit.textCursor().mergeCharFormat(text_format)

    def toggle_selected_heading(self):
        text_format = self._qtextedit.currentCharFormat()

        if text_format.fontPointSize() == self.HEADING_SIZE and \
           text_format.fontWeight() == self.HEADING_WEIGHT and \
           text_format.fontUnderline() == self.HEADING_UNDERLINE:

            text_format.setFontPointSize(self.NORMAL_SIZE)
            text_format.setFontWeight(self.NORMAL_WEIGHT)
            text_format.setFontUnderline(self.NORMAL_UNDERLINE)

        else:
            text_format.setFontPointSize(self.HEADING_SIZE)
            text_format.setFontWeight(self.HEADING_WEIGHT)
            text_format.setFontUnderline(self.HEADING_UNDERLINE)

        self._qtextedit.textCursor().mergeCharFormat(text_format)

    def toggle_html_editor(self):
        if self._html_edit:
            html = self._qtextedit.document().toPlainText()
            self._qtextedit.document().setHtml(html)
        else:
            html = self._qtextedit.document().toHtml()
            self._qtextedit.document().setPlainText(html)
        self._html_edit = not self._html_edit

