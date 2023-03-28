import requests

from lxml import etree


def get_url():
    resource = requests.get(
        'https://jobs.zhaopin.com/CC382087910J40284251407.htm?refcode=4019&srccode=401901&preactionid=3ead6e75-eb8e-45f0-8a02-9e16d99ff17e&u_atoken=7b3cc844-30de-4498-961a-7bcbd0e93f9e&u_asession=01SAgqOXb85BqZNjHmYlezofSz4uCSF0YenaG04gfhKsIdxWLe74iCHCsVk8PWFVZWX0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K_SUZ9ms_sJQOublu0HYsrCmP3FSmeVQnmas47oIV-Y-2BkFo3NEHBv0PZUm6pbxQU&u_asig=05GfVFi5_1L9kS3H0VcOd79WHWvX0cvtL6nHSa2X7SEDGxgoU58Haz0MRssyJFG8DdYeEaNWyUDpEXD6PakBZbwozYVKuNWkJXFJ5auBNPGzvsPUpaATZW75AFAxOoHD5fsgz5SFc-nhqj2Es0lCg4gf1_1uCQNcUCo7KTcXNW9tv9JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzZpdr0mbMAghGuy2nj7R313PdoYfSvDpYGGHKE6jzwspy_5yi_e7rVDu4TD5jFgMue3h9VXwMyh6PgyDIVSG1W_9RETW4t-Jwoj0LqWakBs5uT4N6mo9qseyRZVP0KJCdASPuh_s0l2-ASiZHYL46XhQhGITmn4Z3JyU4XrKa1XkmWspDxyAEEo4kbsryBKb9Q&u_aref=CNmA7dAZiOwFotV%2FX7kzt8CkDtA%3D')
    html = etree.HTML(resource.text)
    title = html.xpath('//*[@id="summary-plane__title"]/text()')
    info = html.xpath('//*[@id="describtion__detail-content"]/text()')
    print(title, "\n", info)
    return resource


if __name__ == "__main__":
    res = get_url()
    print(res)
