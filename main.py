import requests as req, re, requests_random_user_agent
from bs4 import BeautifulSoup
from PIL import Image


print('Warning: Neither Proxy Nor VPN!')


class InstagramProfilePicture:


  def __init__(self, username):
      self.username = username


  def show_profile_picture(self):
    # Request to Instagram
    request_result = req.get(f'https://www.instagram.com/{self.username}/')

    # Search in Data
    soup = BeautifulSoup(request_result.text, 'html.parser')
    body_tags = soup.find_all('body')

    profile_picture_url = re.findall(r"profile_pic_url_hd\":\"([\S]+?)\"", str(body_tags[0]))[0].replace(r'\u0026', '&')
    profile_biography = re.findall(r"biography\":\"(.*?)\"", str(body_tags[0]))[0]

    # Show the Image
    profile_picture_bytes = req.get(profile_picture_url, stream=True).raw
    profile_picture = Image.open(profile_picture_bytes)
    profile_picture.show()


  def show_profile_biography(self):
    # Request to Instagram
    request_result = req.get(f'https://www.instagram.com/{self.username}/')

    # Search in Data
    soup = BeautifulSoup(request_result.text, 'html.parser')
    body_tags = soup.find_all('body')

    # Show the Biography
    profile_biography = re.findall(r"biography\":\"(.*?)\"", str(body_tags[0]))[0]
    print(profile_biography)


IGPP = InstagramProfilePicture('leomessi')
IGPP.show_profile_biography()