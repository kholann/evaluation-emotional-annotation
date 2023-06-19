# evaluation-emotional-annotation
1) файл BoW_with_classifiers_v2.ipynb - эксперименты с мешком слов для классических алгоритмов машинного обучения;
2) файл NN_classification_10_epochs_with_metrics_v2.ipynb - эксперименты с нейронными сетями на 10 эпохах обучения;
3) файл NN_classification_15_epochs_with_metrics_v2.ipynb - эксперименты с нейронными сетями на 15 эпохах обучения;
4) файл NN_classification_5_epochs_with_metrics_v2.ipynb - эксперименты с нейронными сетями на 5 эпохах обучения;
5) файл Navec_with_classifiers_v2.ipynb - эксперименты с векторными представлениями Navec для классических алгоритмов машинного обучения;
6) файл Word2Vec_with_classifiers_v2.ipynb - эксперименты с векторными представлениями Word2Vec для классических алгоритмов машинного обучения;
7) файл Work with ngrams.ipynb - работа со словосочетаниями;
8) файл comments_for_github.csv - комментарии, скаченные из 100 Top групп ВКонтакте на 5.02.2023 года; колонки postDate, commentText (текст в нижнем регистре без id пользователей и групп); всего 131 955 строк;
9) файл data loading from vkontakte.py - скрипт для загрузки постов и комментариев к ним из ВКонтакте;
10) файл df_em_1_token_10.csv - тексты постов с 1 эмодзи и длиной поста не более 11 токенов; колонки img_emoji, word_count, count_emoji, emotion, tonality, class, clean_text; этот файл использовался в экспериментах; 9220 строк;
11) файл emoji_df.csv - файл с описанием эмодзи; колонки emoji, name, group, sub_group, codepoints; 4581 строка;
12) файл posts_for_github.csv - посты, скаченные из 100 Top групп ВКонтакте на 5.02.2023 года; колонки postDate, postText (текст в нижнем регистре без id пользователей и групп); всего 28 751 строка;
13) файл swl.txt - словарь стоп-слов;
14) файл top_100_05_02_2023.csv - id 100 Top групп ВКонтакте на 5.02.2023 года;
15) файл use_rubert-tiny2.ipynb - эксперименты с дообучением модели 'cointegrated/rubert-tiny2'.
