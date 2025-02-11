import random

languages = {
    "1": "English",
    "2": "فارسی",
    "3": "Español",
    "4": "Français",
    "5": "Deutsch",
    "6": "Italiano",
    "7": "日本語",
    "8": "한국어",
    "9": "русский",
    "10": "中文"
}

# Display language selection menu
def select_language():
    print("Please select a language:")
    for key, value in languages.items():
        print(f"{key}: {value}")
    choice = input("Enter the number of your choice: ").strip()
    return languages.get(choice, "English")

# Get the selected language
language = select_language()

# Translations for messages
translations = {
    "English": {
        "welcome": "Welcome to Minesweeper!",
        "select_action": "Enter 'f' to flag, 'u' to unflag, or 'r' to reveal: ",
        "enter_row": "Enter row (0-5): ",
        "enter_column": "Enter column (0-5): ",
        "game_over": "Game Over! You hit a mine!",
        "congratulations": "Congratulations! You've cleared the board!",
        "invalid_input": "Invalid input! Please enter numbers between 0 and 5."
    },
    "فارسی": {
        "welcome": "به مین‌یاب خوش آمدید!",
        "select_action": "برای پرچم‌گذاری 'f'، برای برداشتن پرچم 'u' یا برای نمایش 'r' را وارد کنید: ",
        "enter_row": "ردیف را وارد کنید (0-5): ",
        "enter_column": "ستون را وارد کنید (0-5): ",
        "game_over": "بازی تمام شد! شما روی مین ضربه خوردید!",
        "congratulations": "تبریک! شما تخته را پاک کرده‌اید!",
        "invalid_input": "ورودی نامعتبر! لطفا اعداد بین 0 تا 5 را وارد کنید."
    },
    "Español": {
        "welcome": "¡Bienvenido a Buscaminas!",
        "select_action": "Ingrese 'f' para marcar, 'u' para desmarcar, o 'r' para revelar: ",
        "enter_row": "Ingrese la fila (0-5): ",
        "enter_column": "Ingrese la columna (0-5): ",
        "game_over": "¡Fin del juego! ¡Pisaste una mina!",
        "congratulations": "¡Felicidades! ¡Has limpiado el tablero!",
        "invalid_input": "¡Entrada no válida! Por favor, ingrese números entre 0 y 5."
    },
    "Français": {
        "welcome": "Bienvenue à Démineur!",
        "select_action": "Entrez 'f' pour marquer, 'u' pour démarquer, ou 'r' pour révéler: ",
        "enter_row": "Entrez la rangée (0-5): ",
        "enter_column": "Entrez la colonne (0-5): ",
        "game_over": "Jeu terminé! Vous avez touché une mine!",
        "congratulations": "Félicitations! Vous avez dégagé le plateau!",
        "invalid_input": "Entrée non valide! Veuillez entrer des numéros entre 0 et 5."
    },
    "Deutsch": {
        "welcome": "Willkommen bei Minesweeper!",
        "select_action": "Geben Sie 'f' ein, um zu markieren, 'u' um zu demarkieren oder 'r' um zu enthüllen: ",
        "enter_row": "Geben Sie die Reihe ein (0-5): ",
        "enter_column": "Geben Sie die Spalte ein (0-5): ",
        "game_over": "Spiel vorbei! Sie haben eine Mine getroffen!",
        "congratulations": "Herzlichen Glückwunsch! Sie haben das Brett geräumt!",
        "invalid_input": "Ungültige Eingabe! Bitte geben Sie Zahlen zwischen 0 und 5 ein."
    },
    "Italiano": {
        "welcome": "Benvenuto a Campo Minato!",
        "select_action": "Inserisci 'f' per segnare, 'u' per deselezionare, o 'r' per rivelare: ",
        "enter_row": "Inserisci la fila (0-5): ",
        "enter_column": "Inserisci la colonna (0-5): ",
        "game_over": "Gioco finito! Hai colpito una mina!",
        "congratulations": "Congratulazioni! Hai liberato la tavola!",
        "invalid_input": "Input non valido! Per favore inserisci numeri tra 0 e 5."
    },
    "日本語": {
        "welcome": "マインスイーパーへようこそ！",
        "select_action": "'f'を入力してフラグを立て、'u'でフラグを解除し、'r'で開示します: ",
        "enter_row": "行を入力してください (0-5): ",
        "enter_column": "列を入力してください (0-5): ",
        "game_over": "ゲームオーバー！ 地雷に当たりました！",
        "congratulations": "おめでとうございます！ ボードをクリアしました！",
        "invalid_input": "無効な入力です！ 0から5の数字を入力してください。"
    },
    "한국어": {
        "welcome": "지뢰찾기에 오신 것을 환영합니다!",
        "select_action": "'f'를 입력하여 깃발을 지정하고 'u'로 깃발을 취소하고 'r'로 표시합니다: ",
        "enter_row": "행을 입력하세요 (0-5): ",
        "enter_column": "열을 입력하세요 (0-5): ",
        "game_over": "게임 오버! 지뢰를 밟았습니다!",
        "congratulations": "축하합니다! 보드를 청소했습니다!",
        "invalid_input": "유효하지 않은 입력입니다! 0에서 5 사이의 숫자를 입력하세요."
    },
    "русский": {
        "welcome": "Добро пожаловать в Сапёр!",
        "select_action": "Введите 'f' чтобы пометить, 'u' чтобы снять метку, или 'r' чтобы открыть: ",
        "enter_row": "Введите ряд (0-5): ",
        "enter_column": "Введите столбец (0-5): ",
        "game_over": "Игра окончена! Вы наткнулись на мину!",
        "congratulations": "Поздравляем! Вы очистили доску!",
        "invalid_input": "Неверный ввод! Пожалуйста, введите числа от 0 до 5."
    },
    "中文": {
        "welcome": "欢迎来到扫雷游戏！",
        "select_action": "输入'f'标记，'u'取消标记，或'r'揭示: ",
        "enter_row": "输入行 (0-5): ",
        "enter_column": "输入列 (0-5): ",
        "game_over": "游戏结束！ 你踩到了一颗地雷！",
        "congratulations": "恭喜！ 你已经清理了棋盘！",
        "invalid_input": "输入无效！ 请输入0到5之间的数字。"
    }
}

