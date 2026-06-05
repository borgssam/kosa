# 구구단 프로그램

def print_multiplication_table(dan):
    """특정 단의 구구단을 출력합니다."""
    print(f"\n===== {dan}단 =====")
    for i in range(1, 10):
        result = dan * i
        print(f"{dan} × {i} = {result}")


def print_all_tables():
    """2단부터 9단까지 모든 구구단을 출력합니다."""
    for dan in range(2, 10):
        print_multiplication_table(dan)


def interactive_mode():
    """대화형 모드로 구구단을 조회합니다."""
    while True:
        try:
            dan = int(input("\n조회할 단을 입력하세요 (2-9, 0은 종료): "))
            
            if dan == 0:
                print("프로그램을 종료합니다.")
                break
            
            if 2 <= dan <= 9:
                print_multiplication_table(dan)
            else:
                print("2부터 9 사이의 숫자를 입력하세요.")
        
        except ValueError:
            print("숫자를 입력하세요.")


if __name__ == "__main__":
    print("구구단 프로그램")
    print("1. 전체 구구단 출력")
    print("2. 특정 단 조회")
    
    choice = input("\n선택 (1 또는 2): ")
    
    if choice == "1":
        print_all_tables()
    elif choice == "2":
        interactive_mode()
    else:
        print("잘못된 선택입니다.")
