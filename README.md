# 라이엇 자동 로그인__  
  
__Riot Auto Login__  
__1.0 ver : 2022/07/30 ~ 2022/09/16__  
## <center> ※주의 aution※ </center>
### 라이엇에 문의 결과 이 프로그램은 비인가 외부 프로그램으로 사용시 처벌을 받을 수 있습니다.  
__As a result of contacting Riot, use of this program as an unauthorized external program may result in penalties.__
## 설명서

## 구조도  
![image](https://github.com/user-attachments/assets/55518aee-a7b4-43ef-ad9a-a366b99a4071)
[구조도 링크](https://gitmind.com/app/doc/5r1i53wv0l).

### accountCsvData.csv  
계정 정보를 저장하는 csv 형식의 파일

__index,[account_id, account_password]__ 형식으로 저장

### defaultValueCsvData.csv
> setting_account_idx : 선택 되어있는 계정의 idx 번호  
> > default : 0  
> 
> riot_path : 라이엇 클라이언트의 실행 경로  
> > default : C:/Riot Games/Riot Client/RiotClientServices.exe  
