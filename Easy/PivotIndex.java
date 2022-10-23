public class PivotIndex {
    public int pivotIndex(int[] nums) {
        int left_sum;
        int right_sum;
        for(int i = 0; i<nums.length; i++) {
            left_sum = leftSum(nums, i);
            right_sum = rightSum(nums, i);
            if(left_sum == right_sum) {
                return i;
            }
        }

        return -1;
    }

    // Sum the array to the left of the index point:
    public int leftSum(int[] nums, int index) {
        int sum = 0;
        for(int i = 0; i<index; i++){
            sum = sum + nums[i];
        }
        return sum;
    }

    // Sum the array to the right of the index point:
    public int rightSum(int[] nums, int index) {
        int sum = 0;
        for(int i = nums.length-1; i>index; i--){
            sum = sum + nums[i];
        }

        return sum;
    }
}