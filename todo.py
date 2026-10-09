#储存代码
import json
#现代化路径可以跨平台调用代码
from pathlib import Path

TODO_FILE = Path("todo.json")

#读取数据
def load_todos():
    if not TODO_FILE.exists():
        return []
    #先收货再拆
    return json.loads(TODO_FILE.read_text(encoding="utf=8"))

#保存数据
def save_todos(todos):
    #先打包再发货
    TODO_FILE.write_text((json.dumps(todos,ensure_ascii=False,indent=-2)),encoding="utf-8")

#程序主路口
def main():
    #先加载之前的数据
    todos = load_todos()

    while True:
        print("\n---待办事务清单---")
        print(f"当前共有{len(todos)}项清单")
        print("1.添加任务")
        print("2.查看任务")
        print("3.退出")

        choice = input("请输入选项(1\2\3):").strip()

        if choice == "1":
            task = input("请输入选项:").strip()
            if task:
                todos.append({"id":len(todos)+1,"task":task,"done":False})
                save_todos(todos)
                print("[x]任务已添加")

        elif choice == "2":
            if not todos:
                print("暂无任务")
            else:
                for t in todos:
                    status = "[x]" if t["done"] else []
                    print(f"{status},[{t['id']}],{t['task']}")

        elif choice == "3":
            print("再见,数据已保存!")
            break
        else:
            print("输入错误,请重新输入1,2或3")

#当前文件被运行就直接执行main()
if __name__ == "__main__":
    main()




