class Solution {

    public int binarysearch(int[] nums, int target, int start, int end){

        int mid=-1;

        while(start<=end){

            mid = (start+end)/2;

            if (nums[mid]==target){
                return mid;
            }

            if (nums[mid]<target){
                start = mid + 1;
            }
            else{
                end = mid-1;
            }
        }
        return -1;
    }

    public List<List<Integer>> threeSum(int[] nums) {

        Solution solution = new Solution();

        Arrays.sort(nums);

        Set<List<Integer>> answer = new HashSet<List<Integer>>();

        int temp = 0, target=0;

        for(int i=0; i< nums.length; i++){
            for(int j = i+1; j<nums.length; j++){

                target = nums[i] + nums[j];

                temp =solution.binarysearch(nums, target*-1, j+1, nums.length-1);

                if (temp >=0){
                    answer.add(Arrays.asList(nums[i], nums[j], nums[temp]));
                }

            }
        }
        List<List<Integer>> ans = new ArrayList();
        for(List x: answer){
            ans.add(x);
        }


        return ans;
    }
}