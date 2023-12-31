
# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконала: Хижняк Єлизавета Дмитрівна (Група ІР-24)

### Лабораторна робота №1 (Варіант 3 Рівень 3)

Напишіть функцію, яка приймає невпорядкований масив цілих чисел і повертає довжину найдовшої пікової підпослідовностію Для формування пікової підпослідовності необхідно мінімум 3 числа. Пікова підпослідовність визначається як послідовність чисел, яка починається з меншого числа, після чого наступне число строго більше попереднього, поки вони не досягнуть вершини (максимального значення у підпослідовності). Всі значення після досягнення вершини мають бути завжди меншими від попередника. Наприклад, пікова послідовність може мати вигляд:

1 7 2
Де 7 - є вершиною послідовності

1 2 3 - не є піковою послідовністю (немає лівої частки)
3 2 1 - також не є піковою полідовністю (немає правої частки)
-1 -5 -1 - теж не є піковою послідовністю (необхідно знайти вершину, а не впадину)

У масиві може бути декілька пікових підпослідовностей, необхідно знайти довжину максимальної

Приклад
Для вхідного масиву: 1, 3, 5, 4, 2, 8, 3, 7,  знайдена найдовша пікова підпослідовність має довжину 5 - 1, 3, 5, 4, 2

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити сценарії коли: 
всі елементи масиву посортовані за зростанням, 
посортовані за спаданням, 
масив з 2х елементів, 
не містять пікових підпослідовностей, 
містять 3 пікові послідовності

# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконала: Хижняк Єлизавета Дмитрівна (Група ІР-24)

### Лабораторна робота №2 (Варіант 3 Рівень 3)

Фермер Джон побудував новий довгий загін для худоби, з N (2 <= N <= 100,000) секцій. Секції розташовуються уздовж прямої лінії в положеннях x1, ..., xN (0 <= x-i <= 1 000 000 000).

Його C (2 <= C <= N) корів не люблять нову будівлю і стають агресивними одна до одної, коли вони поставлені в сусідні стійла. Щоб уникнути ситуації, коли корови можуть заподіяти шкоду одна одній, фермер хоче розташувати агресивних корів у стійлах таким чином, щоб мінімальна відстань між будь-якими з них була настільки великою, наскільки це можливо. Яка найбільша мінімальна відстань?


Вхідні дані функції:  
N = 5
С = 3  
free_sections = `[1, 2, 8, 4, 9]

Результат
3

Пояснення: 
У фермера є 5 корів, з яких 3 агресивні. Їх можна роташувати в стійлах 1, 4 та 8 або 1,4, 9. Таким чином мінімальне значення максимальної дистанції становить 3

Підказка:

Оскільки у нас є щонайменше дві корови, найкраще, що ми можемо зробити, це розташувати їх у загоні у першому вільному стійлі і в кінці



# Лабораторні роботи з дисципліни "Алгоритми і структур даних"

## Виконала: Хижняк Єлизавета Дмитрівна (Група ІР-24)

### Лабораторна робота №3 (Варіант 3 Рівень 3)

Для заданого бінарного дерева  реалізуйте функцію, яка обчислює та повертає значення максимального діаметра у бінарному дереві - найвіддаленішу відстань між двома листками. Максимальний діаметр у бінарному дереві визначає найбільшу відстань між будь-якою парою листків (кінцевих вузлів) у дереві. Діаметр вимірюється як кількість ребер, які потрібно пройти, щоб дістатися одного листка від іншого. Максимальний діаметр не обов'язково має включати в себе кореневий вузол 

Нехай у вас задане бінарне дерево такого вигляду:
```
        1
       /  \
      3    2
     / \
    7   4
   /     \
  8       5
 /         \
9           6
```

Для даного дерева максимальний діаметр становить 6: `9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6` -  для проходження від листка 9 до листка 6 слід пройти 6 ребер.

Реалізована вами функція `binary_tree_diameter(tree: BinaryTree) -> int` отримує на вхід корінь бінарного дерева та повертає максимальний діаметр дерева.

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:

```
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу `BinaryTree` наступним чином:

```
root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
```


# Лабораторні роботи з дисципліни "Алгоритми і структур даних"

## Виконала: Хижняк Єлизавета Дмитрівна (Група ІР-24)

### Лабораторна робота №4 (Варіант 1 Рівень 3)

Flood fill (також відомий як початкове заповнення) — це алгоритм, який визначає область, в яку входить певний вузол в багатовимірному масиві.

Він використовується в інструменті заповнення «ковша» програми малювання, щоб заповнити з’єднані, однаково забарвлені області іншим кольором, а також у таких іграх, як Go та Minesweeper.
Застосування для заповнення кольором певної обмеженої області також називається заливкою межі.

