#include "ConsistencyHash.h"

ConsistencyHash::ConsistencyHash(const std::vector<std::string>& nodes, const int& vnodes) {
    this->nodes = nodes;
    this->vnodes = vnodes;
    // printf("827 + 9912 = %" PRIu64 "\n", nodeHash(827, 9912));
    for(int i = 0; i < nodes.size(); i++) {
        for(int j = 0; j < vnodes; j++) {
            uint64_t h = nodeHash(i, j);
            this->ring.push_back(h);
            nodeByHash[h] = this->nodes[i];
        }
    }

    std::sort(this->ring.begin(), this->ring.end());
}

std::string ConsistencyHash::getNode(const std::string& data) {
    uint64_t h = hash(data.c_str(), data.size());
    if(h > ring.back()) {
        return nodes[0];
    }
    

    // 二分搜索优化
    int partition = bisectLeft(h);
    return nodeByHash[ring[partition]];

    // for(int i = 0; i < ringSize; i++) {
    //     if(h <= ring[i]) {
    //         std::unordered_map<uint64_t, std::string>::const_iterator iter = nodeByHash.find(ring[i]);
    //         if(iter != nodeByHash.end()) {
    //             return iter->second;
    //         }
    //         // return nodeByHash[ring[i]];
    //     }
    // }
}

int ConsistencyHash::bisectLeft(uint64_t value) {
    int l = 0, r = ring.size();
    while(l < r) {
        int mid = l + ((r - l) >> 1);
        if(ring[mid] < value) l = mid + 1;
        else r = mid;
    }
    return l;
}

uint64_t ConsistencyHash::hash(const char *src, int length) {
    unsigned char h[16];
    MD5_CTX ctx;
    MD5_Init(&ctx);
    MD5_Update(&ctx, src, length);
    MD5_Final(h, &ctx);

    // for(int i = 0; i < 16; i++) {
    //     printf("%02x", h[i]);
    // }
    uint64_t v = 0;
    for(int i = 0; i < 8; i++) 
        v |= ((uint64_t) h[i + 4]) << (56 - (i << 3));

    return v;
}

uint64_t ConsistencyHash::nodeHash(int i, int j) {
    char src[8];
    src[0] = i >> 24;
    src[1] = i >> 16;
    src[2] = i >> 8;
    src[3] = i;
    src[4] = j >> 24;
    src[5] = j >> 16;
    src[6] = j >> 8;
    src[7] = j;
    return hash(src, 8);
}
