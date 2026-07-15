flowchart TD

A([START]) --> B[/INPUT age/]
B --> C{age MOD 60 = 60+?}
C -- Above 60 --> D[/"DISPLAY Eligible for Senior Discount"/]
C -- Below 60 --> E[/"DISPLAY Not Eligible for Senior Discount"/]
D --> F([END])
E --> F
