#include <algorithm>
#include <stack>

class Solution {
    static const int ALPHABET_SIZE = 256;
public:
    int lengthOfLongestSubstring(string s) {

        int longestInt = 0;
        int subStringInt = 0;
        string longest =  "";
        string substr = "";
        stack<char> gapStack;
        bool charTracker[ALPHABET_SIZE];
        std::fill(charTracker, charTracker+ALPHABET_SIZE, false); //initialize charCount boolean array (is this necessary?)
        for(int c = 0; c < s.size(); c++) {
            //has letter c been seen?
            char letter = s[c];
            if (charTracker[letter]) { //yes
                if (substr.length() > longest.length() )
                    longest = substr; //store current substring if longest
                std::fill(charTracker, charTracker+ALPHABET_SIZE, false); // reset charCount array
                
                // push substring of letters between repeated letter onto stack:   a b c d {x y z} d
                int gapIndex = c-1;
                // cout <<"before stack creation:" <<substr << endl;
                while (gapIndex > 0 && s[gapIndex] != letter) {
                    gapStack.push( s[gapIndex] );
                    gapIndex--;
                }
                
                substr = "";
                if ( !gapStack.empty() ) {
                    //rebuild substring and charTracker from stack
                    while(!gapStack.empty()) {
                        substr.push_back(gapStack.top());
                        if (gapStack.top() < 0 || gapStack.top() > 255) break;
                        charTracker[ gapStack.top() ] = true;
                        gapStack.pop();
                    }
                    // cout <<"after rebuild from stack:" <<substr << endl;
                }
                
            } 
            charTracker[letter] = true; // mark char as seen
            
            substr.push_back(letter); //add char to substring
        }     
        // trim(longest);
        // trim(substr);
        // cout << "--after for loop--" << endl;
        // cout <<  "longest:" << longest << endl;
        // cout <<  "longest.length:" << longest.length() << endl;
        // cout <<  "substr:" << substr << endl;
        // cout <<  "substr.length:" << substr.length() << endl;
        
//         print(longest);
//         print(substr);
        longestInt = countMyBrokenStrings(longest);
        subStringInt = countMyBrokenStrings(substr);
        return (longestInt   >= subStringInt ? longestInt  : subStringInt );
        
    }
    int countMyBrokenStrings(string& s){
        int count = 0;
        for(int i = 0; i< s.length() ; i++)
            if (s[i] != NULL)
             count++;
        
        return count;
    }
    
    void print(string& s) {
       int longCount = 0;
        for (auto& c: s){
            cout << "char: {" << c <<"}" << endl;
            longCount++;
        }
      cout << "str length::: " << longCount << endl;
    }
};
