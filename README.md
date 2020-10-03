# Leetcode Submissions repo
Leetcode question practice to grasp a better understanding of algorithms and datastructures
 
## Useful Techniques

##  Python tips
- `Counter(string)` returns a dictionary which holds number of occurrences of characters
- `dict.get(number, num)` returns the value pertaining to the key if it exists, else it returns the given num

## Sliding Window Template
```
int findSubstring(string s){
        vector<int> map(128,0);
        int counter; // check whether the substring is valid
        int begin=0, end=0; //two pointers, one point to tail and one  head
        int d; //the length of substring

        for() { /* initialize the hash map here */ }

        while(end<s.size()){

            if(map[s[end++]]-- ?){  /* modify counter here */ }

            while(/* counter condition */){ 
                 
                 /* update d here if finding minimum*/

                //increase begin to make it invalid/valid again
                
                if(map[s[begin++]]++ ?){ /*modify counter here*/ }
            }  

            /* update d here if finding maximum*/
        }
        return d;
  }
```