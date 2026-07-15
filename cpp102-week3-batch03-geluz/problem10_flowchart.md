flowchart TD

A([START]) --> B[/INPUT number/]
B --> C{number MOD 2 = 0?}
C -- Yes --> D[/DISPLAY "Even"/]
C -- No --> E[/DISPLAY "Odd"/]
D --> F([END])
E --> F
