# Regular Expressions

$underscore \rightarrow \_$
$letter \rightarrow A|B...|Z|a|b...|z$
$digit \rightarrow 0|1|2...|9$
$underscore\_tail \rightarrow underscore\ (letter|digit)^+$
$id \rightarrow letter\ (letter|digit)^*\ underscore\_tail^*$
$fraction \rightarrow .\ digit^+$
$optional\_exponent \rightarrow (E\ (+|-|\varepsilon)\ digit^+)|\varepsilon$
$integer \rightarrow\ digit^+$
$float \rightarrow digit^*\ fraction\ optional\_exponent$

# DFA 過程

## id

$\varepsilon-closure(\{0\}) = \{0\} \Longrightarrow A$

$move(A, letter) = \{1\}$
$\varepsilon-closure(\{1\}) = \{1, 2, 3, 4, 5, 6\} \Longrightarrow B$ 

$move(A, digit) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(A, underscore\_tail) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, letter) = \{1, 4\}$
$\varepsilon-closure(\{1, 4\}) = \{1, 2, 3, 4, 5, 6\} \Longrightarrow B$

$move(B, digit) = \{1, 4\}$
$\varepsilon-closure(\{1, 4\}) = \{1, 2, 3, 4, 5, 6\} \Longrightarrow B$

$move(B, underscore\_tail) = \{4, 6\}$
$\varepsilon-closure(\{4, 6\}) = \{4, 5, 6\} \Longrightarrow C$

$move(C, letter) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(C, digit) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(C, underscore\_tail) = \{4, 6\}$
$\varepsilon-closure(\{4, 6\}) = \{4, 5, 6\} \Longrightarrow C$

| No | State | letter | digit | underscore_tail |
| - | - | - | - | - |
| 0 | A | B | - | - |
| 1 | B | B | B | C |
| 2 | C | - | - | C |

## fraction

$\varepsilon-closure(\{0\}) = \{0\} \Longrightarrow A$

$move(A, \cdot) = \{1\}$
$\varepsilon-closure(\{1\}) = \{1, 2\} \Longrightarrow B$ 

$move(A, digit) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, \cdot) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, digit) = \{1, 3\}$
$\varepsilon-closure(\{1, 3\}) = \{1, 2, 3\} \Longrightarrow C$

$move(C, \cdot) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(C, digit) = \{1, 3\}$
$\varepsilon-closure(\{1, 3\}) = \{1, 2, 3\} \Longrightarrow C$

| No | State | $\cdot$ | digit |
| - | - | - | - |
| 0 | A | B | - |
| 1 | B | - | C |
| 2 | C | - | C |

## optional_exponent

$\varepsilon-closure(\{0\}) = \{0, 1, 2, 3\} \Longrightarrow A$

$move(A, E) = \{4\}$
$\varepsilon-closure(\{4\}) = \{4, 5, 6, 7, 8, 9\} \Longrightarrow B$

$move(A, +) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(A, -) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(A, digit) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, E) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, +) = \{8\}$
$\varepsilon-closure(\{8\}) = \{8, 9\} \Longrightarrow C$

$move(B, -) = \{8\}$
$\varepsilon-closure(\{8\}) = \{8, 9\} \Longrightarrow C$

$move(B, digit) \{3, 8\}$
$\varepsilon-closure(\{3, 8\}) = \{3, 8, 9\} \Longrightarrow D$

$move(C, E) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(C, +) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(C, -) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(C, digit) \{3, 8\}$
$\varepsilon-closure(\{3, 8\}) = \{3, 8, 9\} \Longrightarrow D$

$move(D, E) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(D, +) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(D, -) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(D, digit) \{3, 8\}$
$\varepsilon-closure(\{3, 8\}) = \{3, 8, 9\} \Longrightarrow D$

| No | State | E | + | - | digit |
| - | - | - | - | - | - |
| 0 | A | B | - | - | - |
| 1 | B | - | C | C | D |
| 2 | C | - | - | - | D |
| 3 | D | - | - | - | D |

