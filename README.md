# Tyype

Um pacote com com objetivo de tratar dados de entrada.

## Instalação

### Instalação via pip:

```sh
python -m pip install -U Tyype
```

## Como Usar

### Lê um valor da entrada padrão e retorna o mesmo caso seja inteiro, caso contrário "None" é retornado

```python
from tyype.tyype import Tyype
Tyype.inty()
```

Para ler valores de ponto flutuante:

```python
from tyype.tyype import Tyype
Tyype.floaty()
```

### Lê um valor da entrada padrão enquanto o mesmo não for inteiro, a cada tentativa e impresso a mensagem de erro passada como parâmetro

```python
from tyype.tyype import Tyype
Tyype.inty('\nDigite um número inteiro.')
```

Para ler valores de ponto flutuante:

```python
from tyype.tyype import Tyype
Tyype.floaty('\nDigite um número.')
```

### Retorna uma lista contendo os valores inteiros passados como argumento na linha de comando

Terminal:
```txt
$ python3 test.py w 3 w 5 6 8
[3, 5, 6, 8]
```

Código:
```python
from tyype.tyype import Tyype
Tyype.inty(1)
```

Caso queira passar mais de um valor por argumento basta passar o parâmetro do "split", nesse caso o método retorna uma lista de listas.

Código:
```python
from tyype.tyype import Tyype
Tyype.inty(1, ',')
```

Terminal:
```txt
$python3 test.py w 3,4,5,6,7 w 5,6.4,3 6 8
[[3, 4, 5, 6, 7], [5, 3], [6], [8]]
```

Para valores de ponto flutuante

Código:
```python
from tyype.tyype import Tyype
Tyype.floaty(1)
Tyype.floaty(1, ',')
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
from tyype.tyype import Tyype
print(Tyype.inty(2))
```

E possível especificar como arquivo está dividido

Código:
```python
from tyype.tyype import Tyype
print(Tyype.inty(2, ' '))
```

Terminal(os testes sempre utilizam o mesmo arquivo):
```txt
$ python3 test.py test.txt
[[1, 4, 1, 1, 2, 5, 2, 3, 987, 2323]]
```

Para valores de ponto flutuante

Código:
```python
from tyype.tyype import Tyype
Tyype.floaty(2)
Tyype.floaty(2, ' ')
```

### Lê uma data(ano, mês e dia) da entrada padrão enquanto a mesma não for válida, a cada tentativa e impresso a mensagem de erro passada como parâmetro

```python
from tyype.tyype import Tyype
Tyype.datey('\nData inválida.')
```

É possível especificar a mensagem para o usuário

```python
from tyype.tyype import Tyype
Tyype.datey('\nData inválida.', '\nDigite o ano:', '\nDigite o mês:', '\nDigite o dia:')
```

### Recebe um valor como parâmetro e retorna o mesmo caso seja inteiro, caso contrário "None" é retornado

Terminal(python3):
```txt
>>> from tyype.tyype import Tyype
>>> print(Tyype.inty2(3))
3
>>> print(Tyype.inty2('3'))
3
>>> print(Tyype.inty2('3.5'))
None
>>> print(Tyype.inty2('dsd'))
None
```

Para valores de ponto flutuante:

```txt
>>> from tyype.tyype import Tyype
>>> print(Tyype.floaty2('3.5'))
3.5
```

### Recebe uma data(ano, mês e dia) como parâmetro e retorna a mesma no formato "date" caso seja válida, caso contrário "None" é retornado

Terminal(python3):
```txt
>>> from tyype.tyype import Tyype
>>> print(Tyype.datey2('2021', 11, 21))
21/11/2021
```

Caso deseje um formato diferente:

```txt
>>> from tyype.tyype import Tyype
>>> print(Tyype.datey2('2021', 11, 21, '%Y-%m-%d'))
2021-11-21
```

### Recebe um arquivo como parâmetro e retorna uma lista com todos os números inteiros

Terminal(python3):
```txt
>>> from tyype.tyype import Tyype
>>> print(Tyype.intyFile('test.txt'))
[1, 4, 1, 1, 2, 5, 2, 2, 3, 2, 7, 3, 3, 4, 4, 9, 8, 7, 3, 2, 3, 2, 3, 2, 3, 4]
```

E possível especificar como arquivo está dividido

Terminal(python3):
```txt
>>> from tyype.tyype import Tyype
>>> print(Tyype.intyFile('test.txt', ' '))
[1, 4, 1, 1, 2, 5, 2, 3, 987, 2323]
```

Para valores de ponto flutuante:

```txt
>>> from tyype.tyype import Tyype
>>> print(Tyype.floatyFile('test.txt', ' '))
[1.0, 4.0, 1.0, 1.0, 2.0, 5.0, 2.0, 2.3, 2.7, 3.0, 3.44, 987.0, 2323.0]
```