---
layout: default
title:  "[SQL] SQL Style Guide"
parent: Study
permalink: /study/sqlstyleguide/
# date: 2023-12-13
last_modified_date: 2023-12-18
---

{: .note-title}
> Background
>
> - Simon Holywell이라는 대단한 스펙의 금융 쪽 개발자가 있는데 이 분이 정리한 [[SQL Style Guide]](https://www.sqlstyle.guide/)가 있다
>   - 위 가이드는 Joe Celko's SQL Programming Style를 바라보고 있음. 이 책에 나온 내용과 호환되는 코딩 스타일이라고 함
> - 코드는 오래전부터 전해져 내러오는 것들이 많고, 보통 이런 것들을 레거시(코드 중 쿼리 한정)라고 한다
>   - 레거시 자체는 긍/부정 모든 의미가 내포되어 있다
>   - 내가 생각할 때 안 좋은 레거시는 가독성이 떨어지는 쿼리다
>   - 그럼 대우를 따져보면, 가독성이 좋은 쿼리는 선한 레거시가 될 수 있다
> - **어떻게 쿼리를 해야 좋다고 할 수 있는걸까?**
>   - 에 대한 답을 현재 회사에선 Simon Holywell의 가이드 문서를 참조하고 있다.
>     - 사실 일 잘하시는 한 분이 이런 문화를 구축하려 했다. 지금은 흐지부지 됐다. 조직 차원에서 이런 문화가 잡힌 것은 아니다. 
>     - 나도 이걸 정리하면서 전파하려고 했으나 팀에서 조차 반대 의견에 부딪혔기 때문에.. 마찬가지로 흐지부지
>     - 어쩌면 레거시는 기술이 아닌 사람 자체가 아닐까라는 오만한 생각도 들었다.
>     - 개발자가 아니라 분석가라서 그렇게까지 코딩 스타일을 통일시킬 필요 없다는 시각도 물론 있을 수 있다. (심지어 예전의 나)
>     - 근데 스타일 맞추면 의외로 일하기 정말 편하다. 시야도 확장되는 느낌
>     - 코딩도 결국 또 하나의 문서라 가독성과 같은 UX를 고려하는 것이 좋다고 생각한다.

***

## White space

### 예약어는 right aligned, value는 left aligned 시켜야 함

- 가장 가독성이 뛰어난 방식(이라 생각함)
- 대신 작성하기는 다소 번거로움. 예약어마다 몇 칸 띄울지가 달라 탭이 아니라 스페이스로 작업해야 하는 번거로움
- 어차피 자주 쓰는 예약어가 정해져 있다보니 익숙해지면 괜찮음

```sql
SELECT c.date
  FROM pubg_mart.cash_mtx AS c
 WHERE c.date = '2023-08-21'
```

- 중간에 일렬로 비워져 있는 곳을 river라고 함
- 두 개의 예약어를 사용해야 하는 경우, 첫번째 예약어에 맞춤. 두번째 예약어는 other side of river로 넘김

```sql
SELECT date,
	   COUNT(*) AS log_count
  FROM pubg_mart.cash_mtx
 GROUP BY date
```

### 언제 newlines / vertical space를 하는지?

- 예약어마다
- 쉼표 후에
    - 보통 SELECT 할 때 한 줄에 한 column을 넣었었는데, 굳이 이렇게 할 필요 없고, logical group으로 구분지어 줄넘기면 됨
    - 줄넘기고 쉼표를 river에 위치시키면서 오른쪽 정렬시키기도 함 (펍지에서만?)
 
```sql
SELECT date
	  ,platform
  FROM pubg_mart.cash_mtx
```

- 개인적으론 logical group이란게 주관적인 기준이 될 수 있어 모든 column을 줄넘기는 것이 좋을 것 같기도 함
- 필자도 [Comma positioning]에서 언급하긴 했는데, 쉼표를 다음 줄에 붙이는건 상당히 hideous, weird 하다는 입장
- 그나마 comment out을 위해서 이렇게 하는 경우를 봐왔지만 이마저도 한계가 있기 때문에 comma seperated list는 term 다음에 comma를 위치시키야 한다고 주장함
- 이건 어디까지나 '가이드'라서.. 고민되네. 코더끼리 모여서 합의한 다음 펍지만의 룰은 만드는게 맞겠지
- large chunks of code 후에


## Indentaion

### Joins

- join은 한 번 들여쓰고 오른쪽 정렬시키면 됨
    - join을 두 번 하는 경우는? 지양. 차라리 with 구문으로 새로 파는게

```sql
SELECT c.date
       m.product_type
  FROM pubg_bi.pubg_economy_sales_report_daily AS c
       LEFT JOIN pubg_meta.meta_all_sales AS m
       ON c.product_id = m.product_id
       AND c.sales_id = m.sales_id
```

### Subqueries

- 똑같이 한 번 들여쓰는데, 키워드는 왼쪽 정렬, 나머지는 오른쪽 정렬

```sql
SELECT A.device,
       A.platform
  FROM (SELECT device,
               platform
          FROM pubg_mart.gcoin_master
         WHERE date = '{target_date}'
           AND device = '{device}') AS A
```

- 데이터브릭스의 주피터노트북으로 작업할 때, 여러 코드를 한번에 indent 해야 하는 경우가 있음
    - sql query의 경우 command + } 로 indent하면 기껏 맞춰놓은 여백이 뭉개짐
    - 해결: 뭉개진 것 하나하나 맞추거나, indent 자체를 모든 줄마다 스페이스 4번으로 실행하거나

