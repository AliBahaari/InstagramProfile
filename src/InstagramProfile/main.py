import requests as req, re, requests_random_user_agent
from bs4 import BeautifulSoup
from PIL import Image


print('Warning: Don\'t Use Neither Proxy Nor VPN')


class InstagramProfile:


  def __init__(self, username):
      self.username = username


  def profile_picture(self):
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
    profile_picture.save(f'images/{self.username}.png')

    print('Profile Picture Saved')


  def profile_biography(self):
    # Request to Instagram
    request_result = req.get(f'https://www.instagram.com/{self.username}/')

    # Search in Data
    soup = BeautifulSoup(request_result.text, 'html.parser')
    body_tags = soup.find_all('body')

    # Show the Biography
    profile_biography = re.findall(r"biography\":\"(.*?)\"", str(body_tags[0]))[0]
  
    if len(profile_biography) > 0:

      with open(f'biographies/{self.username}.txt', 'w', encoding='utf-8') as biography_file:
        encoded_biography = profile_biography.encode('utf-8').decode('unicode-escape').encode('utf-8', 'replace').decode('utf-8')
        biography_file.write(encoded_biography)
        
        print(encoded_biography)
        print('Profile Biography Saved')

    else:
      print('No Biography')


instagramProfile = InstagramProfile('<USERNAME>')
instagramProfile.profile_picture()
instagramProfile.profile_biography()