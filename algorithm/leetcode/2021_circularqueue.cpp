class MyCircularQueue {
    vector<int>q;
    int x;
public:
    MyCircularQueue(int k) {
        vector<int>q(k);
        x = k;
    }

    bool enQueue(int value) {
        if(q.size()<x){
            q.insert(q.begin(), value);
            return true;
        }else
            return false;
    }

    bool deQueue() {
        if(q.size()>0){
            q.pop_back();
            return true;
        }else
            return false;
    }

    int Front() {
        if(q.size()>0)
            return q.back();
        else
            return -1;
    }

    int Rear() {
        if(q.size())
            return q.front();
        else
            return -1;
    }

    bool isEmpty() {
        return q.size()==0;
    }

    bool isFull() {
        return q.size()==x;
    }
};