# Get the translated messages based on selected language
messages = translations.get(language, translations["English"])

# Game settings
width = 6
height = 6
num_mines = 5

# Create the game board
def create_board():
    board = [['+' for _ in range(width)] for _ in range(height)]
    return board

# Place mines randomly on the board
def place_mines(board):
    mines = 0
    while mines < num_mines:
        x = random.randint(0, height - 1)
        y = random.randint(0, width - 1)
        if board[x][y] != '@':
            board[x][y] = '@'
            mines += 1

# Calculate numbers for each cell
def calculate_numbers(board):
    for x in range(height):
        for y in range(width):
            if board[x][y] == '@':
                continue
            count = 0
            for i in range(max(0, x-1), min(height, x+2)):
                for j in range(max(0, y-1), min(width, y+2)):
                    if board[i][j] == '@':
                        count += 1
            board[x][y] = count if count > 0 else ' '

# Display the board
def display_board(board):
    print("  " + " ".join(str(i) for i in range(width)))
    for idx, row in enumerate(board):
        print(idx, " ".join(str(cell) for cell in row))

# Reveal empty cells recursively
def reveal_empty_cells(board, revealed, x, y):
    if revealed[x][y] != '+':
        return
    revealed[x][y] = board[x][y]
    if board[x][y] == ' ':
        for i in range(max(0, x-1), min(height, x+2)):
            for j in range(max(0, y-1), min(width, y+2)):
                if (i, j) != (x, y):
                    reveal_empty_cells(board, revealed, i, j)

# Play the Minesweeper game
def play_game():
    print(messages["welcome"])
    board = create_board()
    place_mines(board)
    calculate_numbers(board)
    
    revealed = [['+' for _ in range(width)] for _ in range(height)]
    
    while True:
        display_board(revealed)
        try:
            action = input(messages["select_action"]).strip().lower()
            x = int(input(messages["enter_row"]))
            y = int(input(messages["enter_column"]))
            
            if action == 'f':
                revealed[x][y] = "F"
            elif action == 'u':
                if revealed[x][y] == "F":
                    revealed[x][y] = '+'
                else:
                    print("No flag to remove at this position.")
            elif action == 'r':
                if board[x][y] == '@':
                    print(messages["game_over"])
                    display_board(board)
                    break
                else:
                    if board[x][y] == ' ':
                        reveal_empty_cells(board, revealed, x, y)
                    else:
                        revealed[x][y] = board[x][y]
                
                    # Check if all non-mine cells are revealed
                    if all(revealed[i][j] != '+' or board[i][j] == '@' for i in range(height) for j in range(width)):
                        print(messages["congratulations"])
                        display_board(board)
                        break
                    
        except (ValueError, IndexError):
            print(messages["invalid_input"])

# Start the game
play_game()
