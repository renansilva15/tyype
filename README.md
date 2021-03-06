# tyype

Um pacote com com objetivo de tratar dados de entrada.

## Instalação

### Instalação via pip:

```sh
python -m pip install -U Tyype
```


## Como Usar

Até o momento o tyype trata dados do inteitos, flutuantes e datas.


## inty() e floaty()

### Lê um valor da entrada padrão e retorna o mesmo caso seja inteiro, caso contrário "None" é retornado

```python
from tyype.inty import *
print(Inty.inty())
```

Para ler valores de ponto flutuante:

```python
from tyype.floaty import *
print(Floaty.floaty())
```


### Lê um valor da entrada padrão enquanto o mesmo não for inteiro, a cada tentativa e impresso a mensagem de erro passada como parâmetro

```python
from tyype.inty import *
print(Inty.inty('\nDigite um número inteiro.'))
```

Para ler valores de ponto flutuante:

```python
from tyype.floaty import *
print(Floaty.floaty('\nDigite um número.'))
```


### Retorna uma lista contendo os valores inteiros passados como argumento na linha de comando

Terminal:
```txt
$ python3 test.py w 3 w 5 6 8
[3, 5, 6, 8]
```

Código:
```python
from tyype.inty import *
print(Inty.inty(1))
```

Caso queira passar mais de um valor por argumento basta passar o parâmetro do "split", nesse caso o método retorna uma lista de listas.

Código:
```python
from tyype.inty import *
print(Inty.inty(1, ','))
```

Terminal:
```txt
$python3 test.py w 3,4,5,6,7 w 5,6.4,3 6 8
[[3, 4, 5, 6, 7], [5, 3], [6], [8]]
```

Para valores de ponto flutuante

Código:
```python
from tyype.floaty import *
print(Floaty.floaty(1))
print(Floaty.floaty(1, ','))
```


### Retorna uma lista de listas contendo os valores inteiros de todos os arquivos passados como argumento na linha de comando(uma lista para cada arquivo)

Arquivo(test.txt):
```txt
1 4 1 a a 1 qwqw
2 5 2 2.3 2.7
3 3.44 987 qwwq S3RL
2323 wqwq qw mari234

```

Terminal:
```txt
$ python3 test.py test.txt
[[1, 4, 1, 1, 2, 5, 2, 2, 3, 2, 7, 3, 3, 4, 4, 9, 8, 7, 3, 2, 3, 2, 3, 2, 3, 4]]
```

Código:
```python
from tyype.inty import *
print(Inty.inty(2))
```

E possível especificar como arquivo está dividido

Código:
```python
from tyype.inty import *
print(Inty.inty(2, ' '))
```

Terminal(os testes sempre utilizam o mesmo arquivo):
```txt
$ python3 test.py test.txt
[[1, 4, 1, 1, 2, 5, 2, 3, 987, 2323]]
```

Para valores de ponto flutuante

Código:
```python
from tyype.floaty import *
print(Floaty.floaty(2))
print(Floaty.floaty(2, ' '))
```


## inty2() e floaty2()

### Recebe um valor como parâmetro e retorna o mesmo caso seja inteiro, caso contrário "None" é retornado

Terminal(python3):
```txt
>>> from tyype.inty import *
>>> print(Inty.inty2(3))
3
>>> print(Inty.inty2('3'))
3
>>> print(Inty.inty2('3.5'))
None
>>> print(Inty.inty2('dsd'))
None
```

Para valores de ponto flutuante:

```txt
>>> from tyype.floaty import *
>>> print(Floaty.floaty2('3.5'))
3.5
```


## intFile() e floatyFile()

### Recebe um arquivo como parâmetro e retorna uma lista com todos os números inteiros

Terminal(python3):
```txt
>>> from tyype.inty import *
>>> print(Inty.intyFile('test.txt'))
[1, 4, 1, 1, 2, 5, 2, 2, 3, 2, 7, 3, 3, 4, 4, 9, 8, 7, 3, 2, 3, 2, 3, 2, 3, 4]
```

E possível especificar como arquivo está dividido

Terminal(python3):
```txt
>>> from tyype.inty import *
>>> print(Inty.intyFile('test.txt', ' '))
[1, 4, 1, 1, 2, 5, 2, 3, 987, 2323]
```

Para valores de ponto flutuante:

```txt
>>> from tyype.floaty import *
>>> print(Floaty.floatyFile('test.txt', ' '))
[1.0, 4.0, 1.0, 1.0, 2.0, 5.0, 2.0, 2.3, 2.7, 3.0, 3.44, 987.0, 2323.0]
```


## datey() e datey2()

### Lê uma data(ano, mês e dia) da entrada padrão enquanto a mesma não for válida, a cada tentativa e impresso a mensagem de erro passada como parâmetro. Por fim a data e retornada.

```python
from tyype.datey import *
print(Datey.datey('\nData inválida.'))
```

É possível especificar a mensagem para o usuário e um formato diferente.

```python
from tyype.datey import *
print(Datey.datey('\nData inválida.', '\nDigite o ano:', '\nDigite o mês:', '\nDigite o dia:', '%d/%m/%Y'))
```


### Recebe uma data(ano, mês e dia) como parâmetro e retorna a mesma no formato "date" caso seja válida, caso contrário "None" é retornado

Terminal(python3):
```txt
>>> from tyype.datey import *
>>> print(Datey.datey2('2021', 11, 21))
2021-11-21
```

Caso deseje um formato diferente:

```txt
>>> from tyype.datey import *
>>> print(Datey.datey2('2021', 11, 21, '%d/%m/%Y'))
21/11/2021
```