/**
스택이나 큐를 사용하는 것이 flat 맵을 구현하는 가장 좋은 방법이지 않을까 함.
-> 자바 스트림의 flatmap도 비슷하지 않을까 싶음.
**/

public class NestedIterator implements Iterator<Integer> {
    
    Deque<NestedInteger> stack = new LinkedList<>();

    public NestedIterator(List<NestedInteger> nestedList) {
        fill(nestedList);
    }
    
    private void fill(List<NestedInteger> nestedList){
        int size=nestedList.size();
        for(int i=size-1; i>=0; i--){
            stack.addLast(nestedList.get(i));
        }
    }
    

    @Override
    public Integer next() {
        return hasNext() ? stack.pollLast().getInteger() : null;
    }

    @Override
    public boolean hasNext() {
        while(!stack.isEmpty() && !stack.peekLast().isInteger()){
            fill(stack.pollLast().getList());
        }
        
        return !stack.isEmpty();
    }
}
