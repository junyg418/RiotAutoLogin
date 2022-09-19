import pandas as pd


# --------------- Format Dataframe ---------------

# -- default_value_df : name 을 인덱스로 사용, header : ['name', 'data']
# default_value_df = pd.read_csv('./csv_file/defaultValueCsvData.csv', header=None, names=['name', 'data'])
# default_value_df.set_index('name', inplace=True)

# account_df : csv 분할자 "/" , head : csv 내에 되어있음, index 제거됨
# account_df = pd.read_csv('./csv_file/accountCsvData.csv', sep='/')

# --------------- Bug ---------------


# --------------- Fixed Bug ---------------

# is_duplicate_value 에서 account_df에 데이터들이 모두 int 일 때 정확한 값을 배출하지 않은 버그 발생


# --------------- RiotRunModule ---------------


def resetting_path(path) -> None:
    """
    riot_path 변경하는 함수
    PathErrorGui.py 에서 사용
    :param path:
        PathErrorGUi -> riot clint path
    :return:
        None
    """
    default_value_df = pd.read_csv('./csv_file/defaultValueCsvData.csv', header=None, names=['name', 'data'])
    default_value_df.set_index('name', inplace=True)

    default_value_df.loc['riot_path', 'data'] = path
    default_value_df.to_csv('./csv_file/defaultValueCsvData.csv', mode='w', header=False)


def get_path() -> str:
    """
    riot_path 불러오는 함수
    :return:
        riot_path
    """
    default_value_df = pd.read_csv('./csv_file/defaultValueCsvData.csv', header=None, names=['name', 'data'])
    default_value_df.set_index('name', inplace=True)

    path = default_value_df.loc['riot_path', 'data']
    return path


# --------------- AccountAddGui ---------------
class AccountAddGuiCsvDataProcess:
    @classmethod
    def add_account(cls, account_id: str, account_pw: str) -> None:
        """
        accountCsvData.csv 파일에 계정을 추가하는 함수
        """
        account_df = pd.read_csv('./csv_file/accountCsvData.csv', sep='/')
        # WARNING df.append will be removed from pandas
        changed_df = account_df.append({'id': account_id, 'password': account_pw}, ignore_index=True)
        changed_df.astype('string')
        changed_df.to_csv('./csv_file/accountCsvData.csv', mode='w', index=False, sep='/')


    @classmethod
    def is_duplicate_value(cls, account_id: str) -> bool:
        """
        아이디가 중복되는지 확인하는 함수
        :return:
            bool
        """
        account_df = pd.read_csv('./csv_file/accountCsvData.csv', sep='/').astype('string')
        bool_list = account_df['id'].isin([account_id]).tolist()
        if True in bool_list:
            return True
        else:
            return False


# --------------- MainGui ---------------

class MainGuiCsvDataProcess:
    @classmethod
    def get_len_account(cls) -> int:
        """
        계정의 개수 return 하는 함수
        :return:
            account_len:int -> 계정의 개수
        """
        account_df = pd.read_csv('./csv_file/accountCsvData.csv', sep='/')

        account_len = len(account_df)
        return account_len

    @classmethod
    def id_to_list(cls) -> list:
        """
        계정들의 아이디를 리스트로 반환해주는 함수
        :return:
            list -> 계정 id list
        """
        account_df = pd.read_csv('./csv_file/accountCsvData.csv', sep='/')

        id_df = account_df['id']
        id_list = id_df.tolist()
        return id_list

    @classmethod
    def select_idx_to_id(cls, idx: int) -> 'str':
        """
        선택된 id 반환 함수
        :param idx:
            index : int -> 아이디의 인덱스
        :return:
            id, password : tuple
        """
        account_df = pd.read_csv('./csv_file/accountCsvData.csv', sep='/')

        account_value_df = account_df.iloc[idx]
        id_value = str(account_value_df.id)
        pw_value = str(account_value_df.password)
        return id_value, pw_value

    @classmethod
    def get_account_default(cls) -> int:
        """
        계정의 기본값을 가져오는 함수
        :return:
            계정의 기본값 -> index: int
        """
        default_value_df = pd.read_csv('./csv_file/defaultValueCsvData.csv', header=None, names=['name', 'data'])
        default_value_df.set_index('name', inplace=True)

        default_data = default_value_df.loc['setting_account_idx', 'data']
        return int(default_data)

    @classmethod
    def set_account_default(cls, value) -> None:
        """
        계정의 기본값이 바뀌었을 떄 변경해주는 함수
        :param value:
            변경된 index 데이터
        :return:
            None
        """
        default_value_df = pd.read_csv('./csv_file/defaultValueCsvData.csv', header=None, names=['name', 'data'])
        default_value_df.set_index('name', inplace=True)

        default_value_df.loc['setting_account_idx', 'data'] = value
        default_value_df.to_csv('./csv_file/defaultValueCsvData.csv', mode='w', header=False)

    @classmethod
    def get_password_to_idx(cls, idx: int) -> str:
        """
        index 를 인자로 idx 순서의 비밀번호를 반환
        :param idx:
            index -> 데이터에 저장되어있는 아이디의 index
        :return:
            password
        """
        account_df = pd.read_csv('./csv_file/accountCsvData.csv', sep='/')

        password = account_df.loc[int(idx), 'password']
        return password

    @classmethod
    def get_password_to_id(cls, account_id: str) -> str:
        """
        id를 입력받고 password를 반환하는 함수
        :param account_id:
            계정의 id -> str
        :return:
            계정의 password -> str
        """
        account_df = pd.read_csv('./csv_file/accountCsvData.csv', sep='/')

        password = account_df[account_df['id'] == account_id].values.tolist()[0][1]
        return password

    # ---- AccountCell -----
    @classmethod
    def delete_account(cls, idx: int) -> None:
        """
        index를 통하여 accountCsvData 의 account 정보 ( 해당하는 행 )을 제거하는 함수
        """
        account_df = pd.read_csv('./csv_file/accountCsvData.csv', sep='/')
        delete_account = account_df.drop(idx, inplace=False).reset_index(drop=True)
        delete_account.to_csv('./csv_file/accountCsvData.csv', mode='w', index=False, sep='/')


if __name__ == '__main__':
    # AccountAddGuiCsvDataProcess.add_account('123','123')
    a = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]}).astype('string')
    print(a.values.tolist())