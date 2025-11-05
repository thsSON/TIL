import java.util.ArrayList;
import java.util.List;

public class P42892 {
    class Node{
        int idx;
        int x;
        int y;

        Node leftNode = null;
        Node rightNode = null;

        public Node(int idx, int x, int y){
            this.idx = idx;
            this.x = x;
            this.y = y;
        }
    }

    public void insert(Node parent, Node child){
        if(parent.x > child.x){
            if(parent.leftNode == null) parent.leftNode = child;
            else insert(parent.leftNode, child);
        }
        else {
            if(parent.rightNode == null) parent.rightNode = child;
            else insert(parent.rightNode, child);
        }
    }

    public void preorder(Node node, List<Integer> result){
        if(node == null) return;
        result.add(node.idx);
        preorder(node.leftNode, result);
        preorder(node.rightNode, result);
    }
    public void postorder(Node node, List<Integer> result){
        if(node == null) return;
        postorder(node.leftNode, result);
        postorder(node.rightNode, result);
        result.add(node.idx);
    }

    public int[][] solution(int[][] nodeinfo) {
        int x,y;
        
        List<Node> nodes = new ArrayList<>();
        for(int i = 0; i < nodeinfo.length; i++){
            x = nodeinfo[i][0];
            y = nodeinfo[i][1];
            nodes.add(new Node(i+1, x, y));
        }

        Node root = nodes.get(0);
        for(int i = 1; i < nodes.size(); i++){
            insert(root, nodes.get(i));
        }

        List<Integer> preorderList = new ArrayList<>();
        List<Integer> postorderList = new ArrayList<>();

        preorder(root, preorderList);
        postorder(root, postorderList);

        int[][] answer = new int[2][nodes.size()];
        for(int i = 0; i < nodes.size(); i++){
            answer[0][i] = preorderList.get(i);
            answer[1][i] = postorderList.get(i);
        }        


        return answer;
    }
}
