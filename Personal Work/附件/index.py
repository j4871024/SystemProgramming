# 在同個目錄下，建立 input.txt 檔案
# 裡面放入要測試的輸入

def char_type(ch):
    ascii_val = ord(ch)  # 取得 ASCII 編碼

    # 判斷是否為字母 (A-Z, a-z)
    if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
        return 'letter'

    # 判斷是否為數字 (0-9)
    elif 48 <= ascii_val <= 57:
        return 'digit'

    # 判斷是否為底線 (_)
    elif ascii_val == 95:
        return 'underscore'

    # 判斷是否為空白字元 (空格、tab、換行、Enter)
    elif ascii_val in (9, 10, 13, 32):
        return 'layout'

    else:
        return ch  # 其他字元


# 比較簡單的定義，只會是裡面的其中一個

# Separators
separators = {';'}

# Brackets
brackets = {'(', ')', '[', ']', '{', '}'}

# Binary Operators
binary_Operators = ['<=', '>=', '<>', '==', '+', '-', '*', '/', '<', '>', '=']

# Keywords
keywords = {'int', 'float', 'bool', 'void',
            'while', 'if', 'else', 'for', 'return'}

# Comments DFA
dfa_comments = {
    0: {'/': 1},
    1: {'*': 2},
    2: {'*': 3, 'other': 2},
    3: {'/': 4, '*': 3, 'other': 2}
}
comments_accept_states = {4}

# integer DFA
dfa_int = {
    0: {'digit': 1},
    1: {'digit': 1}
}
int_accept_states = {1}

# id DFA
dfa_id = {
    0: {'letter': 1},
    1: {'letter': 1, 'digit': 1, 'underscore': 2},
    2: {'letter': 3, 'digit': 3},
    3: {'letter': 3, 'digit': 3, 'underscore': 2},
}

id_accept_states = {1, 3}

# float DFA
dfa_float = {
    0: {'digit': 0, '.': 1},
    1: {'digit': 2},
    2: {'digit': 2, 'E': 3},
    3: {'digit': 5, '+': 4, '-': 4},
    4: {'digit': 5},
    5: {'digit': 5},
}
float_accept_states = {2, 5}


def run_dfa(dfa, accept_states, text, start):
    state = 0
    i = start
    last_accept = -1
    last_accept_pos = start - 1
    length = len(text)

    while i < length:
        c = text[i]
        t = char_type(c)

        # Comments DFA 特殊狀態轉移
        if dfa is dfa_comments:
            if state == 0:
                if c == '/':
                    state = 1
                else:
                    break
            elif state == 1:
                if c == '*':
                    state = 2
                else:
                    break
            elif state == 2:
                if c == '*':
                    state = 3
                else:
                    # 只要不是 '*', 留在狀態 2
                    state = 2
            elif state == 3:
                if c == '/':
                    state = 4
                elif c == '*':
                    state = 3
                else:
                    state = 2
            else:
                break

            if state in accept_states:
                last_accept = state
                last_accept_pos = i
            i += 1
            continue

        # 一般 DFA 狀態轉移
        transitions = dfa.get(state, {})

        if t in transitions:
            state = transitions[t]
        elif c in transitions:
            state = transitions[c]
        else:
            break

        if state in accept_states:
            last_accept = state
            last_accept_pos = i
        i += 1

    if last_accept == -1:
        return -1
    else:
        return last_accept_pos + 1


def lexer(text):
    i = 0
    length = len(text)
    tokens = []

    while i < length:
        c = text[i]
        t = char_type(c)

        # 跳過 layout
        if t == 'layout':
            i += 1
            continue

        try:
            # Comments DFA
            if text.startswith('/*', i):
                end_pos = run_dfa(
                    dfa_comments, comments_accept_states, text, i)
                if end_pos == -1:
                    tokens.append(('Binary Operators', '/'))
                    i += 1
                    continue
                else:
                    tokens.append(('Comments', text[i:end_pos]))
                    i = end_pos
                    continue

            # id DFA + keyword 判斷
            end_pos = run_dfa(dfa_id, id_accept_states, text, i)
            if end_pos != -1:
                word = text[i:end_pos]
                if word in keywords:
                    tokens.append(('Keyword', word))
                else:
                    tokens.append(('id', word))
                i = end_pos
                continue

            # float DFA
            end_pos = run_dfa(dfa_float, float_accept_states, text, i)
            if end_pos != -1:
                tokens.append(('float', text[i:end_pos]))
                i = end_pos
                continue

            # integer DFA
            end_pos = run_dfa(dfa_int, int_accept_states, text, i)
            if end_pos != -1:
                tokens.append(('integer', text[i:end_pos]))
                i = end_pos
                continue

            # 運算子優先匹配（長字串優先）
            matched_op = None
            for op in sorted(binary_Operators, key=lambda x: -len(x)):
                if text.startswith(op, i):
                    matched_op = op
                    break
            if matched_op:
                tokens.append(('Binary Operators', matched_op))
                i += len(matched_op)
                continue

            if c in brackets:
                tokens.append(('Brackets', c))
                i += 1
                continue

            if c in separators:
                tokens.append(('Separators', c))
                i += 1
                continue

            # 錯誤處理
            raise ValueError(f"Unknown token starting at position {i}: {c}")

        except ValueError as e:
            # 中止 lexer、印出目前 tokens
            print_results(tokens)

            raise e  # 讓主程式捕捉錯誤

    return tokens


def print_results(tokens):
    for ttype, val in tokens:
        print(f"{ttype:20}: {val}")


if __name__ == "__main__":
    try:
        with open("input.txt", "r", encoding="utf-8") as file:
            code = file.read()

        tokens = lexer(code)

        print_results(tokens)

    except ValueError as e:
        # 有錯誤的話就輸出錯誤訊息
        print(f"\nLexer Error: {e}")