```sql
    SELECT date, status, COUNT(*)
      FROM pubg_mart.steam_mtx_report
     GROUP BY date, status
```

```sql
        SELECT date, status, COUNT(*)
        FROM pubg_mart.steam_mtx_report
        GROUP BY date, status
```

## 기타

- WITH 구문 관련해선 따로 언급 없음. 나라면?

### CASE 구문 작성 방법

- CASE, WHEN, ELSE, END로 줄 구분하고, 오른쪽 정렬

```sql
SELECT *,
	   CASE country_os
       WHEN 'CN' THEN 'CN'
       ELSE country_ip
       END AS country
  FROM df_user_ready
 WHERE rn = 1
```

### Subquery VS Common Table Expression (CTE)

- 서브쿼리: 하나의 쿼리 안에 다른 쿼리를 포함시키는 것
    - 주 쿼리 내에 포함된 작은 쿼리
    - 주로 SELECT 문의 WHERE 절, FROM 절, HAVING 절에서 사용됨
- CTE: 임시로 결과 집합을 정의하는 것. 이름이 지정된 서브쿼리라고 볼 수 있음
    - 주로 긴 쿼리를 더 작은 논리적 단계로 나누기 위해 사용됨
    - WITH 문을 사용해서 CTE를 정의하고, 이후 주 쿼리에서 해당 CTE를 참조해서 사용
    - 서브쿼리를 반복적으로 사용해야 하는 경우에도 유용함

### 필자는 SQL이나 DB structure에선 OOP를 고려하면 안된다고 함

- OOP는 코드를 객체 단위로 구조화하여 개발하는 방법론
- SQL에 OOP를 적용하는 방법은 ORM, stored procedure, trigger 등이 있음
- 가독성은 떨어지고 복잡성만 높아질 수 있어 상황에 따라 적용해야 함

### Uniform Suffixes: 컬럼명에 아래와 같은 접미어를 붙여서 이해를 도울 수 있음

- _id: a unique identifier such as a column that is a primary key.
- _status: flag value or some other status of any type such as publication_status.
- _total: the total or sum of a collection of values.
- _num: denotes the field contains any kind of number.
- _name: signifies a name such as first_name.
- _seq: contains a contiguous sequence of values.
- _date: denotes a column that contains the date of something.
- _tally: a count.
- _size: the size of something such as a file size or clothing.
- _addr: an address for the record could be physical or intangible such as ip_addr.

## 실제 적용 예시

- 내가 짰던 쿼리에 이 스타일 적용해봤다
- 이전, 이후 비교하는 테이블로 작성해보고 싶었는데, 마크다운 테이블 내에 코드 스니펫 포함시키면 깨지는 것을 처음 알았다.

### 이전
```sql
SELECT
    date
    ,sales.platform
    ,sales.product_id
    ,UPPER(sales.country_code) as country_code
    ,meta.product_type
    ,meta.product_name
    ,sales.gross_unit_sold
    ,sales.gross_sales
FROM
    pubg_bi.pubg_economy_sales_report_daily as sales
    LEFT JOIN
    pubg_meta.meta_all_sales as meta
    ON sales.product_id = meta.product_id
       AND sales.platform = meta.platform 
       AND sales.sales_id = meta.sales_id
WHERE
     date between "{start_date}" and "{end_date}"
AND sales.product_id != '3rd_party'
```

### 이후
```sql
SELECT date,
       s.platform, s.product_id,
       UPPER(s.country_code) AS country_code,
       meta.product_type, meta.product_name,
       s.gross_unit_sold, s.gross_sales
  FROM pubg_bi.pubg_economy_sales_report_daily AS s
	   LEFT JOIN pubg_meta.meta_all_sales AS m
	   ON s.product_id = m.product_id
       AND s.platform = m.platform
       AND s.sales_id = m.sales_id
 WHERE date BETWEEN '{start_date}' AND '{end_date}'
   AND s.product_id != '3rd_party'
```

### 이전
```sql
WITH record_ready (
    SELECT *
    FROM log_bro_record_live.record
    WHERE platform = 'pc'
    AND event_date = '{target_date}'
), record_prep (
    SELECT DISTINCT
        event_date
        ,SPLIT(file_id, 'record.')[1] AS session_id
        ,props.Rank
        ,CAST(props.TimeSurvived AS FLOAT) AS TimeSurvived
        ,props.User
        ,region_server AS server
        ,play_mode
    FROM record_ready
    WHERE CAST(props.TimeSurvived AS FLOAT) <= 2100
)

SELECT event_date
    ,server
    ,play_mode
    ,session_id
    ,SUM(TimeSurvived) AS TimeSurvived
FROM record_prep
GROUP BY event_date, server, play_mode, session_id
```

### 이후
```sql
WITH record_ready (
    SELECT *
      FROM log_bro_record_live.record
     WHERE platform = 'pc'
       AND event_date = '{target_date}'
), record_prep (
    SELECT DISTINCT event_date,
					SPLIT(file_id, 'record.')[1] AS session_id,
					props.Rank,
					CAST(props.TimeSurvived AS FLOAT) AS TimeSurvived,
					props.User, region_server AS server, play_mode
      FROM record_ready
     WHERE CAST(props.TimeSurvived AS FLOAT) <= 2100
)

SELECT event_date, server, play_mode, session_id,
	   SUM(TimeSurvived) AS TimeSurvived
  FROM record_prep
 GROUP BY event_date, server, play_mode, session_id
```












