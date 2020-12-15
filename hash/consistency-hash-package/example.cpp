#include "ConsistencyHash.h"
using namespace std;

// g++ example.cpp ConsistencyHash.cpp -o example -lcrypto -lssl

int main(int argc, char const *argv[])
{
    vector<string> nodes;
    nodes.push_back("mongodb1");
    nodes.push_back("mongodb2");
    nodes.push_back("mongodb3");
    nodes.push_back("mongodb4");
    nodes.push_back("mongodb5");
    ConsistencyHash con(nodes, 5000);

    unordered_map<string, int> nodeStat;
    vector<string>::iterator iter = nodes.begin();
    while(iter != nodes.end()) {
        nodeStat[*iter] = 0;
        iter++;
    }
    for(int group = 0; group < 10000000; group++) {
        string node = con.getNode(to_string(group));
        nodeStat[node]++;
        // unordered_map<string, int>::iterator it = nodeStat.find(node);
        // if(it != nodeStat.end())
        //     nodeStat[node] = it->second + 1;
        // else
        //     cerr << "node: " << node << endl;
    }

    for(auto it = nodeStat.begin(); it != nodeStat.end(); ++it) {
        cout << it->first << ":" << it->second << endl;
    }

    vector<string> nodes2 = nodes;
    nodes2.push_back("mongodb6");

    ConsistencyHash con2(nodes2, 5000);
    int lost = 0;
    for(int group = 0; group < 10000000; group++) {
        string node = con.getNode(to_string(group));
        string node2 = con2.getNode(to_string(group));
        if(node != node2)
            lost++;
    }

    cout << "Lost rate: " << lost / 100000.0 << " count: " << lost << endl;

    return 0;
}
