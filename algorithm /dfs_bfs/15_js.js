

function solution(n, m, k, arr) {

    let ad_list = [ ]

    for (let i = 0; i < n+1; i++){
        ad_list.push([])
    }

    for (let i = 0; i<arr.length; i++){
        ad_list[arr[i][0]] = arr[i][1];

    }

    let visited = [false] *(n+1)

    let q = []


    q.push([0,1])

    visited[1] = true

    while ( q.length !== 0){
        let temp = q.shift()

        let dis = temp[0]
        let now = temp[1]

        for(let i = 0; i< ad_list[now].length; i++) {
            if (visited[ad_list[now][i]] === false) {
                visited[ad_list[now][i]] = dis + 1
                q.push([dis + 1, ad_list[now][i]])
            }
        }

    }


    let answer = []

    for (let i = 1; i< visited.length; i++){
        if (visited[i] === k){
            answer.push(i)
        }
    }

    if (answer.length === 0){
        console.log(-1)
    }
    else{
        for(let i =0; i<answer.length;i++){
            console.log(answer[i])
        }
    }

}


solution(4,4,2, [[1,2],[1,3], [2,3], [2,4]])


