# Стратегия (Strategy)
# Поведенческий паттерн, который позволяет определить семейство алгоритмов и вынести их в собственные классы,
# которые называются — стратегии.

class ImageDecoder:  # Абстрактный интерфейс
    @staticmethod
    def decode(filename):
        raise NotImplementedError()


class PNGImageDecoder(ImageDecoder):  # интерфейс png файла, наследованный от абстрактного
    @staticmethod
    def decode(filename):
        print('PNG decode')


class JPEGImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('JPEG decode')


class GIFImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('GIF decode')


class Image:
    @classmethod
    def open(cls, filename):
        ext = filename.rsplit('.', 1)[-1]
        if ext == 'png':
            decoder = PNGImageDecoder
        elif ext in ('jpg', 'jpeg'):
            decoder = JPEGImageDecoder
        elif ext == 'gif':
            decoder = GIFImageDecoder
        else:
            raise RuntimeError('Невозможно декодировать файл %s' % filename)
        byterange = decoder.decode(filename)
        return cls(byterange, filename)

    def __init__(self, byterange, filename):
        self._byterange = byterange
        self._filename = filename


Image.open('picture.png')  # PNG decode
Image.open('picture.jpg')  # JPEG decode
Image.open('picture.gif')  # GIF decode
