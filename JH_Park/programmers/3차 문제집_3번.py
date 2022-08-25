def solution(distance, scope, times):
    answer = 0
    observers = []
    for s, t in zip(scope, times):
        start, end = min(s), max(s)
        observers.append([start, end, t[0], t[1]])
    # print(observers)
    observers.sort()
    # print(observers)
    # [[범위, 시간]]
    # [[3, 4, 2, 5], [5, 8, 4, 3]]
    # [[4, 6, 2, 4], [7, 8, 2, 2], [10, 11, 3, 3]]
    for obs in observers:
        start, end, work, rest = obs
        obs_cycle = work + rest
        cnt_cycle = (start - 1) // obs_cycle # 사이클 몇번 돌았는지 체크 ex) 7, 8, 4, 3 하면 아직 7인데 사이클이 1이 될 수는 없다. 0 이어야함        
        start -= cnt_cycle * obs_cycle 
        end -= cnt_cycle * obs_cycle
        # print("start ", start)
        # print("end ", end)
        print("cnt_cycle ", cnt_cycle)

        # start 3 end 4 cnt_cycle 0 obs_cycle 7
        # start 5 end 8 cnt_cycle 0 obs_cycle 7

        # start 4 end 6 cnt_cycle 0 obs_cycle 6
        # start 3 end 4 cnt_cycle 1 obs_cycle 4
        # start 4 end 5 cnt_cycle 1 obs_cycle 6

        # 
        if start <= work:
            answer = cnt_cycle * obs_cycle + start
            break
        # 다음 근무 시간이 시작
        if end > obs_cycle:
            answer = cnt_cycle * obs_cycle + obs_cycle + 1
            break
    return answer