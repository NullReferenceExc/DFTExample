import matplotlib.pyplot as plt


def show_dict_on_graphic(title: str, xlabel: str, ylabel: str, dictionary: dict[int, int], blocking: bool):
    """
    Отображает словарь на графике

    Параметры:
        title - заголовок графика
        xlabel - метка по оси X
        ylabel - метка по оси Y
        dictionary - словарь точек для отображения
        blocking - является ли вызов блокирующим
    """

    xs, ys = zip(*dictionary.items()) 
    plt.figure(figsize=(10,8))
    plt.title(title, fontsize=20) 
    plt.xlabel(xlabel, fontsize=15) 
    plt.ylabel(ylabel, fontsize=15) 
    plt.scatter(xs, ys, marker = 'o') 
    for x, y in dictionary.items():
       plt.annotate("", xy = (x, y)) 
    plt.show(block=blocking)