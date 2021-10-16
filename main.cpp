
//#include <bits/stdc++.h>
#include <iostream>
#include <vector>
//#include <utility>
#include <queue>

using namespace std;


//로직
// 다익스트라
//   x 노드를 제외한 모든 노드가 X 노드까지의 최단거리 구하기
// x 노드에서 모든 노드까지 최단 거리 구하기
//위에 두 값 합치기,
// 최대값 프린트!


int main(){

    int t;
    cin >> t;

    for(int i =1; i<t+1; i++){
        int n,m,x;
        cin >> n >> m >> x;

        // 간선 연결 배열 -- 벡터로 표
        vector<vector<pair<int,int>>> ad_list(n+1) ;

        for(int j=0;j<m;j++){
            int a,b,cost;
            cin >> a >> b >> cost;

            // 입력받아서 넣기, a 노드에서 b 노드까지 cost 비용 든다.
            ad_list[a].push_back(make_pair(cost,b));
        }

        vector<int> distance(n+1,100*m+1);
        priority_queue<pair<int,int>> pq;
        // cost, node
        pq.push(make_pair(0,x));


        // x 노드에서 --> 다른 노드로 최단 경로 테이블 구하기
        while(!pq.empty()){
            // 꺼내고 마이너스 제거
            int cost = -pq.top().first;
            int now = pq.top().second;
            pq.pop();

            if(distance[now] < cost) continue;

            for(int i=0; i<ad_list[now].size(); i++){
                int length = ad_list[now][i].first;
                int node = ad_list[now][i].second;

                int new_cost = cost + length;

                if(distance[node] > new_cost){
                    distance[node] = new_cost;
                    // max heap
                    pq.push(make_pair(-new_cost,node ));
                }
            }
        }

        //  갔다가 왔다 경로 합치는 테이블
        vector<int> result_table(n+1,0);

        //   i 노드에서 --> x 까지 최단 경로 구하기
        for(int i=1; i< n+1; i++){
            priority_queue<pair<int,int>> temp_pq;
            vector<int> temp_distance(n+1, 100*m+1);

            temp_pq.push(make_pair(0,i));

            while(!temp_pq.empty()){
                // 꺼내고 마이너스 제거
                int cost = -temp_pq.top().first;
                int now = temp_pq.top().second;
                temp_pq.pop();

                if(distance[now] < cost) continue;

                for(int i=0; i<ad_list[now].size(); i++){
                    int length = ad_list[now][i].first;
                    int node = ad_list[now][i].second;

                    int new_cost = cost + length;

                    if(temp_distance[node] > new_cost){
                        temp_distance[node] = new_cost;
                        // max heap
                        temp_pq.push(make_pair(-new_cost,node ));
                    }
                }
            }
            // result 테이블 갱신
            result_table[i] = temp_distance[x] + distance[i];
        }

        int answer;
        // 최대값 구하기
        answer = *max_element(result_table.begin(), result_table.end());

        for(int i=0; i<result_table.size();i++){
            cout << result_table[i] <<" ";
        }
        cout <<endl;

        cout << "#" << i << " " << answer <<endl;
    }

    return 0;
}