Алгоритм заливки приймає три параметри: початковий вузол, цільовий колір і колір заміни.

Розглянемо наступну матрицю (див. рисунок) 

Нехай ліворуч оригінальне значення кольоріів. Якщо початковий вузол (3, 9), цільовий колір — «ЧОРНИЙ», а колір заміни — «СІРИЙ», тоді алгоритм шукає всі вузли в матриці, які з’єднані з початковим вузлом таким самим кольором та змінює їх на колір заміни. Результат роботи алгоритму наведено праворуч



Формат даних у вхідному файлі input.txt
перший рядок: висота та ширина поля, яке містить кольорові елементи (розділені комою)
другий рядок: координати початкової точки, з якої слід починати зміну кольору
третій рядок: колір заміни

Приклад даних для рисунку зліва:
10,10
3,9
‘G’
      ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']

Результат:
файл output.txt містить значення кольорів комірок поля після виконання заміни (для рисунку справа)

		[‘Y’, ‘Y’, ‘Y’, ‘G’, ‘G’, ‘G’, ‘G’, ‘G’, ‘G’, ‘G’]
[‘Y’, ‘Y’, ‘Y’, ‘Y’, ‘Y’, ‘Y’, ‘G’, ‘C’, ‘C’, ‘C’]
[‘G’, ‘G’, ‘G’, ‘G’, ‘G’, ‘G’, ‘G’, ‘C’, ‘C’, ‘C’]
[‘W’, ‘W’, ‘W’, ‘W’, ‘W’, ‘G’, ‘G’, ‘G’, ‘G’, ‘C’]
[‘W’, ‘R’, ‘R’, ‘R’, ‘R’, ‘R’, ‘G’, ‘C’, ‘C’, ‘C’]
[‘W’, ‘W’, ‘W’, ‘R’, ‘R’, ‘G’, ‘G’, ‘C’, ‘C’, ‘C’]
[‘W’, ‘B’, ‘W’, ‘R’, ‘R’, ‘R’, ‘R’, ‘R’, ‘R’, ‘C’]
[‘W’, ‘B’, ‘B’, ‘B’, ‘B’, ‘R’, ‘R’, ‘C’, ‘C’, ‘C’]
[‘W’, ‘B’, ‘B’, ‘C’, ‘B’, ‘B’, ‘B’, ‘B’, ‘C’, ‘C’]
[‘W’, ‘B’, ‘B’, ‘C’, ‘C’, ‘C’, ‘C’, ‘C’, ‘C’, ‘C’]

# Лабораторні роботи з дисципліни "Алгоритми і структур даних"

## Виконала: Хижняк Єлизавета Дмитрівна (Група ІР-24)

### Лабораторна робота №5 (Варіант 1 Рівень 3)
Критично важливим є постачання газу між сховищами та містами пінгвінів взимку. Вибух газопроводів може призвести до дефіциту палива та викликати значні проблеми у домівках бравих пінгвінів. Тому ряд газопроводів зараз відключили для ремонту.

Ви, як студент курсу Алгоритми і структури даних маєте бажання допомогти Пінгвінам. Ви готові написати для них алгоритм, який перевірить, чи існує спосіб транспортування палива з будь-якого сховища до будь якого міста з використанням газопроводів, які не вивели в ремонт. Зауважте, що газ по трубі можна транспортувати лише в одному напрямку.

Для розв'язання цієї задачі пінгвіни надали вам:

список міст

список газосховищ

список активних газопроводів, у форматі [ ['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Сховище_2'] ], де ['Львів', 'Стрий'] означає наявність газопроводу між містами Львів та Стрий, де подача газу відбувається від Львова до Стрия

Ваша програма має повернути результат у форматі: [ 'газосховище', ['місто_1', 'місто_2'] , де:

газосховище - назва газосховища
['місто_1', 'місто_2'] - список міст, до яких неможливо подати газ з цього газосховища
Зауважте, що газ може подаватись з газосховища до будь якого міста транзитом через інші міста.

У випадку, якщо є зв'язок між усіма газосховищами та містами, поверніть пустий список

# Лабораторні роботи з дисципліни "Алгоритми і структур даних"

## Виконала: Хижняк Єлизавета Дмитрівна (Група ІР-24)

### Лабораторна робота №6 (Варіант 1 Рівень 3)
Створити клас структури даних Trie (префіксне дерево), який містить методи вставки слова, пошуку слова та пошуку префіксу. Реалізувати функцію на мові програмування Python, яка отримує список стрічок patterns і повертає об'єкт класу Trie


