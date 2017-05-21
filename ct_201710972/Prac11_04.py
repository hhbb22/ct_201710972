from PIL import Image
s= Image.open("C:\\Users\\400T6B\\Desktop\\italy.jpg")
s.show()

%matplotlib inline
from matplotlib.pyplot import imshow
imshow(s)

from PIL import Image
s= Image.open ("C:\\Users\\400T6B\Desktop\\italy.jpg")
s.save("C:\\Users\\400T6B\\Desktop\\italy.png")
