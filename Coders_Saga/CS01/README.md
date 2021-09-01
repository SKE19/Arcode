## Coder's Saga, Pt. I: One True Hero

---

*Keys: Fundamentals, Lists, Dictionary*

*Puzzle by [GToidZ](https://github.com/GToidZ)*

### Introduction

The world is doomed to fall into the hands of Lord Buggertron, King of all Glitchers and what the world needs now is a "hero!" But, who would be a hero suitable for this task? Though everyone can beat little Glitchers but the gatekeeper of the first dungeon, Errormancer will always beat heroes with random powers. He is the first obstacle and must be defeated to get to Lord Buggertron!

### Objective

Write a program that will find a suitable hero for a task to defeat the Errormancer.

**The program will take `n` number of inputs.** Each input are formatted like this, **`name,a,b,c,d`**, for `name` is a name of a hero, `a` is a number for Strength (STR) attribute of a hero, `b` is a number for Dexterity (DEX) attribute of a hero, `c` is a number for Intelligence (INT) attribute of a hero, `d` is a number for Luck (LUK) attribute of a hero.

The data for each hero is also registered in the guild, so they decided to use `dictionary` to pair each heroes with their `list` of attributes.

```python

heroes = {
	"name": [STR,DEX,INT,LUK]
	...
}

```

**The guild also has a scout to provide what the Errormancer is vulnerable to. It is found that the Errormancer is weak to heroes that has the same attribute with him that has equal or higher value of him. For example, the Errormancer chosen STR of `16` will be vulnerable to a hero with STR of `>=16`.**

The wizard also prepares his spell template but requires some parameters, take a look at the `def` block below:

```python

def find_hero(attribute, score):
	''' Finds hero(es) that can defeat the Errormancer.
	Parameters
	attribute (int): the attribute chosen for comparison
					 (1: STR, 2: DEX, 3: INT, 4: LUK)
	score (int): the score of the attribute chosen
	
	Returns
	list: list of hero names that can defeat the Errormancer
	None if there are no heroes suitable for deafeating the Errormancer
	'''

	return None  # When there are no heroes suitable for the task, the land may need to wait another day.
```

**The program does not need to print anything, the wizard will only use `find_hero` function.**

### Input Constraints

- 1 <= `n` <= 999 ; Number of heroes enlisted, for the next `n` lines.
- When enlisting a hero, `a,b,c,d` each of them is not more than 30.
- The names will never be the same and starts with a capital letter.

### Hints

- If a hero tries to enlist with a stat that exceeded the maximum of 30, he or she might be a monster in disguise, he or she shouldn't be in the list.

### Sample Test Cases (find_hero parameters are randomized in test cases.)

```python

>>> 3
>>> Howard,16,4,12,17
>>> Janice,10,26,10,5
>>> Ophelia,9,10,24,19
>>> find_hero(2, 18)
['Janice']

```

```python
>>> 3
>>> Howard,16,4,12,17
>>> Janice,10,26,10,5
>>> Ophelia,9,10,24,19
>>> find_hero(1, 10)
['Howard','Janice']
```

```python
>>> 3
>>> Howard,16,4,12,17
>>> Janice,10,26,10,5
>>> DemonLord,32,32,32,32
>>> heroes
{'Howard': [16,4,12,17], 'Janice': [10,26,10,5]}
>>> find_hero(4, 20)
None
```

<br>

## Running Your Program
---
You may clone this repository or download [cs01_test.py](https://github.com/SKE19/Arcode/blob/main/Coders_Saga/CS01/cs01_test.py) and [dict.txt](https://github.com/SKE19/Arcode/blob/main/Coders_Saga/CS01/dict.txt) to get started.

- Create a new file named **cs01.py** with **cs01_test.py** in your working directory.
- Copy the template below to **cs01.py** and start coding!
- Once you're done coding, try running **cs01_test.py** to see if you've passed all the cases! Happy hacking!

```python
def find_hero(attribute, score):
    '''
    Finds hero(es) that can defeat the Errormancer.
    
    Parameters
    attribute (int): the attribute chosen for comparison
                     (1: STR, 2: DEX, 3: INT, 4: LUK)
    score (int): the score of the attribute chosen
    
    Returns
    list: list of hero names that can defeat the Errormancer
    None if there are no heroes suitable for deafeating the Errormancer
    '''
    heroes = dict()

    n = int(input(''))
    for _ in range(n):
		...

    return None # When there are no heroes suitable for the task, the land may need to wait another day.
```

```console
foo@bar:~$ py cs01_test.py
```
