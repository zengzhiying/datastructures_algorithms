class CircularQueue {
public:
    CircularQueue(int max_size);   // 构造方法 初始化队列并设置队列大小
    virtual ~CircularQueue();   // 析构方法
    void clear();   // 清空队列
    bool empty() const; // 判断队列是否为空
    bool full() const;  // 判断队列是否为满
    int length() const; // 计算队列长度
    bool enQueue(int element);  // 新元素入队尾
    bool deQueue(int &element); // 首元素出队 并且用element来拿到出队的值
    void traverse();    // 遍历队列
private:
    int * p;    // 队列指针
    int element_number; // 当前元素个数
    int max_size;   // 队列大小
    int head;   // 队头
    int tail;   // 队尾
};
