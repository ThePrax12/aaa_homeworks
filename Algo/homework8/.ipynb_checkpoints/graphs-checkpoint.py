from typing import List, Tuple, Dict, Optional


class Graph:
    def __init__(self, df_decode: "DataFrame", df_links: "DataFrame") -> None:
        """
        Инициализирует граф, используя данные из df_decode и df_links.

        :param df_decode: DataFrame, содержащий страницу и ее идентификатор.
        :param df_links: DataFrame, содержащий связи между страницами.
        """
        self.encode = dict(zip(df_decode.page_title, df_decode.page_id))
        self.decode = dict(zip(df_decode.page_id, df_decode.page_title))
        a = df_links.groupby(["pl_from"])["pl_to"].apply(set).reset_index()
        self.links = dict(zip(a.pl_from, a.pl_to))

    def bfs(
        self, start_title: str, target_title: str
    ) -> Tuple[Optional[int], List[str]]:
        """
        Выполняет поиск в ширину (BFS) для нахождения кратчайшего пути между двумя страницами.

        :param start_title: Название начальной страницы.
        :param target_title: Название целевой страницы.
        :return: Кортеж из глубины и пути. Если путь не найден, возвращается (None, []).
        """
        start_id = self.encode.get(start_title)
        target_id = self.encode.get(target_title)

        if start_id is None or target_id is None:
            return None, []

        lvl = 0
        queue_idx = 0
        queue = [(start_id, lvl, -1)]
        len_queue = 1
        visited = set(start_id)
        while queue_idx < len_queue:
            current_id = queue[queue_idx][0]

            if current_id == target_id:
                break

            lvl = queue[queue_idx][1] + 1

            for neighbor in self.links.get(current_id, set()):
                if neighbor not in visited:
                    queue.append((neighbor, lvl, queue_idx))
                    visited.add(neighbor)
                    len_queue += 1
            queue_idx += 1
        else:
            return None, []

        depth = queue[queue_idx][1]
        path = self._reconstruct_path(queue, queue_idx)

        return depth, path

    def _reconstruct_path(
        self, queue: List[Tuple[int, int, int]], queue_idx: int
    ) -> List[str]:
        """
        Восстанавливает путь от начальной страницы до целевой.

        :param queue: Очередь с состоянием пути.
        :param queue_idx: Индекс в очереди для восстановления пути.
        :return: Список названий страниц, составляющих путь.
        """
        path = []
        while queue_idx >= 0:
            path.append(self.decode[queue[queue_idx][0]])
            queue_idx = queue[queue_idx][2]
        return list(reversed(path))

    def is_neighbor(self, start_title: str, target_title: str) -> bool:
        """
        Проверяет, является ли одна страница соседом другой.

        :param start_title: Название начальной страницы.
        :param target_title: Название целевой страницы.
        :return: True, если страницы связаны, иначе False.
        """
        start_id = self.encode.get(start_title)
        target_id = self.encode.get(target_title)

        if start_id is None or target_id is None:
            return False

        return target_id in self.links[start_id]


import heapq


class WeightedGraph:
    def __init__(self, df_decode: "DataFrame", df_links: "DataFrame") -> None:
        """
        Инициализирует взвешенный граф с использованием данных из df_decode и df_links.

        :param df_decode: DataFrame, содержащий страницу и ее идентификатор.
        :param df_links: DataFrame, содержащий связи между страницами с весами.
        """
        self.encode = dict(zip(df_decode.page_title, df_decode.page_id))
        self.decode = dict(zip(df_decode.page_id, df_decode.page_title))
        a = df_links.copy()
        a["pl_to"] = df_links.apply(
            lambda row: (row["pl_to"], len(row["pl_title"])), axis=1
        )
        a = a.groupby(["pl_from"])["pl_to"].apply(set).reset_index()
        self.links = dict(zip(a.pl_from, a.pl_to))

    def dijkstra(
        self, start_title: str, target_title: str
    ) -> Tuple[Optional[int], List[str]]:
        """
        Выполняет алгоритм Дейкстры для нахождения кратчайшего пути в графе с весами.

        :param start_title: Название начальной страницы.
        :param target_title: Название целевой страницы.
        :return: Кортеж из кратчайшего расстояния и пути. Если путь не найден, возвращается (None, []).
        """
        start_id = self.encode.get(start_title)
        target_id = self.encode.get(target_title)

        if start_id is None or target_id is None:
            return None, []

        dist = {node: float("inf") for node in self.encode.values()}
        dist[start_id] = 0
        prev = {node: None for node in self.encode.values()}

        priority_queue = [(0, start_id)]
        visited = set()

        while priority_queue:
            current_dist, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node == target_id:
                break

            for neighbor, weight in self.links.get(current_node, []):
                if neighbor in visited:
                    continue

                new_dist = current_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_dist, neighbor))

        path = self._reconstruct_path(prev, target_id)
        return dist[target_id], path

    def _reconstruct_path(
        self, prev: Dict[int, Optional[int]], target_id: int
    ) -> List[str]:
        """
        Восстанавливает путь от начальной страницы до целевой, используя данные о предыдущих вершинах.

        :param prev: Словарь с предыдущими вершинами для каждой страницы.
        :param target_id: Идентификатор целевой страницы.
        :return: Список названий страниц, составляющих путь.
        """
        path = []
        current = target_id
        while current is not None:
            path.append(self.decode[current])
            current = prev[current]
        path.reverse()
        return path

    def is_neighbor(self, start_title: str, target_title: str) -> bool:
        """
        Проверяет, является ли одна страница соседом другой в взвешенном графе.

        :param start_title: Название начальной страницы.
        :param target_title: Название целевой страницы.
        :return: True, если страницы связаны, иначе False.
        """
        start_id = self.encode.get(start_title)
        target_id = self.encode.get(target_title)

        if start_id is None or target_id is None:
            return False
        return target_id in (c[0] for c in self.links[start_id])
