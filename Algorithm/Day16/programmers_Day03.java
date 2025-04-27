package TIL.Algorithm.Day16;

class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = {0};
        
        for(int i = 0; i < wallpaper.length; i++){
            for(int j = 0; j < wallpaper[0].length(); j++){
                if (wallpaper[i].charAt(j) == '#') {
                    answer[0] = i;
                    break;
                }
            }
            if(answer[0] != 0){
                break;
            }
        }

        for(int i = 0; i < wallpaper[0].length(); i++){
            for(int j = 0; j < wallpaper.length; j++){
                if (wallpaper[j].charAt(i) == '#') {
                    answer[1] = i;
                    break;
                }
            }
            if(answer[1] != 0){
                break;
            }
        }

        for(int i = wallpaper.length - 1; i >= 0; i--){
            for(int j = wallpaper[0].length() - 1; j >= 0; j--){
                if (wallpaper[i].charAt(j) == '#') {
                    answer[2] = i + 1;
                    break;
                }
            }
            if(answer[2] != 0){
                break;
            }
        }

        for(int i = wallpaper[0].length() - 1; i >= 0; i--){
            for(int j = wallpaper.length - 1; j >= 0; j--){
                if (wallpaper[j].charAt(i) == '#') {
                    answer[3] = i + 1;
                    break;
                }
            }
            if(answer[3] != 0){
                break;
            }
        }

        return answer;
    }
}


/* 
 
public int[] solution(String[] wallpaper) {
        int minX = Integer.MAX_VALUE;
        int minY = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE;
        int maxY = Integer.MIN_VALUE;
        for(int i=0; i< wallpaper.length;i++ ){
            for(int j=0; j<wallpaper[i].length();j++){
                if(wallpaper[i].charAt(j)=='#'){
                    minX = Math.min(minX,i);
                    minY = Math.min(minY,j);
                    maxX = Math.max(maxX,i);
                    maxY = Math.max(maxY,j);
                }
            }
        }
        return new int[]{minX,minY,maxX+1,maxY+1};
 
*/

public class programmers_Day03 {
    public static void main(String[] args) {
        String[] str = {"..........", 
        ".....#....", 
        "......##..", 
        "...##.....", 
        "....#....."};

        Solution obj = new Solution();
        obj.solution(str);
    }
}
