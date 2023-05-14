import pandas as pd
import requests
from datetime import datetime as dt
import time
from tqdm import tqdm

def searchPosts(groupId, token, file):
    offset = 0  # начальный индекс поиска публикаций
    count = 95  # шаг продвижения индекса поиска публикаций
    try:
        for _ in range(0, 4):
            # формирование списка параметров запроса к api
            params = {'owner_id': groupId, 'offset': offset, 'count': count, 'filter': 'all', 'extended': 1,
                      'access_token': token, 'v': 5.131}
            # отправка запроса с заданными параметрами
            r = requests.get('https://api.vk.com/method/wall.get', params)
            for j in range(0, count):
                postText = str(r.json()['response']['items'][j]['text'])
                if postText != '':
                    file.write(str(r.json()['response']['items'][j]['id']) + ';' + str(
                        dt.fromtimestamp(r.json()['response']['items'][j]['date']).strftime('%Y%m%d %H:%M:%S')) +
                               ';' + str(r.json()['response']['items'][j]['text']).replace(';', ',').replace('\n', ' ') + ';' + str(groupId) + '\n')
            offset += count  # наращивание шага продвижения по публикациям
            # принудительная «остановка» работы программы, для соблюдения требований api по количеству запрсов
            time.sleep(2)
    except Exception as error:
        print(error)

def writeThreadsComments(groupId, postId, commentId, userToken, file):
    params = {'owner_id': groupId, 'post_id': postId, 'comment_id': commentId, 'need_likes': 0, 'offset': 0,
              'count': 20, 'preview_lenght': 0, 'extended': 1, 'access_token': userToken, 'v': 5.131}
    try:
        r = requests.get('https://api.vk.com/method/wall.getComments', params)
        commentsCount = int(r.json()['response']['count'])
        for i in range(0, commentsCount):
            try:
                commentText = str(r.json()['response']['items'][i]['text'])
                if commentText != '':
                    file.write(str(int(r.json()['response']['items'][i]['id'])) + ';' + str(
                        int(r.json()['response']['items'][i]['from_id'])) +
                               ';' + str(int(postId)) + ';' + str(
                        dt.fromtimestamp(r.json()['response']['items'][i]['date']).strftime('%Y%m%d %H:%M:%S')) +
                               ';' + str(r.json()['response']['items'][i]['text']).replace(';', ',').replace('\n', ' ') + '\n')
            except Exception as error:
                print("Error in writeThreadsComments." + str(error))
                continue
        time.sleep(2)
    except Exception as error:
        print("Error in writeThreadsComments." + str(error))

def searchPostComments(groupId, postID, userToken, file):
    params = {'owner_id': groupId, 'post_id': postID, 'need_likes': 0, 'offset': 0, 'count': 95,
              'preview_lenght': 0, 'extended': 1, 'access_token': userToken, 'v': 5.131}
    try:
        r2 = requests.get('https://api.vk.com/method/wall.getComments', params)
        commentsCount = int(r2.json()['response']['count'])
        print('commentsCount:', commentsCount)
        for i in range(0, commentsCount):
            try:
                countThreads = int(r2.json()['response']['items'][i]['thread']['count'])
                commentId = int(r2.json()['response']['items'][i]['id'])
                if countThreads != 0:
                    commentText = str(r2.json()['response']['items'][i]['text'])
                    if commentText != '':
                        file.write(str(int(r2.json()['response']['items'][i]['id'])) + ';' + str(
                            int(r2.json()['response']['items'][i]['from_id'])) +
                                   ';' + str(int(postID)) + ';' + str(
                            dt.fromtimestamp(r2.json()['response']['items'][i]['date']).strftime('%Y%m%d %H:%M:%S')) +
                                   ';' + str(r2.json()['response']['items'][i]['text']).replace(';', ',').replace('\n', ' ') + '\n')
                        writeThreadsComments(groupId, postID, commentId, userToken, file)
                    else:
                        commentText = str(r2.json()['response']['items'][i]['text'])
                        if commentText != '':
                            file.write(str(int(r2.json()['response']['items'][i]['id'])) + ';' + str(
                                int(r2.json()['response']['items'][i]['from_id'])) +
                                       ';' + str(int(postID)) + ';' + str(
                                dt.fromtimestamp(r2.json()['response']['items'][i]['date']).strftime(
                                    '%Y%m%d %H:%M:%S')) +
                                       ';' + str(r2.json()['response']['items'][i]['text']).replace(';', ',').replace('\n', ' ') + '\n')
            except Exception as error:
                print("Error in searchComments" + str(error))
                continue
        time.sleep(2)
    except Exception as error:
        print("Error in searchComments" + str(error))

if __name__ == "__main__":
    #нужен токен для доступа к API
    token = ''

    #1) для получения постов из 100 топ групп ВКонтакте
    # заккоментировать этот блок кода для получения комментариев по скачанным постам

    top_100_groups = pd.read_csv('top_100_05_02_2023.csv', delimiter=';')
    with open('posts.csv', 'a') as file:
        file.write('postID;postDate;postText;groupId' + '\n')
        for index, row in tqdm(top_100_groups.iterrows()):
            group_id = '-' + str(int(row['id']))
            print(index, group_id)
            searchPosts(group_id, token, file)

    #2) данный блок кода нужен для получения комментариев к постам из блока 1
    # закомментировать этот блок кода для получения постов,
    # так как сначала получаем посты и сохраняем их в файл posts.csv,
    # затем по полученным постам из файла posts.csv получаем комментарии к ним и сохраняем их в файл comments.csv

    # posts = pd.read_csv('posts.csv', delimiter=';')
    # with open('comments.csv', 'a') as file:
    #     file.write('commentId;commentatorId;postID;postDate;commentText' + '\n')
    #     for index, row in tqdm(posts.iterrows()):
    #         post_id = str(int(row['postID']))
    #         groupId = str(int(row['groupId']))
    #         print(groupId, post_id)
    #         searchPostComments(groupId, post_id, token, file)
