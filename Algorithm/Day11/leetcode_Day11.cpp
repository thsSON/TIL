#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        vector<string> findRepeatedDnaSequences(string s) {
            vector<string> result;
            unordered_set<string> seen, repeat;
    
            if( s.size() >= 10 ){
                for(size_t i = 0; i < s.size() - 10; i++){
                    string substring = s.substr(i, 10);
    
                    if(seen.count(substring)){
                        repeat.insert(substring);
                    } else{
                        seen.insert(substring);
                    }
                }
            }
    
            result.assign(repeat.begin(), repeat.end());
    
            return result;
        }
};
