flowchart TD

A([START]) --> B[/INPUT number/]
B --> C{number MOD 0 = 0+?}
C -- Above 0 --> D[/"DISPLAY Above Sea Level"/]
C -- Exactly 0 --> E[/"DISPLAY At Sea Level"/]
C -- Below 0 --> F[/"DISPLAY Below Sea Level"/]
D --> G([END])
E --> G
F --> G
