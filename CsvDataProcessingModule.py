import pandas as pd

default_value_df = pd.read_csv('./csv_file/defaultValueCsvData.csv', header=None, names=['name', 'data'])
default_value_df.set_index('name', inplace=True)


def resetting_path(path) -> None:
    """
    riot_path 변경하는 함수
    PathErrorGui.py 에서 사용
    :param path:
        PathErrorGUi -> riot clint path
    :return:
        None
    """
    default_value_df.loc['riot_path', 'data'] = path
    default_value_df.to_csv('./csv_file/defaultValueCsvData.csv', mode='w', header=False)


def get_path() -> str:
    """
    riot_path 불러오는 함수
    :return:
        riot_path
    """
    return default_value_df.loc['riot_path', 'data']