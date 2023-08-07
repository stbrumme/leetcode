class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        reverse(nums.begin(), nums.end());

        int maxx = 0;
        for (int x = 0; x < nums.size(); x++)
        {
            int a = nums[x];
            if (3*a <= maxx)
                break;

            for (int y = x+1; y < nums.size(); y++)
            {
                int b = nums[y];
                if (a+b+b <= maxx)
                    break;

                for (int z = y+1; z < nums.size(); z++)
                {
                    int c = nums[z];

                    if (b + c <= a)
                        break;
                    if (a+b+c <= maxx)
                        break;

                    maxx = a+b+c;
                }
            }
        }
        return maxx;
    }
};
