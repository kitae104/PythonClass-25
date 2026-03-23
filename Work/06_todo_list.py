def add_todo(todos: list, title: str) -> None:
    """할 일 추가"""
    todos.append({"title": title.strip(), "done": False})

def toggle_todo(todos: list, idx: int) -> bool:
    """완료 상태 토글"""
    if 0 <= idx < len(todos):
        todos[idx]["done"] = not todos[idx]["done"]
        return True
    return False

def remove_todo(todos: list, idx: int) -> bool:
    """할 일 삭제"""
    if 0 <= idx < len(todos):
        todos.pop(idx)
        return True
    return False

def list_todos(todos: list) -> None:
    """목록 출력"""
    if not todos:
        print("할 일이 없습니다.")
        return
    for i, t in enumerate(todos):
        mark = "✅" if t["done"] else "⬜"
        print(f"{i}. {mark} {t['title']}")

def main():
    todos = []
    menu = (
        "\n[메뉴] 1)추가 2)토글 3)삭제 4)목록 0)종료\n선택 > "
    )
    while True:
        sel = input(menu).strip()
        if sel == "1":
            title = input("할 일 내용을 입력: ").strip()
            if title:
                add_todo(todos, title)
                print("추가 완료!")
        elif sel == "2":
            idx = int(input("토글할 인덱스: "))
            print("변경 완료!" if toggle_todo(todos, idx) else "잘못된 인덱스")
        elif sel == "3":
            idx = int(input("삭제할 인덱스: "))
            print("삭제 완료!" if remove_todo(todos, idx) else "잘못된 인덱스")
        elif sel == "4":
            list_todos(todos)
        elif sel == "0":
            print("프로그램 종료.")
            break
        else:
            print("메뉴를 다시 선택하세요.")

main()