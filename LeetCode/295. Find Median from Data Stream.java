class MedianFinder {
    
    PriorityQueue<Integer> high=new PriorityQueue<>((a,b)-> b-a);
    PriorityQueue<Integer> low=new PriorityQueue<>();
    boolean even=true;
    
    public MedianFinder() {
        
    }
    
    public void addNum(int num) {
        if(even){
            high.add(num);
            low.add(high.poll());
        }else{
            low.add(num);
            high.add(low.poll());
        }
        even = !even;
    }
    
    public double findMedian() {
        return even ? (low.peek()+high.peek())/2.0 : low.peek();
    }
}
