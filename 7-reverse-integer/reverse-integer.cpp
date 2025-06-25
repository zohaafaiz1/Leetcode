class Solution {
public:
    int reverse(int x) {
        int answer=0;
        while(x!=0){

            int digit=x%10;
            if((answer>INT_MAX/10)||(answer<INT_MIN/10)){// to check the upper & lower limit 
            return 0;
            }
            answer=answer*10+digit;
        
            x=x/10;
        }
        return answer;
    }
};