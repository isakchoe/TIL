#include <iostream>
#include <vector>
#include <unordered_set>


using namespace std;

int find_p(vector<int>& parent, int x){
    if(parent[x] != x){
        parent[x] = find_p(parent, parent[x]);
    }
    return parent[x];
}

void uni(int a, int b, vector<int>& parent){
    int x = parent[a];
    int y = parent[b];

    if(x>y){
        parent[x] = y;
    }
    else {
        parent[y] = x;
    }
}


int main() {

    int T;
    cin >> T;

    for(int i =1; i <T+1; i++){
        int n, m;
        cin >> n >> m;
        vector<int> parent (n+1, 0);

        for(int k=1; k<n+1;k++){
            parent[k] = k;
        }

//        입력받기
        for(int j =0; j<m;j++){
            int a, b;
            cin >> a >> b;
            if(find_p(parent,a) != find_p(parent,b)){
                uni(a,b,parent);
            }
        }

        for(int i=1; i<n+1;i++){
            find_p(parent,i);
        }

        int answer;
        unordered_set<int> kind;

        for(int i=1; i<n+1;i++){
            kind.insert(parent[i]);
        }
        answer = kind.size();
        cout << '#' << i << " "<< answer <<endl;
    }
    return 0;

}
