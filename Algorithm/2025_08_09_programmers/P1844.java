import java.util.LinkedList;
import java.util.Queue;

class P1844 {
    class Node{
        int x;
        int y;
        int dist;

        public Node(int x, int y, int dist){
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }
    public int solution(int[][] maps) {
        
        // 상하좌우
        int[] dx = {0, 0, -1, 1}; 
        int[] dy = {-1, 1, 0, 0};

        int N = maps.length, M = maps[0].length;
        boolean[][] visited = new boolean[N][M];
        Queue<Node> queue = new LinkedList<Node>();

        visited[0][0] = true;
        queue.offer(new Node(0, 0, 1));

        while(!queue.isEmpty()){
            Node curNode = queue.poll();
            int x = curNode.x;
            int y = curNode.y;
            int dist = curNode.dist;

            if(x == M - 1 && y == N - 1){    // 도착
                return dist;
            }

            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(0 <= nx && nx < M && 0 <= ny && ny < N && maps[ny][nx] == 1 && !visited[ny][nx]){
                    visited[ny][nx] = true;
                    queue.offer(new Node(nx, ny, dist + 1));
                }
            }
        }  
        return -1;
    }
}

// 프로그래머스 1844 문제 - https://school.programmers.co.kr/learn/courses/30/lessons/1844