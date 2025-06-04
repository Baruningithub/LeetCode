 
class Solution {
    public int trap(int[] height) {
        int area=0;
        int n=height.length;
        int r[]=new int[n];
        int l[]=new int[n];
        l[0]=height[0];
        for(int i=1;i<n;i++){
            l[i]=Math.max(l[i-1],height[i]);
        }
        r[n-1]=height[n-1];
        for(int j=n-2;j>=0;j--){
            r[j]=Math.max(height[j],r[j+1]);
        }

        for(int i=0;i<n;i++){
            area+=Math.min(r[i],l[i])-height[i];
        }
        return area;
    }
}