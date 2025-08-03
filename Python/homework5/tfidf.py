import math


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
        words = {}
        untransformed_corpus = [corp.lower().split() for corp in corpus]
        for corp in untransformed_corpus:
            for word in corp:
                words[word] = 1

        self.features = list(words.keys())

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


class TfidfTransformer:

    @staticmethod
    def tf_transform(count_matrix: list) -> list:
        """Трансформация числового вектора из CountVectorizer в tf матрицу

        Данная функция считает tf матрицу

        Args:
            corpus (list): матрица с числами из CountVectorizer

        Returns:
           list : список списков tf матрица
        """
        return [
            [round(el / sum(vector), 3) for el in vector] for vector in count_matrix
        ]

    @staticmethod
    def idf_transform(count_matrix: list) -> list:
        """Трансформация числового вектора из CountVectorizer в idf вектор

        Данная функция считает idf вектор

        Args:
            corpus (list): матрица с числами из CountVectorizer

        Returns:
           list : список (idf вектор)
        """
        vector_shape = len(count_matrix[0])
        D = len(count_matrix)
        ans = []
        for i in range(vector_shape):
            d = sum([1 for vector in count_matrix if vector[i] != 0])
            ans.append(round(math.log((D + 1) / (d + 1)) + 1, 3))
        return ans

    def fit_transform(self, count_matrix: list) -> list:
        """Трансформация списка строк в tf-idf матрицу

        Данная функция считает tf-idf матрицу

        Args:
            corpus (list): матрица с числами из CountVectorizer

        Returns:
           list : список списков - tf-idf матрица
        """
        tf_matrix = self.tf_transform(count_matrix)
        idf_matrix = self.idf_transform(count_matrix)
        vector_shape = len(count_matrix[0])
        vectors_cnt = len(count_matrix)
        for i in range(vector_shape):
            for j in range(vectors_cnt):
                tf_matrix[j][i] = round(tf_matrix[j][i] * idf_matrix[i], 3)

        return tf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        self.transformer = TfidfTransformer()

    def fit_transform(self, corpus: list) -> list:
        """Трансформация числового вектора из CountVectorizer в tf-idf матрицу

        Данная функция считает tf-idf матрицу (CountVectorizer + TfidfTransformer)

        Args:
            corpus (list): список строк, содержащих слова

        Returns:
           list : список списков - tf-idf матрица
        """
        transformed_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(transformed_matrix)


if __name__ == "__main__":
    # tests
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    vectorizer = TfidfVectorizer()

    print(vectorizer.fit_transform(corpus))
    print(vectorizer.get_feature_names())
