import java.util.Collections;

class Solution {


    public int lengthOfLIS(int[] nums) {


    List<Integer> array_list = new ArrayList<>(nums.length);

    for(int x: nums){

        int index  = Collections.binarySearch(array_list, x);

        if (index < 0){
            index = ~index;
        }

        if (array_list.size() == index){
            array_list.add(x);
        }
        else{
            array_list.set(index, x);
        }
    }
        return array_list.size();
    }

    public static void main(String[] args){

    System.out.println(new Solution().lengthOfLIS([1, 2, 3,45, 23,-23, 12, 19]))

    }

}