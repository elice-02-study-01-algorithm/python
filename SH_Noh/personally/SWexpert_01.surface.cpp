#include<iostream>
using namespace std;

int N;
int** samsung;

int dy[4] = {1, -1, 0, 0};
int dx[4] = {0, 0, 1, -1};

void sinking(int** country, int height);
void counting(int x, int y, int visited[100][100]);

int main(int argc, char** argv) {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

	int test_case;
	int T;

	cin >> T;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for (test_case = 1; test_case <= T; ++test_case)
	{
        cin >> N; //삼성국의 한 변의 길이

        samsung = new int*[N]; // 배열을 선언할 때, 이중 포인터를 사용한다.
        for (int i = 0; i < N; i++) {
            samsung[i] = new int[N]; // 각 row마다 다양한 길이의 배열 크기를 생성할 수 있다.
            fill_n(samsung[i], N, 0); // 지역변수로 선언했다면 초기화 해주어야 한다.
            for (int j = 0; j < N; j++) {
                cin >> samsung[i][j];
            }
        }

        // 최대 높이 따로 검사하지 않고 모두 물에 잠겨 영역이 0개일 때까지 실행
        int max_district = 0;
        int height = 0;
        int district = 100; // 대강 최대 100개의 구역을 넘길 수 없음
        while (district != 0) {
            // 1년씩 물에 잠기는 함수
            sinking(samsung, height);
            district = 0;
            int visited[100][100]={0};
            for (int i = 0; i < N; ++i) {
                for(int j = 0; j < N; ++j) {
                    if (samsung[i][j] != 0 && visited[i][j] == 0) {
                        // 몇 개의 구역으로 나뉘었는지 세는 함수
                        counting(i, j, visited);
                        district += 1;
                    }
                }
            }
            max_district = max(max_district, district);
            // cout << height << "?" << district << "max" << max_district << "\n";
            height++;
        }

        cout << "#" << test_case << " " << max_district << "\n";

        /* 메모리 해제 */
        for (int i = 0; i < N; i++)
            delete [] samsung[i];
        delete [] samsung;
    }

	return 0; //정상종료시 반드시 0을 리턴해야합니다.
}

void sinking(int** country, int height) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
        {
            // 물 높이 == 구역 높이가 되면 0으로 변경
            if (country[i][j] == height) {
                country[i][j] = 0;
            }
        }
    }
}

void counting(int x, int y, int visited[100][100]) {
    visited[x][y] = 1;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        
        // 구역을 벗어나면 continue
        if(nx < 0 || nx >= N || ny < 0 || ny >= N)
            continue;
        // 잠겼거나(0) 이미 방문했을 경우 continue
        if(samsung[nx][ny] == 0 || visited[nx][ny] == 1)
            continue;

        counting(nx, ny, visited);
    }
}