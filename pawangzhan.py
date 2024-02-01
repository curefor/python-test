import requests
from bs4 import BeautifulSoup

search_url = "https://search.bilibili.com/all?keyword=chuu%E8%A1%A3%E6%9C%8D&from_source=webtop_search&spm_id_from=333.1007&search_source=2"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}

try:
    response = requests.get(search_url, headers=headers)
    response.raise_for_status()  # 这将引发错误，如果响应的HTTP状态代码不是200-400之间。
    soup = BeautifulSoup(response.content, 'html.parser')
    video_ids = [link["href"].split('/')[-1] for link in soup.select('.video-item .info a')]

    if not video_ids:
        print("No video IDs found. Check the HTML structure.")
    else:
        print(f"Found {len(video_ids)} video IDs.")

    for bvid in video_ids:
        comments_url = f"https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid={bvid}&sort=2"
        comments_response = requests.get(comments_url, headers=headers)
        comments_data = comments_response.json()

        if 'data' in comments_data and 'replies' in comments_data['data']:
            for comment in comments_data['data']['replies']:
                print(f"Video {bvid} Comment: {comment['content']['message']}")
        else:
            print(f"Failed to fetch comments for video {bvid}.")

except Exception as e:
    print(f"Error occurred: {e}")
print(soup.prettify()[:1000])  # 打印HTML内容的前1000个字符。
