집합
집합은 다른 컬렉션(특히 시퀀스)과 비슷해 보이지만, 차이점이 있다. 집합은 원소에 순서(번호)나 키를 붙여 관리하지 않는다
또, 시퀀스와 매핑은 동일한 값을 여러 개 중복으로 저장할 수 있지만 집합은 동일한 원소는 하나만 가질 수 있다.
그래서 어떤 원소가 집합에 포함되는지는 알 수 있어도, 그 원소가 몇 번째인지 또는 몇 개나 있는지는 알 수 없다.

파이썬에서 집합을 표현하고 정의하는 양식은 리스트의 표현 양식과 거의 똑같다. {1, 2, 3, 4}와 같이 중괄호({})를 이용해 데이터를 묶고, 각 원소를 쉼표로 구분한다. 대괄호 대신 중괄호로 감싼다는 점만 리스트와 다르다. 중괄호는 {키1: 값1, 키2: 값2}와 같이 사전을 표현하는 양식에도 사용되는데, 사전은 콜론(:)으로 표현된 키-값 쌍을 담기 때문에 집합의 양식과 차이가 있다.