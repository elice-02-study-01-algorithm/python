def solution(distance, scope, times):
    tmp = sorted(scope,key=lambda x:min(x))
    bind = {(min(i),max(i)):times[scope.index(i)] for i in tmp}
    
    for gard,time in bind.items():
        # print('new_gard, gard_line :',gard)
        current_time = sum(time)
        init_time,res = divmod(gard[0],current_time)
        init_time = init_time*current_time+1
        
        # print('감시시작 :',init_time,'& 감시마지막 :',init_time+time[0])
        for i in range(init_time,init_time+time[0]):
            if gard[0]<=i<=gard[1]:
                return i
        # print('감시시작 :',init_time+current_time,'& 감시마지막 :',init_time+current_time+time[0])
        for i in range(init_time+current_time,init_time+current_time+time[0]):
            if gard[0]<=i<=gard[1]:
                return i

    return distance