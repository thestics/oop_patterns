from typing import Optional, List

from PIL import Image
import abc


class DisplayObject(abc.ABC):
    @abc.abstractmethod
    def display(self):
        pass


class ImageFile(DisplayObject):
    
    def __init__(self, path: str):
        self.img = Image.open(path)
    
    def display(self):
        self.img.show()


class ImageProxy(DisplayObject):
    img_file: Optional[ImageFile]
    
    def __init__(self, path):
        self.path = path
        self.img_file = None
    
    def display(self):
        if self.img_file is None:
            self.img_file = ImageFile(path=self.path)
        self.img_file.display()


class ImageGallery:
    
    def __init__(self, images: List[str]):
        self.img_paths = images
    
    def show(self):
        for path in self.img_paths:
            p = ImageProxy(path)
            p.display()


if __name__ == '__main__':
    g = ImageGallery([
        "resource/pic1.jpg",
        "resource/pic2.jpg",
        "resource/pic3.jpg",
        "resource/pic4.jpg",
        "resource/pic5.jpg",
    ])
    g.show()
