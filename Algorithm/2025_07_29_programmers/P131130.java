import java.util.ArrayList;

class P131130 {
    public int solution(int[] cards) {
        int answer = 0, max1, max2;
        boolean openedBoxes[] = new boolean[cards.length];
        ArrayList<Integer> boxCnt = new ArrayList<>();

        for(int i = 0;i < cards.length; i++){
            if(openedBoxes[i]){  
                continue;
            }

            int k = 0, j = cards[i];
            while(true){
                if(openedBoxes[j - 1]) break;

                openedBoxes[j - 1] = true;
                j = cards[j - 1];
                k++;
            }
            boxCnt.add(k);
        }
        if(boxCnt.size() == 1){
            answer = 0;
        }
        else{
            max1 = 0;
            max2 = 0;

            for(int num : boxCnt){
                if(num > max1){
                    max2 = max1;
                    max1 = num;
                }
                else if(num > max2){
                    max2 = num;
                }
            }
            answer = max1 * max2;
        }
        return answer;
    }
}

// // 프로그래머스 131130 문제 - https://school.programmers.co.kr/learn/courses/30/lessons/131130
