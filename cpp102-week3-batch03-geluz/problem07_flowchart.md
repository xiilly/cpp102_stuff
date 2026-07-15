flowchart TD

A([START]) --> B[/INPUT weight1/]
B --> C[/INPUT weight2/]
C --> D[/INPUT weight3/]
D --> E["semester standing = weight1 + weight2 + weight3 / 3"]
E --> F[/DISPLAY semester standing/]
F --> G([END])
