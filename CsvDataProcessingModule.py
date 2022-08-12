import pandas as pd

# TODO :사용된 파일에 따라서 불러와지는 df 다르게 변환

# --------------- RiotRunModule ---------------
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
    path = default_value_df.loc['riot_path', 'data']
    return path


# --------------- MainGui ---------------
account_df = pd.read_csv('./csv_file/accountCsvData.csv', sep='/')


def get_len_account() -> int:
    """
    계정의 개수 return 하는 함수
    :return:
        account_len:int -> 계정의 개수
    """
    account_len = len(account_df)
    return account_len


def df_id_to_list() -> list:
    """
    계정들의 아이디를 리스트로 반환해주는 함수
    :return:
        list -> 계정 id list
    """
    id_df = account_df['id']
    id_list = id_df.tolist()
    return id_list


def select_idx_to_id(idx: int) -> 'str':
    """
    선택된 id 반환 함수
    :param idx:
        index : int -> 아이디의 인덱스
    :return:
        id, password : tuple
    """
    account_value_df = account_df.iloc[idx]
    id_value = str(account_value_df.id)
    pw_value = str(account_value_df.password)
    return id_value, pw_value


if __name__ == '__main__':
    select_idx_to_id(1)
