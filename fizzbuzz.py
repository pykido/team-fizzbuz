for i in range(1, 101):              # 1부터 100까지 100번 반복
    if i % 3 == 0 and i % 5 == 0:    # 3과 5의 공배수일 때
        print('FizzBuzz')            # FizzBuzz 출력
        continue
    if i % 3 == 0:                   # 3의 배수일 때
        print('Fizz')                # Fizz 출력
        continue
    if i % 5 == 0:                   # 5의 배수일 때
        print('Buzz')                # Buzz 출력
        continue
    print(i)                         # 아무것도 해당되지 않을 때 숫자 출력
