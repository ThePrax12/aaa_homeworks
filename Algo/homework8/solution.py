import pandas as pd
from graphs import Graph, WeightedGraph

df_decode = pd.read_csv("simple_english_wiki_pages.csv", dtype=str)
df_links = pd.read_csv("simple_english_wiki_pagelinks.csv", dtype=str)

# task1
print("task1:")
gr1 = Graph(df_decode, df_links)
depth, path = gr1.bfs("Analytics", "Algorithm")
print(depth, path)

# task2
print("task2:")
for link in path:
    if gr1.is_neighbor(link, "Algorithm"):
        print(link)

# task3
print("task3:")
gr2 = WeightedGraph(df_decode, df_links)
depth, path = gr2.dijkstra("Analytics", "Algorithm")
print(depth, path)

# task4
print("task4:")
for link in path:
    if gr2.is_neighbor(link, "Algorithm"):
        print(link)