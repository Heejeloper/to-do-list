# 메뉴창
planned_list = []
while True: 
    x = input("하고자 하는 일을 입력해주세요. 1) 오늘 일정확인 2) 완료 일정 체크 3) 일정 추가하기 4) 종료하기: " )
    try:
        first_input = int(x)
        if first_input == 1:
            print(planned_list)
        elif first_input == 3:
            y = input("추가할 일정을 써주세요: ")
            print(y)
            z = input("이 일정을 추가할까요?[y/n]: ")
            if z == "y":
                planned_list.append(y)
            else:
                continue

        elif first_input == 2:
            print("현재 남은 일정입니다: ")
            i = 0
            for i in range(len(planned_list)):
                print(i, planned_list[i])
            a = input("몇 번 일정을 완료하셨나요? 번호를 입력해주세요: ")
            try:
                b = int(a)
                planned_list.remove(planned_list[b])
            except:
                continue

        elif first_input == 4:
            break
        else:
            continue
    except:
        continue
