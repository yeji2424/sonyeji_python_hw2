#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 단순 연결 리스트

class Node():
    def __init__ (self):
        self.data=None
        self.link=None
import random

node1=Node()
node1.data=random.randrange(1,46)

node2=Node()
node2.data=random.randrange(1,46)
node1.link=node2

node3=Node()
node3.data=random.randrange(1,46)
node2.link=node3

node4=Node()
node4.data=random.randrange(1,46)
node3.link=node4

node5=Node()
node5.data=random.randrange(1,46)
node4.link=node5

node6=Node()
node6.data=random.randrange(1,46)
node5.link=node6

print(node1.data,end=' ')
print(node1.link.data,end=' ')
print(node1.link.link.data,end=' ')
print(node1.link.link.link.data,end=' ')
print(node1.link.link.link.link.data,end=' ')
print(node1.link.link.link.link.link.data,end=' ')


# In[13]:


# 원형리스트

class Node():
    def __init__(self):
        self.data = None
        self.link  = None
        self.prev = None
    
def printNodes(start):
    current = start
    if current == None :
        return
    print('정방향 --->',current.data,end=' ')
    while current.link != None :
        current = current.link
        print(current.data,end=' ')
    print()
    print('역방향---->',current.data,end=' ')
    while current.prev != None:
        current = current.prev
        print(current.data,end=' ')
    print()
    
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)
    
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.prev = pre
        memory.append(node)
        
    printNodes(head)


# In[168]:


# 스택

def isStackFull():
    global SIZE,stack,top
    if(top >= SIZE-1):
        return True
    else :
        return False
def isStackEmpty():
    global SIZE,stack,top
    if (top == -1):
        return True 
    else :
        return False
def push(data):
    global SIZE,stack,top
    if(isStackFull()):
        print('스택이 꽉 찼습니다.')
        return
    top += 1
    stack[top]=data
def pop():
    global SIZE,stack,top
    if(isStackEmpty()):
        print('스택이 비었습니다.')
        return 
    data = stack[top]
    stack[top]=None
    top -= 1
    return data

SIZE = 100
stack=[None for _ in range(SIZE)]
top=-1 

if __name__ == "__main__" :
    
    line =str('진달래꽃\n나 보기가 역겨워\n가실 때에는\n말 없이 고이 보내드리오리다.')
    print("---------원본---------\n",end =' ')
    for i in range(0,len(line)):
        push(line[i])
    print(line)
    print('---------------------')
    print('----거꾸로 처리한 결과----')
    for i in range(0,len(line)):
        popline=pop()  
        print(popline,end=' ')
       


# In[252]:


#큐

def isQueueFull():
    global SIZE,queue,front,rear
    if ((rear+1)%SIZE== front):
        return True
    else :
        return False
    
def isQueueEmpty() :
    global SIZE,queue,front,rear
    if (front == rear):
        return True
    else:
        return False

def enQueue(data):
    global SIZE,queue,front,rear
    if(isQueueFull()):
        print('큐가 꽉 찼습니다')
        return
    rear = (rear+1)%SIZE
    queue[rear]=data
    
def deQueue(data):
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print('큐가 비었습니다.')
        return
    front = (front+1)%SIZE
    data = queue[front]
    queue[front]=None
    return data

def peek():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print('큐가 비었습니다')
        return
    return queue[(front+1)%SIZE]

SIZE = 6
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == "__main__" :
    
    waitcall = [('사용',9),('고장',3),('환불',4),('환불',4),('고장',3)]
    
    timesum = 0

    for i in range (0,len(waitcall)) :
        if queue[i]== None :
            print('\n귀하의 대기 예상시간은 0분 입니다.')
        else :
            timesum += queue[i][1]
            print("\n귀하의 대기 예상시간은",timesum,'분 입니다.')
        print('현재 대기 콜 ----> ',queue)
        enQueue(waitcall[i])
        
    print('\n최종 대기 콜 ---- >',queue)
    print('프로그램 종료!')
    

