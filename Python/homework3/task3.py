class CountVectorizer:
    def __init__(self):
        """Инициализируем класс

          Инициализируем класс и создаём пустой список будущего базиса слов
           """
        self.features = []

    def fit_transform(self, corpus: list) -> list:
        """Трансформация списка строк в числовые вектора

           Данная функция запоминает все слова и трнасформирует все строки из списка в числовые вектора

            Args:
                corpus (list): список строк, содержащих слова

            Returns:
               list : список списков (числовые вектора для каждой строки)
            """
        text = ' '.join(corpus).lower().split()
        words = {}
        for word in text:
            words[word] = words.get(word, 0) + 1
        self.features = list(words.keys())

        untransformed_corpus = [corp.lower().split() for corp in corpus]
        transformed_corpus = []
        for corp in untransformed_corpus:
            corp_cnt = dict.fromkeys(words.keys(), 0)
            for word in corp:
                corp_cnt[word] += 1
            transformed_corpus.append(list(corp_cnt.values()))

        return transformed_corpus

    def get_feature_names(self) -> list:
        """Возвращаем список всех слов, участвующих в обучении (трансформации)

           Returns:
              list : список всех слов (без дублей), которые участвовали в обучении
           """
        return self.features


if __name__ == '__main__':
    # tests
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(count_matrix)
    print(vectorizer.get_feature_names())
