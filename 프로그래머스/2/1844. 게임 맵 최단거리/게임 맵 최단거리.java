import java.io.*;
import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer=0;
        Queue<int[]> q=new ArrayDeque();
        int[] dxs={1,-1,0,0};
        int[] dys={0,0,1,-1};
        q.add(new int[]{0,0});
        int[][] visited=new int[maps.length][maps[0].length];
        visited[0][0]=1;
        
        
        while(!q.isEmpty()){
            int[] cur=q.poll();
            int x=cur[0];
            int y=cur[1];
            
            for(int i=0;i<4;i++){
                int nx=x+dxs[i], ny=y+dys[i];
                if(0<=nx && nx<maps.length && 0<=ny && ny<maps[0].length
                  && visited[nx][ny]==0 && maps[nx][ny]==1){
                    q.add(new int[]{nx,ny});
                    visited[nx][ny]=visited[x][y]+1;
                }
            }
        }
        
        if(visited[maps.length-1][maps[0].length-1]==0){
            return -1;
        }else{
            return visited[maps.length-1][maps[0].length-1];
            
        }
    }
}