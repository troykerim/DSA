'''
Leetcode 1472 - Design Browser History

You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

    BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
    void visit(string url) Visits url from the current page. It clears up all the forward history.
    string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
    string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


This solution uses a doubly linked list
'''
# Create the LL class
class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.cur = ListNode(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.cur.next = ListNode(url, self.curr)
        self.cur = self.cur.next
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev 
            steps -= 1 
        return self.cur.val
        
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.cur.next and steps > 0:
            self.cur = self.cur.next 
            steps -= 1 
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)