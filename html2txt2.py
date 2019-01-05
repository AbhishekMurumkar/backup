from bs4 import BeautifulSoup
soup = BeautifulSoup("E:\\abhishek\\odfpy-master\\odfpy-master\\odt2txt.txt")
print(soup.get_text())