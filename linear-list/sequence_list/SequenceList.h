class SequenceList {
public:
    SequenceList(int max_size);
    ~SequenceList();
    void clear();
    bool empty();
    int length();
    bool get(int i, int *element);
    int locate(int *element);
    bool prior(int *current_element, int *prev_element);
    bool next(int *current_element, int *next_element);
    void traverse();
    bool insert(int i, int *element);
    bool remove(int i, int *element);

private:
    int *p;
    int max_size;   // 最大长度
    int element_number; // 当前长度
};
