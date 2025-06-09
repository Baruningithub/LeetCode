class Solution {
    public int trailingZeroes(int n) {
        if(n==0) return 0;
        int c = 0;
        int div = 5;
        while (n >= div){
            c += n/div;
            div *= 5;
        }
        return c;
    }
    
}