## float

$\varepsilon-closure(\{0\}) = \{0, 1, 2\} \Longrightarrow A$

$move(A, digit) = \{0, 2\}$
$\varepsilon-closure(\{0, 2\}) = \{0, 1, 2\} \Longrightarrow A$

$move(A, fraction) = \{3\}$
$\varepsilon-closure(\{3\}) = \{3\} \Longrightarrow B$

$move(A, optional\_exponent) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, digit) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, fraction) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, optional\_exponent) = \{4\}$
$\varepsilon-closure(\{4\}) = \{4\} \Longrightarrow C$

$move(C, digit) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(C, fraction) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(C, optional\_exponent) = \phi$
$\varepsilon-closure(\phi) = \phi$

| No | State | digit | fraction | optional_exponent |
| - | - | - | - | - |
| 0 | A | A | B | - |
| 1 | B | - | - | C |
| 2 | C | - | - | - |

## underscore

$\varepsilon-closure(\{0\}) = \{0\} \Longrightarrow A$

$move(A, \_) = \{1\}$
$\varepsilon-closure(\{1\}) = \{1\} \Longrightarrow B$

$move(B, \_) = \phi$
$\varepsilon-closure(\phi) = \phi$

| No | State | _ |
| - | - | - |
| 0 | A | B |
| 1 | B | - |

## letter

$\varepsilon-closure(\{0\}) = \{0\} \Longrightarrow A$

$move(A, [A-Za-z]) = \{1\}$
$\varepsilon-closure(\{1\}) = \{1\} \Longrightarrow B$

$move(B, [A-Za-z]) = \phi$
$\varepsilon-closure(\phi) = \phi$

| No | State | [A-Za-z] |
| - | - | - |
| 0 | A | B |
| 1 | B | - |

## digit

$\varepsilon-closure(\{0\}) = \{0\} \Longrightarrow A$

$move(A, [0-9]) = \{1\}$
$\varepsilon-closure(\{1\}) = \{1\} \Longrightarrow B$

$move(B, [0-9]) = \phi$
$\varepsilon-closure(\phi) = \phi$

| No | State | [0-9] |
| - | - | - |
| 0 | A | B |
| 1 | B | - |

## underscore_tail

$\varepsilon-closure(\{0\}) = \{0\} \Longrightarrow A$

$move(A, underscore) = \{1\}$
$\varepsilon-closure(\{1\}) = \{1, 2, 3\} \Longrightarrow B$

$move(A, letter) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(A, digit) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, underscore) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, letter) = \{1, 4\}$
$\varepsilon-closure(\{1, 4\}) = \{1, 2, 3, 4\} \Longrightarrow C$

$move(B, digit) = \{1, 4\}$
$\varepsilon-closure(\{1, 4\}) = \{1, 2, 3, 4\} \Longrightarrow C$

$move(C, underscore) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(C, letter) = \{1, 4\}$
$\varepsilon-closure(\{1, 4\}) = \{1, 2, 3, 4\} \Longrightarrow C$

$move(C, digit) = \{1, 4\}$
$\varepsilon-closure(\{1, 4\}) = \{1, 2, 3, 4\} \Longrightarrow C$

| No | State | underscore | letter | digit |
| - | - | - | - | - |
| 0 | A | B | - | - |
| 1 | B | - | C | C |
| 2 | C | - | C | C |

## integer

$\varepsilon-closure(\{0\}) = \{0, 1\} \Longrightarrow A$

$move(A, digit) = \{0, 2\}$
$\varepsilon-closure(\{0, 2\}) = \{0, 1, 2\} \Longrightarrow B$

$move(B, digit) = \{0, 2\}$
$\varepsilon-closure(\{0, 2\}) = \{0, 1, 2\} \Longrightarrow B$

