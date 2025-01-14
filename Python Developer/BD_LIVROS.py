class Bookstore:
  def __init__(self, page_num):
    self.page_num = page_num

  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"

class Digital(Bookstore):
  def __init__(self, name, author, gender, page_num, **kw):
    self.name = name
    self.author = author
    self.gender = gender
    super().__init__(page_num)

class Physical(Bookstore):
  def __init__(self, name, author, gender, cover_type, page_num, **kw):
    self.name = name
    self.author = author
    self.gender = gender
    self.cover_type = cover_type
    super().__init__(page_num)

book_001 = Digital(" Raven", " Jhosua", " Terror", 300)
book_002 = Physical(" Vitu Baitola", " Rayran", " Patifaria", " Hard corver", 69)

print(book_001.name)
print(book_002)