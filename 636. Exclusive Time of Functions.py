#636. Exclusive Time of Functions
#On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

#Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

#You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

#A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

#Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        """
        ["0:start:0","1:start:2","1:end:5","0:end:6"]
        
        out: [0, 0]
        stack: [0, 0]
        
        if next is a start:
        update out[previous_command_idx] += time difference
        
        else:
        update out[cur_command_idx] += time difference
        pop out top
        if stack:
            convert next_top command start the end time of the current command
        
        return out
        O(n), O(n)
        
        """
        
        stack = []
        out = [0] * n
        for log in logs:
            part1, part2, part3 = log.split(':')
            command_idx, ts = int(part1), int(part3)
            if not stack:
                stack.append((command_idx, ts))
                
            else:
                
                if part2 == 'start':
                    prev_idx, prev_ts = stack.pop()
                    out[prev_idx] += ts - prev_ts
                    stack.append((prev_idx, ts))
                    stack.append((command_idx, ts))
                
                else:
                    prev_idx, prev_ts = stack.pop()
                    out[command_idx] += ts - prev_ts + 1
                    if stack:
                        prev_idx, prev_ts = stack.pop()
                        stack.append((prev_idx, ts + 1))
        return out
                        
                    
                    
                    
                
            
            
            
            
            
        