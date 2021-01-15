//Scope of a variable code
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Difference {
    private:
    vector<int> elements;
  
  	public:
  	int maximumDifference;

	// Add your code here
    Difference(vector<int> d){
        elements = d;
    }
    void computeDifference(){
        
        int diff{0};
        maximumDifference=0;
        
        for(int i{0}; i<elements.size(); i++){
            
            for(int j{i+1}; j<elements.size(); j++){
                diff = abs(elements.at(i)-elements.at(j));
                
                if(diff>maximumDifference){
                    maximumDifference = diff; 
                }
            }
        }
    }
}; // End of Difference class

int main() {
    int N;
    cin >> N;
    
    vector<int> a;
    
    for (int i = 0; i < N; i++) {
        int e;
        cin >> e;
        
        a.push_back(e);
    }
    
    Difference d(a);
    
    d.computeDifference();
    
    cout << d.maximumDifference;
    
    return 0;
}