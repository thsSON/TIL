import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class P49189 {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        int distances[] = new int[n + 1];
        int maxDistance = 0;
        Queue<Integer> q = new LinkedList<>();
        
        // build_graph
        for(int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        for(int e[] : edge){
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        Arrays.fill(distances, -1);

        // BFS
        q.add(1);
        distances[1] = 0;
        while(!q.isEmpty()){
            int currentNode = q.poll();
            maxDistance = distances[currentNode];

            for (int neighbor : graph.get(currentNode)) {
                if(distances[neighbor] < 0){
                    q.add(neighbor);
                    distances[neighbor] = distances[currentNode] + 1;
                }
            }
            System.out.println(currentNode);
        }
        
        for (int i : distances) {
            if(i == maxDistance){
                answer++;
            }
        }

        return answer;
    }
}

// 프로그래머스 49189번 문제 - https://school.programmers.co.kr/learn/courses/30/lessons/49189