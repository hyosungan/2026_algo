import java.util.*;
import java.io.*;

class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        long big=Math.max(a,b);
        if(big==a){
            while(b<=a){
                answer+=b;
                b+=1;
            }
        }
        
        else{
            while(a<=b){
                answer+=a;
                a+=1;
            }
        }
        
        return answer;
    }
}