| No | State | digit |
| - | - | - |
| 0 | A | B |
| 1 | B | B |

## ID Plus

$\varepsilon-closure(\{0\}) = \{0\} \Longrightarrow A$

$move(A, letter) = \{1\}$
$\varepsilon-closure(\{1\}) = \{1, 2, 4\} \Longrightarrow B$

$move(A, digit) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(A, underscore) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, letter) = \{1, 4\}$
$\varepsilon-closure(\{1, 4\}) = \{1, 2, 4\} \Longrightarrow B$

$move(B, digit) = \{1, 4\}$
$\varepsilon-closure(\{1, 4\}) = \{1, 2, 4\} \Longrightarrow B$

$move(B, underscore) = \{3\}$
$\varepsilon-closure(\{3\}) = \{3\} \Longrightarrow C$

$move(C, letter) = \{4\}$
$\varepsilon-closure(\{4\}) = \{2, 4\} \Longrightarrow D$

$move(C, digit) = \{4\}$
$\varepsilon-closure(\{4\}) = \{2, 4\} \Longrightarrow D$

$move(C, underscore) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(D, letter) = \{4\}$
$\varepsilon-closure(\{4\}) = \{2, 4\} \Longrightarrow D$

$move(D, digit) = \{4\}$
$\varepsilon-closure(\{4\}) = \{2, 4\} \Longrightarrow D$

$move(D, underscore) = \{3\}$
$\varepsilon-closure(\{3\}) = \{3\} \Longrightarrow C$

| No | State | letter | digit | underscore |
| - | - | - | - | - |
| 0 | A | B | - | - |
| 1 | B | B | B | C |
| 2 | C | D | D | - |
| 3 | D | D | D | C |

## float plus

$\varepsilon-closure(\{0\}) = \{0, 1\} \Longrightarrow A$

$move(A, digit) = \{0\}$
$\varepsilon-closure(\{0\}) = \{0, 1\} \Longrightarrow A$

$move(A, \cdot) = \{2\}$
$\varepsilon-closure(\{2\}) = \{2\} \Longrightarrow B$

$move(A, E) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(A, +) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(A, -) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, digit) = \{3\}$
$\varepsilon-closure(\{3\}) = \{3, 4\} \Longrightarrow C$

$move(B, \cdot) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, E) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, +) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(B, -) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(C, digit) = \{3\}$
$\varepsilon-closure(\{3\}) = \{3, 4\} \Longrightarrow C$

$move(C, \cdot) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(C, E) = \{5\}$
$\varepsilon-closure(\{5\}) = \{5\} \Longrightarrow D$

$move(C, +) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(C, -) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(D, digit) = \{7\}$
$\varepsilon-closure(\{7\}) = \{7\} \Longrightarrow E$

$move(D, \cdot) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(D, E) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(D, +) = \{6\}$
$\varepsilon-closure(\{6\}) = \{6\} \Longrightarrow F$

$move(D, -) = \{6\}$
$\varepsilon-closure(\{6\}) = \{6\} \Longrightarrow F$

$move(E, digit) = \{7\}$
$\varepsilon-closure(\{7\}) = \{7\} \Longrightarrow E$

$move(E, \cdot) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(E, E) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(E, +) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(E, -) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(F, digit) = \{7\}$
$\varepsilon-closure(\{7\}) = \{7\} \Longrightarrow E$

$move(F, \cdot) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(F, E) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(F, +) = \phi$
$\varepsilon-closure(\phi) = \phi$

$move(F, -) = \phi$
$\varepsilon-closure(\phi) = \phi$

| No | State | $\cdot$ | digit | E | + | - |
| - | - | - | - | - | - | - |
| 0 | A | B | A | - | - | - |
| 1 | B | - | C | - | - | - |
| 2 | C | - | C | D | - | - |
| 3 | D | - | E | - | F | F |
| 4 | E | - | E | - | - | - |
| 5 | F | - | E | - | - | - |