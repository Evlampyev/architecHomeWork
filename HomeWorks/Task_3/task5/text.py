class Text:
    def __init__(self, text):
        self.text = text

    def __getinitargs__(self):
        return self.text
