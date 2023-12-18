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

Description: In the paper [1] possibilities of applying machine and deep learning methods to emotionality evaluation of posts text with emojis from the VKontakte social network are investigated. An unbalanced data set with posts text is described, the data set is annotated by 15 classes. In these classes emotional and tonal components of text are taken into account. Experiments are conducted on the obtained data set with using 6 classical machine learning methods, their ensembles with hard and soft voting, and 3 neural network methods. The best result by classification quality metrics was obtained for the Bag of words + VotingClassifier ensemble method with soft voting on lemmatized text with punctuation and emoji: F1-macro measure = 69.70%, F1-weighted measure = 82.06% and for the recurrent neural network GRU on 15 epochs of training: F1-measure macro = 48.77%, F1-measure weighted = 83.74%.

[1] Bykova A. P. Evaluation of Emotionality of Posts with Emojis in the
VKontakte Social Network Using Machine and Deep Learning Methods // Computational Linguistics
and Computational Ontologies. Vol. 7 (Proceedings of the XXVI International Joint
Scientific Conference «Internet and Modern Society», IMS-2023, St. Petersburg, June 26–28, 2023). —
St.Petersburg: ITMO University, 2023. P. 12–22. DOI: 10.17586/2541-9781-2023-7-12–22 
https://scholar.google.com/scholar_url?url=https://ims.itmo.ru/File/docs/IMS-2023_Lingvo_v1.pdf%23page%3D12&hl=ru&sa=X&d=14313465105493062565&ei=FqFoZa33HonemQHkpK3wAQ&scisig=AFWwaeak0dRkvdWOPWeigzsdKAxF&oi=scholaralrt&hist=aCrViNkAAAAJ:4759714380015671822:AFWwaeZWBc6L6tuBcF1jIdfvtTaB&html=&pos=5&folt=cit
