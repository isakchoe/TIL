


//#include <bits/stdc++.h>
#include <iostream>
#include <vector>
//#include <utility>
#include <queue>

using namespace std;

//1795 번

//로직
// 다익스트라
//   x 노드를 제외한 모든 노드가 X 노드까지의 최단거리 구하기
// x 노드에서 모든 노드까지 최단 거리 구하기
//위에 두 값 합치기,
// 최대값 프린트!


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    for(int i =1; i<t+1; i++){
        int n,m,x;
        cin >> n >> m >> x;

        // 간선 연결 배열 -- 벡터로 표
        vector<vector<pair<int,int>>> ad_list(n+1);
        vector<vector<pair<int,int>>> reverse_ad_list (n+1);

        for(int j=0;j<m;j++){
            int a,b,cost;
            cin >> a >> b >> cost;

            // 입력받아서 넣기, a 노드에서 b 노드까지 cost 비용 든다.
            ad_list[a].push_back(make_pair(cost,b));
            reverse_ad_list[b].push_back(make_pair(cost,a));
        }

        vector<int> distance(n+1,100*m+1);
        priority_queue<pair<int,int>> pq;
        // cost, node
        pq.push(make_pair(0,x));
        // 본인 출발 0
        distance[x] = 0;


        // x 노드에서 --> 다른 노드로 최단 경로 테이블 구하기
        while(!pq.empty()){
            // 꺼내고 마이너스 제거
            int cost = -pq.top().first;
            int now = pq.top().second;
            pq.pop();

            if(distance[now] < cost) continue;

            for(int k=0; k < ad_list[now].size(); k++){
                int length = ad_list[now][k].first;
                int node = ad_list[now][k].second;

                int new_cost = cost + length;

                if(distance[node] > new_cost){
                    distance[node] = new_cost;
                    // max heap
                    pq.push(make_pair(-new_cost,node ));
                }
            }
        }

            // 간선리스트 역방향   특정노드 --> x 노드까지 거리
        vector<int> reverse_distance(n+1,100*m+1);
        priority_queue<pair<int,int>> reverse_pq;
        // cost, node
        reverse_pq.push(make_pair(0,x));
        // 본인 출발 0
        reverse_distance[x] = 0;


        // x 노드에서 --> 다른 노드로 최단 경로 테이블 구하기
        while(!reverse_pq.empty()){
            // 꺼내고 마이너스 제거
            int cost = -reverse_pq.top().first;
            int now = reverse_pq.top().second;
            reverse_pq.pop();

            if(reverse_distance[now] < cost) continue;

            for(int k=0; k < reverse_ad_list[now].size(); k++){
                int length = reverse_ad_list[now][k].first;
                int node = reverse_ad_list[now][k].second;

                int new_cost = cost + length;

                if(reverse_distance[node] > new_cost){
                    reverse_distance[node] = new_cost;
                    // max heap
                    reverse_pq.push(make_pair(-new_cost,node ));
                }
            }
        }

        vector<int>result_table (n+1);

        for(int index =1; index<n+1;index++){
            result_table[index] = distance[index] + reverse_distance[index];
        }



        int answer;
            // 최대값 구하기
            answer = *max_element(result_table.begin(), result_table.end());


//            for (int i = 0; i < result_table.size(); i++) {
//                cout << result_table[i] << " ";
//            }
//            cout << '\n';

            cout << "#" << i << " " << answer << "\n";

        }
    return 0;
}