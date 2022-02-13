---
layout: default
title:  "Pyspark"
parent: Coding
# nav_order: 97
---


분석 업무는 pyspark를 사용해서 진행하는데 이것이 python와 Spark의 결합이란 것은 알겠지만, spark에 대한 백그라운드가 없어 분석에 필요한 노하우(?)가 생기질 않고 구글링으로 연명하고 있는 중이다. 이런 내가 딱해서 확실히 정리해보려고 한다.

***




```
df.groupBy('col1').pivot('col2').agg(sum('col3'))
```





