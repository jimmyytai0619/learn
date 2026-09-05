package DataStructure.Queue;

import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args){
        
        Queue<String> queue = new LinkedList<String>();
        
        System.out.println(queue.isEmpty());
        //if the queue is empty then will return true

        queue.offer("Karen");
        queue.offer("Chad");
        queue.offer("Harold");

        //System.out.println(queue.peek());
        //System.out.println(queue.contains("Harold"));
        //System.out.println(queue.size());
        //queue.poll();

        System.out.println(queue);

    }

}
