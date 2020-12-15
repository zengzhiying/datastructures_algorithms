#include <iostream>
#include <vector>
#include <cstdint>
// #include <map>
#include <unordered_map>
#include <algorithm>
#include <stdio.h>
#include <inttypes.h>

#include <openssl/md5.h>

class ConsistencyHash
{
public:
    ConsistencyHash(const std::vector<std::string>& nodes, const int& vnodes);
    // ~ConsistencyHash();
    std::string getNode(const std::string& data);


private:
    std::vector<std::string> nodes;
    std::vector<uint64_t> ring;
    int vnodes;
    std::unordered_map<uint64_t, std::string> nodeByHash;

    uint64_t hash(const char *src, int length);
    uint64_t nodeHash(int i, int j);
    int bisectLeft(uint64_t value);
    
};


